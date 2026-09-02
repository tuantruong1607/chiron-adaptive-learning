from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from threading import RLock
from typing import Protocol
from uuid import UUID, uuid4

from sqlalchemy import func, select, update
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from .auth import Principal
from .config import get_settings
from .db import get_session_factory, set_tenant_context
from .persistence.tables import chat_messages, chat_threads, learning_events
from .schemas import TutorAnswer


class ConversationAccessError(PermissionError):
    pass


@dataclass(frozen=True, slots=True)
class ConversationMessage:
    role: str
    content: str


@dataclass(frozen=True, slots=True)
class ConversationTurn:
    thread_id: UUID
    history: list[ConversationMessage]
    replay: TutorAnswer | None = None


class ConversationMemory(Protocol):
    def begin_turn(
        self,
        *,
        principal: Principal,
        course_id: UUID | str,
        thread_id: UUID | None,
        question: str,
        idempotency_key: str,
    ) -> ConversationTurn: ...

    def finish_turn(
        self,
        *,
        principal: Principal,
        course_id: UUID | str,
        thread_id: UUID,
        answer: TutorAnswer,
        idempotency_key: str,
    ) -> TutorAnswer: ...


def _answer_metadata(answer: TutorAnswer) -> dict:
    return {"tutor_answer": answer.model_dump(mode="json")}


def _answer_from_metadata(metadata: dict | None) -> TutorAnswer | None:
    payload = (metadata or {}).get("tutor_answer")
    return TutorAnswer.model_validate(payload) if payload else None


class PostgresConversationMemory:
    def __init__(self, history_message_limit: int = 8) -> None:
        self.history_message_limit = history_message_limit

    @staticmethod
    def _require_thread(
        session: Session, *, principal: Principal, course_id: UUID, thread_id: UUID
    ) -> None:
        owned = session.scalar(
            select(chat_threads.c.id).where(
                chat_threads.c.id == thread_id,
                chat_threads.c.tenant_id == principal.tenant_id,
                chat_threads.c.learner_id == principal.user_id,
                chat_threads.c.course_id == course_id,
                chat_threads.c.status == "active",
            )
        )
        if owned is None:
            raise ConversationAccessError("Conversation thread not found")

    @staticmethod
    def _next_sequence(session: Session, thread_id: UUID) -> int:
        sequence = session.scalar(
            update(chat_threads)
            .where(chat_threads.c.id == thread_id)
            .values(
                next_sequence=chat_threads.c.next_sequence + 1,
                updated_at=func.now(),
                last_message_at=func.now(),
            )
            .returning(chat_threads.c.next_sequence)
        )
        if sequence is None:
            raise ConversationAccessError("Conversation thread not found")
        return int(sequence)

    @staticmethod
    def _append_event(
        session: Session,
        *,
        principal: Principal,
        course_id: UUID,
        thread_id: UUID,
        event_type: str,
        payload: dict,
        idempotency_key: str,
    ) -> None:
        session.execute(
            pg_insert(learning_events)
            .values(
                id=uuid4(),
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course_id,
                thread_id=thread_id,
                event_type=event_type,
                payload=payload,
                idempotency_key=idempotency_key,
            )
            .on_conflict_do_nothing(constraint="uq_learning_event_idempotency")
        )

    def begin_turn(
        self,
        *,
        principal: Principal,
        course_id: UUID | str,
        thread_id: UUID | None,
        question: str,
        idempotency_key: str,
    ) -> ConversationTurn:
        if not isinstance(course_id, UUID):
            raise TypeError("PostgreSQL conversation memory requires a course UUID")
        with get_session_factory()() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            if thread_id is None:
                proposed_thread_id = uuid4()
                inserted_thread_id = session.scalar(
                    pg_insert(chat_threads)
                    .values(
                        id=proposed_thread_id,
                        tenant_id=principal.tenant_id,
                        course_id=course_id,
                        learner_id=principal.user_id,
                        status="active",
                        title=question[:240],
                        initial_idempotency_key=idempotency_key,
                    )
                    .on_conflict_do_nothing(constraint="uq_chat_thread_initial_request")
                    .returning(chat_threads.c.id)
                )
                thread_id = inserted_thread_id or session.scalar(
                    select(chat_threads.c.id).where(
                        chat_threads.c.tenant_id == principal.tenant_id,
                        chat_threads.c.learner_id == principal.user_id,
                        chat_threads.c.course_id == course_id,
                        chat_threads.c.initial_idempotency_key == idempotency_key,
                    )
                )
                if thread_id is None:
                    raise RuntimeError("Conversation thread conflict could not be resolved")
            else:
                self._require_thread(
                    session, principal=principal, course_id=course_id, thread_id=thread_id
                )

            replay_row = (
                session.execute(
                    select(chat_messages.c.metadata).where(
                        chat_messages.c.tenant_id == principal.tenant_id,
                        chat_messages.c.thread_id == thread_id,
                        chat_messages.c.idempotency_key == f"{idempotency_key}:assistant",
                    )
                )
                .mappings()
                .first()
            )
            replay = _answer_from_metadata(replay_row["metadata"]) if replay_row else None
            if replay is not None:
                return ConversationTurn(thread_id=thread_id, history=[], replay=replay)

            user_key = f"{idempotency_key}:user"
            rows = (
                session.execute(
                    select(chat_messages.c.role, chat_messages.c.content)
                    .where(
                        chat_messages.c.thread_id == thread_id,
                        chat_messages.c.idempotency_key != user_key,
                    )
                    .order_by(chat_messages.c.sequence.desc())
                    .limit(self.history_message_limit)
                )
                .mappings()
                .all()
            )
            history = [
                ConversationMessage(role=row["role"], content=row["content"])
                for row in reversed(rows)
            ]

            existing_user = session.scalar(
                select(chat_messages.c.id).where(
                    chat_messages.c.tenant_id == principal.tenant_id,
                    chat_messages.c.thread_id == thread_id,
                    chat_messages.c.idempotency_key == user_key,
                )
            )
            if existing_user is None:
                sequence = self._next_sequence(session, thread_id)
                session.execute(
                    pg_insert(chat_messages).values(
                        id=uuid4(),
                        tenant_id=principal.tenant_id,
                        thread_id=thread_id,
                        role="user",
                        sequence=sequence,
                        content=question,
                        idempotency_key=user_key,
                    )
                )
                self._append_event(
                    session,
                    principal=principal,
                    course_id=course_id,
                    thread_id=thread_id,
                    event_type="tutor.user_message",
                    payload={"thread_id": str(thread_id), "sequence": sequence},
                    idempotency_key=f"{idempotency_key}:user-event",
                )
            return ConversationTurn(thread_id=thread_id, history=history)

    def finish_turn(
        self,
        *,
        principal: Principal,
        course_id: UUID | str,
        thread_id: UUID,
        answer: TutorAnswer,
        idempotency_key: str,
    ) -> TutorAnswer:
        if not isinstance(course_id, UUID):
            raise TypeError("PostgreSQL conversation memory requires a course UUID")
        answer = answer.model_copy(update={"thread_id": thread_id})
        with get_session_factory()() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            self._require_thread(
                session, principal=principal, course_id=course_id, thread_id=thread_id
            )
            assistant_key = f"{idempotency_key}:assistant"
            existing = (
                session.execute(
                    select(chat_messages.c.metadata).where(
                        chat_messages.c.tenant_id == principal.tenant_id,
                        chat_messages.c.thread_id == thread_id,
                        chat_messages.c.idempotency_key == assistant_key,
                    )
                )
                .mappings()
                .first()
            )
            replay = _answer_from_metadata(existing["metadata"]) if existing else None
            if replay is not None:
                return replay
            sequence = self._next_sequence(session, thread_id)
            session.execute(
                pg_insert(chat_messages).values(
                    id=uuid4(),
                    tenant_id=principal.tenant_id,
                    thread_id=thread_id,
                    role="assistant",
                    sequence=sequence,
                    content=answer.answer,
                    citations=[citation.model_dump(mode="json") for citation in answer.citations],
                    metadata=_answer_metadata(answer),
                    idempotency_key=assistant_key,
                )
            )
            self._append_event(
                session,
                principal=principal,
                course_id=course_id,
                thread_id=thread_id,
                event_type="tutor.response",
                payload={
                    "thread_id": str(thread_id),
                    "sequence": sequence,
                    "trace_id": str(answer.trace_id),
                    "provider": answer.provider,
                    "model": answer.model,
                    "refused": answer.refused,
                    "route": answer.route,
                    "retrieval_strategy": answer.retrieval_strategy,
                },
                idempotency_key=f"{idempotency_key}:assistant-event",
            )
        return answer


class InMemoryConversationMemory:
    def __init__(self, history_message_limit: int = 8) -> None:
        self.history_message_limit = history_message_limit
        self._lock = RLock()
        self._threads: dict[UUID, dict] = {}
        self._initial_requests: dict[tuple[str, str, str, str], UUID] = {}

    def begin_turn(
        self,
        *,
        principal: Principal,
        course_id: UUID | str,
        thread_id: UUID | None,
        question: str,
        idempotency_key: str,
    ) -> ConversationTurn:
        with self._lock:
            if thread_id is None:
                request_key = (
                    str(principal.tenant_id),
                    str(principal.user_id),
                    str(course_id),
                    idempotency_key,
                )
                thread_id = self._initial_requests.get(request_key)
                if thread_id is None:
                    thread_id = uuid4()
                    self._threads[thread_id] = {
                        "tenant_id": principal.tenant_id,
                        "learner_id": principal.user_id,
                        "course_id": str(course_id),
                        "messages": [],
                        "answers": {},
                    }
                    self._initial_requests[request_key] = thread_id
            record = self._threads.get(thread_id)
            if not record or (
                record["tenant_id"] != principal.tenant_id
                or record["learner_id"] != principal.user_id
                or record["course_id"] != str(course_id)
            ):
                raise ConversationAccessError("Conversation thread not found")
            replay = record["answers"].get(idempotency_key)
            if replay is not None:
                return ConversationTurn(thread_id=thread_id, history=[], replay=replay)
            history = list(record["messages"][-self.history_message_limit :])
            if not any(
                item.get("idempotency_key") == f"{idempotency_key}:user"
                for item in record["messages"]
            ):
                record["messages"].append(
                    {
                        "role": "user",
                        "content": question,
                        "idempotency_key": f"{idempotency_key}:user",
                    }
                )
            return ConversationTurn(
                thread_id=thread_id,
                history=[ConversationMessage(item["role"], item["content"]) for item in history],
            )

    def finish_turn(
        self,
        *,
        principal: Principal,
        course_id: UUID | str,
        thread_id: UUID,
        answer: TutorAnswer,
        idempotency_key: str,
    ) -> TutorAnswer:
        with self._lock:
            record = self._threads.get(thread_id)
            if not record or record["learner_id"] != principal.user_id:
                raise ConversationAccessError("Conversation thread not found")
            replay = record["answers"].get(idempotency_key)
            if replay is not None:
                return replay
            answer = answer.model_copy(update={"thread_id": thread_id})
            record["answers"][idempotency_key] = answer
            record["messages"].append(
                {
                    "role": "assistant",
                    "content": answer.answer,
                    "idempotency_key": f"{idempotency_key}:assistant",
                }
            )
            return answer


@lru_cache
def get_conversation_memory() -> ConversationMemory:
    if get_settings().use_postgres:
        return PostgresConversationMemory()
    return InMemoryConversationMemory()
