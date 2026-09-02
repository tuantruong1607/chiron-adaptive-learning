import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Login to get token
login_data = json.dumps({
    "tenant_slug": "chiron-demo",
    "email": "learner@chiron.local",
    "password": "chiron-demo-2026"
}).encode("utf-8")

req = urllib.request.Request(
    "http://localhost:8000/api/v1/auth/token",
    data=login_data,
    headers={"Content-Type": "application/json", "User-Agent": "Chiron-Test/1.0"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        token = res.get("access_token")
        print("[OK] Auth Token acquired successfully!")

        # 2. Call Tutor API with a real conceptual question
        tutor_data = json.dumps({
            "course": "rag-intensive",
            "question": "Vì sao mô hình Hybrid Search lại cần kết hợp Dense Retrieval và Sparse BM25?",
            "data_sensitivity": "public"
        }).encode("utf-8")

        tutor_req = urllib.request.Request(
            "http://localhost:8000/api/v1/tutor",
            data=tutor_data,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Idempotency-Key": "test-live-tutor-key-001",
                "User-Agent": "Chiron-Test/1.0"
            },
            method="POST"
        )

        print("[...] Calling Live Tutor Agent with Real LLM...")
        with urllib.request.urlopen(tutor_req, timeout=25) as tutor_resp:
            answer_payload = json.loads(tutor_resp.read().decode("utf-8"))
            print(f"[OK] Live Tutor Response Received! (Provider: {answer_payload.get('provider')})")
            print("--------------------------------------------------")
            print("Câu trả lời từ Real LLM Agent:")
            print(answer_payload.get("answer"))
            print("--------------------------------------------------")
            print(f"Citations count: {len(answer_payload.get('citations', []))}")
            for c in answer_payload.get("citations", []):
                print(f" - [{c.get('source_span_id')}]: {c.get('title')} ({c.get('locator')})")
except Exception as e:
    print(f"[ERR] Tutor live test failed: {e}")
