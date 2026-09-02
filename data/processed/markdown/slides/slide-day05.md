---
schema_version: 1
course_id: rag-intensive
document_id: "ce7696ee-0dc9-5d7e-afbb-858546844287"
document_version_id: "660bca7b-8f27-5568-9c09-5c7e98f32bc5"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "AI Product Thinking & Requirements"
source_file: "slide day05.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide day05.pdf"
source_sha256: "8a777a1e0d8b61b8250035b93326e9006479ef670419a834f2a0c72c5a00949e"
parser_version: chiron-structured-markdown-v1
page_count: 44
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":44}"
language: vi
---

# AI Product Thinking & Requirements

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"3c888ba8-b783-5e2f-be1a-966d0bf534b6","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"AI Product Thinking & Requirements","extraction_method":"pdf-text-layer"},"checksum":"72c3137cde5d78a4a16fda3a943bcc9d3f06aad833e309e326308e9bdb67235d"} -->

## Slide 1 - AI Product Thinking & Requirements

AICB-P1 · Ngày 5 · Build agent xong, nhưng sản phẩm cho ai? T ên Giảng Viên VinUniversity · Phase 1 · T uần 1 · 2026

---

<!-- chiron-source-span: {"source_span_id":"d8dddc44-eee4-5fe0-93c7-24da73aeec22","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"2eac8d4135ee98d844e3df1eed6729810968989fff2d5e561882a23d0d055fec"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Bạn đã build agent đẹp. Nhưng user không dùng. Tại sao?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"d695bea1-7c24-59dc-b1a9-780defc6e6b8","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"8855ffef5900f91f8b634dc84a2e2219a181a04dac19caf93539363d8c0409a2"} -->

## Slide 3 - Nội Dung Bài Học

1. Product thinking cho AI

2. Responsible AI fundamentals

3. User research cho AI products

4. Requirements engineering

5. PRD anatomy cho AI products

6. User stories cho AI

7. Risk register & go/no-go

8. Lab 5 + deliverable cuối buổi Giảng viên (VinUni) AICB · Ngày 5 T uần 1 1 / 31

---

<!-- chiron-source-span: {"source_span_id":"adf1b43a-8394-59ff-b05a-bb739249d856","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Ngày 5","extraction_method":"pdf-text-layer"},"checksum":"2ed5dd043541d1b0988fdf507060010deb10ac6d539e3ad8f7c78a1f855b24e8"} -->

## Slide 4 - Mục Tiêu Ngày 5

- Hiểu khác biệt giữa AI product và software feature thông thường

- Biết cách chuyển user needs thành requirements đo được

- Viết được PRD có thể dùng chung cho PM, BA, Engineer, Stakeholder

- Lập được risk register cho AI product với logic likelihood × impact
Cuối buổi này, học viên phải trả lời được: cho ai, giá trị gì, đo bằng gì, rủi ro nào, và khi nào go/no-go. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 2 / 31

---

<!-- chiron-source-span: {"source_span_id":"c2fb68c2-eec6-5811-b02c-215ec4d8ff72","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"60706477ea67ff23732d66633ae07a32a26e513283e387b177aef79cb59a6239"} -->

## Slide 5 - Deliverable Cuối Ngày

1 PRD dài 3–5 trang + 1 Risk Matrix cho sản phẩm AI đang đề xuất.

- PRD chính bám vào multi-agent system của Day 04

- Có thể tham chiếu thêm các use case quen thuộc: AI support agent, trợ lý
tra cứu chính sách, ticket routing, AI sales assistant

- Risk matrix phải có ít nhất 5 rủi ro: hallucination, bias, privacy, cost, adoption
Giảng viên (VinUni) AICB · Ngày 5 T uần 1 3 / 31

---

<!-- chiron-source-span: {"source_span_id":"92b93625-d167-504c-bc74-c60e795cd470","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Product Thinking Cho AI","extraction_method":"pdf-text-layer"},"checksum":"92d62ac0cde76e4096c1dcd9e71ccc1f1ec130be3e9d363fe2def27425400f3a"} -->

## Slide 6 - Product Thinking Cho AI

01 Build agent xong chưa đủ; phải build đúng thứ cho đúng người dùng

---

<!-- chiron-source-span: {"source_span_id":"9aa33427-b2a6-5b43-9eb5-e07e743a1edd","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Hai Kiểu Thất Bại Phổ Biến","extraction_method":"pdf-text-layer"},"checksum":"8fa92cd2cfc93141b108373ceeff2d9af9005f5dfe14e08cad6015e87410ce57"} -->

## Slide 7 - Hai Kiểu Thất Bại Phổ Biến

Build the wrong thing

- Không hiểu job-to-be-done

- Chọn sai persona mục tiêu

- User không thấy giá trị đủ lớn
để quay lại Build the thing wrong

- Requirements mơ hồ

- Không có acceptance criteria
đo được

- Không lường trước risk và edge
cases Lưu ý: Với AI product, value clarity và requirement quality quan trọng không kém model quality. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 4 / 31

---

<!-- chiron-source-span: {"source_span_id":"3690fe62-3fbd-58df-b2ab-11e9f0e3716e","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"AI Product Khác Software Product Ở Đâu?","extraction_method":"pdf-text-layer"},"checksum":"38b96a064ae0e9417f1986026285ee5ea51e10a2311911c7c7b735e660848329"} -->

## Slide 8 - AI Product Khác Software Product Ở Đâu?

Khía cạnh Software thường AI product Output deterministic hơn xác suất, có biến thiên Kỳ vọng user ít mơ hồ hơn dễ kỳ vọng quá mức hoặc hiểu sai Definition of done pass/fail khá rõ cần threshold chất lượng, SLA, fallback Iteration loop build rồi ship build, test, observe, cali- brate, re-ship Đừng viết requirement cho AI như viết requirement cho một CRUD form. AI cần thêm quality bands, fallbacks, và trust design. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 5 / 31

---

<!-- chiron-source-span: {"source_span_id":"03a59a06-05b3-5470-bdff-92e87a45db7c","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Jobs-to-be-Done Cho AI","extraction_method":"pdf-text-layer"},"checksum":"7a93c8960e08408f532323a1fba76794bfa5b5b9b36f74a5eddd66113f2ffca5"} -->

## Slide 9 - Jobs-to-be-Done Cho AI

User muốn hoàn thành việc gì? Ví dụ: trả lời ticket nhanh hơn. User muốn cảm thấy thế nào? T ự tin hơn, ít sợ sai hơn. User muốn được nhìn nhận ra sao? Trông chuyên nghiệp hơn, phản hồi nhanh hơn. Lưu ý: Nếu chỉ nhìn functional job, bạn dễ build một agent “đúng chức năng” nhưng không được dùng lại. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 6 / 31

---

<!-- chiron-source-span: {"source_span_id":"c143826e-19b2-536c-b24c-252368342077","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Use Cases Quen Thuộc Để Nghĩ Product Value","extraction_method":"pdf-text-layer"},"checksum":"0c33cae8d16d50bb258dc396f218cb87adfa99e240c53cbd0e16dace4a0b7402"} -->

## Slide 10 - Use Cases Quen Thuộc Để Nghĩ Product Value

- AI support agent: giảm thời gian
trả lời, tăng consistency

- Tra cứu chính sách nội bộ: giảm
thời gian tìm văn bản, giảm hỏi lặp lại

- Ticket routing agent: phân luồng
nhanh, giảm queue sai nhóm

- AI sales assistant: sàng lọc lead,
tóm tắt nhu cầu, gợi ý bước tiếp theo Ưu tiên use case trả lời được 4 câu: ai dùng, đau ở đâu, thành công đo bằng gì, fail gây hại gì. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 7 / 31

---

<!-- chiron-source-span: {"source_span_id":"c6cdc25a-fd01-5e9d-8eba-0dfa6f8d3833","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"North Star Metric Cho AI Product","extraction_method":"pdf-text-layer"},"checksum":"4b9a52a3ba794aaf48d86ae32b5e22207a5def2d27d80d17cff9dd9ef11f0bfc"} -->

## Slide 11 - North Star Metric Cho AI Product

Use case North star gợi ý Cảnh báo AI support agent first-response resolution rate đừng chỉ đo số lượng trả lời Tra cứu văn bản time-to-answer đúng nguồn đừng chỉ đo độ dài câu trả lời Ticket routing đúng nhóm ngay từ lần đầu đừng chỉ đo tốc độ phân loại AI sales assistant tỷ lệ lead đủ điều kiện đừng chỉ đo số lead được chấm điểm Define success before scope Giảng viên (VinUni) AICB · Ngày 5 T uần 1 8 / 31

---

<!-- chiron-source-span: {"source_span_id":"89769fe8-a981-5b9f-be86-743446771b03","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Responsible AI Fundamentals","extraction_method":"pdf-text-layer"},"checksum":"638d0205d49c2286da2861c1322887c9c7e274b2832cded9f4d23953603473cd"} -->

## Slide 12 - Responsible AI Fundamentals

02 Responsible AI cần được phản ánh ngay trong yêu cầu sản phẩm và cách kiểm soát rủi ro

---

<!-- chiron-source-span: {"source_span_id":"a320a9f8-4ed6-5bfd-935c-81cf277dbf01","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"5 Trụ Cột Responsible AI","extraction_method":"pdf-text-layer"},"checksum":"ad2caa136767e6198b1c0b9c6089f7bef7127303eb059ae98cf56df4b72ec2c9"} -->

## Slide 13 - 5 Trụ Cột Responsible AI

Không thiên lệch bất hợp lý Đủ ổn định để user tin dùng Chỉ dùng dữ liệu thật sự cần thiết Phù hợp với nhiều nhóm người dùng Biết AI làm gì và giới hạn ở đâu Các nguyên tắc này cần được chuyển thành product decisions, require- ments, và risk items. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 9 / 31

---

<!-- chiron-source-span: {"source_span_id":"93548fcc-5a66-5fc7-aa1b-b5361b0a8f11","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Bias, Privacy, Transparency: Nói Theo Ngôn Ngữ PM/BA","extraction_method":"pdf-text-layer"},"checksum":"d686a5b61180f560906542c6e7a34c3b5dd6a86ca101786226405f6c36dc49f1"} -->

## Slide 14 - Bias, Privacy, Transparency: Nói Theo Ngôn Ngữ PM/BA

Vấn đề Hỏi gì khi discovery Phải đi vào require- ment nào Bias AI có đối xử khác nhau giữa các nhóm user không? test set đa dạng, hu- man review cho case nhạy cảm Privacy Có PII / dữ liệu nhạy cảm không? data minimization, masking, retention policy Transparency User có biết đây là AI và khi nào nên override không? disclosure, citation, escalation path Giảng viên (VinUni) AICB · Ngày 5 T uần 1 10 / 31

---

<!-- chiron-source-span: {"source_span_id":"9ea45e1a-ae36-5492-b520-773626cae8b0","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"AI Act EU 2024: Góc Nhìn Product","extraction_method":"pdf-text-layer"},"checksum":"7cc140f9fdcf80e2c969d5a095cc074a4471cb1fbaf185234503f96aeb451863"} -->

## Slide 15 - AI Act EU 2024: Góc Nhìn Product

- Không cần học thuộc luật trong buổi này; cần hiểu rằng một số use case AI sẽ
bị yêu cầu risk management, documentation, và human oversight chặt hơn.

- Với PM/BA, tác động thực tế là: requirement, logging, disclosure, exception
handling, và review process phải được nghĩ từ đầu.

- Khi sản phẩm đi vào ngành nhạy cảm như tuyển dụng, tín dụng, y tế, giáo
dục, mức độ cẩn trọng phải tăng mạnh. Lưu ý: Responsible AI không chỉ là “đúng về mặt đạo đức”, mà còn là giảm rủi ro vận hành và pháp lý. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 11 / 31

---

<!-- chiron-source-span: {"source_span_id":"e34b9081-5005-5420-9904-94b68d87a939","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"User Research Cho AI Prod","extraction_method":"pdf-text-layer"},"checksum":"414f7093261fe9904c5de6c6680f346af37891a6538aa2cda8f9f8a51ebda004"} -->

## Slide 16 - User Research Cho AI Prod

03 User Research Cho AI Prod- ucts Nếu không hiểu trust, control, và expectation, bạn sẽ viết requirement sai ngay từ đầu

---

<!-- chiron-source-span: {"source_span_id":"2cd14094-5572-54a9-a038-eaccb9bd0457","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"4 Câu Hỏi User Research Đặc Thù Cho AI","extraction_method":"pdf-text-layer"},"checksum":"7b82630ace07710d6c88c154b5e3da7f323bc23f2029af358cd3037816e0f0b6"} -->

## Slide 17 - 4 Câu Hỏi User Research Đặc Thù Cho AI

1. User muốn AI tự làm đến mức nào, và ở bước nào họ muốn giữ quyền kiểm soát?

2. User tin AI dựa trên điều gì: tốc độ, citation, confidence, hay kết quả thực tế?

3. Khi AI sai, user muốn fallback nào: chỉnh tay, escalate người thật, hay thử lại?

4. User đang kỳ vọng AI là trợ lý, copilot, hay người thay thế? Lưu ý: Nhiều AI product fail vì team ngầm giả định user muốn “full automation”, trong khi thực tế user chỉ muốn decision support. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 12 / 31

---

<!-- chiron-source-span: {"source_span_id":"c72b8b64-ad9f-5377-8ae2-5f4b49cbb24a","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Persona Cho AI Cần Thêm Chiều Nào?","extraction_method":"pdf-text-layer"},"checksum":"cd7de4a24193aadd6e66233d654b45cfecdbfbe8a8e0e7cd94c403ccaf35e013"} -->

## Slide 18 - Persona Cho AI Cần Thêm Chiều Nào?

### Persona thường có

- Vai trò

- Mục tiêu công việc

- Pain points

- Bối cảnh sử dụng

### Persona cho AI cần thêm

- AI literacy level

- Mức sẵn sàng tin automation

- Ngưỡng chấp nhận sai

- Mức độ muốn explainability
Giảng viên (VinUni) AICB · Ngày 5 T uần 1 13 / 31

---

<!-- chiron-source-span: {"source_span_id":"67662f14-86d6-5d9b-a924-fdacd73ecba4","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Feedback Loops: Thu Tín Hiệu Gì Từ User?","extraction_method":"pdf-text-layer"},"checksum":"ec6986b19fc9c8a63214efe7695b53845f05e8b73186a38d62c9911fad0d3570"} -->

## Slide 19 - Feedback Loops: Thu Tín Hiệu Gì Từ User?

Loại tín hiệu Ví dụ Dùng để làm gì Explicit feed- back thumbs up/down, rating xác định chất lượng user cảm nhận Behavioral signal copy, rephrase, override, abandon phát hiện trust, friction, và điểm nghẽn Outcome sig- nal resolved, booked, escalated nối AI quality với business value Nếu không biết sẽ thu feedback gì sau khi launch, bạn đang viết requirement cho một hệ thống khó học và khó cải thiện. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 14 / 31

---

<!-- chiron-source-span: {"source_span_id":"3445cadf-f641-5191-8e0d-9f6e748c9b31","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Requirements Engineering","extraction_method":"pdf-text-layer"},"checksum":"093175ab1315632cfc545a413bfb72dafe5baff12b8711aca3fd9efd0b7c5d70"} -->

## Slide 20 - Requirements Engineering

04 T ừ ý tưởng mơ hồ sang đặc tả đủ rõ để team build, test, và vận hành

---

<!-- chiron-source-span: {"source_span_id":"fb8d4f47-6068-537a-97e4-f5704f141deb","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Từ Vague Đến Specific","extraction_method":"pdf-text-layer"},"checksum":"b9453b7948277a8013ee373fd3af2ccfb62fa077e908d398c971e39c2346c5b9"} -->

## Slide 21 - Từ Vague Đến Specific

Requirement mơ hồ “Agent phải trả lời nhanh, chính xác, và thông minh.” Requirement đo được “Agent phải trả lời trong dưới 5 giây ở p95, trích dẫn đúng nguồn nội bộ, và escalate sang người thật khi confi- dence thấp.” Lưu ý: Nếu engineer không biết cách test, thì requirement đó chưa đủ rõ. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 15 / 31

---

<!-- chiron-source-span: {"source_span_id":"c6e6ca06-9af6-511b-913c-d3fe72ebb7e6","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"3 Nhóm Requirement Cần Có Cho AI Product","extraction_method":"pdf-text-layer"},"checksum":"1ec0f42c78195be744ba33d3a02fcb5adcc7ec235c008a98c20698de77c6934c"} -->

## Slide 22 - 3 Nhóm Requirement Cần Có Cho AI Product

Nhóm Ví dụ Vì sao quan trọng Functional tóm tắt ticket, phân loại lead, tra cứu văn bản mô tả AI phải làm việc gì Non-functional latency SLA, uptime, cost budget bảo vệ trải nghiệm và khả năng vận hành AI-specific hallucination threshold, ex- plainability, fallback phản ánh bản chất rủi ro của AI Translate value into testable requirements Giảng viên (VinUni) AICB · Ngày 5 T uần 1 16 / 31

---

<!-- chiron-source-span: {"source_span_id":"650e676d-37c7-5e3e-b127-e8ca1c266fa4","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Acceptance Criteria Cho AI Phải Trông Như Thế Nào?","extraction_method":"pdf-text-layer"},"checksum":"9df26854500f746a3ce87c19d5b5ff7fe018edc76b47ba3bf5973e054e9834ed"} -->

## Slide 23 - Acceptance Criteria Cho AI Phải Trông Như Thế Nào?

- Có trigger rõ: Khi user hỏi về chính sách hoàn tiền...

- Có hành vi mong đợi: agent phải trích dẫn văn bản nguồn và trả lời bằng
tiếng Việt lịch sự.

- Có ngưỡng đo được: trong dưới 6 giây; nếu thiếu thông tin thì agent phải hỏi
lại.

- Có failure handling: nếu không tìm thấy nguồn phù hợp, agent phải nói rõ giới
hạn và chuyển hướng. When X happens, the agent shouldY within Z seconds, and if failure condition occurs, it should fallback behavior. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 17 / 31

---

<!-- chiron-source-span: {"source_span_id":"9c2a8cb4-d31e-571a-adfc-5bf0a16f8524","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"PRD Anatomy","extraction_method":"pdf-text-layer"},"checksum":"6a3dc3581e8173b59478e4fe0826daf03913c8343d636e44643994e0e53956bc"} -->

## Slide 24 - PRD Anatomy

05 PRD là contract giữa PM, BA, Engineer, và Stakeholder

---

<!-- chiron-source-span: {"source_span_id":"86e5b5bf-cebe-5681-8b74-6068c6128057","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"8 Phần Của Một PRD AI Product","extraction_method":"pdf-text-layer"},"checksum":"52ae95be7705b1379f2d16f56aeb887fbb48e421cf5e3ee1f1146a15e2d00ad1"} -->

## Slide 25 - 8 Phần Của Một PRD AI Product

1. Problem 2. T arget User 3. Success Metrics

4. T echnical Architecture

5. Feature Requirements 6. Non-functional

7. Acceptance Criteria 8. Risks Lưu ý: Đừng xem PRD là file để “điền cho đủ”. PRD tốt phải làm rõ quyết định, giảm tranh cãi mơ hồ, và giúp team biết thế nào là done. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 18 / 31

---

<!-- chiron-source-span: {"source_span_id":"6d21e0fc-6574-54e4-9b59-32808851fd9a","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Success Metrics Hierarchy","extraction_method":"pdf-text-layer"},"checksum":"02bfb28b1f0c8c7e4754dcc962171b866cc726a902d54aa5491051c6783b1658"} -->

## Slide 26 - Success Metrics Hierarchy

T ầng Ví dụ Câu hỏi PM/BA phải trả lời Business KPI cost saved, revenue, CSAT sản phẩm này tạo giá trị gì? Product metric task completion, repeat us- age, escalation rate user có thực sự dùng và hoàn thành việc không? AI metric accuracy, latency, citation rate hệ AI có vận hành đủ tốt để nâng product metric không? Metrics hierarchy keeps teams aligned Giảng viên (VinUni) AICB · Ngày 5 T uần 1 19 / 31

---

<!-- chiron-source-span: {"source_span_id":"c3d234b7-76bc-52c4-b199-1af5b6236c5c","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Anti-patterns Trong PRD AI","extraction_method":"pdf-text-layer"},"checksum":"62b12e96e3a851cdcf0cdd6fbbf008eb8189b97adc87f1f39003f23a4f01c01b"} -->

## Slide 27 - Anti-patterns Trong PRD AI

- Chỉ mô tả tính năng, không mô tả problem và target user

- Viết metric kiểu “càng cao càng tốt”, không có baseline hay threshold

- Thiếu non-functional requirements: latency, cost, privacy, escalation

- Không có risk section nên đến lúc triển khai mới tranh luận về bias, privacy,
adoption

- Viết solution quá sớm, chưa chứng minh user value hoặc workflow fit
Giảng viên (VinUni) AICB · Ngày 5 T uần 1 20 / 31

---

<!-- chiron-source-span: {"source_span_id":"9ffd9c3a-d330-59da-b2e8-15478d56c87b","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"User Stories Cho AI","extraction_method":"pdf-text-layer"},"checksum":"0a634c9d71bce10d25d1f25e2dedbf1acecd39f3bd00728eaed5fc3bc6b1de7c"} -->

## Slide 28 - User Stories Cho AI

06 User story tốt phải đủ rõ để engineer build, tester verify, và stakeholder đồng thuận

---

<!-- chiron-source-span: {"source_span_id":"b5faa068-d970-5ea0-8f56-a7cf537407fc","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"T emplate User Story Chuẩn","extraction_method":"pdf-text-layer"},"checksum":"29d08e0628107102d4b7c3ea87a6d6e894f0fe2897c0b3c3a4ffc49bf1c826e9"} -->

## Slide 29 - T emplate User Story Chuẩn

As [persona], I want [AI capability], so that [business value].

- Persona phải là người dùng thật, không phải “hệ thống”

- AI capability phải mô tả hành vi, không phải tên model

- Business value phải nối được sang KPI hoặc pain point
Giảng viên (VinUni) AICB · Ngày 5 T uần 1 21 / 31

---

<!-- chiron-source-span: {"source_span_id":"3736f379-d0f4-58e6-828e-034a15316211","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Ví Dụ User Stories Cho Các Use Case Quen Thuộc","extraction_method":"pdf-text-layer"},"checksum":"6ba8f284c8b9750ed4432fa4ca8db278784e7ad5037b50b1a23fd8e3f7203f68"} -->

## Slide 30 - Ví Dụ User Stories Cho Các Use Case Quen Thuộc

- AI support agent: As a support agent, I want AI to draft the first response

```text
from past policy and ticket context, so that I can resolve routine cases faster.
```

- Tra cứu chính sách: As an HR staff member, I want AI to answer policy
questions with source citation, so that I can respond consistently and reduce manual lookup time.

- Ticket routing: As an operations lead, I want AI to suggest the right queue for
incoming requests, so that misrouting drops and response time improves. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 22 / 31

---

<!-- chiron-source-span: {"source_span_id":"62c0db22-8ffd-5853-8553-d87488f90679","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Acceptance Criteria Và Edge Cases Đi Kèm User Story","extraction_method":"pdf-text-layer"},"checksum":"13402e25cc8a44391b5a2347e927865123af5e80f37bc3b10b4cd4a448fae558"} -->

## Slide 31 - Acceptance Criteria Và Edge Cases Đi Kèm User Story

Thành phần Ví dụ Vì sao cần Happy path trả lời đúng nguồn trong dưới 6 giây định nghĩa kết quả mong đợi Edge case câu hỏi mơ hồ, câu hỏi thiếu dữ liệu, tiếng lóng tránh ảo tưởng cov- erage Error state không có nguồn, tool timeout, con- fidence thấp buộc thiết kế fall- back & escalation Giảng viên (VinUni) AICB · Ngày 5 T uần 1 23 / 31

---

<!-- chiron-source-span: {"source_span_id":"40f738b5-b7d8-57f5-9eb7-28e35f106b1b","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Risk Register","extraction_method":"pdf-text-layer"},"checksum":"03655ff28f5027097394e186dc4af3a4427d39fe1a054b21086c2913c2a2d613"} -->

## Slide 32 - Risk Register

07 Không có risk register, team sẽ nói về risk quá muộn và quá cảm tính

---

<!-- chiron-source-span: {"source_span_id":"5ac4249d-daca-56f5-825f-3f1d6e7fd901","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"AI Risk T axonomy","extraction_method":"pdf-text-layer"},"checksum":"d01e737102aa19b380de463d1bf62bb23b1ff47989f7bb790202d1618e75ef3a"} -->

## Slide 33 - AI Risk T axonomy

Nhóm risk Ví dụ Mitigation gợi ý Technical hallucination, tool failure, latency spike eval, fallback, timeouts, mon- itoring Data PII leak, stale source, bad labeling masking, access control, data QA Business adoption thấp, unclear ROI, wrong workflow fit pilot, success metrics, JTBD validation Ethical unfair outcome, opaque decision human review, disclosure, au- dit sample Regulatory logging thiếu, compliance gap documentation, approval flow, policy review Risk thinking must be explicit Giảng viên (VinUni) AICB · Ngày 5 T uần 1 24 / 31

---

<!-- chiron-source-span: {"source_span_id":"c6ebcede-fcf2-5e80-a1cc-7a6f87f9cbf5","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Risk Matrix: Likelihood × Impact","extraction_method":"pdf-text-layer"},"checksum":"8dc2467998672a51f028d8e9afa912571b6afdc654af1c8324d88721b3785c45"} -->

## Slide 34 - Risk Matrix: Likelihood × Impact

Impact Likelihood Monitor Mitigate ReduceEscalate / Go-No-Go1 2 3 4 5 1: Privacy leak 2: Hallucination on sensitive advice 3: Cost spike 4: Adoption risk 5: Minor wording inconsistency Giảng viên (VinUni) AICB · Ngày 5 T uần 1 25 / 31

---

<!-- chiron-source-span: {"source_span_id":"b7043722-27d7-5174-a101-15fdcb5cf6a2","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Go / No-Go Criteria Dựa Trên Risk Threshold","extraction_method":"pdf-text-layer"},"checksum":"b1a925a5e735b2a5624128883630ef719979ce915ab06cef4768a6e7fbd7467c"} -->

## Slide 35 - Go / No-Go Criteria Dựa Trên Risk Threshold

- Go: risk cao đã có mitigation rõ, acceptance criteria đo được, owner rõ.

- Conditional go: pilot giới hạn, human-in-the-loop, guardrails chặt, scope
hẹp.

- No-go: chưa xử lý privacy / compliance risk lớn, chưa có fallback, hoặc chưa
chứng minh user value. Risk register giúp team biết build trong điều kiện nào, ship ở mức nào, và khi nào phải dừng. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 26 / 31

---

<!-- chiron-source-span: {"source_span_id":"affe8354-749f-5729-9c3f-48ffbd2e178a","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Thực Hành","extraction_method":"pdf-text-layer"},"checksum":"f749e0226d0d94a925e8cda88dff94155cd7d557788896e91e4983f9c99e0fae"} -->

## Slide 36 - Thực Hành

08 Lab 5: Viết PRD và Risk Matrix cho sản phẩm AI đủ rõ để cả PM, BA, Engineer cùng dùng

---

<!-- chiron-source-span: {"source_span_id":"8274866f-d337-5de2-9f8a-bd67c9028670","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Hands-on 5: Cách Chạy Lab","extraction_method":"pdf-text-layer"},"checksum":"c5c44394f3061510df736bf376cca5e0d16ccb16179b6a239e06d3b96f042ea3"} -->

## Slide 37 - Hands-on 5: Cách Chạy Lab

1. Chọn artifact chính: multi-agent system Day 04 hoặc 1 use case quen thuộc được giảng viên duyệt.

2. Viết Problem, T arget User, Success Metrics, Architecture ở mức đủ để team hiểu scope.

3. Viết ít nhất 3 user stories với acceptance criteria và edge cases.

4. Lập risk matrix cho 5 rủi ro chính: hallucination, bias, privacy, cost, adoption. Lưu ý: Lab này không chấm “văn hay”. Lab này chấm mức độ rõ, đo được, hành động được. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 27 / 31

---

<!-- chiron-source-span: {"source_span_id":"015fc3df-572d-5518-bd04-6f9be0e8debf","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Deliverable Cuối Buổi","extraction_method":"pdf-text-layer"},"checksum":"4a773b711b5a4fefd61786330653ea61a88de5da0d227222f80d3301e62a87fb"} -->

## Slide 38 - Deliverable Cuối Buổi

- PRD 3–5 trang gồm đủ 8 phần cốt lõi

- Risk Matrix likelihood × impact

- 3 user stories có acceptance criteria và failure handling

- Decision note: đề xuất go / conditional go / no-go và lý do
Có target user rõ chưa? Metric có đo được chưa? Non-functional có đủ chưa? Risk có owner và mitigation chưa? Giảng viên (VinUni) AICB · Ngày 5 T uần 1 28 / 31

---

<!-- chiron-source-span: {"source_span_id":"256e538c-7d04-5d5c-85e1-213b15d87ce8","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"PRD Skeleton — Ví Dụ T ối Thiểu","extraction_method":"pdf-text-layer"},"checksum":"3cb80382d5fa2c7f6bfee50c2f3fc46e62d877212a62ee9e4964331a3492d6b2"} -->

## Slide 39 - PRD Skeleton — Ví Dụ T ối Thiểu

Internal Policy Assistant Problem HR team mất nhiều thời gian trả lời câu hỏi lặp lại về chính sách. T arget User HR staff và line managers cần tra cứu nhanh, đúng nguồn. Success Metrics

- Time-to-answer giảm 50%

- Citation coverage > 95%

- Escalation rate < 15%
Risks

- Hallucination on policy
interpretation

- PII leakage in uploaded documents
PRD skeleton không cần dài ngay từ đầu. Điều quan trọng là mỗi mục đều nối được sang quyết định, metric, hoặc risk cụ thể. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 29 / 31

---

<!-- chiron-source-span: {"source_span_id":"c8ddd0e6-db87-529c-a442-8d88157bc8c2","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"a4eb5b897ab656a39582babc121f74e5cfac7c7cd1fe791bee4cf8c88b5d9a74"} -->

## Slide 40 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Product thinking trước code: phải hiểu user, workflow, và value trước khi bàn sâu đến tính năng hay model. 2 PRD là contract giữa PM, BA, Engineer, và Stakeholder; file này phải giảm mơ hồ chứ không được tăng mơ hồ. 3 Responsible AI phải đi vào requirement, acceptance criteria, và risk register ngay từ đầu thay vì xử lý muộn. 4 Nếu thiếu acceptance criteria và go/no-go threshold, team rất dễ build sai hướng dù implementation có tốt. Giảng viên (VinUni) AICB · Ngày 5 T uần 1 29 / 31

---

<!-- chiron-source-span: {"source_span_id":"334cac5e-c0c9-5984-b29a-19dd94b0ac84","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"ed02cb3ad93847b8be5164aaaf6223ea6d766b993d96265c3b97637170ee78bd"} -->

## Slide 41 - Tiếp theo & Bài tập

AI Product & Project Manage- ment “Day 05 giúp bạn viết đúng sản phẩm. Nhưng khi stakeholder đổi ý, uncertainty tăng, và sprint chạy thật, bạn sẽ quản lý dự án AI như thế nào?”

- Xem lại PRD vừa viết và đánh
dấu 2 giả định chưa được kiểm chứng

- Chuẩn bị 1 use case muốn đem
sang bài MVP / PoC của ngày tiếp theo Giảng viên (VinUni) AICB · Ngày 5 T uần 1 30 / 31

---

<!-- chiron-source-span: {"source_span_id":"8b3fb83a-966b-5f61-8563-118509a476ea","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"T ài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"5aefefd1ea329b0ea7cf1a88664c9879ce046474c9f6ab7d962ed733ee799669"} -->

## Slide 42 - T ài Liệu Tham Khảo

1 Google PAIR. People + AI Guidebook. pair.withgoogle.com/guidebook-v2/ 2 NIST. AI Risk Management Framework (AI RMF 1.0). nist.gov 3 European Union. AI Act - Regulation (EU) 2024/1689. eur-lex.europa.eu 4 Duke University. AI Product Management Specialization. coursera.org Giảng viên (VinUni) AICB · Ngày 5 T uần 1 31 / 31

---

<!-- chiron-source-span: {"source_span_id":"2a7bdead-de85-59a0-a8f6-531ef621dc8c","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"0fe32cf8fbb9aa23a05f3dc2df7eeeb9b8434dead3dff12037e6f0c367e709be"} -->

## Slide 43 - Hỏi & Đáp

PRD của bạn đang giúp team quyết định nhanh hơn, hay chỉ làm file dài hơn?

---

<!-- chiron-source-span: {"source_span_id":"1a5091ad-9195-56ed-aab9-6e5fea76657e","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"90706460cce89d415c81d44037821752c0b0ea9e126dc0c7fbc9f7dea9923ddc"} -->

## Slide 44 - Cảm ơn!

Email: lecturer@vinuni.edu.vn Slides & tài liệu: github.com/aicb-vinuni Lab template: bit.ly/aicb-day05-lab
