# Chiron Railway fast-track

Mục tiêu release đầu: web + authenticated API + PostgreSQL/Redis/Qdrant + hybrid retrieval + tutor. Reranker và Graph-lite không chặn release; giữ sau feature flag.

## Production baseline

- `RERANK_ENABLED=false`
- `GRAPH_LITE_ENABLED=false`
- `RETRIEVAL_MAX_SUBQUERIES=1`
- Groq main, Gemini fallback chỉ cho sensitivity được phép
- PostgreSQL runtime dùng non-owner role; migration dùng `DATABASE_ADMIN_URL`
- Qdrant collection phải khớp embedding manifest `chiron_chunks_v1 / multilingual-e5-large-mean-batch32-v2`

## Railway services

1. PostgreSQL managed service.
2. Redis managed service.
3. Qdrant Docker service với volume mount `/qdrant/storage`.
4. `chiron-api`: root directory `/services/api`, Dockerfile auto-detected.
5. `chiron-worker`: root directory `/services/worker`, Dockerfile auto-detected.
6. `chiron-web`: root directory `/`; set `RAILWAY_DOCKERFILE_PATH=/apps/web/Dockerfile`.

API settings:

- Pre-deploy command: `alembic upgrade head`
- Start command: lấy từ Dockerfile
- Healthcheck path: `/readyz`
- Healthcheck timeout: 300 seconds
- Public domain: API chỉ cần public nếu không dùng hoàn toàn qua Next.js BFF.

Worker settings:

- Start command: `celery -A chiron_worker.app:celery_app worker --loglevel=INFO --pool=threads --concurrency=2`
- Không chạy bulk corpus indexing trong production request path.

Web settings:

- Healthcheck path: `/`
- `API_BASE_URL` trỏ tới private API URL.
- `WEB_BASE_URL` là public HTTPS origin chính xác của web; mutation BFF từ origin khác bị từ chối.

Biến môi trường tối thiểu nằm trong `deploy/railway.env.example`. Không commit secret thật.

## Release order

1. Tạo PostgreSQL, Redis và Qdrant volume.
2. Restore Qdrant snapshot và kiểm tra collection/vector count.
3. Deploy API; pre-deploy migration phải dùng owner URL, runtime dùng non-owner URL.
4. Deploy worker và chờ model warm.
5. Deploy web với private API URL.
6. Chạy smoke: `/readyz` -> login -> `/auth/me` -> retrieval có citation -> tutor.

## Go/no-go gate

Go khi:

- `/readyz` trả 200 với PostgreSQL, Redis, Qdrant ready.
- Alembic ở head và runtime role không phải owner/superuser.
- Qdrant point count khớp manifest; citation mở đúng locator.
- Login/refresh/logout và một retrieval/tutor flow pass.
- `GRAPH_LITE_ENABLED=false`, `RERANK_ENABLED=false` ở release đầu.

No-go khi migration dùng runtime role, Qdrant thiếu snapshot, collection/model version lệch, hoặc readiness 503.
