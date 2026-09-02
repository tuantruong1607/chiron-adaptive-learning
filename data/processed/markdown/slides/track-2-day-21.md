---
schema_version: 1
course_id: rag-intensive
document_id: "8c38b2e3-0a50-5498-b4c6-30862d0a9301"
document_version_id: "4f68fa7c-e4ed-5a18-abaf-ea7a94ac3cf6"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "CI/CD for AI Systems"
source_file: "track 2 - day 21.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 21.pdf"
source_sha256: "d94dc5799bcf94e7c9a35390df217fae6eca7f09a9e7ac0ad132e725583c36de"
parser_version: chiron-structured-markdown-v1
page_count: 40
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":40}"
language: vi
---

# CI/CD for AI Systems

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"de9a0dd9-b3b2-5628-883d-76417ddfe3f0","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"CI/CD for AI Systems","extraction_method":"pdf-text-layer"},"checksum":"bf820be1398b3a9872c4c65a21403e63e86763edfc44e028e28cfa199a7d3779"} -->

## Slide 1 - CI/CD for AI Systems

Tự động hoá vòng đời model: từ thí nghiệm đến production AICB-P2T2 · Ngày 21 · Chương 5: Vận Hành Giảng viên · VinUniversity · Phase 2 · Track 2 · Tuần 5

---

<!-- chiron-source-span: {"source_span_id":"d0207a98-c44b-543e-b898-1f220e5dae5c","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃY SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"d4d4a6cd7d9647e96461fd7e4331f20f8526e3f97ad532850ffb751e181a6343"} -->

## Slide 2 - HÃY SUY NGHĨ...

"Code thay đổi mỗi ngày — model cũng vậy. CI/CD cho AI khác gì CI/CD cho software thông thường?"

### Case Study
Một team deploy model mới mỗi tuần bằng tay.

- 3 lần model bị regression nhưng không ai biết đến khi user phản hồi.

- Sau khi có CI/CD pipeline: ZERO regression lọt production trong 6 tháng.
Giữ câu hỏi này trong đầu suốt buổi học hôm nay 2 / 38

---

<!-- chiron-source-span: {"source_span_id":"9afacd35-26af-546a-8bef-86b8adc20a4c","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"16b72a1bc313ba0932d8ab1681ce7cde811131334f0693da495cb298a5a4404b"} -->

## Slide 3 - Nội Dung Bài Học

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 3 / 38 01 MLflow Experiment Tracking & Model Registry 30 min 02 DVC Data Version Control & Pipelines 30 min 03 GitHub Actions CI Pipeline cho AI 30 min 04 CD Model Deployment Strategies 20 min 05 Testing Pyramid cho AI Systems 15 min 06 MLflow Model Serving & A/B Testing 15 min 07 Live Demo: Full CI/CD Pipeline 20 min 08 Key Takeaways & Preview Ngày 22 10 min

---

<!-- chiron-source-span: {"source_span_id":"2dc80dc7-0e13-566f-a3ed-ed79508aa469","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Bài Học","extraction_method":"pdf-text-layer"},"checksum":"cebe417991b20765055b9a03557a1674af9a049b20312e0b34b0f1068b51ee31"} -->

## Slide 4 - Mục Tiêu Bài Học

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 4 / 38

### Sau buổi học này, bạn sẽ có thể
01 Setup MLflow tracking server và log experiments một cách có hệ thống, so sánh runs qua UI. 02 Implement DVC cho data versioning, tạo reproducible ML pipelines với dvc.yaml. 03 Build GitHub Actions CI/CD pipeline tự động test, train, eval và deploy AI models. 04 Áp dụng các deployment strategies (canary, blue/green, shadow) để giảm rủi ro khi release model mới.

---

<!-- chiron-source-span: {"source_span_id":"8c9bb1e8-26cb-5bbc-82f9-7491bf202de2","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"21298eb0ed1eb4cf40317934251aedc2bb8aa9df06297f8da3b338808c9b4d21"} -->

## Slide 5 - Deliverable Cuối Ngày

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 5 / 38 MLflow tracking server + DVC-versioned dataset + GitHub Actions pipeline chạy auto test/deploy MLflow UI ≥ 3 tracked experiments với params, metrics, và artifacts được log đầy đủ DVC Pipeline 3 stages (prepare → train → evaluate) chạy dvc repro thành công GitHub Actions Workflow pass: test → train → eval gate → deploy trên repo thực Model Registry Model được register trong MLflow Registry và promote lên Staging

---

<!-- chiron-source-span: {"source_span_id":"1ff3d08c-c79e-59fe-b45f-0df35427aee4","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"MLflow: Experiment Tracking & Model Registry","extraction_method":"pdf-text-layer"},"checksum":"a06e79a7457bf7aa75380caa09ca621e3e3d2f177c30f3ef863b9990aa1a04a3"} -->

## Slide 6 - MLflow: Experiment Tracking & Model Registry

01 Theo dõi, so sánh, và quản lý vòng đời model một cách hệ thống

---

<!-- chiron-source-span: {"source_span_id":"8b95114a-3e7a-5e77-b025-2c3d3fe9f624","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"MLflow: 4 Thành Phần Cốt Lõi","extraction_method":"pdf-text-layer"},"checksum":"e41237fff0da303e4c1d64706076b75f12aac38e4d9f7dda4f77b88a557d028b"} -->

## Slide 7 - MLflow: 4 Thành Phần Cốt Lõi

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 7 / 38 MLflow là open-source platform để quản lý toàn bộ vòng đời ML — từ thí nghiệm đến production. Tracking Log parameters, metrics, artifacts và source code. So sánh runs qua web UI hoặc API. Projects Đóng gói code để reproducibility. Chạy lại bất kỳ run nào trên bất kỳ platform nào. Models Chuẩn hoá format packaging (mlflow.sklearn,.pytorch,.pyfunc). Deploy lên nhiều nền tảng khác nhau. Registry Quản lý lifecycle: None → Staging → Production → Archived. Workflow review & approve trước khi promote.

---

<!-- chiron-source-span: {"source_span_id":"3a655c11-146d-561c-a6ac-f22c892e2da5","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"MLflow Tracking: Log Experiments","extraction_method":"pdf-text-layer"},"checksum":"15721f0ac6958681fced8ea826dfa2a852516be31a8cf609eb0ad2474919e8c3"} -->

## Slide 8 - MLflow Tracking: Log Experiments

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 8 / 38

```text
import mlflow
from mlflow.models import infer_signature
mlflow.set_experiment("sentiment-v2")
with mlflow.start_run(run_name="lr_0001_ep10"):
```
# Log hyperparameters mlflow.log_param("lr", 0.001) mlflow.log_param("epochs", 10) mlflow.log_param("batch_size", 32) # Training loop

### for epoch in range(10)
loss = train_one_epoch(model, loader) acc = evaluate(model, val_loader) mlflow.log_metric("train_loss", loss, step=epoch) mlflow.log_metric("val_accuracy", acc, step=epoch) # Save artifacts & model mlflow.log_artifact("confusion_matrix.png") mlflow.sklearn.log_model( model, "model", signature=infer_signature(X_val, y_pred) ) Params Hyperparameters, data version, model config — bất biến trong một run Metrics Loss, accuracy — log tại mỗi step/epoch để vẽ đồ thị so sánh Artifacts Plots, confusion matrix, config files lưu cùng run để trace back Signature Input/output schema tự động suy diễn — cần thiết cho serving

---

<!-- chiron-source-span: {"source_span_id":"de769474-4a57-5de8-9dcd-ff8737a93b02","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"MLflow: So Sánh Runs & LLM Autolog","extraction_method":"pdf-text-layer"},"checksum":"88583bc8ff1cb6f1eba5de28eea65fe5a23fee2ac0b22d90d2ce6c1f7fadadce"} -->

## Slide 9 - MLflow: So Sánh Runs & LLM Autolog

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 9 / 38 So Sánh Runs trong MLflow UI

- Filter & sort runs theo bất kỳ metric nào

- Parallel Coordinates Chart — thấy ngay lr nào cho
loss thấp nhất

- Scatter Plot — compare accuracy vs latency

- Diff params giữa 2 runs để debug regression

- Download artifacts, view confusion matrix trực tiếp trên
UI LLM Autolog (MLflow 2.8+) # OpenAI autolog mlflow.openai.autolog() # LangChain autolog mlflow.langchain.autolog()

### # Tự động log
# - Prompt templates # - Input / output content # - Token usage (prompt, completion) # - Latency per call # - Model name & version # - Retrieval context (RAG)

- Không cần sửa code, chỉ cần gọi autolog() trước khi run

- Hỗ trợ: OpenAI, LangChain, LlamaIndex, Anthropic Claude

---

<!-- chiron-source-span: {"source_span_id":"0f45714c-7e7b-598a-b7bb-08838efba5f4","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"MLflow Model Registry: Lifecycle Management","extraction_method":"pdf-text-layer"},"checksum":"ed5b0b0dae45a3f2984af793521a0babf9a19accbe2568df3c44ed14512628c0"} -->

## Slide 10 - MLflow Model Registry: Lifecycle Management

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 10 / 38 None register Staging approve Production retire Archived reject ↩ Mỗi version Có stage riêng. Nhiều version cùng tồn tại — team có thể A/B test champion vs challenger. Annotations Ghi lý do promote/reject, link đến eval report, người approve — full audit trail. Alias champion = Production version, challenger = A/B candidate. Load bằng tên alias. Webhook Trigger CI/CD khi model chuyển stage — tự động deploy staging khi Staging được approve.

---

<!-- chiron-source-span: {"source_span_id":"3728600d-99d4-5b40-b9a8-be8fa14fa903","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"MLflow Registry: API & Best Practices","extraction_method":"pdf-text-layer"},"checksum":"e61d35a2e63ea6d7d504d313b85adedb623363ea34d2d06fe51cb4fa1c9facf3"} -->

## Slide 11 - MLflow Registry: API & Best Practices

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 11 / 38

```text
import mlflow
from mlflow import MlflowClient
client = MlflowClient()
```
# Register model từ run result = mlflow.register_model( model_uri=f"runs:/{run_id}/model", name="sentiment_classifier" ) # Promote to Staging client.transition_model_version_stage( name="sentiment_classifier", version=result.version, stage="Staging" ) # Load model bằng alias "champion" model = mlflow.sklearn.load_model( model_uri="models:/sentiment_classifier@champion" ) Naming Convention Dùng tên model rõ ràng: {task}_{arch}_{version} VD: sentiment_bert_base, fraud_lgbm_v2 Tag Strategy Tag với: data_version, git_commit, eval_accuracy

- Trace back ngay khi có incident
Approval Workflow Require ≥1 reviewer approve trước khi promote Staging

- Production
Dùng webhook để notify Slack Rollback Plan Luôn giữ previous Production version ở Archived

- 1 API call để rollback nếu cần

---

<!-- chiron-source-span: {"source_span_id":"52c530d2-d8b6-5a1b-8870-1c585ffafffa","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"DVC: Data Version Control","extraction_method":"pdf-text-layer"},"checksum":"5be908cf150f2b0bb64920f3a2403c153c3535e77e94829785ca16bf28995d68"} -->

## Slide 12 - DVC: Data Version Control

02 Git cho data — versioning, pipelines, và reproducibility

---

<!-- chiron-source-span: {"source_span_id":"ca09c0ab-d467-5607-bfa0-c66c9467a91b","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Vấn Đề: Data Không Có Version Control","extraction_method":"pdf-text-layer"},"checksum":"0e5e734ce11de280d5325778ddcf484a382d9c7fe0e08f86b69a6815e8f2e8fa"} -->

## Slide 13 - Vấn Đề: Data Không Có Version Control

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 13 / 38 ? Không tái tạo được kết quả "Hôm qua model đạt 92% nhưng hôm nay chỉ còn 88%" — không biết data đã thay đổi hay code? ! Merge conflict với data lớn Git không track được file GB. Team dùng shared folder → overwrite nhau, không có history. × Experiment không gắn với data MLflow log metrics nhưng không biết train trên data version nào → A/B comparison vô nghĩa. $ Storage lãng phí Mỗi người copy data riêng → duplicates tốn hàng chục GB. Không có deduplication.

---

<!-- chiron-source-span: {"source_span_id":"89402ff3-004f-587c-8ebc-c886fcc82fed","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"DVC: Git cho Data","extraction_method":"pdf-text-layer"},"checksum":"7d83b49d4d516b31cf6d869ac2deb7a800094ba43f536a4653e7bd313a042e02"} -->

## Slide 14 - DVC: Git cho Data

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 14 / 38 # 1. Khởi tạo DVC trong repo git init && dvc init # 2. Add data file (tạo.dvc pointer) dvc add data/training_set.parquet # → Tạo data/training_set.parquet.dvc # → Thêm data/ vào.gitignore tự động # 3. Commit.dvc file vào git git add data/training_set.parquet.dvc.gitignore git commit -m "track training dataset v1" # 4. Push data lên remote storage dvc push # 5. Team member pull data git clone <repo> dvc pull # download đúng version data Pointer File (.dvc) File nhỏ lưu hash của data. Git track.dvc file → checkout code = checkout data đúng version. Content-Addressable Data lưu theo hash nội dung → không tốn dung lượng cho duplicates dù có 100 versions. Remote Supports Amazon S3, Google GCS, Azure Blob, SSH server, HDFS — cùng API dvc push/pull. Offline-first Làm việc local không cần mạng. Sync remote khi cần — giống git push/pull.

---

<!-- chiron-source-span: {"source_span_id":"aca5181d-bf2b-5d77-a5ab-694a730cc5b5","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"DVC Remote Storage: Cấu Hình","extraction_method":"pdf-text-layer"},"checksum":"b3615948c41a1fa08d844625be22560bae3862f34d0e4a2561fd4a94f3644704"} -->

## Slide 15 - DVC Remote Storage: Cấu Hình

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 15 / 38 # Setup S3 remote (khuyến nghị cho production) dvc remote add -d myremote s3://my-bucket/dvc-store dvc remote modify myremote region us-east-1 # Google Cloud Storage dvc remote add gcs_remote gs://my-gcs-bucket/data # Azure Blob Storage dvc remote add azure_remote azure://mycontainer/data # SSH server (on-premise) dvc remote add ssh_remote ssh://user@server:/path/data # Xem danh sách remotes dvc remote list # Push / pull dvc push # upload tất cả data dvc pull data/train.parquet # pull một file cụ thể Best Practices cho Remote Storage

- Dùng S3/GCS cho team production — có
versioning và ACL

- Cấu hình IAM role cho CI/CD, không dùng
access key cứng

- Bật S3 server-side encryption cho data nhạy cảm

- Dùng dvc remote modify --local để lưu
credentials local (không commit)

- Set lifecycle policy trên S3: move cold data sang
Glacier sau 90 ngày

- Cache locally với DVCCACHE — tránh re-
download khi checkout branches

- Tách remote: dev (fast) và archive (cheap cold
storage)

---

<!-- chiron-source-span: {"source_span_id":"2503ca37-1777-52b5-97a4-8950e35a7789","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"DVC Pipeline: Reproducible Workflows","extraction_method":"pdf-text-layer"},"checksum":"2ad2a15222fd4ff00faac9a16fa4ca8e56e5e1cf548053e887a6d6d6daa1654a"} -->

## Slide 16 - DVC Pipeline: Reproducible Workflows

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 16 / 38 # dvc.yaml

### stages

### prepare
cmd: python src/prepare.py

### deps
- data/raw/
- src/prepare.py

### outs
- data/processed/

### train
cmd: python src/train.py --lr ${params.lr}

### deps
- data/processed/
- src/train.py
- params.yaml

### outs
- models/model.pkl

### metrics

### - metrics.json
cache: false

### evaluate
cmd: python src/evaluate.py

### deps
- models/model.pkl
- data/test/

### metrics

### - eval_metrics.json
cache: false dvc repro Chạy lại stages bị stale (deps thay đổi). Smart caching — bỏ qua stages chưa thay đổi. dvc dag Visualize pipeline DAG trong terminal. Thấy ngay dependency graph. dvc metrics show So sánh metrics.json giữa các lần chạy. Hiện diff rõ ràng. dvc params diff HEAD~1 So sánh params giữa current và previous commit.

---

<!-- chiron-source-span: {"source_span_id":"de707692-d8cc-58cd-adb1-5c7444b33469","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"DVC Experiments: So Sánh Hyperparameters","extraction_method":"pdf-text-layer"},"checksum":"0b3f4a6f413b4722dd7a809f44298844ae4f4e42c43c72f7896789befa0a78fa"} -->

## Slide 17 - DVC Experiments: So Sánh Hyperparameters

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 17 / 38 # Chạy experiment với param khác nhau dvc exp run --set-param lr=0.001 dvc exp run --set-param lr=0.01 dvc exp run --set-param lr=0.1 --set-param epochs=20 # Chạy nhiều experiments song song dvc exp run --set-param lr=0.001,0.01,0.1 --jobs 3 # Xem kết quả so sánh dvc exp show # ┏━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┓ # Experiment lr epochs accuracy ┃ ┃ ┃ ┃ ┃ # ┡━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━┩ # │ workspace │ 0.01 │ 10 │ 0.924 │ # │ exp-abc123 │ 0.001 │ 10 │ 0.918 │ # │ exp-def456 │ 0.1 │ 10 │ 0.891 │ # │ exp-ghi789 │ 0.1 │ 20 │ 0.912 │ # Apply kết quả tốt nhất vào workspace dvc exp apply exp-abc123 # Persist experiment thành branch dvc exp branch exp-abc123 best-lr-001 Git + DVC Workflow

- git commit → code version

- dvc push → data version

- .dvc file liên kết 2 layer lại

- Bất kỳ ai git clone + dvc pull

- reproduce y hệt kết quả

### DVC vs MLflow
DVC: pipeline + data versioning MLflow: metrics + model registry

- Dùng cả hai, không chọn một

---

<!-- chiron-source-span: {"source_span_id":"63a832a9-1382-57e5-b384-b47122bf3c32","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"GitHub Actions: CI Pipeline cho AI","extraction_method":"pdf-text-layer"},"checksum":"369367b67756493835ad4050e3347cca97461dd533bbdc6a75b253b3de6acbec"} -->

## Slide 18 - GitHub Actions: CI Pipeline cho AI

03 Tự động hoá test, train và eval mỗi khi code thay đổi

---

<!-- chiron-source-span: {"source_span_id":"240e7d88-0bb1-57ad-8a58-fb8de1b1b300","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"CI/CD cho AI: Khác Gì Software Thông Thường?","extraction_method":"pdf-text-layer"},"checksum":"16eec1248253f628ee1b06fc84357de0be8136b126e7de452578cdcb143d4760"} -->

## Slide 19 - CI/CD cho AI: Khác Gì Software Thông Thường?

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 19 / 38 Khía cạnh CI/CD Software truyền thống CI/CD cho AI Artifact Binary / Docker image Model weights + metadata Test Unit test, integration test + Model eval, data validation Versioning Git cho code Git + DVC cho code + data Deploy Deterministic — code giống nhau Non-deterministic — cần eval gate Rollback trigger Error rate tăng + Accuracy drop, bias metrics Pipeline input Code changes only Code hoặc data changes Thời gian build Vài phút Vài phút → vài giờ (training)

---

<!-- chiron-source-span: {"source_span_id":"bcf3d330-1796-5982-8531-4864bb2c56ef","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"CI Pipeline Architecture cho AI Projects","extraction_method":"pdf-text-layer"},"checksum":"e71117552a69cd6e2d7a9001e38df5eda5f8200ab9106ef904423401381f320a"} -->

## Slide 20 - CI Pipeline Architecture cho AI Projects

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 20 / 38 git push / PR Data Validation Model Training Eval Gate Deploy (if pass) Block Deploy × accuracy drop >2% Trigger on: push (main), pull_request (main) → mọi PR đều qua pipeline trước khi merge Path Filter Training job chỉ chạy khi data/ hoặc src/ thay đổi — tránh retrain khi sửa docs Fail Fast Data Validation fail → dừng pipeline ngay, không chạy training tốn GPU Eval Gate So sánh new model vs production baseline — block deploy nếu accuracy drop >2%

---

<!-- chiron-source-span: {"source_span_id":"18dc89c5-46cf-59a6-8063-95e176146653","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"GitHub Actions: Cấu Trúc Workflow YAML","extraction_method":"pdf-text-layer"},"checksum":"75bc4b576033a077f8ac2cc031490e698145a95c72e920844c71fda22758b1a6"} -->

## Slide 21 - GitHub Actions: Cấu Trúc Workflow YAML

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 21 / 38 name: AI CI/CD Pipeline

### on

### push
branches: [main]

### pull_request
branches: [main]

### env
MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }} AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}

### jobs

### data-validation
runs-on: ubuntu-latest

### steps
- uses: actions/checkout@v4
- uses: actions/setup-python@v5
with: { python-version: "3.11" } - uses: actions/cache@v4

### with
path: ~/.cache/pip key: pip-${{ hashFiles('requirements.txt') }}

```text
- run: pip install -r requirements.txt
```
- run: dvc pull data/
- run: great_expectations checkpoint run data_quality
# Fail fast nếu data drift detected Secrets Management MLFLOW_TRACKING_URI, AWS keys → GitHub Secrets. KHÔNG hardcode trong workflow file. Dependency Cache actions/cache với key = hash(requirements.txt)

- Giảm 60-80% thời gian setup.
Job Dependencies needs: [data-validation] → training chỉ chạy khi validation pass. Sequential control flow. OIDC Federation Production: dùng OIDC thay vì long-lived AWS keys. Hết hạn sau mỗi run.

---

<!-- chiron-source-span: {"source_span_id":"7c15ce68-c423-56e9-9755-d450ffb0e67b","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"CI Job: Data Validation với Great Expectations","extraction_method":"pdf-text-layer"},"checksum":"580b2e294b7e4def4a9f661f1caa36aad1c6e74173a36d4b65086f3cf0d0a613"} -->

## Slide 22 - CI Job: Data Validation với Great Expectations

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 22 / 38 #.github/workflows/ai-cicd.yml (tiếp theo)

### train
needs: [data-validation] runs-on: ubuntu-latest if: | github.event_name == 'push' && contains(toJson(github.event.commits.*.modified), '"data/') || contains(toJson(github.event.commits.*.modified), '"src/')

### steps
- uses: actions/checkout@v4
- run: dvc pull data/
- run: dvc repro train
- run: |
mlflow run. --entry-point train \ -P lr=0.001 -P epochs=10 # great_expectations/checkpoints/data_quality.yml name: data_quality class_name: Checkpoint

### validations

### - batch_request
datasource_name: training_data expectation_suite_name: training.warning

### action_list
- name: store_validation_result
action: { class_name: StoreValidationResultAction } - name: send_slack_alert action: { class_name: SlackNotificationAction } Các kiểm tra Data Quality

- Schema validation: đúng columns, đúng
dtypes

- Null rate: mỗi column ≤ 5% null

- Value range: tuổi 0–120, price > 0

- Distribution drift: KL-divergence vs
baseline

- Duplicate rows < 0.1%

```text
• Label balance: minority class ≥ 10%
```

- Volume check: ≥ 10,000 rows mỗi batch

- Freshness: data không cũ hơn 7 ngày

---

<!-- chiron-source-span: {"source_span_id":"a2fae960-cefb-5b2e-b5ae-5b82c9a34b97","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"CI Job: Eval Gate — Safety Net Quan Trọng Nhất","extraction_method":"pdf-text-layer"},"checksum":"7773ad6e2ce879bc720e9ae950349f40a38c6c0ef0f17a46df23d3003963477d"} -->

## Slide 23 - CI Job: Eval Gate — Safety Net Quan Trọng Nhất

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 23 / 38 # compare_models.py

```text
import mlflow, sys, json
def eval_gate(new_model_uri, prod_model_uri,
threshold=0.02):
client = mlflow.MlflowClient()
```
# Load cả hai models new_model = mlflow.sklearn.load_model(new_model_uri) prod_model = mlflow.sklearn.load_model(prod_model_uri) # Evaluate trên held-out test set new_acc = evaluate(new_model, X_test, y_test) prod_acc = evaluate(prod_model, X_test, y_test) delta = new_acc - prod_acc

### print(f"New: {new_acc:.4f} | Prod: {prod_acc:.4f} | Δ={delta
+.4f}")

### if delta < -threshold
print(f"FAIL: accuracy drop {delta:.4f} > threshold {- threshold}") sys.exit(1) # GitHub Actions job fails → blocks deploy print("PASS: new model >= baseline - threshold")

### # GitHub Actions step
# - run: python compare_models.py # --new models:/sentiment/$(cat new_version.txt) # --prod models:/sentiment@champion # --threshold 0.02 Eval Gate Best Practices

- Dùng FIXED held-out test set — không
shuffle mỗi lần eval

- Track nhiều metrics: accuracy, F1, AUC,
latency P95

- Threshold khác nhau theo metric: accuracy
±2%, latency ±10%

- Log eval results vào MLflow để có history

- Comment kết quả vào PR để reviewer thấy

- Nếu pass borderline: yêu cầu manual
review thay vì auto-deploy

---

<!-- chiron-source-span: {"source_span_id":"8504abf7-7a2f-5cac-baed-a597918f0743","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"CI Best Practices cho AI Repositories","extraction_method":"pdf-text-layer"},"checksum":"48113297d9bed3e8fb4f8b06b66bb2fa28d1ac6509166cc53a9ff28209d31ce6"} -->

## Slide 24 - CI Best Practices cho AI Repositories

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 24 / 38 Secrets & Credentials GitHub Secrets cho MLFLOW_TRACKING_URI, AWS keys. Dùng OIDC federation cho production — không có long-lived keys. Caching Strategy

```text
actions/cache với pip (key=hash
requirements), DVC cache trên S3.
```
Self-hosted runner nếu cần GPU — tiết kiệm 10x cost. Matrix Builds Test trên Python 3.10, 3.11, 3.12. Matrix strategy cho AI: test across model sizes, CUDA versions. Conditional Execution Path filters: train job chỉ chạy khi src/ hoặc data/ thay đổi. Doc-only PR bỏ qua training → tiết kiệm tiền GPU. Parallelism Chạy unit test, lint, data validation song song (jobs độc lập). Fail fast: cancel running jobs khi một job fail. Notifications Slack webhook khi pipeline fail, khi eval gate block deploy. Post kết quả eval vào PR comment tự động.

---

<!-- chiron-source-span: {"source_span_id":"db6e29f5-1a42-5a8e-960c-74b6cf096f54","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"CD: Model Deployment Strategies","extraction_method":"pdf-text-layer"},"checksum":"76f804a1d22efbe5a61ec4986b83f316e207a76d3ce726519085b2d2079e6056"} -->

## Slide 25 - CD: Model Deployment Strategies

04 Giảm rủi ro khi deploy model mới vào production

---

<!-- chiron-source-span: {"source_span_id":"3f4508b1-886f-5003-a73e-742e2af12fa9","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"4 Deployment Strategies cho AI Models","extraction_method":"pdf-text-layer"},"checksum":"2ac2d9e2b9ec975d0b7215f955a8e5df3a5d01e2a514f585285125134a905629"} -->

## Slide 26 - 4 Deployment Strategies cho AI Models

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 26 / 38 Canary Cách hoạt động: Route 5% traffic → model mới, tăng dần khi healthy Phát hiện lỗi sớm, kiểm soát risk từng bước✓ Cần monitoring tốt, traffic split logic phức tạp✗ Blue/Green Cách hoạt động: Deploy v2 song song v1, switch load balancer khi ready Zero downtime, instant rollback qua load balancer✓ Tốn gấp đôi resource khi cả hai env chạy song song✗ Shadow Cách hoạt động: Model mới xử lý traffic nhưng không trả response Test với real traffic không ảnh hưởng user✓ Không test user reaction, tốn compute gấp đôi✗ Rolling Cách hoạt động: Thay từng pod một trong Kubernetes deployment Đơn giản, default K8s, không cần extra infra✓ Slow rollback, mixed versions trong quá trình deploy✗

---

<!-- chiron-source-span: {"source_span_id":"773ee54c-9002-5ec0-942e-3cb5e0c404f2","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Canary Deployment: Deep-Dive","extraction_method":"pdf-text-layer"},"checksum":"83446adc7aab4b4e5a833be424688c14bb99406d6b40d4c03dedfcbd1aff263f"} -->

## Slide 27 - Canary Deployment: Deep-Dive

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 27 / 38 Load Balancer (Istio / ALB) 95% 5% Model v1 (stable) Model v2 (canary) Monitor: P99 latency · accuracy · error rate

### Rollout Steps
5% traffic health check

- 
25% traffic health check

- 
50% traffic health check

- 
100% traffic health check Rollback trigger: P99 latency vượt threshold HOẶC accuracy drop >2% → auto rollback về v1

---

<!-- chiron-source-span: {"source_span_id":"6edb8862-7eb2-5f9f-b0d5-5c63add6e2da","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Blue/Green & Shadow Mode: Chi Tiết","extraction_method":"pdf-text-layer"},"checksum":"f05f156ee0c82a42cacb9cf36d5c0709a536913cdb66045cce98396b480a0171"} -->

## Slide 28 - Blue/Green & Shadow Mode: Chi Tiết

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 28 / 38 Blue/Green Deployment

- Deploy v2 hoàn toàn độc lập với v1 đang chạy

- Chạy smoke test & integration test trên v2

- Switch load balancer → toàn bộ traffic sang v2

- Keep v1 sống thêm 30 phút → instant rollback nếu cần

- Sau 30 phút stable → shutdown v1, giải phóng
resource Khi nào dùng: deploy lớn, cần zero downtime tuyệt đối Trade-off: tốn gấp đôi infrastructure cost trong khi switch Shadow Mode (Dark Launch)

- Request được forward tới CẢ HAI models

- Response của v1 trả về user như bình thường

- Response của v2 (shadow) chỉ được log, không trả
user

- So sánh outputs: latency, predictions, errors

- Hoàn toàn zero risk với user experience
Khi nào dùng: model thay đổi lớn, muốn validate trước Trade-off: tốn compute gấp đôi, không test user reaction

---

<!-- chiron-source-span: {"source_span_id":"5a4d3e5b-f24f-5228-aa9e-6dec4fdfbf61","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Multi-Environment CD Pipeline","extraction_method":"pdf-text-layer"},"checksum":"1fb5f5671225c50f3fe2a56645f008260a770fdcd1e4e7c04bdc7676a9591efd"} -->

## Slide 29 - Multi-Environment CD Pipeline

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 29 / 38 Development Auto deploy mọi commit Smoke test nhanh (< 2 min) Dữ liệu giả lập

- 
Staging Auto deploy khi dev pass Full integration tests Dữ liệu thật (subset) Eval gate vs baseline

- 
Production Manual approval required Canary deployment Monitor 30 phút Rollback plan ready GitOps cho AI với ArgoCD /

### Flux
Declarative deployment — mọi thay đổi infra đều qua git commit → auto-sync từ repo → rollback bằng git revert

---

<!-- chiron-source-span: {"source_span_id":"3b231880-1deb-5c4b-b8da-8d11b337d82b","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Testing Pyramid cho AI Systems","extraction_method":"pdf-text-layer"},"checksum":"1cd1d6815a1e93d5dd65434187eb1d4916a88d54a890aaf61041bd3d81fa9bac"} -->

## Slide 30 - Testing Pyramid cho AI Systems

05 Từ unit test đến load test — đảm bảo chất lượng ở mọi tầng

---

<!-- chiron-source-span: {"source_span_id":"03173b60-894c-5e41-b3a5-c4a791e20db4","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"AI Testing Pyramid: Tổng Quan","extraction_method":"pdf-text-layer"},"checksum":"215df748f12123985064c0464224fb4d52e8e550c078f7b9902fa9ee8f68c847"} -->

## Slide 31 - AI Testing Pyramid: Tổng Quan

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 31 / 38 Load Tests k6 / Locust P95 < 500ms tại 50 RPS Data Tests Great Expectations Schema, distribution, quality Model Tests pytest + custom scripts Behavioral, performance regression Integration Tests pytest End-to-end inference pipeline với sample inputs Unit Tests pytest (fast) Data preprocessing, tokenization, feature engineering

---

<!-- chiron-source-span: {"source_span_id":"fec304c9-986b-5a0f-92b3-0ef1a2e84499","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Unit Tests & Integration Tests","extraction_method":"pdf-text-layer"},"checksum":"52af8f8d35ce4bc63546e75560b507df9adc44d014c14ab3763d81b34eccb2f6"} -->

## Slide 32 - Unit Tests & Integration Tests

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 32 / 38 # Unit tests: test từng function độc lập

```text
import pytest
from src.preprocessing import clean_text, tokenize
def test_clean_text_removes_html():
assert clean_text("<b>hello</b>") == "hello"
def test_tokenize_max_length():
tokens = tokenize("word " * 600, max_len=512)
assert len(tokens) <= 512
def test_feature_engineering_no_leakage():
```
"""Test rằng feature engineer không dùng future data""" df = make_test_df(n=100) features = engineer_features(df, target_col="label") assert "label" not in features.columns # Integration tests: test toàn bộ pipeline

```text
def test_inference_pipeline_e2e():
```
"""Full pipeline: raw input → prediction""" payload = {"text": "This product is great!"} response = client.post("/predict", json=payload) assert response.status_code == 200 assert "label" in response.json() assert "confidence" in response.json() assert 0.0 <= response.json()["confidence"] <= 1.0 Checklist cho Unit Tests

- Test tất cả preprocessing steps riêng lẻ

- Test edge cases: empty input, null, max
length

- Test tokenization với special characters,
tiếng Việt

- Test feature engineering: không data
leakage

- Mock external calls (API, DB) trong unit
tests

- Coverage ≥ 80% cho src/ module

- Chạy dưới 30 giây cho toàn bộ unit test
suite

- Integration test: dùng fixture nhỏ (100
samples)

---

<!-- chiron-source-span: {"source_span_id":"7da6bfb9-a4cb-5913-bd6d-7f627f20b1be","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Model Tests · Data Tests · Load Tests","extraction_method":"pdf-text-layer"},"checksum":"4197348f1ba5f790cf45f6310fd047e961f866fb3d4090a568295a7878a5363c"} -->

## Slide 33 - Model Tests · Data Tests · Load Tests

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 33 / 38 Model Tests — Behavioral & Regression

- Behavioral: model PHẢI từ chối nội dung harmful

- Invariance: xoay ảnh 90° → prediction không đổi

- Directional: thêm 'not' vào câu → sentiment đổi chiều

- Regression: accuracy trên golden test set ≥ v_prev - 0.5%

- Fairness: accuracy gap giữa subgroups < 3%
Data Tests — Great Expectations

- Schema: đúng columns, đúng dtypes, không extra columns

- Completeness: null rate mỗi column ≤ threshold

- Distribution: KS test so với baseline distribution

- Volume: số rows trong expected range [min, max]

- Chạy trên mỗi new data version, log kết quả vào MLflow
Load Tests — k6 / Locust

- Baseline: 50 RPS, P95 < 500ms, error rate < 0.1%

- Stress test: tăng dần đến 500 RPS tìm breaking point

- Soak test: 50 RPS trong 1 giờ — check memory leak

- Spike test: 0 → 500 RPS đột ngột — check auto-scaling

- Fail pipeline nếu bất kỳ SLA nào bị vi phạm

---

<!-- chiron-source-span: {"source_span_id":"66c3aff3-4a75-5cb5-ac39-b2c6969d94a0","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"MLflow Model Serving & A/B Testing","extraction_method":"pdf-text-layer"},"checksum":"c2674b194b664e764323c22527b6331b96a0ca1f484e4b81ce7fe9c0b525c611"} -->

## Slide 34 - MLflow Model Serving & A/B Testing

06 Từ model registry đến production endpoint, A/B test và gradual rollout

---

<!-- chiron-source-span: {"source_span_id":"b90308ac-b4f3-5d28-b7cd-3083d02f67e4","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"MLflow Model Serving: Các Tuỳ Chọn","extraction_method":"pdf-text-layer"},"checksum":"4b1c4a850f0b88dabedeb1d196a5239e6b2288eaac3d7d44255b50430a3fc820"} -->

## Slide 35 - MLflow Model Serving: Các Tuỳ Chọn

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 35 / 38 # Local serving — phát triển và testing mlflow models serve \ -m "models:/sentiment_classifier/Production" \ -p 5000 --no-conda # Test endpoint

```text
curl -X POST http://localhost:5000/invocations \
```
-H "Content-Type: application/json" \ -d '{"inputs": [{"text": "Great product!"}]}' # Build Docker image mlflow models build-docker \ -m "models:/sentiment_classifier/Production" \ -n sentiment-serving:v1.0 # Deploy lên Kubernetes với KServe kubectl apply -f - <<EOF apiVersion: serving.kserve.io/v1beta1 kind: InferenceService

### metadata
name: sentiment-classifier

### spec

### predictor

### model
storageUri: "s3://models/sentiment/v1" modelFormat: { name: mlflow }

### resources
requests: { cpu: "1", memory: "2Gi" } EOF Local mlflow models serve Dành cho dev/test. Khởi động nhanh. Docker mlflow models build-docker Portable, dùng cho staging deploy. Cloud AWS SageMaker, Azure ML, Databricks Managed infrastructure, auto-scaling. Kubernetes Seldon Core, KServe Production-grade, custom scaling policy.

---

<!-- chiron-source-span: {"source_span_id":"496fc498-af3c-5752-a519-de4cd30b88a0","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"A/B Testing cho AI Models","extraction_method":"pdf-text-layer"},"checksum":"7b85ffa199dbe082c24700cd793ac4fb101c6e7a98f16e87d75074dd098f1131"} -->

## Slide 36 - A/B Testing cho AI Models

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 36 / 38

```text
import hashlib, mlflow
def route_request(user_id: str, pct_b: float = 0.1):
```
"""Route user to variant A or B deterministically.""" h = int(hashlib.md5(user_id.encode()).hexdigest(), 16)

```text
return "B" if (h% 100) < (pct_b * 100) else "A"
def predict(user_id: str, text: str):
variant = route_request(user_id)
model = model_b if variant == "B" else model_a
with mlflow.start_run(run_id=EXPERIMENT_RUN_ID):
prediction = model.predict([text])
```
# Log outcome for statistical analysis mlflow.log_metric(f"click_{variant}", 1) mlflow.log_metric(f"latency_{variant}", elapsed_ms)

```text
return prediction
```
# Statistical significance check

```text
from scipy import stats
chi2, p_value = stats.chi2_contingency(contingency_table)
```

### if p_value < 0.05
print(f"Statistically significant at 95% confidence") print(f"Winner: {'B' if ctr_b > ctr_a else 'A'}") Traffic Routing Hash user_id → deterministic assignment. Same user luôn thấy cùng variant (consistency). Sample Size Minimum 1,000 samples/variant trước khi kết luận. Dùng power analysis để tính trước. Significance Level p-value < 0.05 (95% confidence) để declare winner. Corridor cho multiple comparisons: Bonferroni. Metric Selection Primary: business KPI (CTR, revenue). Guardrail: latency P95, error rate không được tăng.

---

<!-- chiron-source-span: {"source_span_id":"ce201118-6f3c-562c-ab4f-56ba8e577257","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Live Demo: Full CI/CD Pipeline","extraction_method":"pdf-text-layer"},"checksum":"6a6f307a5ebad993166f6ef83325170458c4d470ebfe7c6cd38b4c11d47bc5dd"} -->

## Slide 37 - Live Demo: Full CI/CD Pipeline

07 git push → production trong 8 phút

---

<!-- chiron-source-span: {"source_span_id":"f457d2ea-bd67-5dcf-a48c-114617d20933","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Live Demo: Từ Code Push đến Production","extraction_method":"pdf-text-layer"},"checksum":"c6a9c9def63631758a4f5486688408265d037f6dcca221ff4e4ff885108ae5a9"} -->

## Slide 38 - Live Demo: Từ Code Push đến Production

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 38 / 38 01 git push → GitHub Actions trigger Push commit lên main. GitHub Actions workflow kích hoạt tự động. Quan sát Jobs chạy trong real-time. 02 DVC pull + dvc repro Pipeline pull đúng data version. dvc repro chạy lại stages bị stale. Smart cache bỏ qua stages unchanged. 03 Train + log MLflow Train model, log params/metrics/artifacts vào MLflow. Register vào Model Registry ở stage Staging. 04 Eval Gate: compare vs baseline compare_models.py lấy Production baseline từ Registry. So sánh accuracy. Pass → tiếp tục. Fail → block deploy. 05 Canary deploy: 5% → 100% Canary 5% traffic. Monitor 2 phút. Nếu P99 latency và accuracy OK → rollout 100%. BONUS Simulate model regression → block Cố tình degrade model. Quan sát eval gate tự động block. Zero regression lọt production.

---

<!-- chiron-source-span: {"source_span_id":"c3b665d1-eadb-5fcf-822a-e09f28103585","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"d2b74fe9f757ed99814e7d4b98c680f1d6a251128c12293b637689cabcc205a6"} -->

## Slide 39 - Key Takeaways

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 39 / 38 Những ý chính cần nhớ sau buổi học hôm nay 1 MLflow + DVC = Full Reproducibility Bất kỳ ai clone repo + dvc pull đều reproduce y hệt kết quả. MLflow track experiments, DVC track data — hai công cụ bổ sung nhau, không thay thế nhau. 2 Eval Gate là Safety Net Quan Trọng Nhất Never deploy without comparing to baseline. Eval gate là lớp bảo vệ cuối cùng. Case study: 0 regression lọt production trong 6 tháng sau khi implement CI/CD. 3 Canary Deployment Giảm Risk 90% Big-bang release là nguồn gốc của sự cố. Invest vào gradual rollout: 5% → 25% → 50% → 100% với health checks. Rollback ngay khi metrics degrade.

---

<!-- chiron-source-span: {"source_span_id":"95aa277f-fa57-5ca1-b31c-dfffdd1f2eee","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Preview Ngày 22 & Bài Tập","extraction_method":"pdf-text-layer"},"checksum":"c7a87f24337a42b4e7ba4dedaa57622c78a4307d7c858d3fa05778a9c1818587"} -->

## Slide 40 - Preview Ngày 22 & Bài Tập

Giảng viên · VinUniversity AICB · Ngày 21 · CI/CD for AI Systems 40 / 38 Ngày 22: LLMOps & Prompt Versioning "LangSmith, Weights & Biases Weave cho LLM-specific operations — prompt là code, phải version control"

- LangSmith: tracing, prompt hub, evaluations

- W&B Weave: LLM-specific experiment tracking

- Prompt versioning workflow trong CI/CD

- LLM regression testing: eval suite tự động
Lab #21 — Bài Tập (2 giờ)

- Setup MLflow tracking server local (SQLite backend)

- Convert training script để log params, metrics, artifacts

- Setup DVC với S3/GCS remote + pipeline 3 stages

- Viết GitHub Actions workflow: test → train → eval →
deploy

- Đăng ký tài khoản LangSmith (free tier)

- Đọc trước: LangSmith docs (tracing & Prompt Hub)
Slide & template → lms.vinuni.edu.vn | AICB-P2T2 Ngày 21 | CI/CD for AI Systems
