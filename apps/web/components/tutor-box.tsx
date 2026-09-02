"use client";

import { ArrowUp, CircleNotch, Lightning, Quotes, Sparkle } from "@phosphor-icons/react";
import { FormEvent, useRef, useEffect, useState } from "react";

type Citation = {
  title: string;
  locator: string;
  excerpt?: string;
  source_span_id?: string;
};

type Message = {
  id: string;
  role: "user" | "assistant";
  content: string;
  provider?: string;
  citations?: Citation[];
};

const SUGGESTED_QUESTIONS = [
  "Vì sao RRF không dùng raw score?",
  "Khi nào nên dùng Graph-Lite routing thay vì direct retrieval?",
  "Cách xử lý rủi ro Context Stuffing trong RAG?",
];

export function TutorBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [threadId, setThreadId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const chatBottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatBottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function submitQuestion(qText: string) {
    if (qText.trim().length < 3 || loading) return;
    const currentQuestion = qText.trim();
    const requestId = crypto.randomUUID();
    setMessages((current) => [
      ...current,
      { id: `${requestId}:user`, role: "user", content: currentQuestion },
    ]);
    setQuestion("");
    setError(null);
    setLoading(true);
    try {
      const response = await fetch("/api/tutor", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Idempotency-Key": requestId,
        },
        body: JSON.stringify({ question: currentQuestion, threadId }),
      });
      if (!response.ok) {
        const errJson = await response.json().catch(() => ({}));
        throw new Error(errJson.error || errJson.detail || "Tutor unavailable");
      }
      const data = await response.json();
      setThreadId(data.thread_id);
      setMessages((current) => [
        ...current,
        {
          id: `${requestId}:assistant`,
          role: "assistant",
          content: data.answer,
          provider: data.provider,
          citations: data.citations && data.citations.length > 0 ? data.citations : undefined,
        },
      ]);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Tutor đang tạm thời không khả dụng. Vui lòng thử lại sau.",
      );
    } finally {
      setLoading(false);
    }
  }

  function handleFormSubmit(event: FormEvent) {
    event.preventDefault();
    submitQuestion(question);
  }

  return (
    <section className="tutor-panel" aria-labelledby="tutor-title">
      <div className="panel-heading">
        <div>
          <span style={{ display: "inline-flex", alignItems: "center", gap: "0.25rem" }}>
            <Sparkle size={14} weight="fill" /> Grounded AI Tutor Agent
          </span>
          <h2 id="tutor-title">Hỏi đáp thông minh từ giáo trình</h2>
        </div>
      </div>
      {messages.length ? (
        <div className="tutor-answer" aria-live="polite" style={{ maxHeight: "360px", overflowY: "auto" }}>
          {messages.map((message) => (
            <div
              key={message.id}
              className={message.role === "user" ? "tutor-question" : undefined}
              style={{
                marginBottom: "1rem",
                padding: "0.75rem 1rem",
                borderRadius: "0.5rem",
                background: message.role === "user" ? "var(--surface-sunken, rgba(255,255,255,0.04))" : "var(--surface-elevated, rgba(255,255,255,0.08))",
                borderLeft: message.role === "assistant" ? "3px solid #38bdf8" : "none",
              }}
            >
              {message.role === "assistant" && (
                <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.35rem", fontSize: "0.75rem", color: "#38bdf8", fontWeight: 600 }}>
                  <Sparkle size={13} weight="fill" /> Chiron AI Tutor
                  {message.provider && message.provider !== "mock" && (
                    <span style={{ fontSize: "0.7rem", color: "var(--text-muted, #94a3b8)", fontWeight: 400 }}>
                      ({message.provider})
                    </span>
                  )}
                </div>
              )}
              <div style={{ whiteSpace: "pre-line", lineHeight: 1.6 }}>{message.content}</div>
              {message.citations && message.citations.length > 0 && (
                <div style={{ marginTop: "0.5rem", display: "flex", flexDirection: "column", gap: "0.35rem" }}>
                  <div style={{ fontSize: "0.75rem", color: "var(--text-muted, #94a3b8)", fontWeight: 500 }}>
                    Nguồn trích dẫn:
                  </div>
                  {message.citations.map((c, i) => (
                    <button
                      key={i}
                      type="button"
                      style={{
                        textAlign: "left",
                        fontSize: "0.75rem",
                        padding: "0.3rem 0.5rem",
                        borderRadius: "0.25rem",
                        background: "rgba(56, 189, 248, 0.08)",
                        border: "1px solid rgba(56, 189, 248, 0.2)",
                        color: "#38bdf8",
                        cursor: "pointer",
                      }}
                      title={c.excerpt}
                    >
                      <Quotes size={13} style={{ display: "inline", marginRight: "0.25rem" }} />
                      <strong>{c.title}</strong> — {c.locator}
                    </button>
                  ))}
                </div>
              )}
            </div>
          ))}
          {loading && (
            <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", padding: "0.75rem", color: "#38bdf8", fontSize: "0.85rem" }}>
              <CircleNotch size={18} className="animate-spin" />
              <span>Chiron AI đang tra cứu giáo trình và suy luận câu trả lời...</span>
            </div>
          )}
          {error && <p role="alert" style={{ color: "#f87171", fontSize: "0.85rem", marginTop: "0.5rem" }}>{error}</p>}
          <div ref={chatBottomRef} />
        </div>
      ) : (
        <div className="tutor-empty">
          <Quotes size={26} />
          <p>
            Hỏi về bất kỳ khái niệm RAG / AI nào trong khóa học. AI Tutor sẽ tra cứu tài liệu và giải thích chi tiết có trích dẫn.
          </p>
          <div style={{ marginTop: "0.75rem", display: "flex", flexDirection: "column", gap: "0.35rem", width: "100%" }}>
            <span style={{ fontSize: "0.75rem", color: "var(--text-muted, #94a3b8)" }}>Gợi ý câu hỏi:</span>
            {SUGGESTED_QUESTIONS.map((sug, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => submitQuestion(sug)}
                style={{
                  textAlign: "left",
                  fontSize: "0.78rem",
                  padding: "0.35rem 0.6rem",
                  borderRadius: "0.35rem",
                  background: "rgba(255,255,255,0.05)",
                  border: "1px solid rgba(255,255,255,0.1)",
                  color: "inherit",
                  cursor: "pointer",
                  display: "flex",
                  alignItems: "center",
                  gap: "0.35rem",
                }}
              >
                <Lightning size={13} color="#f59e0b" weight="fill" /> {sug}
              </button>
            ))}
          </div>
        </div>
      )}
      <form onSubmit={handleFormSubmit} className="tutor-form" style={{ marginTop: "0.75rem" }}>
        <label htmlFor="tutor-question" className="sr-only">Câu hỏi của bạn</label>
        <div>
          <input
            id="tutor-question"
            value={question}
            onChange={(event) => setQuestion(event.target.value)}
            placeholder="Đặt câu hỏi về RAG, Chunking, Hybrid Search..."
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading || question.trim().length < 3}
            aria-label="Gửi câu hỏi"
          >
            {loading ? <CircleNotch size={18} className="animate-spin" /> : <ArrowUp size={18} weight="bold" />}
          </button>
        </div>
      </form>
    </section>
  );
}
