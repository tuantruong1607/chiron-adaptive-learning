import urllib.request
import json
import sys

# Ensure UTF-8 output on Windows terminal
sys.stdout.reconfigure(encoding='utf-8')

tests = [
    ("API Health Check", "http://localhost:8000/healthz"),
    ("API Readiness Check", "http://localhost:8000/readyz"),
    ("Web Homepage", "http://localhost:3001/"),
    ("Web Exams (100 Questions Mock)", "http://localhost:3001/exams"),
    ("Web Labs (Hybrid Search)", "http://localhost:3001/labs/hybrid-search"),
    ("API Mock Exam DE-01 (100 Questions)", "http://localhost:8000/api/v1/mock-exams/de-01"),
]

for name, url in tests:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Chiron-Probe/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read()
            extra = ""
            if "de-01" in url:
                parsed = json.loads(data.decode("utf-8"))
                q_count = len(parsed.get("questions", []))
                extra = f" -> Questions count: {q_count}"
            print(f"[OK] {name}: HTTP {resp.status}{extra}")
    except Exception as e:
        print(f"[ERR] {name}: Failed -> {e}")
