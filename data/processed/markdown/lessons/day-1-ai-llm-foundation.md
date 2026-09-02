---
schema_version: 1
course_id: rag-intensive
document_id: "6e3357e9-4457-5076-bc58-64b744f322a7"
document_version_id: "c189e833-e1a2-540b-9683-6be652fbce9b"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "AI & LLM Foundation — phân tích & breakdown từng slide"
source_file: "day-1-ai-llm-foundation.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\day-1-ai-llm-foundation.html"
source_sha256: "040a401c3787017b4f9e383c9693fc11037e3a1219980a788886145391ab539b"
parser_version: chiron-structured-markdown-v1
html_section_count: 18
interactive_module_count: 3
interactive_control_count: 9
language: vi
---

# AI & LLM Foundation — phân tích & breakdown từng slide

> 83 slide, đi từ "nghe AI" đến "gọi AI" trong một ngày. Bài này đặt 
 nền cho toàn bộ khoá học: mọi khái niệm ở Ngày 7, 8, 9, 11, 24, 25 đều là hệ quả của một câu duy nhất 
 được lặp lại xuyên suốt — model chỉ đoán token tiếp theo.

<!-- chiron-source-span: {"source_span_id":"384d7e01-6c08-50d8-8913-a7769619b3f9","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"day-1-ai-llm-foundation.html"},"checksum":"6b76d7e3531556ed12239e13fcb79220ef65f7eaabbeb5d9840b6b509bef7314"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Đây là bài **nền** — không phải bài dễ, mà là bài mà mọi bài sau đều dựa vào. Đặc điểm 
 của nó: rất nhiều khái niệm, mỗi khái niệm chỉ được nói một lần, và *ba phần cuối* (chọn model, 
 chi phí token, gọi API) mới là phần bạn dùng hằng ngày.

Bài có một sợi chỉ xuyên suốt mà slide 26 gọi là **"thần chú"**: *"Model chỉ đoán token tiếp theo — mọi thứ khác là hệ quả."* Nếu ở bất kỳ đoạn nào bạn thấy rối, 
 quay lại câu đó và hỏi: *điều này là hệ quả của việc đoán token như thế nào?* Gần như luôn có 
 câu trả lời.

Lượt 1 · ~20 phút

Nắm mạch chính

- Đọc slide 27, 30–31, 52, 
 65, 68, 81
- Nhìn Hình 3 (vòng lặp đoán token) — hình quan trọng nhất cả bài
- Mục tiêu: giải thích được token, context và chi phí liên hệ với nhau ra sao

Lượt 2 · ~70 phút

Chương 3, 7, 8 kỹ

- Ba chương này là phần dùng được ngay: cơ chế · tiền · cách gọi
- Làm hết "Dự đoán trước khi kéo" ở 3 mô-đun — phần đắt giá nhất
- Chương 2 (lịch sử) đọc một lượt cho có mạch, đừng học thuộc mốc

Lượt 3 · ~20 phút

Trước quiz

- 6 hiểu lầm — bài nền nên hiểu lầm ở đây kéo theo cả khoá
- Cheat sheet — bốn bảng và một công thức tiền
- Từ điển — token, context, attention, temperature, MoE, RLHF

"Bạn đang dùng AI mỗi ngày — nhưng thực sự bên trong nó đang làm gì?"

"một vòng lặp đoán token, được nuôi bằng dữ liệu, đang chờ bạn điều khiển."

bằng lời của mình

---

<!-- chiron-source-span: {"source_span_id":"9a73734b-d348-5f7d-bc10-b0c2d69736cc","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"day-1-ai-llm-foundation.html"},"checksum":"6ca74dbaa72b4f28dd684973b5378dc0c7dc0c34fb96d527e192961fa342e10b"} -->

## 00 Mở đầu

Slide 1–4: câu hỏi dẫn dắt, agenda và bốn thứ mang về cuối ngày.

### Slide 1–3 Trang bìa và agenda

> Trích slide 
>  "AI IN ACTION — Day 1. AI & LLM Foundation. 
>  Bạn đang dùng AI mỗi ngày — nhưng thực sự bên trong nó đang làm gì? " 
>  "Agenda: Bức tranh AI & các tầng của AI · Lịch sử AI 70 năm · Bên trong LLM: cơ chế vận hành · 
>  Từ LLM đến AI Agent · Landscape: model hôm nay & cuộc đua hiện tại · Chọn model & chi phí 
>  token · Gọi API lần đầu · Tổng kết" 
>  " Từ 'nghe AI' đến 'gọi AI' trong một ngày "

Agenda tám mục này có một cấu trúc đáng để ý: nó đi từ **rộng nhất tới cụ thể nhất**, 
 và điểm chuyển nằm đúng ở giữa.

| Nửa đầu — hiểu | Nửa sau — làm |
| --- | --- |
| Bức tranh AI · Lịch sử · Bên trong LLM · Từ LLM đến Agent | Landscape · Chọn model & chi phí · Gọi API · Tổng kết |
| Trả lời "nó là gì và hoạt động ra sao" | Trả lời "tôi dùng nó thế nào và tốn bao nhiêu" |
| Kiến thức bền — cơ chế không đổi | Kiến thức mau cũ — tên model, giá cả đổi hằng quý |

không lỗi thời

khung tư duy

"Bản đồ này sẽ cũ trong vài tháng — thứ bền là cách đọc bản đồ."

### Slide 4 Bốn thứ mang về cuối ngày

> Trích slide 
>  " 1 Hiểu được — Giải thích được LLM hoạt động thế nào — bằng trực giác, không cần 
>  công thức. 2 Nắm được — Token, context, chi phí, độ trễ liên hệ với nhau ra sao. 
>  3 Gọi được — Lần gọi API đầu tiên — và hiểu cấu trúc của một lần gọi model. 
>  4 Build được — Một chatbot dòng lệnh đơn giản có streaming." 
>  "Không cần nền toán. Chỉ cần tò mò và một chiếc máy tính."

Mục **số 2** là mục dễ bị coi nhẹ nhất và lại là mục có giá trị thực dụng cao nhất. 
 Chú ý cách nó được phát biểu: không phải "biết token là gì" mà là *"token, context, chi phí, độ trễ **liên hệ với nhau** ra sao"*.

[Slide 70](#s69) nói thẳng ra: *"Cả hai cùng quy về một thứ: số token model phải 
 đọc và sinh ra — đó là 'một núm vặn'."*

Nghĩa là bạn không có bốn thứ để cân đối, bạn có **một**:

• *Context dài hơn* ⇒ nhiều token hơn ⇒ đắt hơn **và** chậm hơn 
 • *Output dài hơn* ⇒ nhiều token hơn ⇒ đắt hơn **và** chậm hơn 
 • *Model lớn hơn* ⇒ mỗi token đắt hơn **và** chậm hơn

Điều này rất tiện: **tối ưu chi phí và tối ưu tốc độ là cùng một 
 việc**. Bạn không phải chọn giữa hai. Ba mô-đun tương tác trong tài liệu này tồn tại để bạn 
 thấy quan hệ đó bằng số thật.

chịu khó giữ một mô hình tinh thần 
 nhất quán

quy được mọi hiện tượng về cùng một nguyên nhân

---

<!-- chiron-source-span: {"source_span_id":"94338e09-2a14-51f7-9aa6-a4b0865b3f02","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Bức tranh AI","source_file":"day-1-ai-llm-foundation.html"},"checksum":"87e907bf57ed18eb3eb9e263f8a0e3314867c1074f678f0043fab80fb60eb088"} -->

## 01 Bức tranh AI

Slide 5–7: các tầng lồng nhau, và ba nhóm AI theo việc chúng làm.

### Slide 5–6 AI, ML, Deep Learning, GenAI, LLM nằm ở đâu

> Trích slide 
>  " AI — chiếc ô lớn nhất: mọi hệ thống có yếu tố 'thông minh'. kể cả hệ luật 
>  tay, robot… 
>  Machine learning — học từ dữ liệu thay vì viết luật tay. lọc spam · gợi ý phim 
>  Deep learning — mạng nơ-ron nhiều tầng tự học đặc trưng. nhận diện ảnh · giọng nói 
>  Generative AI — sinh nội dung mới: văn bản, ảnh, code. 
>  LLM — model nền chuyên ngôn ngữ, tim của làn sóng hiện nay. GPT · Claude · Kimi " 
>  "LLM không phải toàn bộ AI — nhưng nó là tầng nền của gần hết trải nghiệm AI bạn dùng hôm nay"

Đây là hình lồng nhau kinh điển, và giá trị của nó không nằm ở việc nhớ thứ tự mà ở chỗ nó **ngăn một hiểu lầm rất phổ biến**: coi "AI" và "LLM" là đồng nghĩa.

_Sơ đồ: Năm tầng lồng nhau từ trí tuệ nhân tạo tới mô hình ngôn ngữ lớn - Năm hình chữ nhật lồng vào nhau từ ngoài vào trong. Ngoài cùng là Artificial Intelligence, bao gồm cả hệ luật viết tay và robot. Bên trong là Machine Learning, học từ dữ liệu thay vì viết luật tay, ví dụ lọc spam và gợi ý phim. Tiếp theo là Deep Learning, mạng nơ-ron nhiều tầng tự học đặc trưng, ví dụ nhận diện ảnh và giọng nói. Trong nữa là Generative AI, sinh nội dung mới gồm văn bản, ảnh và code. Trong cùng là LLM, model nền chuyên ngôn ngữ, ví dụ GPT, Claude và Kimi._

Hình 1 — Năm tầng lồng nhau (slide 6).

bao hàm

Khi bạn có một bài toán, câu hỏi đầu tiên *không* phải "dùng LLM thế nào" mà là **"bài toán này thuộc tầng nào"**.

Phân loại email spam, dự đoán khách bỏ dịch vụ, chấm điểm tín dụng — đây là bài toán *machine learning cổ điển*. Một mô hình nhỏ chạy trong vài mili giây, miễn phí, chính xác hơn 
 và giải thích được. Dùng LLM cho những việc đó là chậm hơn, đắt hơn, và kém tin cậy hơn.

Đây chính là bài học mà [slide 65](#s65) phát biểu lại ở tầng 
 chọn model: *"việc đơn giản mà gọi frontier → phí tiền"*. Ở đây nó còn mạnh hơn — *có những việc không nên gọi LLM chút nào*.

### Slide 7 Ba nhóm AI: phân loại · sinh nội dung · hành động

> Trích slide 
>  " Discriminative AI — Giỏi phân loại, dự đoán: lọc spam, phát hiện gian lận, 
>  nhận diện ảnh. Input → một nhãn, một con số " 
>  " Generative AI — Sinh ra thứ mới: văn bản, ảnh, code. ChatGPT, Claude, Midjourney. 
>  Prompt → nội dung mới " 
>  " Agentic AI — Nhận mục tiêu rồi tự làm nhiều bước: lập kế hoạch, dùng công cụ, 
>  hành động. Goal → Plan → Action " 
>  "LLM là engine chung của cả Generative lẫn Agentic. Hành trình khóa học: LLM Foundation → Agent → 
>  Multi-Agent → Deploy → Evaluate"

Ba nhóm này phân biệt theo **hình dạng đầu vào–đầu ra**, và đó là cách phân biệt sắc 
 nhất vì nó quyết định luôn cách bạn đánh giá chúng:

| Nhóm | Vào → Ra | Đo chất lượng bằng gì | Học ở ngày nào |
| --- | --- | --- | --- |
| Discriminative | Input → một nhãn / một số | Accuracy, precision, recall — có đáp án đúng duy nhất | Không thuộc phạm vi khoá này |
| Generative | Prompt → nội dung mới | Khó — không có một đáp án đúng. Cần LLM-as-Judge, RAGAS… | Ngày 8, 14, 24 |
| Agentic | Goal → Plan → Action | Khó nhất — phải đo cả đường đi, không chỉ kết quả | Ngày 3, 9, 20, 23 |

Với discriminative AI, bạn có nhãn đúng nên chấm điểm là chuyện hiển nhiên. Với generative AI, 
 "câu trả lời tốt" là gì đã là một câu hỏi mở — nên cần cả một ngày (Ngày 24) chỉ để bàn cách đo. 
 Với agentic AI, kết quả đúng vẫn có thể che một đường đi sai.

Nhìn hành trình khoá học mà slide vẽ ra — *LLM Foundation → Agent → Multi-Agent → Deploy → Evaluate* — sẽ thấy Evaluate nằm **cuối cùng**. Đó không phải vì nó ít quan trọng, mà vì bạn phải có thứ để đo trước đã. 
 Ngày 24 sẽ nói ngược lại một cách gay gắt: *"Không eval = không production."*

---

<!-- chiron-source-span: {"source_span_id":"a5e4cd86-f339-5e0e-a14a-f662f7a4eedb","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Lịch sử AI 70 năm","source_file":"day-1-ai-llm-foundation.html"},"checksum":"9943f8060622a8f86690a80dd778f02d3e485d1ea03a6a2902b745f2a1e13b9c"} -->

## 02 Lịch sử AI 70 năm

Slide 8–24: hai mùa đông, hai lần đổi nền tảng, và nút thắt mà Transformer tháo được.

### Slide 8–20 Bảy mươi năm gói trong một bảng — đọc lấy mạch, đừng học thuộc mốc

> Trích slide 
>  "Khai sinh, lời hứa đầu tiên · 2 lần mùa đông, cách tiếp cận chạm trần · Từ model đơn lẻ sang 
>  system có khả năng hành động như agent"

Mười ba slide lịch sử có **một cấu trúc lặp lại ba lần**, và nhận ra cấu trúc đó đáng 
 giá hơn nhớ từng mốc:

```text
một cách tiếp cận mới  →  làm được vài thứ ấn tượng  →  CHẠM TRẦN  →  đổi nền tảng
        │                                                    │
        │  1956–1973  symbolic + perceptron                   │  mùa đông 1
        │  1980–1987  expert system (luật viết tay)           │  mùa đông 2
        │  2012–2024  deep learning + scaling                 │  "data wall" (slide 61)
        ▼
   mỗi lần trần bị chạm, câu hỏi của cả ngành đổi — chứ không phải công cụ đổi
```

| Mốc | Chuyện gì xảy ra | Bài học còn dùng được hôm nay |
| --- | --- | --- |
| 1956 Dartmouth | Cụm từ "Artificial Intelligence" ra đời | Giả định gốc: nếu mô tả được trí thông minh đủ rõ thì máy mô phỏng được — giả định này vẫn chưa được chứng minh hay bác bỏ |
| 1969–1973 | Symbolic đuối trước ngữ cảnh; perceptron quá đơn giản. Báo cáo Lighthill cắt tiền | Bùng nổ tổ hợp: bài toán nhỏ duyệt hết được nên trông "thông minh"; thế giới thật sinh quá nhiều nhánh |
| 1980 Expert system | Đổi chiến lược: bỏ trí tuệ tổng quát, giải thật tốt một miền hẹp bằng luật | Vẫn đúng: thu hẹp phạm vi là cách rẻ nhất để tăng độ tin cậy. Trục Topical của guardrail (Ngày 24) là hậu duệ trực tiếp |
| ~1987 Mùa đông 2 | Tri thức phải nhập tay; luật càng nhiều càng khó cập nhật; gãy trước ngoại lệ mới | Đây là lý do machine learning thắng: không phải vì thông minh hơn, mà vì bảo trì được |
| 2009 ImageNet | Fei-Fei Li xây bộ dữ liệu 14 triệu ảnh gán nhãn tay, hơn 20.000 loại vật | "Đôi khi dữ liệu tốt hơn đánh bại thuật toán khôn hơn" — câu này quay lại ở Ngày 21 (fine-tuning) và Ngày 8 (RAG) |
| 2012 AlexNet | Thắng ImageNet nhờ ba thứ cùng lúc: dữ liệu lớn + kiến trúc sâu + GPU | Không đột phá nào đến từ một yếu tố. Đây là mẫu hình lặp lại — xem slide 66, ba trục làm model giỏi hơn |
| 2016 AlphaGo | Học 150.000 ván người, rồi tự chơi với chính mình hàng triệu lần | Mầm của RLVR (Ngày 22, 24): khi có cách tự chấm đúng-sai, model vượt được dữ liệu con người |

Hai mùa đông không xảy ra vì máy tính yếu hay người làm dở. Chúng xảy ra vì **cách tiếp cận chạm trần của chính nó**: symbolic không chịu nổi số lượng ngữ cảnh, 
 expert system không chịu nổi chi phí bảo trì tri thức.

Và [slide 61](#s61) nói rằng điều tương tự đang xảy ra lần 
 thứ ba: *"2024 model đã đọc gần hết văn bản công khai của nhân loại (data wall) → 'to hơn + 
 đọc nhiều hơn' không còn thắng chắc"*. Khác biệt là lần này ngành đã có sẵn hai hướng đi tiếp 
 (luyện đề tự chấm và cho model thời gian nghĩ) nên chưa có mùa đông thứ ba.

### Slide 21–22 Nút thắt của RNN, và vì sao Transformer tháo được nó

> Trích slide 
>  "Nút thắt của RNN: đọc hết rồi mới nói — từng bước một. đọc lần lượt từng chữ → nén cả câu 
>  vào MỘT vector → CỔ CHAI → decoder sinh từng từ một " 
>  "① Câu càng dài → càng quên chữ đầu — chữ đầu 'mờ' dần trong vector duy nhất, như người cố 
>  nhớ một câu rất dài bằng trí nhớ ngắn hạn 
>  ② Từng bước một → chậm, khó mở rộng — muốn chữ thứ 100 phải chờ đủ 99 bước trước, không song 
>  song được, khó scale lên model lớn " 
>  " Transformer thắng không phải vì phép màu — nó tháo đúng nút thắt này: cho mọi từ nhìn 
>  nhau cùng lúc. "

Đây là slide giải thích *vì sao* hay nhất trong cả chương lịch sử, vì nó nêu **hai** vấn đề chứ không phải một — và vấn đề thứ hai mới là vấn đề quyết định.

_Sơ đồ: Nút thắt của RNN so với cách attention cho mọi từ nhìn nhau cùng lúc - Nửa trên là RNN: các từ được đọc lần lượt từ trái sang phải, mỗi bước phụ thuộc bước trước, rồi toàn bộ câu bị nén vào một vector duy nhất gọi là cổ chai, sau đó decoder sinh từng từ một. Hai hệ quả là chữ đầu bị mờ dần và không song song hoá được. Nửa dưới là attention: mọi từ nhìn thẳng sang mọi từ khác cùng lúc, không có vector cổ chai, nên vừa giữ được liên hệ xa vừa tính song song được._

Hình 2 — Nút thắt RNN và lối thoát của attention (slide 21, 34).

"nó"

slide 33

thẳng

Vấn đề ① (quên chữ đầu) là vấn đề *chất lượng* — dễ thấy, dễ kể, và là thứ hay được nhắc.

Vấn đề ② (không song song hoá được) là vấn đề *kỹ thuật huấn luyện*, nghe khô khan hơn — 
 nhưng nó mới là thứ mở khoá kỷ nguyên hiện tại. GPU mạnh ở chỗ làm hàng nghìn phép tính *cùng lúc*. Một kiến trúc buộc phải tính bước 99 xong mới tính được bước 100 thì không tận 
 dụng được điều đó, bất kể bạn có bao nhiêu GPU.

**Hệ quả:** Transformer không chỉ hiểu ngữ cảnh tốt hơn — 
 nó cho phép *đổ tiền vào compute để lấy chất lượng*, và đó chính là "luật chơi 2020–2024" 
 mà [slide 37](#s37) gọi là scaling law. Không có tính song song, scaling law không tồn tại.

chi phí tăng theo bình phương độ dài

slide 31

slide 61

### Slide 23–24 2022: ChatGPT và sự hội tụ của cả ngành

> Trích slide 
>  "ChatGPT xuất hiện như một trải nghiệm đại chúng. Lần đầu tiên rất đông người dùng phổ thông có 
>  thể trực tiếp chạm vào một mô hình ngôn ngữ mạnh, thông qua một giao diện đơn giản đến mức ai cũng 
>  hiểu cách dùng." 
>  "Trước khi ChatGPT bùng nổ, nghiên cứu mô hình ngôn ngữ phân thành rất nhiều nhánh → 
>  ChatGPT xuất hiện, chứng minh hiệu quả → trọng tâm của toàn ngành bắt đầu dồn về cùng một trục"

Điều đáng chú ý: **ChatGPT không phải một đột phá kỹ thuật**. Model bên dưới 
 (GPT-3.5) đã tồn tại; Transformer có từ 2017; RLHF đã được công bố trong bài InstructGPT đầu 2022. 
 Cái mới là *giao diện* và *quyền truy cập*.

Cùng một năng lực kỹ thuật, đóng gói khác nhau cho kết quả khác nhau về bậc độ lớn. Playground 
 của OpenAI đã cho phép gõ prompt từ trước — nhưng nó trông như một công cụ dành cho lập trình viên. 
 Một ô chat trông như tin nhắn thì *ai cũng biết phải làm gì*.

Đây là lý do [slide 47](#s47) tách riêng "bốn cách chạm vào 
 LLM" thành một trục: **mức truy cập quyết định bạn làm được gì**, và với phần lớn người 
 dùng, mức truy cập dễ nhất là mức duy nhất tồn tại. Với bạn — người sắp gọi API — thì ngược lại: 
 bạn đang chọn mức khó hơn để đổi lấy quyền kiểm soát.

#### Ô kiểm tra — Chương 1 & 2

Trả lời thành tiếng trước khi mở đáp án.

**1.** Bạn được giao bài toán "phân loại email khiếu nại của khách thành 5 nhóm". 
 Vì sao câu trả lời "dùng LLM" chưa chắc đúng? Áp dụng

#### Đáp án

**Vì đây là bài toán *discriminative* (slide 7): input → một nhãn.** Nó nằm 
 ở tầng machine learning cổ điển, không cần tới tầng trong cùng của hình lồng nhau.

**So sánh:** một mô hình phân loại nhỏ chạy trong vài mili giây, gần như miễn phí, 
 chính xác hơn trên tập dữ liệu của bạn, và *giải thích được* vì sao nó chọn nhãn đó. Một LLM 
 thì chậm hơn, tốn tiền theo token, và có thể trả về nhãn thứ sáu bạn không hề định nghĩa.

**Khi nào LLM vẫn hợp lý:** khi bạn *chưa có dữ liệu gán nhãn* — LLM làm 
 được zero-shot ngay ngày đầu, còn mô hình phân loại cần vài nghìn mẫu. Chiến lược thường dùng: 
 LLM để khởi động và tự sinh nhãn, rồi huấn luyện một mô hình nhỏ thay thế khi đã đủ dữ liệu.

**Ý chung:** câu hỏi đầu tiên không phải "dùng LLM thế nào" mà "bài toán này thuộc 
 tầng nào".

**2.** Slide nói RNN có hai nhược điểm. Nhược điểm nào thật sự mở khoá kỷ nguyên 
 LLM khi được giải quyết, và vì sao? Phân tích

#### Đáp án

**Nhược điểm ② — không song song hoá được.**

Nhược điểm ① (câu dài thì quên chữ đầu) là vấn đề chất lượng, dễ thấy và hay được nhắc. Nhưng ② 
 là vấn đề *huấn luyện*: RNN buộc phải tính xong bước 99 mới tính được bước 100, nên không 
 tận dụng được GPU — thứ mạnh ở chỗ làm hàng nghìn phép tính cùng lúc.

**Hệ quả:** attention cho phép tính mọi cặp token cùng lúc ⇒ dùng hết công suất 
 GPU ⇒ huấn luyện được model nghìn tỷ tham số ⇒ *scaling law* tồn tại (thêm compute và dữ 
 liệu thì model khôn lên một cách dự đoán được, slide 37).

**Nói cách khác:** không có tính song song thì không có scaling law, và không có 
 scaling law thì không có kỷ nguyên hiện tại. Transformer thắng không chỉ vì hiểu ngữ cảnh tốt hơn 
 mà vì nó *huấn luyện được ở quy mô RNN không với tới*.

**Cái giá:** attention tốn n² theo độ dài — mỗi token nhìn mọi token khác. Đó là 
 gốc của việc context dài vừa đắt vừa chậm.

**3.** Hai mùa đông AI có điểm chung gì, và điều tương tự đang được cảnh báo hôm 
 nay là gì? Hiểu

#### Đáp án

**Điểm chung: cả hai xảy ra vì cách tiếp cận *chạm trần của chính nó*, không phải 
 vì máy yếu hay người dở.**

• **Mùa đông 1** — symbolic đuối trước số lượng ngữ cảnh của thế giới thật 
 (bùng nổ tổ hợp); perceptron quá đơn giản. Báo cáo Lighthill 1973 kết luận AI làm được ít hơn 
 nhiều so với lời hứa → cắt tiền. 
 • **Mùa đông 2** — expert system tạo giá trị thật nhưng tri thức phải nhập tay, luật 
 càng nhiều càng khó cập nhật, và gãy trước ngoại lệ mới. Vấn đề là *chi phí bảo trì*.

**Hôm nay:** slide 61 gọi tên **"data wall"** — đến 2024 model đã đọc 
 gần hết văn bản công khai của nhân loại, nên "to hơn + đọc nhiều hơn" không còn thắng chắc.

**Khác biệt so với hai lần trước:** lần này ngành đã có sẵn hai hướng đi tiếp khi 
 trần bị chạm — *luyện đề tự chấm* (RLVR: toán có đáp số, code có test) và *cho model thời gian nghĩ* (test-time compute). Nên chưa có mùa đông thứ ba.

---

<!-- chiron-source-span: {"source_span_id":"28920cca-3ce7-5612-95d0-fe5af67c3d3e","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Bên trong LLM","source_file":"day-1-ai-llm-foundation.html"},"checksum":"f8c2a30473f8264f1826e64e9a490ece7fa34e323a46000eca0f82d04d940c7b"} -->

## 03 Bên trong LLM

Slide 25–36: vòng lặp đoán token, token, context, attention — chương nền của cả khoá.

### Slide 25–26 Bản đồ năm chặng và "thần chú"

> Trích slide 
>  " 3A Cỗ máy đoán token — LLM là gì · xác suất · vòng lặp · token · context · 
>  3B Attention — cách model nhìn ngữ cảnh · multi-head · ứng dụng · 
>  3C Model được tạo ra — tham số · training · RLHF · 
>  3D Model có "hiểu" không? — tranh luận · thí nghiệm Othello-GPT · 
>  3E Giới hạn & sống chung — cutoff · hallucination · học vẹt · cách chạm vào" 
>  "Thần chú xuyên suốt: 'Model chỉ đoán token tiếp theo — mọi thứ khác là hệ quả.' "

Câu thần chú này không phải khẩu hiệu cho vui — nó là **công cụ chẩn đoán**. Gần như 
 mọi hành vi kỳ lạ của LLM đều suy ra được từ nó, và bảng dưới là cách dùng:

| Hiện tượng bạn gặp | Suy ra từ "chỉ đoán token tiếp theo" như thế nào |
| --- | --- |
| Model bịa ra một trích dẫn không tồn tại | Nó không tra cứu — nó chọn chuỗi token nghe hợp lý nhất. Một trích dẫn giả trông y hệt trích dẫn thật về mặt thống kê |
| Model quên yêu cầu đặt ở giữa prompt dài | Attention có hạn và phân bố không đều; token ở giữa nhận ít chú ý hơn ( slide 31 ) |
| Hỏi lại y hệt lại ra câu khác | Đầu ra là phân bố xác suất, không phải một đáp án. Lấy mẫu từ phân bố thì mỗi lần một khác ( slide 77 ) |
| Bảo "nghĩ từng bước" thì đúng, không bảo thì sai | Mỗi token sinh ra được nối lại vào context — cho nó viết nháp là cho nó thêm context để đoán các token sau ( slide 50 ) |
| Chat càng dài càng đắt | Model không nhớ gì; toàn bộ lịch sử được gửi lại mỗi lượt ( slide 78 ) |
| Tiếng Việt tốn tiền hơn tiếng Anh | Tokenizer cắt tiếng Việt thành nhiều mảnh hơn, mà tiền tính theo mảnh ( slide 30 ) |

sống chung

### Slide 27 LLM là gì — một bộ não nền, không phải một chatbot

> Trích slide 
>  "LLM (Large Language Model) là một mô hình ngôn ngữ rất lớn, thường dựa trên kiến trúc Transformer, 
>  được luyện trên hàng nghìn tỷ mảnh chữ để học cách đoán mảnh chữ tiếp theo trong ngữ cảnh." 
>  "Nhờ được luyện đủ rộng, nó trở thành một nền chung: thay vì mỗi việc train một model riêng, 
>  cùng một model làm được rất nhiều việc." 
>  " Chatbot chỉ là một dạng sản phẩm đóng gói quanh bộ não đó — lớp áo bên ngoài. "

Câu chốt này sửa một hiểu lầm rất phổ biến, và nó có hệ quả trực tiếp lên cách bạn thiết kế sản 
 phẩm: **chatbot không phải hình dạng mặc định của một sản phẩm AI**. Nó chỉ là hình dạng 
 dễ thấy nhất.

Slide vẽ một model nền ở giữa, toả ra chatbot, tóm tắt tài liệu, viết code, dịch & phân tích. 
 Điều đáng chú ý: **ba trong bốn cái đó không có giao diện chat**.

Với **SmartCheck AI**, đây là câu hỏi thiết kế thật: kiosk check-in *có cần* một ô chat không? Khách đứng trước màn hình, tay xách vali, thường chỉ muốn bấm vài nút. Một luồng 
 có nút bấm rõ ràng, gọi LLM ở *bên trong* để hiểu ý và điền form, có thể tốt hơn hẳn một ô 
 chat trắng — vì ô chat trắng bắt người dùng tự nghĩ ra phải nói gì.

Đây chính là ý "lớp áo bên ngoài": bộ não giống nhau, lớp áo do bạn chọn 
 theo bối cảnh sử dụng.

**Chú thích nhỏ ở cuối slide đáng đọc**, vì nó gói cả bốn bài sau vào một dòng: *"Model hiện nay chủ yếu là kiến trúc decoder-only (GPT, Claude, Gemini, Kimi), nhiều model dùng 
 MoE; sau pre-training còn các bước căn chỉnh (SFT, RLHF/DPO) và luyện suy luận (reasoning training, 
 từ 2025)."* Bốn bước đó là nội dung [slide 38](#s38), và *căn chỉnh* là trọn vẹn 
 một ngày ở Track 3 (Ngày 22).

### Slide 28–29 Đầu ra là một phân bố xác suất, và vòng lặp predict → append → rerun

> Trích slide 
>  "Bên trong Transformer: đầu ra luôn là một phân bố xác suất. Với mọi ngữ cảnh, model chấm điểm 
>  MỌI từ trong từ vựng — 'land' 22%, 'forest' 9%… — rồi chọn theo xác suất đó" 
>  "Sinh văn bản = đoán → nối vào câu → đoán tiếp. Mỗi token mới được nối vào ngữ cảnh, rồi model 
>  chạy lại từ đầu — vòng lặp predict → append → rerun "

Hai slide này là **trái tim của cả bài**. Chú ý ba chữ trong cụm *predict → append → **rerun***: model không "tiếp tục viết" như người viết tiếp 
 một câu. Nó **chạy lại từ đầu** với ngữ cảnh dài thêm một token.

_Sơ đồ: Vòng lặp sinh văn bản: đoán một token, nối vào ngữ cảnh, rồi chạy lại từ đầu - Ngữ cảnh hiện tại được đưa vào model. Model chấm điểm mọi từ trong từ vựng và trả ra một phân bố xác suất, ví dụ land hai mươi hai phần trăm, forest chín phần trăm, water sáu phần trăm. Một token được chọn theo phân bố đó, rồi nối vào cuối ngữ cảnh. Ngữ cảnh mới dài hơn một token được đưa lại vào model từ đầu, và vòng lặp lặp lại cho tới khi gặp điều kiện dừng. Bên dưới minh hoạ ngữ cảnh dài dần qua bốn bước, cho thấy mỗi token mới đều phải đọc lại toàn bộ phần trước._

Hình 3 — Vòng lặp đoán token (slide 28–29).

một

**① Vì sao output đắt hơn input.** Toàn bộ input được đọc *một lần* trong một 
 lượt chạy. Nhưng để sinh 200 token output, model phải chạy *200 lượt* — mỗi lượt lại đọc lại 
 cả ngữ cảnh đang dài dần. Đó là gốc của tỷ lệ 3–5 lần ở [slide 68](#s68).

**② Vì sao có streaming.** Token được sinh *lần lượt*, nên hiển thị lần lượt 
 là hiển thị đúng bản chất. Giao diện "đang gõ" không phải hiệu ứng trang trí — nó là lộ trình thật 
 của vòng lặp ( [slide 78](#s78) ).

**③ Vì sao model "không nhớ".** Mỗi lần gọi API là một vòng lặp mới, bắt đầu từ ngữ 
 cảnh bạn gửi. Không có gì được giữ lại giữa hai lần gọi — "trí nhớ" là do *bạn* gửi lại lịch 
 sử.

**④ Vì sao "nghĩ từng bước" làm model đúng hơn.** Mỗi token 
 nháp được nối vào ngữ cảnh, nên các token sau được đoán *dựa trên phần nháp đó*. Cho model 
 viết nháp là cho nó thêm dữ kiện để đoán tiếp — đó là toàn bộ cơ chế của Chain-of-Thought 
 ( [slide 50](#s50) ).

mỗi bước

toàn bộ từ vựng

temperature

top_p

slide 77

cách đọc cái bảng xác suất vốn đã có sẵn

### Slide 30 Token — model không đọc "từ", model đọc mảnh chữ

> Trích slide 
>  "Model không nhìn từ nguyên vẹn. Nó cắt văn bản thành các mảnh nhỏ gọi là token: có từ là một 
>  mảnh, có từ vỡ ba bốn mảnh, cả dấu câu và khoảng trắng cũng là mảnh." 
>  "Ví dụ: 'Hello world' ≈ 2 token, nhưng 'Xin chào' có thể tới 3–4 token." 
>  " Tiếng Việt, code, JSON tốn token hơn tiếng Anh thường — vì dấu thanh, ký tự đặc 
>  biệt và cấu trúc bị cắt nhỏ ra." 
>  "Mọi thứ model làm đều quy ra token — và mỗi token đều có giá."

Đoạn về tiếng Việt là đoạn có **hệ quả tài chính trực tiếp** với bạn, và nó đáng được 
 nói rõ hơn slide:

Tokenizer của phần lớn model được huấn luyện chủ yếu trên văn bản tiếng Anh, nên tiếng Anh được 
 cắt hiệu quả nhất — nhiều từ thông dụng là một token trọn vẹn. Tiếng Việt có dấu thanh và tổ hợp ký 
 tự ít gặp hơn trong dữ liệu đó, nên hay bị vỡ thành nhiều mảnh.

Hệ quả: cùng một ý, bản tiếng Việt tốn nhiều token hơn bản tiếng Anh — nên **đắt hơn và chậm hơn**, và *chiếm nhiều chỗ hơn trên bàn làm việc* (context).

**Việc nên làm:** đừng ước lượng token bằng cách đếm từ. 
 Hãy chạy thử prompt thật của bạn qua tokenizer của chính model bạn dùng, rồi lấy con số đó làm cơ 
 sở tính chi phí. Slide chỉ đúng một nửa khi nói "'Xin chào' có thể tới 3–4 token" — con số chính 
 xác phụ thuộc tokenizer, và *khác nhau giữa các model*.

**Code và JSON cũng tốn token bất thường**, vì lý do tương tự: dấu ngoặc, thụt lề, 
 dấu phẩy, tên biến viết liền — mỗi thứ đều thành mảnh riêng. Điều này quan trọng khi bạn thiết kế *structured output*: bắt model trả JSON có tên trường dài dòng là trả tiền cho những tên trường 
 đó, ở mỗi lần gọi, mãi mãi.

mỗi lần gọi

slide 69

mô-đun hoá đơn

### Slide 31 Context — bàn làm việc có hạn của model

> Trích slide 
>  "Mỗi lần trả lời, model chỉ nhìn được một lượng chữ có hạn — gọi là context. Hãy hình dung một 
>  bàn làm việc: mọi thứ muốn model 'thấy' phải bày lên bàn." 
>  "Quy đổi: 128K token ≈ một cuốn sách 300 trang; 1M token ≈ 45 cuốn sách trên bàn cùng lúc." 
>  "Bàn đầy quá thì đồ ở giữa bàn dễ bị bỏ sót — đặt điều quan trọng ở giữa một prompt rất dài, 
>  model có thể 'quên' mất." 
>  " Context càng dài càng tốn tiền và càng chậm — bàn rộng không có nghĩa là dùng tốt "

Ẩn dụ "bàn làm việc" là ẩn dụ tốt nhất trong cả bài, vì nó đúng ở **ba mặt cùng lúc** — và biết nó đúng ở đâu, sai ở đâu là dấu hiệu bạn thật sự hiểu:

| Mặt | Ẩn dụ bàn làm việc | Thực tế trong model |
| --- | --- | --- |
| ✓ Có giới hạn | Bàn chỉ để được từng ấy đồ | Context window có trần cứng; vượt là bị từ chối |
| ✓ Phải bày ra mới thấy | Đồ trong ngăn kéo thì không dùng được | Model chỉ biết những gì nằm trong context lần gọi này |
| ✓ Bày lộn xộn thì khó tìm | Bàn đầy quá thì đồ ở giữa bị lấp | Hiện tượng "lost in the middle" — chú ý phân bố không đều |
| ✕ Chỗ ẩn dụ sai | Bày thêm đồ lên bàn thì miễn phí | Mỗi token trên "bàn" đều tính tiền, ở MỖI lần gọi |

**① Tốn tiền.** Context là input token, và bạn trả tiền cho nó *mỗi lần gọi*. Nhét cả tài liệu 100 trang vào để hỏi một câu là trả tiền cho 100 trang đó, 
 rồi lại trả tiếp ở câu hỏi sau.

**② Chậm hơn.** Attention tốn theo bình phương độ dài — mỗi token nhìn mọi token 
 khác. Gấp đôi context không phải gấp đôi thời gian mà nhiều hơn thế.

**③ Chất lượng có thể *giảm*.** Đây là điều phản trực giác nhất. Thêm ngữ 
 cảnh không liên quan làm loãng sự chú ý — model có nhiều thứ để nhìn hơn nhưng lượng chú ý thì cố 
 định. Slide 36 gọi thẳng: *"Context rác = attention rác."*

**Hệ quả thiết kế, và đây là mầm của cả Ngày 8:** giải pháp 
 cho tài liệu dài *không* phải là mua model có context lớn hơn, mà là **lấy đúng đoạn liên quan rồi mới nhét vào** — tức là RAG. Slide 36 nói đúng câu đó: *"Cho tra sổ thay vì bắt nhớ."*

ước lượng thô

ít trang hơn

slide 30

mục con số

### Slide 32–35 Attention và multi-head — chữ T trong GPT

> Trích slide 
>  "Thay vì đọc tuần tự từng chữ, cơ chế attention cho phép mỗi token: chủ động 'quay đầu' nhìn lại 
>  các token trước đó · chấm điểm mức độ liên quan của từng token · khóa nghĩa theo ngữ cảnh — 'nó' là 
>  quyển sách hay cái túi, tùy theo nó chú ý vào từ nào" 
>  " 'Lan bỏ quyển sách vào túi vì nó quá dày' — muốn biết 'nó' = quyển sách hay cái túi, 
>  mô hình so khớp 'nó' với TẤT CẢ token trước đó, không chỉ token liền kề." 
>  " Multi-head: Model có nhiều con mắt chuyên môn nhìn cùng một câu một lúc: 
>  con mắt đại từ · con mắt không gian · con mắt cú pháp. Mỗi con mắt nhìn một khía cạnh, rồi model 
>  tổng hợp lại."

Ví dụ *"Lan bỏ quyển sách vào túi vì nó quá dày"* được chọn rất khéo, vì nó là một câu mà **chỉ ngữ nghĩa mới giải quyết được** — không có quy tắc ngữ pháp nào nói "nó" chỉ vào 
 đâu. Đổi một tính từ là đổi đáp án: *"…vì nó quá **đầy** "* thì "nó" là cái túi.

Slide 34 so attention với convolution — cửa sổ 3 từ quanh mỗi từ. Với cửa sổ đó, "nó" chỉ nhìn 
 thấy *"vì nó quá"*. Từ *"quyển"* và *"sách"* nằm ngoài tầm, nên mối liên hệ 
 quyết định bị cắt mất.

Attention không có cửa sổ: mỗi token nhìn **toàn bộ** các token trước và tự chấm 
 điểm cái nào đáng chú ý. Cái giá là chi phí bình phương — nhưng đổi lại là khả năng giữ liên hệ xa, 
 và đó là đánh đổi làm nên kỷ nguyên hiện tại.

**Về multi-head:** ẩn dụ "nhiều con mắt chuyên môn" là ẩn dụ 
 dạy học tốt, nhưng cần một cảnh báo — *không ai gán nhiệm vụ cho từng head*. Chúng tự phân 
 hoá trong lúc huấn luyện, và việc diễn giải "head này lo đại từ" là kết quả nghiên cứu *sau khi* mổ xẻ model, không phải thiết kế ban đầu. Slide 48 cũng tự nhắc điều tương tự: *"Attention map cho thấy model NHÌN VÀO ĐÂU — chứ không chứng minh model hiểu."*

### Slide 36 Ba quy tắc dùng attention hiệu quả — slide thực dụng nhất chương 3

> Trích slide 
>  " 1 Đặt điều quan trọng đầu – cuối. Đầu và cuối prompt được chú ý nhiều nhất; 
>  đồ ở giữa dễ bị bỏ sót — yêu cầu quan trọng đừng chôn giữa." 
>  " 2 Giữ bàn làm việc sạch. Context rác = attention rác. Khi chat dài, tóm tắt lại 
>  thay vì kéo theo mọi thứ; khi vibe code, đưa đúng file liên quan, không dán cả repo." 
>  " 3 Cho tra sổ thay vì bắt nhớ. Tài liệu dài: lấy đoạn liên quan nhét vào context 
>  (RAG) thay vì trông chờ model nhớ hết hoặc nhét cả cuốn." 
>  " Agent mạnh không phải vì context khổng lồ — mà vì nó có tools để lấy đúng thứ vào bàn 
>  làm việc đúng lúc "

Ba quy tắc này là **toàn bộ prompt engineering thực dụng** mà bạn cần cho tuần đầu, và 
 mỗi quy tắc là mầm của một ngày học riêng:

| Quy tắc | Suy ra từ cơ chế nào | Nở thành bài nào |
| --- | --- | --- |
| Đặt điều quan trọng đầu – cuối | Chú ý phân bố không đều theo vị trí | Ngày 4 — Prompt Engineering |
| Giữ bàn làm việc sạch | Lượng chú ý cố định; thêm nhiễu là loãng tín hiệu | Ngày 25 — quản lịch sử hội thoại · Ngày 17 — Memory Systems |
| Cho tra sổ thay vì bắt nhớ | Model chỉ biết cái nằm trong context lần gọi này | Ngày 7–8 — Embedding, Chunking, RAG Pipeline |

*"Agent mạnh không phải vì context khổng lồ — mà vì nó có tools để lấy đúng thứ vào bàn làm 
 việc đúng lúc."*

Câu này bác bỏ trước một hiểu lầm sẽ rất phổ biến khi bạn thấy các model quảng cáo context 1 triệu 
 token: **context lớn hơn không thay thế được việc chọn đúng thứ để đưa vào**. Nó chỉ 
 nâng trần, mà trần không phải vấn đề — *chất lượng thứ bạn bày lên bàn* mới là vấn đề.

Và nó là lý do vì sao kiến trúc agent (Ngày 3, 9, 20, 23) tồn tại: agent 
 không phải một model thông minh hơn, nó là một **vòng làm việc biết đi lấy thứ nó cần**. [Slide 52](#s52) nói đúng điều đó bằng bốn mức độ.

#### Ô kiểm tra — Chương 3

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao token đầu ra đắt hơn token đầu vào 3–5 lần? Giải thích từ vòng lặp 
 sinh văn bản. Hiểu

#### Đáp án

**Vì input được đọc một lần, còn mỗi token output đòi một lượt chạy riêng.**

Vòng lặp là *predict → append → **rerun***. Toàn bộ prompt được xử lý trong 
 một lượt (và song song hoá được rất tốt). Nhưng để sinh 200 token, model phải chạy **200 
 lượt** — mỗi lượt lại đọc lại toàn bộ ngữ cảnh đang dài thêm, và mỗi lượt phải chờ lượt 
 trước xong vì token sau phụ thuộc token trước.

**Nói cách khác:** đọc thì song song được, viết thì không. Đó là gốc của cả chênh 
 lệch giá lẫn chênh lệch tốc độ.

**Hệ quả thực hành:** núm vặn chi phí lớn nhất là *kiểm soát độ dài output* ( `max_tokens`, và yêu cầu ngắn gọn trong prompt) — không phải cắt input.

**2.** Đội bạn định nâng cấp lên model có context 1 triệu token để "khỏi phải làm 
 RAG". Phản biện. Đánh giá

#### Đáp án

**Context lớn hơn nâng trần, nhưng trần không phải vấn đề.** Ba lý do:

**① Tiền.** Context là input token và bạn trả tiền *mỗi lần gọi*. Nhét cả 
 kho tài liệu vào để hỏi một câu là trả tiền cho cả kho, rồi trả lại ở câu sau. RAG lấy vài đoạn — 
 rẻ hơn hàng chục tới hàng trăm lần.

**② Tốc độ.** Attention tốn theo bình phương độ dài. Gấp đôi context không phải 
 gấp đôi thời gian mà nhiều hơn thế.

**③ Chất lượng có thể GIẢM.** Đây là điểm phản trực giác và là điểm mạnh nhất: 
 thêm ngữ cảnh không liên quan làm loãng sự chú ý — model có nhiều thứ để nhìn hơn nhưng lượng chú 
 ý cố định. Cộng thêm hiện tượng "lost in the middle": thông tin ở giữa prompt dài dễ bị bỏ sót. 
 Slide 36 gọi thẳng: *"Context rác = attention rác."*

**Câu chốt của slide 36:** *"Agent mạnh không phải vì context khổng lồ — mà vì 
 nó có tools để lấy đúng thứ vào bàn làm việc đúng lúc."*

**3.** Vì sao cùng một prompt viết bằng tiếng Việt tốn nhiều tiền hơn bản tiếng 
 Anh, và bạn nên làm gì với thông tin đó? Áp dụng

#### Đáp án

**Vì tokenizer cắt tiếng Việt thành nhiều mảnh hơn, mà tiền tính theo mảnh.** Tokenizer của phần lớn model được huấn luyện chủ yếu trên tiếng Anh, nên nhiều từ tiếng Anh thông 
 dụng là một token trọn vẹn; tiếng Việt có dấu thanh và tổ hợp ký tự ít gặp hơn nên hay bị vỡ.

**Ba hệ quả cùng lúc:** đắt hơn, chậm hơn, và *chiếm nhiều chỗ hơn trong 
 context* — nên "128K token ≈ 300 trang" là con số cho tiếng Anh, tiếng Việt được ít trang hơn.

**Việc nên làm:**

• Đừng ước lượng token bằng cách đếm từ — chạy prompt thật qua tokenizer của *chính model bạn 
 dùng*, vì con số khác nhau giữa các model. 
 • Ưu tiên tối ưu **system prompt**, vì nó được gửi lại mỗi lần gọi. Cắt 200 token 
 thừa × 30.000 lượt/tháng = tiết kiệm 6 triệu token. 
 • Với structured output, đặt tên trường JSON ngắn — bạn trả tiền cho tên trường ở mỗi lần gọi, 
 mãi mãi.

---

<!-- chiron-source-span: {"source_span_id":"8e35df84-edcc-50d5-a2ce-24a6b2c42fce","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Model được tạo ra như thế nào","source_file":"day-1-ai-llm-foundation.html"},"checksum":"424c887bba3dc682c5ad952cc5c70720b8112037719b6beed81e053d43649264"} -->

## 04 Model được tạo ra như thế nào

Slide 37–48: tham số, bốn bước huấn luyện, câu hỏi "có hiểu không", và giới hạn bẩm sinh.

### Slide 37 Tham số, scaling law và MoE

> Trích slide 
>  "Sau khi luyện xong, những gì model 'biết' nằm trong các con số cố định bên trong gọi là tham số 
>  — hãy hình dung như khớp nối thần kinh: luyện càng kỹ, các khớp nối càng được siết đúng." 
>  " Tham số không phải thứ bạn chỉnh khi dùng model — nó được đóng gói sẵn trong 
>  'bộ não' (file weights). Bạn chỉ chỉnh được context và các núm vặn lúc gọi (như temperature)." 
>  "2020 GPT-3: 175 tỷ — một 'bác sĩ đa năng', mọi token đều đi qua toàn bộ khớp nối (dense). 
>  2026 Kimi K3: 2.800 tỷ — một 'bệnh viện đa khoa', mỗi token chỉ gọi vài chuyên gia (MoE)." 
>  "Luật chơi 2020–2024: cứ thêm compute + dữ liệu là model khôn lên một cách dự đoán được 
>  (scaling law, Kaplan et al. 2020)"

Câu in đậm giữa slide là câu quan trọng nhất cho người mới, vì nó vẽ ra **ranh giới giữa cái bạn điều khiển được và cái bạn không**:

|  | Cố định trong "bộ não" | Bạn chỉnh được lúc gọi |
| --- | --- | --- |
| Là gì | Tham số (weights) — kết quả của quá trình huấn luyện | Context (system prompt, câu hỏi, tài liệu) và các núm vặn ( temperature, top_p, max_tokens ) |
| Quyết định | Model biết gì và giỏi gì | Model nhìn thấy gì và chọn chữ ra sao |
| Đổi được không | Chỉ bằng fine-tuning (Ngày 21) — tốn kém, cần dữ liệu | Đổi tự do, mỗi lần gọi một khác, miễn phí |

Rất nhiều người nghĩ "model trả lời sai ⇒ phải fine-tune". Nhưng nhìn bảng trên sẽ thấy hai cột 
 giải hai loại vấn đề khác nhau:

• Model *không biết* thông tin nội bộ của bạn ⇒ vấn đề **context** ⇒ đưa 
 thông tin vào (RAG). Fine-tune không giải được, vì nó không thêm sự kiện mới một cách đáng tin. 
 • Model *biết* nhưng trả lời sai định dạng hoặc sai giọng điệu ⇒ vấn đề **hành vi** ⇒ sửa prompt trước, fine-tune sau nếu prompt không đủ.

Ngày 21 phát biểu lại nguyên tắc này thành một câu: *"fine-tune không sửa knowledge gap"*. Nó đã nằm sẵn ở đây, trong slide 37 của ngày đầu tiên.

Ẩn dụ của slide rất chuẩn: *bác sĩ đa năng* (dense — mọi token đi qua toàn bộ tham số) so 
 với *bệnh viện đa khoa* (MoE — mỗi token chỉ gọi vài chuyên gia). [Slide 67](#s66) nói rõ hơn: ví dụ 2 trong 8 chuyên gia được kích hoạt cho mỗi token.

Hệ quả với bạn: **số tham số không còn là chỉ báo tốt về giá và 
 tốc độ**. Một model MoE 2.800 tỷ có thể rẻ hơn và nhanh hơn một model dense 400 tỷ. Nên khi 
 so sánh model, hãy so bằng *giá mỗi triệu token* và *độ trễ đo được* — hai thứ nhà 
 cung cấp công bố — chứ đừng so bằng số tham số.

### Slide 38–39 Bốn bước biến cỗ máy đoán chữ thành trợ lý

> Trích slide 
>  "① Pre-training — 'đọc cả thư viện': học tiếng nói và kiến thức từ hàng nghìn tỷ 
>  token. ② SFT — 'được chỉ cách trả lời': học theo ví dụ mẫu để ra dáng trợ lý. 
>  ③ RLHF/DPO — 'được uốn nắn': học theo phản hồi con người, an toàn và dễ chịu hơn. 
>  ④ Luyện suy luận — 'giải đề tự chấm' (từ 2025): luyện toán/code có đáp án kiểm chứng 
>  được → model biết làm nháp trước khi trả lời." 
>  " Đọc vạn cuốn sách chưa chắc biết trả lời phỏng vấn — đó là lý do cần bước ②, ③, ④ " 
>  "RLHF: ① Model viết nhiều câu trả lời → ② Người chấm xếp hạng → REWARD MODEL (máy chấm điểm thay 
>  người) → ③ Huấn luyện theo điểm: tăng xác suất câu ghi điểm cao. Lặp lại hàng nghìn lần → model dần 
>  'biết nghe lời'"

Ẩn dụ "đọc vạn cuốn sách chưa chắc biết trả lời phỏng vấn" giải thích chính xác vì sao có bốn bước 
 thay vì một. Mỗi bước dạy một thứ **khác loại**:

| Bước | Dạy cái gì | Dữ liệu là gì | Học sâu ở |
| --- | --- | --- | --- |
| ① Pre-training | Kiến thức và cách dùng ngôn ngữ | Hàng nghìn tỷ token văn bản thô | — |
| ② SFT | Format — dáng dấp của một câu trả lời | Cặp (câu hỏi, câu trả lời mẫu) | Ngày 21 |
| ③ RLHF / DPO | Hành vi — cái nào tốt hơn cái nào | Xếp hạng của con người giữa các câu trả lời | Ngày 22 |
| ④ Luyện suy luận | Cách nghĩ — làm nháp trước khi trả lời | Bài có đáp án kiểm chứng được bằng máy | Ngày 22 (GRPO, RLVR) |

Nhìn sơ đồ RLHF ở slide 39 kỹ sẽ thấy con người **không** chấm trực tiếp cho model. 
 Con người chỉ *xếp hạng* vài câu trả lời; từ những xếp hạng đó, người ta huấn luyện một 
 model thứ hai — **reward model** — làm "máy chấm điểm thay người".

Lý do rất thực dụng: cần *hàng nghìn lần* lặp để uốn model, mà con người thì không chấm 
 nổi hàng nghìn lần. Reward model là cách nhân bản khả năng phán xét của con người lên quy mô máy.

**Cái giá của mẹo này** — và đây là lý do Ngày 22 tồn tại: 
 reward model *cũng chỉ là một model*, nên nó chấm sai được, và policy có thể học cách "ăn 
 gian" nó (reward hacking). DPO ra đời chính để bỏ hẳn bước reward model đi.

"từ 2025"

có cách kiểm tra 
 đúng-sai bằng máy

Ngày 22

slide 20

### Slide 40–43 Model có "hiểu" không — thí nghiệm Othello-GPT

> Trích slide 
>  "Chỉ đoán token tiếp theo thôi — vậy sao trông giống đang hiểu mình nói gì? 
>  ① Mô hình thế giới bên trong? (nén thế giới thành biểu diễn có cấu trúc) ② Nôn lại dữ liệu huấn 
>  luyện? (chỉ ghép các mẫu chữ theo xác suất)" 
>  "Thí nghiệm Othello-GPT: ✗ Không được dạy luật chơi ✗ Không hề thấy bàn cờ 8×8 ✗ Không biết quân 
>  trắng–đen — chỉ thấy chuỗi ký tự. Câu hỏi: đoán được nước đi tiếp theo không?" 
>  "→ nước đi hợp lệ, tỷ lệ đi sai luật chỉ 0.01%. Không ai cho nó xem bàn cờ — 
>  để đoán đúng token tiếp theo, cỗ máy tự xây một mô hình thế giới bên trong" 
>  "① Que thử đọc được toàn bộ bàn cờ — từ activation bên trong, probe đọc ra trạng thái từng ô. 
>  ② Lật một quân trong 'đầu' nó → nước đi đổi theo — tức nó thật sự dùng bàn cờ đó để 
>  chơi."

Đây là phần hay nhất về mặt trí tuệ trong cả bài, và điều làm nó thuyết phục nằm ở **bước thứ hai** — phần can thiệp — chứ không phải bước thứ nhất.

**Bước 1 (probe đọc ra bàn cờ)** chỉ chứng minh thông tin về bàn cờ *có mặt* trong activation. Nhưng có mặt không có nghĩa là *được dùng* — nó có thể chỉ 
 là sản phẩm phụ, một thứ tương quan mà model không hề dựa vào để quyết định.

**Bước 2 (lật một quân trong biểu diễn nội bộ, thấy nước đi đổi theo đúng luật)** mới chứng minh quan hệ *nhân quả*: model thật sự đọc cái bàn cờ đó để chọn nước.

Phân biệt **tương quan** và **nhân quả** ở đây 
 là bài học phương pháp dùng được ở mọi nơi khác. Chính slide 48 áp lại nó cho attention map: *"Attention map cho thấy tương quan, không chứng minh nhân quả."*

Othello-GPT chứng minh rằng **một model được huấn luyện chỉ để đoán token có thể tự xây một 
 biểu diễn có cấu trúc về miền của nó**. Đó là một kết quả mạnh và bất ngờ.

Nó *không* chứng minh: rằng LLM "hiểu" theo nghĩa con người hiểu; rằng mọi LLM đều xây 
 world model cho mọi miền; hay rằng tranh luận "vẹt thống kê" đã kết thúc. Othello là một trò chơi 
 với luật đơn giản, trạng thái hữu hạn và quan sát đầy đủ — thế giới thật thì không.

Slide 40 dẫn cả hai phía: Turing 1950 và bài "Stochastic parrots" 
 (Bender et al. 2021). Đó là cách trình bày trung thực, và khi trả lời quiz bạn nên giữ đúng thái độ 
 đó — nêu được bằng chứng của cả hai bên là câu trả lời tốt hơn nhiều so với chọn phe.

### Slide 44–46 Ba giới hạn bẩm sinh, và một điều model làm mà bạn không biết

> Trích slide 
>  " Bong bóng thời gian — Model bị 'đóng băng' tại ngày ngừng đọc (knowledge cutoff). 
>  Nói chắc như đúng rồi — Model tối ưu cho câu nghe hợp lý, không phải tra sự thật — 
>  nên có thể tự tin mà sai (hallucination). Bàn làm việc có hạn — Context có trần; 
>  quá dài vừa tốn tiền vừa dễ bỏ sót thông tin ở giữa." 
>  " Đây không phải lỗi tạm thời — đó là bản chất của cỗ máy đoán token. " 
>  "Vì sao model vẫn sai: nó rất giỏi học vẹt đường tắt. Phân loại spam → model thực chất đã học 
>  'đếm số hyperlink'. Suy luận ngôn ngữ (MNLI) → model thực chất đã học 'câu có động từ phủ định'. 
>  Benchmark cao ≠ model hiểu đúng thứ bạn tưởng " 
>  "Model không chỉ mô hình hóa thế giới — nó mô hình hóa cả BẠN. […] Từ cách bạn viết, model tự 
>  dựng một 'hồ sơ' về bạn — và hồ sơ đó ảnh hưởng câu trả lời."

Ba giới hạn đầu đều là **hệ quả trực tiếp của "chỉ đoán token tiếp theo"**, và mỗi cái 
 có một cách sống chung cụ thể:

| Giới hạn | Vì sao nó là bản chất, không phải bug | Cách sống chung | Học ở |
| --- | --- | --- | --- |
| Bong bóng thời gian | Kiến thức nằm trong tham số, mà tham số đóng băng lúc huấn luyện xong | Đưa thông tin mới vào context: RAG, tool gọi API, tìm kiếm web | Ngày 7–8 |
| Nói chắc như đúng rồi | Model tối ưu cho chuỗi token nghe hợp lý, không có cơ chế nào phân biệt "biết" với "đoán" | Bắt trích nguồn; kiểm tra bám nguồn bằng NLI; guardrail đầu ra | Ngày 11, 24 |
| Bàn làm việc có hạn | Attention tốn theo bình phương; chú ý phân bố không đều | Lấy đúng đoạn thay vì nhét cả kho; tóm tắt lịch sử | Ngày 8, 17, 25 |

Ba ví dụ đó không phải model kém. Chúng là model **rất giỏi tìm ra cách rẻ nhất để đạt 
 điểm cao** — và cách rẻ nhất thường không phải cách bạn muốn:

• Phân loại spam → học "đếm số hyperlink" thay vì hiểu nội dung. Email sạch nhiều link vẫn bị gán 
 spam. 
 • Suy luận ngôn ngữ → học "câu có động từ phủ định không" thay vì suy luận. Đổi cấu trúc dữ liệu 
 test là điểm tụt ngay.

**Câu chốt là câu đáng dán lên tường:** *"Benchmark cao ≠ model hiểu đúng thứ bạn tưởng — luôn test trên dữ liệu của chính mình."* Đây là mầm của cả [slide 72](#s71) (benchmark có đáng tin không) và của Ngày 14, Ngày 24. 
 Nó cũng là lý do Ngày 24 nói *"chỉ có một bài test đáng tin hoàn toàn: việc của chính bạn, trên 
 dữ liệu của chính bạn"*.

Ví dụ tiếng Bồ Đào Nha: model dùng động từ giống đực, rồi ngay khi người dùng nhắc tới *chiếc váy*, câu sau chuyển sang tính từ giống cái. **Không ai bảo nó làm vậy** — từ cách bạn viết, model tự dựng một "hồ sơ" về bạn, và hồ sơ đó ảnh hưởng câu trả lời.

**Hai hệ quả:** ① tích cực — đây là lý do nêu rõ persona và 
 bối cảnh trong prompt lại hiệu quả đến vậy; bạn đang *chủ động* điền cái hồ sơ đó thay vì để 
 model đoán. ② cần cảnh giác — model đang suy diễn về người dùng từ những tín hiệu không ai kiểm 
 soát, và suy diễn đó có thể sai hoặc mang định kiến. Với sản phẩm phục vụ khách hàng như **SmartCheck AI**, đây là một rủi ro thật: model có thể đối xử khác nhau với hai khách 
 chỉ vì cách họ gõ chữ.

### Slide 47–48 Bốn cách chạm vào LLM, và bài thực hành mở hộp đen

> Trích slide 
>  " Chat app (ChatGPT · Claude · Kimi) — nhanh nhất, không cần code · 
>  Coding assistant (Cursor · Copilot) — AI ngồi trong IDE · 
>  API — gọi model bằng code ★ hôm nay học cái này · 
>  Self-host (open-weight · Kimi K3 · Llama) — kiểm soát dữ liệu tuyệt đối" 
>  "khởi động nhanh, tiện dùng → ← mức kiểm soát & tùy biến. Cùng một bộ não nền, bốn mức 
>  quyền truy cập — mức truy cập quyết định bạn tùy biến được tới đâu " 
>  "Nghịch để tin: ① Gõ một câu, xem nó bị cắt thành token thế nào. ② Vặn temperature từ 0 lên cao, 
>  nhìn bảng xác suất đổi ra sao. ③ Mở attention map, bấm vào một token, xem nó 'đang nhìn' những token 
>  nào." 
>  " 'Temperature đổi cách model CHỌN CHỮ — chứ không đổi kiến thức model có' · 
>  'Attention map cho thấy model NHÌN VÀO ĐÂU — chứ không chứng minh model hiểu' "

Trục đánh đổi ở slide 47 rất rõ và đáng nhớ: **càng tiện thì càng ít kiểm soát**. 
 Nhưng có một chiều thứ ba mà slide không vẽ ra và lại quan trọng với dự án thật — *dữ liệu của bạn đi đâu*:

| Cách | Tiện | Kiểm soát | Dữ liệu đi đâu | Hợp khi |
| --- | --- | --- | --- | --- |
| Chat app | ★★★ | ★ | Sang nhà cung cấp; có thể bị dùng để huấn luyện tuỳ gói | Thăm dò, học, việc cá nhân |
| Coding assistant | ★★★ | ★★ | Code của bạn sang nhà cung cấp | Viết code hằng ngày |
| API | ★★ | ★★★ | Sang nhà cung cấp, nhưng bạn kiểm soát gửi gì | Xây sản phẩm |
| Self-host | ★ | ★★★★ | Không đi đâu cả | Dữ liệu nhạy cảm, hoặc quy mô lớn |

Vụ Samsung mà [Ngày 24](track-3-day-24.html) kể — kỹ sư dán source code vào ChatGPT 
 rồi cả công ty bị cấm dùng — là hệ quả trực tiếp của việc chọn sai ô trong bảng này.

Với **SmartCheck AI**, cột này còn có một tầng pháp lý: 
 kiosk xử lý họ tên, số CCCD, số điện thoại của khách. Ngày 24 nêu Nghị định PDPL — *chuyển dữ liệu cá nhân qua biên giới cần đồng ý và đánh giá tác động*. Nghĩa là lựa chọn 
 giữa hàng "API" và hàng "Self-host" ở đây *không* chỉ là bài toán kỹ thuật hay chi phí. Cách 
 dung hoà rẻ nhất: dùng API nhưng **bôi đen dữ liệu cá nhân trước khi gửi** — thứ bạn 
 kiểm soát được chính vì bạn đang ở hàng API chứ không phải hàng chat app.

---

<!-- chiron-source-span: {"source_span_id":"1069e13f-0ad7-567c-8ed3-8f81551bfc77","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Từ LLM đến AI Agent","source_file":"day-1-ai-llm-foundation.html"},"checksum":"f0366f4e38b11d3999e2f9258b7faf33c55018944633776800ebb48dea26a2d7"} -->

## 05 Từ LLM đến AI Agent

Slide 49–54: Chain-of-Thought, lớp adaptation, bốn mức độ tự chủ, và giải phẫu một agent.

### Slide 49–50 Chain-of-Thought — chỉ thêm "giấy nháp", từ sai thành đúng

> Trích slide 
>  "Bài toán: 'Có 5 quả bóng tennis. Mua thêm 2 hộp, mỗi hộp 3 quả. Hỏi tổng cộng có bao nhiêu quả?'" 
>  " Không có nháp — Model đọc câu hỏi → bật ra đáp án ngay: 'Đáp án là 27 quả.' ✗ SAI" 
>  " Có giấy nháp — 'Bắt đầu có 5 quả. Mỗi hộp 3 quả × 2 hộp = 6 quả. 5 + 6 = 11. 
>  Đáp án là 11 quả.' ✓ ĐÚNG" 
>  "Cùng một model, cùng một câu hỏi — cho nó được viết nháp từng bước, bản chất suy luận lộ ra"

Đây là ví dụ đáng nhớ nhất cả bài, vì nó cho thấy một điều rất lạ: **khả năng của model không 
 đổi, nhưng kết quả đổi** — chỉ vì bạn cho nó thêm chỗ để viết.

Nhớ lại: mỗi token sinh ra được **nối vào context**, rồi model chạy lại từ đầu.

**Không có nháp:** model phải nhảy thẳng từ câu hỏi tới con số. Toàn bộ phép tính 
 phải xảy ra trong *một lượt chạy*, qua các tầng của mạng — không có chỗ nào để lưu kết quả 
 trung gian.

**Có nháp:** "2 hộp × 3 quả = 6" được viết ra thành token thật, nối vào context. 
 Ở bước tiếp theo, model *đọc lại* con số 6 đó như một dữ kiện có sẵn — nó không phải nhớ, 
 nó chỉ cần đọc.

**Nói ngắn gọn:** giấy nháp biến *tính nhẩm* thành *tính ra giấy*. Context trở thành bộ nhớ làm việc bên ngoài. Đây là hệ quả trực tiếp và đẹp 
 nhất của câu thần chú "chỉ đoán token tiếp theo".

**Vì sao điều này quan trọng ngoài phạm vi bài toán đố:** nó là mầm của *test-time compute* mà [slide 61](#s61) gọi là "trận đua mới ②", và của cả họ 
 reasoning model (o1, R1). Ý tưởng giống hệt, chỉ khác quy mô: thay vì bạn phải viết *"hãy nghĩ từng bước"*, model được huấn luyện để tự làm nháp — và làm nháp rất dài.

là token output

slide 68

chất lượng cao hơn, đổi bằng tiền và độ trễ

### Slide 51–53 Lớp adaptation, bốn mức độ, và giải phẫu một agent

> Trích slide 
>  "LLM đứng một mình chưa làm được gì nhiều. Prompt tĩnh — một lượt hỏi đáp: ✗ Không dữ liệu mới 
>  ✗ Không hành động ngoài đời ✗ Không nhớ gì sau câu trả lời" 
>  "LỚP ADAPTATION: LLM (bộ não) + Context (dữ liệu của mình) + Tools (search · API · database) + 
>  Memory (sổ tay ghi nhớ) + Guardrails (lan can an toàn) + Eval (tự chấm lại chính mình). 
>  Sản phẩm AI thật = bộ não LLM + hệ thống bao quanh — phần khó thường nằm ở hệ thống " 
>  " LEVEL 0 Bộ não suy luận — LLM trần · LEVEL 1 Có kết nối — 
>  + tools · LEVEL 2 Biết lập kế hoạch — + tự chia mục tiêu thành nhiều bước, tự kiểm 
>  tra kết quả · LEVEL 3 Đội agent phối hợp — nhiều agent chuyên biệt chia việc" 
>  " Agent = Goal + Reasoning + Tools + Memory + Action — chạy thành vòng lặp cho 
>  tới khi xong việc"

Câu *"phần khó thường nằm ở hệ thống"* là câu định hình cả khoá học. Sáu thành phần của lớp 
 adaptation ánh xạ gần như một-một vào các ngày còn lại:

_Sơ đồ: Bốn mức độ từ LLM trần tới đội agent phối hợp, và vòng lặp năm bộ phận của một agent - Nửa trên là bốn mức tăng dần. Level 0 là LLM trần, không công cụ, không dữ liệu mới. Level 1 thêm tools nên vượt khỏi bong bóng thời gian. Level 2 thêm khả năng lập kế hoạch, tự chia mục tiêu thành nhiều bước và tự kiểm tra. Level 3 là nhiều agent chuyên biệt chia việc như một đội ngũ. Mức tự chủ và tác động thật tăng dần từ trái sang phải. Nửa dưới vẽ vòng lặp của một agent gồm năm bộ phận: mục tiêu, bộ não suy luận, công cụ, hành động, và bộ nhớ ghi lại các bước, với mũi tên quay lại từ hành động về bộ não để lặp tiếp._

Hình 4 — Bốn mức độ và vòng lặp agent (slide 52–53).

giống nhau

số thứ được nối vào quanh nó

| Thành phần lớp adaptation | Giải quyết giới hạn nào ở slide 44 | Học sâu ở ngày |
| --- | --- | --- |
| Context — dữ liệu của mình | Bong bóng thời gian | Ngày 7–8 |
| Tools — search, API, database | Bong bóng thời gian + không hành động được | Ngày 3–4, 9 |
| Memory — sổ tay ghi nhớ | Không nhớ gì sau câu trả lời | Ngày 17 |
| Guardrails — lan can an toàn | Nói chắc như đúng rồi | Ngày 11, 24 |
| Eval — tự chấm lại chính mình | Không biết mình sai ở đâu | Ngày 14, 24 |

Kiosk check-in dùng LangGraph, có node phân loại, định tuyến, gọi tool, cổng phê duyệt và 
 finalize. Nó ở đâu?

**Level 2.** Có tools (Level 1) *và* có luồng nhiều bước với điều kiện định 
 tuyến, retry hữu hạn, kiểm tra trước khi hành động. Chưa phải Level 3 vì chỉ có một agent, không có 
 nhiều agent chuyên biệt chia việc.

**Điều đáng nói:** nhảy lên Level 3 *không* phải mục 
 tiêu mặc định. Ngày 20 (Multi-Agent) sẽ nói rõ multi-agent thêm rất nhiều chi phí điều phối và điểm 
 hỏng. Với một kiosk có phạm vi hẹp, Level 2 làm tốt gần như chắc chắn là lựa chọn đúng — và [Ngày 25](track-3-day-25.html) chỉ ra chỗ đáng đầu tư tiếp theo không phải thêm agent mà 
 là thêm *độ tin cậy* cho agent đang có.

### Slide 54 Voyager — agent tự xây thư viện kỹ năng

> Trích slide 
>  "GPT-4 (bộ não) → Viết code kỹ năng mới → Chạy trong Minecraft (có feedback thật) → Pass/Fail? 
>  fail → sửa, làm lại · ✅ đạt → cất vào THƯ VIỆN KỸ NĂNG" 
>  "Task mới: 'chế tạo bàn chế tác' → truy xuất top-5 skill liên quan → làm nhanh hơn, ít sai hơn" 
>  " Agent giỏi không chỉ vì bộ não to — vì nó tích lũy kỹ năng thành thư viện và tái sử 
>  dụng "

Voyager minh hoạ hai ý mà bốn mức độ ở slide trước chưa nói hết:

Minecraft cung cấp **feedback thật**: code chạy được hay không, kỹ năng đạt hay 
 fail. Không có tín hiệu đó, vòng lặp "thử → sửa → thử lại" không hoạt động, vì agent không biết mình 
 đang tiến hay lùi.

Đây là cùng một điều kiện với RLVR ở [slide 38](#s38) và với 
 AlphaGo tự chơi ở phần lịch sử: **khi có cách kiểm tra bằng máy, hệ thống tự cải thiện được 
 mà không cần người**. Câu hỏi đầu tiên khi thiết kế một agent tự cải thiện là: *tín hiệu đúng-sai của tôi đến từ đâu?* Nếu không trả lời được, vòng lặp sẽ chỉ là lặp.

lấy 5 kỹ năng liên quan nhất

code kỹ năng

đoạn tài liệu

slide 36

"Agent mạnh không phải vì context khổng lồ — mà vì nó có tools để lấy đúng thứ vào bàn làm việc 
 đúng lúc."

#### Ô kiểm tra — Chương 4 & 5

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao thí nghiệm Othello-GPT cần *hai* bước (probe và can thiệp)? 
 Bước một mình có đủ không? Phân tích

#### Đáp án

**Không đủ — vì bước 1 chỉ chứng minh tương quan, bước 2 mới chứng minh nhân quả.**

**Bước 1 (probe đọc ra trạng thái từng ô từ activation):** chứng minh thông tin về 
 bàn cờ *có mặt* bên trong model. Nhưng có mặt không có nghĩa là được dùng — nó có thể chỉ 
 là sản phẩm phụ mà model không hề dựa vào để quyết định nước đi.

**Bước 2 (lật màu một quân trong biểu diễn nội bộ, thấy nước đi hợp lệ đổi theo đúng 
 luật):** chứng minh model *thật sự đọc* cái bàn cờ đó để chơi.

**Bài học phương pháp dùng được ở nơi khác:** chính slide 48 áp lại nó cho 
 attention map — *"cho thấy tương quan, không chứng minh nhân quả"*. Nhìn thấy model "chú ý" 
 vào đâu không chứng minh nó dùng chỗ đó để quyết định.

**Cẩn trọng cần nêu:** kết quả này không chứng minh LLM "hiểu" như người, cũng 
 không kết thúc tranh luận "vẹt thống kê". Othello có luật đơn giản, trạng thái hữu hạn, quan sát 
 đầy đủ — thế giới thật thì không.

**2.** Cùng một model, cùng một câu hỏi, chỉ thêm "hãy nghĩ từng bước" thì từ sai 
 thành đúng. Giải thích bằng vòng lặp đoán token, và nêu cái giá. Hiểu

#### Đáp án

**Vì giấy nháp biến tính nhẩm thành tính ra giấy — context trở thành bộ nhớ làm việc bên 
 ngoài.**

Nhớ vòng lặp: mỗi token sinh ra được *nối vào context* rồi model chạy lại từ đầu.

• **Không nháp:** model phải nhảy thẳng từ câu hỏi tới đáp số. Toàn bộ phép tính 
 phải xảy ra trong *một lượt chạy*, không có chỗ lưu kết quả trung gian. 
 • **Có nháp:** "2 hộp × 3 quả = 6" được viết ra thành token thật. Ở bước sau, model *đọc lại* con số 6 như một dữ kiện có sẵn — không phải nhớ, chỉ cần đọc.

**Cái giá:** giấy nháp là *token output* — loại đắt nhất (gấp 3–5 lần 
 input). Một câu trả lời có suy luận từng bước có thể tốn gấp năm lần câu trả lời thẳng, và chậm 
 hơn tương ứng.

**Mở rộng:** đây là mầm của test-time compute và của họ reasoning model — cùng ý 
 tưởng, khác quy mô. Với reasoning model, phần nháp có thể dài hơn cả câu trả lời, nên khi tính chi 
 phí đừng chỉ đếm phần bạn nhìn thấy.

**3.** SmartCheck AI đang ở mức nào trong bốn mức, và có nên nhắm lên Level 3 
 không? Đánh giá

#### Đáp án

**Level 2.** Có tools (Level 1) *và* có luồng nhiều bước với điều kiện định 
 tuyến, retry hữu hạn, cổng phê duyệt trước hành động rủi ro. Chưa phải Level 3 vì chỉ có một agent, 
 không có nhiều agent chuyên biệt chia việc.

**Không nên nhắm Level 3 — ít nhất là chưa.** Ba lý do:

① **Phạm vi hẹp không cần chia việc.** Check-in khách sạn là một luồng tuyến tính 
 với vài nhánh; multi-agent giải bài toán "nhiều chuyên môn khác nhau", mà ở đây không có. 
 ② **Multi-agent thêm chi phí điều phối và điểm hỏng** — Ngày 20 nói rõ. Mỗi agent 
 thêm vào là một chỗ nữa có thể hỏng, một chỗ nữa tốn token. 
 ③ **Khoảng trống thật nằm chỗ khác.** Ngày 25 chỉ ra hệ hiện tại không có circuit 
 breaker, không có provider dự phòng, không đo P95 — tức là ba trong sáu nhóm lỗi còn trống. Đầu tư 
 vào *độ tin cậy của agent đang có* cho lợi ích lớn hơn nhiều so với thêm agent.

**Nguyên tắc:** mức cao hơn không phải mục tiêu mặc định. Nó chỉ đáng khi bài toán 
 thật sự đòi hỏi năng lực mà mức hiện tại không đáp ứng được.

---

<!-- chiron-source-span: {"source_span_id":"b48d5fa3-85ca-5452-ab89-44814de4a90b","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Landscape hôm nay","source_file":"day-1-ai-llm-foundation.html"},"checksum":"2b00e69134f14bee589427f468bfa6528202d21e6d94c92eeb62f8523ad86206"} -->

## 06 Landscape hôm nay

Slide 55–63: giá rơi, năng lực hội tụ, kiến trúc chạm trần, và token không chỉ là chữ.

### Slide 55–59 Ba xu hướng: giá rơi · năng lực hội tụ · từ model sang system

> Trích slide 
>  "Mỗi năm có hàng chục model đáng chú ý — đừng học thuộc tên, hãy học quỹ đạo " 
>  "Cùng một mức năng lực, giá rơi khoảng 10 lần mỗi năm. Việc năm ngoái phải dùng 
>  model đắt nhất — năm nay model rẻ đã làm được" 
>  "Năng lực hội tụ — và model mở đang bắt kịp model đóng. Không còn một model bỏ xa phần còn lại — 
>  chọn model là bài toán phương pháp, không phải bài toán nhớ tên " 
>  "Từ model đơn lẻ sang hệ thống biết hành động. Làn sóng hiện tại không phải 'model nào mạnh hơn' 
>  — mà là system nào dùng model khôn hơn "

Ba xu hướng này có **một hệ quả chung** mà slide không gộp lại, nhưng đáng gộp vì nó 
 quyết định cách bạn đầu tư thời gian:

| Xu hướng | Nghĩa là gì với bạn | Cái gì mất giá | Cái gì lên giá |
| --- | --- | --- | --- |
| Giá rơi ~10× mỗi năm | Ràng buộc chi phí hôm nay có thể biến mất năm sau | Tối ưu vi mô cho một mức giá cụ thể | Kiến trúc dễ đổi model |
| Năng lực hội tụ | Không có model nào "đúng" tuyệt đối | Thuộc lòng bảng xếp hạng | Phương pháp tự đo trên việc của mình |
| Từ model sang system | Lợi thế nằm ở phần bao quanh, không ở model | Chờ model mạnh hơn để giải bài toán | RAG, tools, guardrails, eval — tức phần còn lại của khoá |

Nếu giá rơi 10 lần mỗi năm và năng lực hội tụ, thì **model bạn chọn hôm nay gần như chắc 
 chắn không phải model bạn dùng sau 12 tháng**. Điều đó biến "dễ đổi model" từ một thứ 
 nice-to-have thành một yêu cầu thiết kế.

Cụ thể: tách lời gọi model ra sau một lớp mỏng của riêng bạn, đừng rải `client.chat.completions.create(...)` khắp codebase. [Slide 79](#s78) nói cú 
 pháp OpenAI và Anthropic *tương đương* — nên lớp mỏng đó thật sự mỏng.

Và đây cũng là tiền đề của [Ngày 25](track-3-day-25.html): 
 khi đã có lớp trừu tượng đó rồi, thêm *fallback chain* gần như miễn phí. Một quyết định phục 
 vụ hai mục đích — đổi model cho rẻ, và sống sót khi provider chết.

"tổng hợp từ bảng giá các nhà cung cấp, 2023–2026"

bậc độ lớn

mục con số

### Slide 60–62 Cái gì đi lên, cái gì chạm trần — slide có nhiều thông tin nhất chương

> Trích slide 
>  " Cái gì ĐI LÊN: Cách đánh số ghế khôn hơn (RoPE) · Cuốn sổ ghi chú dùng chung 
>  (GQA/MLA) — đọc context dài rẻ đi nhiều lần · Bệnh viện đa khoa (MoE) — 175 tỷ → 2.800 tỷ tham số · 
>  Bàn làm việc — từ 2–3 trang (2K) tới 45 cuốn sách (1M token)" 
>  " Cái gì CHẠM TRẦN: Đọc hết sách trong thư viện — 2024 model đã đọc gần hết văn 
>  bản công khai của nhân loại ('data wall') → 'to hơn + đọc nhiều hơn' không còn thắng chắc. 
>  Trận đua mới ① — luyện đề tự chấm (RLVR). Trận đua mới ② — được 
>  nghĩ kỹ (test-time compute)" 
>  "Lõi Transformer không đổi từ 2017 — như động cơ đốt trong: piston vẫn là piston, nhưng mọi thứ 
>  xung quanh được tối ưu điên cuồng." 
>  "SWE-bench Verified: 33% (6/2024) → 81% (2/2026) — đang chạm trần bão hòa quanh 80%: 
>  benchmark này sắp 'hết khó' để phân biệt model "

Ẩn dụ động cơ đốt trong rất chuẩn và đáng nhớ: **kiến trúc lõi không đổi trong 9 năm**. 
 Mọi tiến bộ đến từ ba chỗ khác — và biết ba chỗ đó giúp bạn đọc được tin tức model mà không bị choáng:

| Hướng cải tiến | Giải quyết cái gì | Bạn thấy nó ở đâu khi dùng |
| --- | --- | --- |
| Nén dữ liệu hiệu quả hơn RoPE · GQA/MLA · MoE | Chi phí và độ dài context | Context window to hơn, giá rẻ hơn, tốc độ nhanh hơn — mà tên model vẫn thế hệ cũ |
| Luyện bằng bài tập tự chấm RLVR | Chất lượng suy luận ở miền có đáp án kiểm chứng được | Model đột nhiên giỏi toán và code hơn hẳn, nhưng viết văn thì không đổi mấy |
| Cho model thời gian nghĩ test-time compute | Chất lượng, đổi bằng độ trễ và tiền | Chế độ "reasoning" — chậm hơn nhiều, đắt hơn nhiều, đúng hơn ở bài khó |

Nhớ lại cấu trúc lặp lại ở [chương lịch sử](#s9): một cách tiếp cận chạm trần của chính 
 nó, rồi ngành đổi câu hỏi. Scaling law (2020–2024) là cách tiếp cận thứ ba, và trần của nó là **hết dữ liệu** — không phải hết tiền hay hết GPU.

**Khác biệt so với hai lần trước:** lần này hai hướng đi 
 tiếp đã có sẵn khi trần bị chạm. Cả hai đều *không cần thêm dữ liệu người*: RLVR sinh tín 
 hiệu từ máy chấm (toán có đáp số, code có test), test-time compute không cần dữ liệu mới chút nào — 
 chỉ cần cho model nhiều lượt chạy hơn. Đó là lý do chưa có mùa đông thứ ba.

Slide ghi rõ nó *"sắp hết khó để phân biệt model"*. Khi một benchmark tiến gần trần, chênh 
 lệch giữa hai model trên benchmark đó không còn nói lên nhiều — mọi model đều gần 80% thì 2 điểm 
 chênh là nhiễu.

Đây là lý do phải ra đề mới (SWE-bench Pro), và cũng là mầm của [slide 72](#s71): benchmark là tín hiệu, không phải bằng chứng. Nối thẳng sang [Ngày 24](track-3-day-24.html), nơi cả một ngày dành cho việc tự dựng bộ đo của riêng mình.

### Slide 63 Multimodal — "token" không chỉ là chữ

> Trích slide 
>  "Mọi thứ bạn vừa học — token, context, attention — không chỉ dùng cho chữ viết." 
>  "Hãy nhớ lại 'bàn làm việc' của model: ngày xưa nó chỉ bày được chữ. Giờ người ta cắt ảnh thành 
>  những mảnh nhỏ, cắt tiếng thành những đoạn ngắn — rồi gọi chúng là 'token' y như mảnh chữ, và bày 
>  lên đúng cái bàn đó." 
>  " Bộ não bên trong không đổi — vẫn là cỗ máy đoán token tiếp theo. Chỉ khác là 
>  giờ nó 'nhìn' được hình, 'nghe' được tiếng."

Slide này ngắn nhưng có giá trị lớn: nó cho thấy **mọi thứ bạn học ở chương 3 vẫn áp dụng 
 nguyên vẹn** cho ảnh, PDF, audio. Bạn không phải học lại một mô hình tinh thần mới.

Nếu ảnh được cắt thành token và bày lên cùng cái bàn, thì mọi hệ quả về token đều áp dụng:

• **Ảnh tốn context** — một ảnh độ phân giải cao có thể ngốn hàng nghìn token, đẩy 
 tài liệu khác ra khỏi bàn. 
 • **Ảnh tốn tiền** — và thường nhiều hơn người ta tưởng. Gửi 10 ảnh trong một prompt có 
 thể đắt hơn cả trang văn bản. 
 • **Ảnh làm chậm** — nhiều token hơn ⇒ chậm hơn, đúng "một núm vặn" ở [slide 70](#s69).

Với **SmartCheck AI**: nếu kiosk chụp ảnh CCCD để đọc thông 
 tin, đó không phải một tính năng "miễn phí thêm vào" — nó là một khoản token đáng kể trên mỗi lượt 
 check-in. Và nó chạm thẳng vào vấn đề dữ liệu cá nhân ở [slide 47](#s47): ảnh giấy tờ là 
 dữ liệu nhạy cảm hơn cả văn bản.

---

<!-- chiron-source-span: {"source_span_id":"08a1bea1-420f-5ee3-9601-d48dce8ad1aa","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Chọn model & chi phí token","source_file":"day-1-ai-llm-foundation.html"},"checksum":"9e18342483a48d68f278fcf3d40ebe3654dedcc1e89616f4fd957431dd08efd3"} -->

## 07 Chọn model & chi phí token

Slide 64–72: khung chọn tầng, ba trục làm model giỏi hơn, và kinh tế học của token.

### Slide 64–65 Chọn model theo TẦNG, không chọn theo tên

> Trích slide 
>  " Hai lỗi đối xứng: ✗ việc đơn giản mà gọi frontier → phí tiền · 
>  ✗ việc khó mà cố dùng rẻ → kết quả tệ" 
>  " TẦNG 1 — FRONTIER ĐÓNG — đắt nhất, chỉ trả cho việc thật sự khó · 
>  TẦNG 2 — RẺ MÀ MẠNH — giải quyết đa số việc hằng ngày 
>  ★ MẶC ĐỊNH THỬ TẦNG NÀY TRƯỚC · 
>  TẦNG 3 — SELF-HOST / SIÊU RẺ — khi cần kiểm soát dữ liệu hoặc chi phí quy mô lớn" 
>  " Bắt đầu từ model đủ tốt và đủ rẻ — chỉ nâng tầng khi kết quả thực sự chặn use case "

Khung ba tầng này là **phần bền nhất của cả chương** — tên model sẽ đổi, nhưng cách 
 chọn thì không. Điều đáng chú ý là chiến lược mà slide khuyên: *bắt đầu từ tầng 2, đi lên chỉ khi 
 bị chặn*.

Trực giác nói: dùng model tốt nhất để có kết quả tốt nhất, tối ưu chi phí sau. Nhưng có hai lý do 
 khiến điều đó sai:

**① Bạn không biết mình cần gì cho tới khi thử.** Nếu tầng 2 đã đủ, bạn tiết kiệm 
 được rất nhiều mà không mất gì. Nếu không đủ, *chỗ nó không đủ* là thông tin quý — nó nói cho 
 bạn biết bài toán khó ở đâu, và đôi khi câu trả lời không phải nâng tầng mà là sửa prompt hoặc thêm 
 context.

**② Đi từ đắt xuống rẻ khó hơn đi từ rẻ lên đắt.** Khi đã xây quanh model frontier, 
 prompt và luồng của bạn ngầm dựa vào năng lực của nó. Hạ tầng về sau thường vỡ ở những chỗ bạn không 
 lường được. Đi lên thì ngược lại — thường chỉ cần đổi tên model.

Đây cũng chính là logic của [fallback ladder 
 ở Ngày 25](track-3-day-25.html), nhìn từ chiều ngược lại: nếu bạn đã chạy được ở tầng 2, thì tầng 1 là bậc nâng cấp 
 sẵn có khi cần, và tầng 3 là bậc dự phòng khi cần rẻ.

tầng 2

không phải vì chất lượng

### Slide 66–67 Ba trục làm model "giỏi hơn" — tham số chỉ là MỘT

> Trích slide 
>  " Trục 1 — Pretraining scale. Cùng ngân sách tính toán (Chinchilla, 2022): 
>  MT-NLG 530B, Gopher 280B, GPT-3 175B, Chinchilla 70B ← ÍT tham số nhất mà THẮNG cả 3 
>  — vì được nuôi bằng dữ liệu tương xứng đúng tỉ lệ. To không bằng cân đối. " 
>  " Trục 2 — Post-training. CÙNG 175 tỷ tham số, chỉ khác có RLHF hay không 
>  (InstructGPT, 2022): GPT-3 175B chỉ pretrain — 15% người ưa thích; InstructGPT 175B cùng size + RLHF 
>  — 85%." 
>  " Trục 3 — Test-time / agentic compute. CÙNG một model (Claude Opus 4.8), chỉ đổi 
>  bộ đề / harness: SWE-bench Verified 88.6% vs SWE-bench Pro 69.2% — lệch tới 19 điểm cùng một 
>  model."

Ba trục này là **slide chống hiểu lầm quan trọng nhất của chương**, vì "model to hơn 
 thì giỏi hơn" là niềm tin mặc định của gần như mọi người mới. Ba bằng chứng, ba kiểu:

| Trục | Thí nghiệm giữ cố định cái gì | Kết quả | Bài học |
| --- | --- | --- | --- |
| 1 · Pretraining | Cùng ngân sách tính toán, khác số tham số và lượng dữ liệu | Model nhỏ nhất (70B) thắng cả ba model to hơn | Tỷ lệ tham số/dữ liệu quan trọng hơn kích thước |
| 2 · Post-training | Cùng 175 tỷ tham số, chỉ khác có RLHF | 15% → 85% người ưa thích | Cách uốn nắn quan trọng hơn kích thước |
| 3 · Test-time | Cùng một model duy nhất, chỉ đổi bộ đề/harness | Lệch 19 điểm | Cách cho model "được nghĩ" quan trọng hơn kích thước |

Con số 88,6% và 69,2% là **hai bộ đề khác nhau** (SWE-bench Verified — đề một file, 
 đã bão hoà; SWE-bench Pro — đề đa file, khó hơn), chứ không phải cùng một bộ đề với hai harness khác 
 nhau.

Nên kết luận đúng từ cặp số này là: **"cùng một model, đổi độ khó của đề thì điểm lệch 19 
 điểm"** — tức là bài học về *benchmark*, không phải về test-time compute. Nó củng cố [slide 72](#s71) rất mạnh: điểm số chỉ có nghĩa kèm theo tên bộ đề.

**Điều đó không làm trục 3 sai** — test-time compute thật sự 
 là một trục có thật và quan trọng (bằng chứng đơn giản nhất là chính ví dụ Chain-of-Thought ở [slide 50](#s50) ). Chỉ là cặp số cụ thể này minh hoạ cho một ý khác với nhãn của nó. 
 Ghi vào [mục con số](#numbers).

trục 3 nằm hoàn toàn trong tay bạn

trục duy nhất bạn điều khiển được cũng là trục cho hiệu ứng 
 đáng kể nhất mà không tốn tiền nâng cấp model

### Slide 68 Token có giá: vé vào rẻ, vé ra đắt gấp 3–5 lần

> Trích slide 
>  " VÉ VÀO — INPUT (1×) chữ BẠN gửi đi: prompt · system instruction · context · 
>  lịch sử chat. rẻ — model chỉ cần đọc " 
>  " VÉ RA — OUTPUT (3–5×) chữ MODEL viết ra — nó phải tự sinh từng mảnh một, vừa 
>  chậm vừa tốn. đắt — model phải 'vắt óc' " 
>  "HÓA ĐƠN — 1 LẦN GỌI API: input 1.150 tok × $3/1M = $0.00345 · output 200 tok × $15/1M = $0.00300 
>  · TỔNG ≈ $0.0065 " 
>  " Input tokens + Output tokens = Chi phí mỗi lần gọi — kiểm soát output là núm vặn lớn 
>  nhất "

Phép tính này **đúng chính xác** — kiểm lại: 1.150 × 3 ÷ 1.000.000 = $0,00345; 
 200 × 15 ÷ 1.000.000 = $0,00300; tổng $0,00645, làm tròn $0,0065. Điều đáng chú ý nằm ở tỷ lệ:

1.150 input + 200 output = 1.350 token. Output là **14,8%** số token, nhưng 
 $0,00300 / $0,00645 = **46,5%** chi phí.

**Vì sao:** đúng như [Hình 3](#f3) giải thích — input được đọc một lượt, 
 output đòi một lượt chạy cho *mỗi* token, mỗi lượt lại đọc lại toàn bộ ngữ cảnh đang dài dần. 
 Đọc thì song song được, viết thì không.

**Hệ quả:** câu chốt của slide đúng — *"kiểm soát output là núm vặn lớn nhất"*. Cụ thể: đặt `max_tokens` hợp lý, và *yêu cầu ngắn gọn ngay trong prompt* ("trả lời trong 3 gạch đầu dòng"). Một prompt dài thêm 
 100 token rẻ hơn nhiều so với một câu trả lời dài thêm 100 token.

**Câu cuối slide đáng làm ngay từ ngày đầu:** *"Đọc mục usage trong mỗi response — 
 đó là hóa đơn chi tiết giúp bạn kiểm soát chi phí từ ngày đầu."* Trường `usage` có sẵn trong mọi response ( [slide 76](#s76) ) và ghi nó vào log tốn vài 
 dòng. Không ghi thì cuối tháng bạn chỉ có một con số tổng, không biết tính năng nào đắt — 
 đúng lời cảnh báo của [Ngày 25](track-3-day-25.html): *"cần cost theo feature/user/model để tìm đường call đắt"*.

#### Tương tác Hoá đơn một lần gọi API — và chọn tầng model đáng bao nhiêu tiền

Đặt số token vào/ra và lưu lượng. Mô-đun tính hoá đơn mỗi lần gọi, mỗi tháng, và so 
 bốn tầng model với nhau.

Mặc định đúng ví dụ [slide 68](#s68): **1.150 token vào, 200 token ra**, 
 giá $3/$15 — ra **$0,0065** một lần gọi.

Đoán trước: output chỉ chiếm **14,8%** số token. Vậy nó chiếm bao nhiêu phần trăm 
 hoá đơn?

#### Nhìn biểu đồ rồi mở

**46,5% — gần một nửa hoá đơn, từ chưa tới 15% số token.**

**Vì sao:** vé ra đắt gấp 5 lần vé vào ($15 so với $3). Nhân 14,8% với 5 rồi chuẩn 
 hoá lại thì ra đúng con số đó. Đây là lý do câu chốt của slide là *"kiểm soát output là núm vặn lớn nhất"*, chứ không phải cắt input.

**Thử điều đáng thử nhất:** giữ nguyên mọi thứ, kéo output từ 200 lên **800** token — hoá đơn nhảy từ $0,0065 lên **$0,0155**, tức **gấp 2,4 lần**, chỉ vì câu trả lời dài hơn. Trong khi kéo *input* từ 1.150 lên 
 1.800 (thêm 650 token, nhiều hơn cả) chỉ làm hoá đơn lên $0,0084 — tăng 30%.

**Bài học vận hành:** khi tối ưu chi phí, thứ tự đúng là ① rút ngắn output 
 ( `max_tokens` + yêu cầu súc tích trong prompt) → ② hạ tầng model → ③ cắt input. 
 Nhiều đội làm ngược, bắt đầu bằng việc cắt system prompt — chỗ ít tác dụng nhất.

*Thử thêm:* chuyển sang tầng "rẻ mà mạnh" ($0,8/$4) — cùng khối lượng, hoá đơn tháng rơi **3,75 lần**. Con số 3,75 này không phụ thuộc bạn đặt bao nhiêu token, vì giá vào và 
 giá ra của hai tầng cùng tỷ lệ với nhau.

- **Control - Token vào 1.150**: min `50`, max `8000`, step `50`, default `1150`

- **Control - Token ra 200**: min `20`, max `4000`, step `20`, default `200`

- **Control - Lưu lượng 1.000 lượt/ngày**: min `10`, max `20000`, step `10`, default `1000`

Tầng model

Frontier $5/$25

Chuẩn $3/$15

Rẻ mà mạnh $0,8/$4

Một lần gọi

—

—

Chi phí mỗi tháng

—

—

Output chiếm bao nhiêu hoá đơn

—

—

Token mỗi tháng

—

vào + ra

vé vào (input) vé ra (output)

#### Xem bảng so bốn tầng



#### Công thức & giới hạn của mô hình

- chi phí = (token_vào × giá_vào + token_ra × giá_ra) / 1.000.000. Tháng = ngày × 30.
- Giá các tầng lấy từ bảng ở slide 83 (7/2026): Opus 4.8 $5/$25 · 
 Sonnet 4.6 $3/$15 · Haiku 4.5 $0,8/$4. Giá thay đổi liên tục — slide 57 nói giá 
 rơi khoảng 10 lần mỗi năm, nên hãy tra giá hiện tại trước khi dùng con số nào ra ngoài.
- Giả định giá phẳng. Thực tế nhiều nhà cung cấp có prompt caching (giảm mạnh 
 giá cho phần prefix lặp lại) và batch API (giảm ~50% nếu chấp nhận chờ) — hai thứ này có thể đổi 
 hẳn kết luận ở lưu lượng lớn.
- Không tính token của phần "suy luận" ở reasoning model. Với các model đó, phần nháp cũng là 
 output và có thể dài hơn cả câu trả lời — xem slide 50.
- Số token phải đo bằng tokenizer thật, không ước lượng bằng số từ — đặc biệt 
 với tiếng Việt ( slide 30 ).

### Slide 69–70 Prompt dài = hoá đơn dài, và "một núm vặn, hai hệ quả"

> Trích slide 
>  " system prompt + context: TRẢ TIỀN LẠI MỖI LẦN GỌI " 
>  "Lần gọi thứ nhất: 50 (câu hỏi user) + 300 (system prompt — lặp lại mỗi lần! ) + 
>  800 (context tra sổ RAG) + 200 (output) = 1.350 tok " 
>  "Lần gọi thứ mười — history đã phình ra: 50 + 300 + 1.200 (history tích lũy) + 800 + 200 = 
>  2.550 tok. mỗi lượt chat cũ được gửi lại toàn bộ → càng chat càng đắt " 
>  "Nhiều token hơn = vừa chậm hơn, vừa đắt hơn. Cả hai cùng quy về một thứ: số token model 
>  phải đọc và sinh ra — đó là 'một núm vặn'. " 
>  "Ví dụ tiền thật — chatbot 1.000 lượt/ngày: 1.350 tok × 1.000 lượt × 30 ngày ≈ 40 triệu 
>  token/tháng. Cùng một việc đủ tốt, giá 3/2026 — chọn sai tầng là trả đắt gấp 4 lần mỗi 
>  tháng: Haiku $36 · Sonnet $135"

Slide 69 chỉ ra cơ chế mà nhiều người chỉ phát hiện khi nhìn hoá đơn: **chatbot không có trí nhớ, nên "trí nhớ" là thứ bạn phải trả tiền để gửi lại mỗi lượt**. 
 Mô-đun dưới đây cho bạn thấy nó phình ra thế nào.

#### Tương tác Vì sao càng chat càng đắt — và tóm tắt lịch sử cứu được bao nhiêu

Mỗi lượt chat, toàn bộ lịch sử được gửi lại. Mô-đun mô phỏng một cuộc hội thoại và so 
 ba chiến lược quản lịch sử.

Mặc định theo [slide 69](#s69): system prompt **300** token, context RAG **800**, mỗi lượt người dùng hỏi **50** và model trả **200**. Lượt 1 tốn 1.350 token — đúng con số của slide.

Đoán trước: đến **lượt thứ 20**, một lượt tốn bao nhiêu token, và cả cuộc hội thoại 
 cộng dồn tốn gấp mấy lần so với việc mỗi lượt đều là lượt đầu?

#### Xem biểu đồ rồi mở

**Lượt thứ 20 tốn 6.100 token — gấp 4,5 lần lượt đầu.** Và cả cuộc hội thoại 20 
 lượt tốn **74.500 token**, so với 27.000 nếu mỗi lượt độc lập — tức **gấp 2,8 lần**.

**Vì sao phình:** mỗi lượt trước đó đóng góp 250 token (50 hỏi + 200 đáp) vào lịch 
 sử, và lịch sử đó được gửi lại *toàn bộ* ở mọi lượt sau. Đây là tăng trưởng bậc hai — 
 lượt thứ n phải trả cho tất cả n−1 lượt trước.

**Bật "tóm tắt lịch sử"** (nén phần cũ xuống còn 200 token khi vượt ngưỡng): cả 
 cuộc hội thoại còn **36.250 token** — **tiết kiệm 51%**. Và quan 
 trọng hơn con số: chi phí mỗi lượt trở nên *gần như phẳng* thay vì tăng mãi, nên bạn dự 
 đoán được chi phí cho một cuộc hội thoại dài bất kỳ.

**Đây chính là lời khuyên ở [slide 36](#s36)** — *"khi chat dài, tóm tắt lại thay vì kéo theo mọi thứ"* — nhưng giờ bạn có con số cho nó. 
 Và nó có lợi kép: rẻ hơn *và* chất lượng tốt hơn, vì "context rác = attention rác".

*Thử thêm:* kéo system prompt từ 300 lên 1.000 token. Với 20 lượt, riêng system prompt 
 đã ngốn 20.000 token — nhiều hơn cả tổng câu hỏi và câu trả lời. Đây là lý do system prompt là chỗ 
 đáng tối ưu nhất: bạn trả tiền cho nó ở *mỗi* lượt.

- **Control - System prompt 300 token**: min `0`, max `2000`, step `50`, default `300`

- **Control - Context RAG mỗi lượt 800 token**: min `0`, max `4000`, step `100`, default `800`

- **Control - Mỗi lượt: hỏi 50 · đáp 200**: min `50`, max `1000`, step `50`, default `200`

- **Control - Số lượt hội thoại 20**: min `2`, max `50`, step `1`, default `20`

Quản lịch sử

Gửi lại toàn bộ

Tóm tắt khi dài

Không gửi lịch sử

Lượt cuối tốn

—

—

Cả cuộc hội thoại

—

—

Chi phí cả cuộc

—

giá $3/$15

Tóm tắt tiết kiệm

—

so với gửi lại toàn bộ

system + context (cố định mỗi lượt) lịch sử tích luỹ hỏi + đáp của lượt này

#### Xem dạng bảng



#### Công thức & giới hạn của mô hình

- Lượt n: token = system + context + lịch_sử(n) + hỏi + đáp, trong đó 
 lịch_sử(n) = (n−1) × (hỏi + đáp) ở chế độ gửi lại toàn bộ.
- Chế độ tóm tắt: khi lịch sử vượt 1.000 token, phần cũ được nén xuống còn 
 200 token cố định. Hai con số này là giả định của tài liệu này để minh hoạ, không 
 có trên slide — chiến lược tóm tắt thật có nhiều biến thể (cửa sổ trượt, tóm tắt đệ quy, memory 
 có cấu trúc — Ngày 17).
- Chế độ không gửi lịch sử: mỗi lượt độc lập. Rẻ nhất, nhưng model không hiểu 
 được câu hỏi tham chiếu tới lượt trước ("cái đó giá bao nhiêu?").
- Chi phí quy ước toàn bộ token vào là input, phần "đáp" của lượt hiện tại là output. 
 Đơn giản hoá: thực tế các lượt đáp cũ nằm trong lịch sử được tính giá 
 input ở lượt sau — mô hình đã tính đúng như vậy.
- Không mô hình hoá prompt caching, thứ có thể giảm mạnh chi phí phần prefix 
 lặp lại (system prompt). Nếu nhà cung cấp của bạn có tính năng này, tiết kiệm thật sẽ khác đáng kể.
- Không mô hình hoá trần context: hội thoại đủ dài sẽ vượt context window và bị từ chối 
 — một lý do nữa để tóm tắt, ngoài lý do tiền.

### Slide 71–72 Phong cách model, và benchmark có đáng tin không

> Trích slide 
>  "Cùng một prompt — ba model, ba phong cách trả lời. Claude: mạch lạc, thiên cấu trúc → hợp phân 
>  tích, viết tài liệu dài · GPT: tự nhiên, linh hoạt → hợp app/chat đa dụng · Gemini/Kimi: bám nhiều 
>  tài liệu → hợp workflow nhiều file" 
>  " Chọn model không chỉ là chọn giá và điểm số — còn là chọn phong cách " 
>  "Benchmark có đáng tin không? — tin vừa thôi. ① Model học vẹt đường tắt 
>  ② Đề thi bị bão hòa ③ Học tủ đề (benchmaxxing) — model có thể được luyện đúng dạng đề để ăn điểm." 
>  "Ví dụ profile không phẳng: 2023 GPT-4 đỗ Bar exam ở top 10% — nhưng Codeforces dưới 5%. 
>  Điểm cao ở kỳ thi này không nói gì về kỳ thi khác. " 
>  " Chỉ có một bài test đáng tin hoàn toàn: việc của chính bạn, trên dữ liệu của chính bạn. "

Ví dụ Bar exam so với Codeforces là ví dụ mạnh nhất chống lại việc đọc benchmark một cách ngây thơ: **cùng một model, cùng một thời điểm, top 10% ở kỳ thi này và dưới 5% ở kỳ thi kia**. 
 Không có một con số duy nhất nào tóm tắt được năng lực của một model.

| Bẫy | Cơ chế | Bạn phát hiện bằng cách nào |
| --- | --- | --- |
| Học vẹt đường tắt | Model tìm ra tín hiệu rẻ tiền tương quan với đáp án (slide 45) | Đổi cấu trúc dữ liệu test — điểm tụt ngay |
| Đề bão hoà | Mọi model đều gần trần nên chênh lệch là nhiễu (SWE-bench Verified ~81%) | Nhìn khoảng cách giữa top 5 model — nếu dưới vài điểm thì bỏ qua bảng đó |
| Học tủ đề | Model được luyện đúng dạng đề để ăn điểm | Gần như không phát hiện được từ bên ngoài |

**Bẫy thứ ba nguy hiểm nhất** vì nó không để lại dấu vết 
 quan sát được: bạn không biết dữ liệu huấn luyện của model có chứa bộ đề hay không. Đó là lý do câu 
 chốt của slide là câu duy nhất đứng vững: *bài test đáng tin duy nhất là việc của chính bạn, trên 
 dữ liệu của chính bạn.*

"Lấy một prompt trong công việc của bạn, chạy thử trên 2–3 model, so sánh."

eval ở Ngày 24

SmartCheck AI

Ngày 24

#### Ô kiểm tra — Chương 6 & 7

Trả lời thành tiếng trước khi mở đáp án.

**1.** Trong một lần gọi 1.150 token vào và 200 token ra, output chỉ chiếm 14,8% 
 số token. Nó chiếm bao nhiêu phần trăm hoá đơn, và hệ quả cho việc tối ưu chi 
 phí? Áp dụng

#### Đáp án

**46,5% — gần một nửa hoá đơn.** Vì vé ra đắt gấp 5 lần vé vào ($15 so với $3): 
 input $0,00345, output $0,00300, tổng $0,00645.

**Vì sao output đắt:** input được đọc một lượt và song song hoá được; output đòi 
 một lượt chạy cho mỗi token, mỗi lượt lại đọc lại toàn bộ ngữ cảnh đang dài dần.

**Thứ tự tối ưu đúng:** ① rút ngắn output ( `max_tokens` + yêu cầu súc 
 tích trong prompt) → ② hạ tầng model → ③ cắt input. Nhiều đội làm ngược, bắt đầu bằng cắt system 
 prompt — chỗ ít tác dụng nhất cho một lần gọi đơn lẻ.

**Con số minh hoạ:** kéo output từ 200 lên 800 làm hoá đơn gấp 2,4 lần; thêm 650 
 token *input* (nhiều hơn) chỉ làm tăng 30%.

*Ngoại lệ đáng nêu:* với hội thoại nhiều lượt, system prompt lại là chỗ đáng tối ưu nhất 
 — vì nó được gửi lại ở **mỗi** lượt (slide 69).

**2.** Chatbot của bạn ổn ở lượt đầu nhưng hoá đơn tăng nhanh bất thường theo độ 
 dài hội thoại. Chẩn đoán và đề xuất. Phân tích

#### Đáp án

**Chẩn đoán: model không có trí nhớ, nên toàn bộ lịch sử được gửi lại ở mỗi lượt.** Lượt thứ n phải trả tiền cho tất cả n−1 lượt trước — đây là tăng trưởng bậc hai theo số lượt, không 
 phải tuyến tính.

**Con số cụ thể** (system 300, context 800, mỗi lượt hỏi 50 đáp 200): lượt 1 tốn 
 1.350 token, lượt 20 tốn **6.100** — gấp 4,5 lần. Cả cuộc 20 lượt tốn 74.500 token so 
 với 27.000 nếu mỗi lượt độc lập.

**Đề xuất, theo thứ tự hiệu quả:**

① **Tóm tắt lịch sử** khi vượt ngưỡng — tiết kiệm ~50% và làm chi phí mỗi lượt gần 
 như phẳng, nên dự đoán được. Đây là lời khuyên của slide 36: "tóm tắt lại thay vì kéo theo mọi thứ". 
 ② **Rà lại system prompt** — nó được gửi lại mỗi lượt, nên cắt 200 token thừa ở đây 
 nhân với số lượt. 
 ③ **Xem lại context RAG** — có cần lấy 800 token tài liệu ở *mọi* lượt không, 
 hay chỉ ở lượt cần tra cứu?

**Lợi ích kép của ①:** rẻ hơn *và* chất lượng tốt hơn — "context rác = 
 attention rác". Ngoài ra nó tránh cho hội thoại dài vượt trần context và bị từ chối.

**3.** Một model đạt top 10% ở kỳ thi luật sư. Đồng nghiệp kết luận "model này 
 thông minh, dùng cho mọi việc". Phản biện. Đánh giá

#### Đáp án

**Profile năng lực không phẳng.** Chính model đó (GPT-4, 2023) đỗ Bar exam top 10% 
 nhưng ở Codeforces *dưới 5%*. Cùng một model, cùng thời điểm — điểm cao ở kỳ thi này không 
 nói gì về kỳ thi khác.

**Ba lý do benchmark chỉ nên "tin vừa thôi" (slide 72):**

① **Học vẹt đường tắt** — model tìm tín hiệu rẻ tiền tương quan với đáp án thay vì 
 hiểu (slide 45: phân loại spam thành "đếm hyperlink"). Đổi cấu trúc dữ liệu test là điểm tụt. 
 ② **Đề bão hoà** — SWE-bench Verified đã ~81%; khi mọi model gần trần thì chênh lệch 
 vài điểm là nhiễu. 
 ③ **Học tủ đề** — model có thể được luyện đúng dạng đề. *Đây là bẫy nguy hiểm nhất 
 vì gần như không phát hiện được từ bên ngoài*: bạn không biết dữ liệu huấn luyện có chứa bộ đề 
 hay không.

**Kết luận đúng:** benchmark là *tín hiệu*, không phải bằng chứng. Bài test 
 đáng tin duy nhất là **việc của chính bạn, trên dữ liệu của chính bạn** — chạy prompt 
 thật của bạn qua 2–3 model rồi so sánh.

---

<!-- chiron-source-span: {"source_span_id":"15d95af5-1bca-571f-88ce-f248eb215728","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Gọi API lần đầu","source_file":"day-1-ai-llm-foundation.html"},"checksum":"521347590d1663f8d3e9dfb746bc195fd96ccb6eaaf310451ee555c5f325c4c1"} -->

## 08 Gọi API lần đầu

Slide 73–79: bốn lớp của một prompt, giải phẫu request/response, hai núm vặn, và chatbot có trí nhớ.

### Slide 73–75 Một lần gọi API, và bốn lớp của một prompt

> Trích slide 
>  "① Prompt (system + user + context) → ② API call (gửi request 
>  tới provider) → ③ Token stream (model sinh từng mảnh) → ④ Response 
>  (nội dung + usage + lý do dừng)" 
>  " Gọi API = điều khiển một vòng next-token từ xa — không phép màu, đúng cơ chế 
>  mình vừa học. Mỗi API call luôn có 3 thứ phải kiểm soát cùng lúc: chất lượng — độ trễ — chi phí." 
>  " LỚP 1 System instruction — 'Lời dặn đầu ca': model là ai, cư xử thế nào, không 
>  được làm gì. LỚP 2 User input — Câu hỏi/yêu cầu của người dùng trong lượt này. 
>  LỚP 3 Context bổ sung — Tài liệu, lịch sử chat, dữ liệu tra sổ. 
>  LỚP 4 Output mong muốn — Dạng kết quả: gạch đầu dòng? bảng? JSON? dài bao nhiêu?" 
>  " Viết rõ cả 4 lớp = đã làm tốt một nửa 'prompt engineering' "

Bốn lớp này là khung viết prompt đơn giản nhất mà vẫn đủ dùng. Điều đáng chú ý: **ba lớp đầu ai cũng viết, lớp thứ tư thì hay bị bỏ** — và đó là lớp có tác động lớn nhất 
 tới chi phí.

| Lớp | Trả lời câu hỏi | Bỏ qua thì sao | Ảnh hưởng chi phí |
| --- | --- | --- | --- |
| 1 · System | Model là ai, cư xử thế nào | Model tự chọn giọng điệu, không nhất quán giữa các lượt | Trả tiền mỗi lượt (slide 69) — chỗ đáng tối ưu nhất trong hội thoại dài |
| 2 · User | Lần này người dùng muốn gì | — | Nhỏ |
| 3 · Context | Model cần nhìn thấy dữ liệu nào | Model dựa vào trí nhớ trong tham số ⇒ dễ bịa | Thường là phần lớn nhất của input |
| 4 · Output mong muốn | Kết quả trông như thế nào, dài bao nhiêu | Model viết dài theo mặc định của nó | Lớn nhất — output đắt gấp 3–5 lần input |

Thêm một câu *"trả lời trong tối đa 3 gạch đầu dòng"* tốn khoảng 10 token input, và có thể 
 cắt câu trả lời từ 600 token xuống 150. Ở giá $3/$15, đó là tiết kiệm **$0,00675 mỗi lần gọi** — hơn gấp đôi chi phí của toàn bộ phần input trong ví dụ ở [slide 68](#s68).

Nó cũng giải quyết luôn vấn đề *chất lượng*: câu trả lời có ràng 
 buộc định dạng thường dễ dùng hơn cho phần code phía sau, và tránh được kiểu trả lời dài dòng mà [Ngày 24](track-3-day-24.html) gọi là length bias. Đây là một trong số ít chỗ mà rẻ hơn 
 và tốt hơn đi cùng nhau.

### Slide 76 Giải phẫu request và response

> Trích slide 
>  "REQUEST: {"model": "gpt-5.6-terra", "messages": [{"role": "system", …}, {"role": "user", …}], 
>  "max_tokens": 500, "temperature": 0} — ① tên model 'số tổng đài' · ② 3 vai trò: 
>  system/user/assistant · ③ trần độ dài trả lời · ④ độ 'liều' (0 = ổn định)" 
>  "RESPONSE: {"choices": [{"message": {…}, "finish_reason": "stop"}], 
>  "usage": {"prompt_tokens": 1150, "completion_tokens": 200, "total_tokens": 1350}} 
>  — ⑤ câu trả lời ở choices[0].message.content · ⑥ stop = tự kết thúc | 
>  length = hết hạn mức | tool_calls · ⑦ hóa đơn chi tiết" 
>  " Đọc usage mỗi lần gọi — đừng để cuối tháng mới giật mình nhìn hóa đơn "

Hai trường trong response đáng để ý hơn cả nội dung câu trả lời, và cả hai đều hay bị bỏ qua ở dự 
 án mới:

finish_reason

Ba giá trị, ba tình huống hoàn toàn khác nhau:

• `stop` — model tự kết thúc. Câu trả lời **hoàn chỉnh**. 
 • `length` — **đã đụng trần `max_tokens` và bị cắt giữa chừng**. 
 Câu trả lời *không hoàn chỉnh* — JSON có thể thiếu dấu đóng ngoặc, danh sách có thể thiếu mục 
 cuối. 
 • `tool_calls` — model muốn gọi tool, chưa phải câu trả lời cuối. Đây là nền của agent 
 (Ngày 3, 4, 9).

**Lỗi phổ biến nhất của người mới:** không kiểm `finish_reason`, rồi `json.loads()` ném lỗi ở production mà không hiểu vì sao — 
 trong khi nguyên nhân chỉ là `max_tokens` đặt quá thấp. Kiểm trường này là một dòng `if`, và nó nên có ngay từ lần gọi đầu tiên.

usage

Ba con số: `prompt_tokens`, `completion_tokens`, `total_tokens`. 
 Ghi chúng vào log tốn vài dòng, và **không khôi phục được về sau**.

Đây chính xác là điều [Ngày 25](track-3-day-25.html) nhấn mạnh: *"Đừng chỉ tổng cost theo ngày. Cần cost theo feature/user/model để tìm đường call đắt và tối ưu 
 đúng nơi."* Không ghi thì cuối tháng bạn chỉ có một con số tổng và không biết cắt ở đâu. Nếu bạn 
 chỉ làm **một** việc sau khi đọc bài này, hãy làm việc này.

system

user

assistant

assistant

bạn gửi lại lịch sử

assistant

slide 78

mô-đun lịch sử

input

### Slide 77 Hai núm vặn chọn từ: temperature và top_p

> Trích slide 
>  " temperature — 'núm vặn độ liều'. T = 0: luôn chọn từ chắc nhất → ổn định, lặp 
>  lại, hợp code & phân tích. T = 1: cân bằng tự nhiên. T = 2: phân bố phẳng ra → đa dạng, 'phiêu', 
>  dễ lạc đề" 
>  " top_p — 'chỉ xem top đầu bảng' (p = 0.9). Giữ nhóm cộng dồn ≥ 90%, cắt & 
>  chuẩn hóa lại → 'sao' (đuôi dài xác suất thấp) bị loại khỏi lựa chọn. Thường chỉ vặn một trong hai." 
>  " Lưu ý quan trọng: hai núm này không làm model thông minh hơn — chỉ đổi cách chọn từ, 
>  không thêm tri thức. " 
>  "Mặc định an toàn: temperature = 0 cho việc cần ổn định — chỉ tăng khi thật sự cần đa dạng"

Câu in đậm là câu quan trọng nhất, và nó là hệ quả trực tiếp của [Hình 3](#f3): **bảng xác suất đã được tính xong rồi**. Hai núm này chỉ đổi *cách đọc* cái bảng 
 đó — chúng không thể tạo ra kiến thức model không có.

#### Tương tác Temperature & top_p — hai cách đọc cùng một bảng xác suất

Câu *"Một tách ___"* với bốn ứng viên. Kéo hai núm và xem phân bố biến dạng — 
 nhưng để ý: **thứ tự các từ không bao giờ đổi**.

Ở **T = 1** (mặc định), phân bố là: cà phê 60% · trà 25% · mưa 10% · sao 5%.

Đoán trước hai điều: ① kéo T xuống **0,1** thì "cà phê" lên bao nhiêu? ② Kéo T lên **2,0** thì "cà phê" còn bao nhiêu — nó có tụt xuống dưới "trà" không?

#### Kéo rồi mở

**① T = 0,1 → "cà phê" gần như 100%.** Nhiệt độ thấp làm phân bố nhọn hoắt: từ 
 chắc nhất nuốt gần hết xác suất. Đó là ý nghĩa của "tất định" — chạy lại nhiều lần đều ra cùng 
 một kết quả.

**② T = 2,0 → "cà phê" còn 42,7%, "trà" lên 27,6%.** Phân bố phẳng ra rõ rệt — 
 nhưng **"cà phê" vẫn đứng đầu**.

**Và đây là điều quan trọng nhất của mô-đun này:** dù bạn kéo T tới đâu, *thứ tự bốn từ không bao giờ thay đổi*. Temperature không làm model đổi ý về từ nào hợp lý 
 hơn — nó chỉ đổi mức độ model *chịu chọn* những từ kém hợp lý hơn.

Đó chính xác là điều slide muốn nói: *"hai núm này không làm model thông minh hơn — chỉ đổi 
 cách chọn từ, không thêm tri thức."* Nếu model không biết câu trả lời đúng, vặn temperature 
 không giúp gì cả — nó chỉ đổi *kiểu sai*.

**Thử tiếp với top_p:** kéo top_p xuống **0,85** ở T = 1. "cà phê" + 
 "trà" đã cộng dồn 85%, nên "mưa" và "sao" bị *cắt hẳn khỏi lựa chọn* — xác suất về 0, và 
 hai từ còn lại được chuẩn hoá lên. Đây là khác biệt cơ bản với temperature: **temperature làm mềm, top_p thì chặt đứt**.

*Vì sao "thường chỉ vặn một trong hai":* vặn cả hai cùng lúc làm hiệu ứng khó dự đoán — 
 temperature đổi hình dạng phân bố, mà top_p lại cắt dựa trên chính hình dạng đó. Chọn một núm và 
 giữ núm kia ở mặc định.

- **Control - temperature 1,00**: min `5`, max `200`, step `5`, default `100`

- **Control - top_p tắt (1,00)**: min `30`, max `100`, step `1`, default `100`

Từ chắc nhất

—

—

Số từ còn trong lựa chọn

—

—

Chế độ

—

—

Độ bất định

—

entropy — càng cao càng khó đoán

từ chắc nhất các từ còn lại đã bị top_p cắt

#### Xem dạng bảng



#### Công thức & giới hạn của mô hình

- Phân bố gốc ở T = 1 là giả định minh hoạ của tài liệu này (60/25/10/5), không 
 có trên slide. Slide chỉ vẽ bốn cột không ghi số.
- Công thức chuẩn: p_i ∝ exp(logit_i / T). Vì ở đây lấy logit = ln(p) 
 nên tương đương p_i ∝ p_i^(1/T) rồi chuẩn hoá — đúng cách temperature hoạt động thật.
- top_p: sắp xếp giảm dần, cộng dồn tới khi đạt ngưỡng p, cắt phần còn lại, chuẩn hoá lại.
- Chỉ mô phỏng MỘT bước chọn từ. Trong thực tế việc chọn xảy ra ở mọi token, và 
 các lựa chọn ảnh hưởng lẫn nhau — nên tác động lên cả câu trả lời lớn hơn nhiều so với những gì 
 một bước cho thấy.
- Từ vựng thật có 50.000–200.000 token, không phải 4. Đuôi phân bố dài hơn rất nhiều, nên top_p 
 cắt đi hàng vạn ứng viên chứ không phải hai.
- Ở T = 0 thật, phần lớn API chuyển sang chọn tất định (greedy) chứ không lấy mẫu. Mô-đun dừng ở 
 T = 0,05 để công thức còn định nghĩa được.

### Slide 78–79 Chatbot = vòng lặp + trí nhớ; streaming = nhả chữ từng mảnh

> Trích slide 
>  "'Trí nhớ' của chatbot đến từ đâu? ① nối vào history → ② gửi TOÀN BỘ history → MODEL 
>  (stateless) → ③ trả lời → nối tiếp vào history" 
>  " Model không nhớ gì giữa hai lần gọi — 'trí nhớ' là do MÌNH gửi lại history mỗi lần " 
>  "Streaming — next-token nhìn tận mắt. Đây chính là bản chất next-token: model đoán → nhả một 
>  mảnh → đoán tiếp. Giao diện 'đang gõ' chỉ là lộ trình của vòng lặp. " 
>  "OpenAI: client.chat.completions.create(...) →.choices[0].message.content 
>  · Anthropic: client.messages.create(...) →.content[0].text. 
>  Đổi base_url là code gọi API chuyển sang model tự host gần như nguyên vẹn. "

Chữ **`stateless`** trong sơ đồ là chữ quan trọng nhất của slide, và nó có 
 hai hệ quả trái ngược nhau — một phiền, một tiện:

|  | Hệ quả | Nghĩa là gì |
| --- | --- | --- |
| Phiền | Bạn phải tự giữ và gửi lại lịch sử | Càng chat càng đắt ( mô-đun lịch sử ) và có thể vượt trần context |
| Tiện | Bạn kiểm soát hoàn toàn model nhìn thấy gì | Sửa được lịch sử, tóm tắt được, xoá được một lượt, chèn được ngữ cảnh mới — model không có "ý riêng" nào giữ lại |

Vì model không giữ trạng thái, **lịch sử là dữ liệu của bạn** và bạn muốn làm gì với 
 nó cũng được:

• *Tóm tắt phần cũ* để tiết kiệm token — [slide 36](#s36), và mô-đun ở trên. 
 • *Chèn kết quả tra cứu* vào giữa hội thoại — đây chính là RAG (Ngày 8). 
 • *Thay một tin nhắn độc hại bằng "[đã bị gỡ]"* — đây là phòng thủ Session Poisoning ở [Ngày 24](track-3-day-24.html), và nó **chỉ khả thi vì model stateless**. 
 • *Lưu và khôi phục hội thoại* — nền của checkpointing trong LangGraph (Ngày 23).

Nói cách khác: cái nghe như một hạn chế ( *"model chẳng nhớ gì"* ) 
 thật ra là thứ cho bạn toàn quyền. Nếu model tự giữ trạng thái bên trong, không kỹ thuật nào ở trên 
 làm được.

base_url

tương đương về mặt logic

rẻ tới mức không có lý do gì không làm

slide 57

usage

---

<!-- chiron-source-span: {"source_span_id":"df4a6556-447f-5d4e-b5c6-a275854a8dc4","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Tổng kết","source_file":"day-1-ai-llm-foundation.html"},"checksum":"940918778bf5f6cf1e0ae4d2c482804abdf91e6e50ca530ca3d3f494eb3c9681"} -->

## 09 Tổng kết

Slide 80–83: năm ý mang về, câu trả lời cho câu hỏi đầu ngày, và tài liệu đọc thêm.

### Slide 80–82 Năm ý mang về, và câu trả lời cho câu hỏi mở đầu

> Trích slide 
>  "1. LLM = cỗ máy Transformer đoán token tiếp theo từ context — mọi thứ khác là hệ quả. 
>  2. Từ cỗ máy đoán chữ thành trợ lý: pre-training → SFT → căn chỉnh → luyện đề tự chấm & được 
>  nghĩ kỹ. 3. Model có giới hạn bẩm sinh: bong bóng thời gian, nói chắc như đúng rồi, bàn làm việc có 
>  hạn — nên đừng tin benchmark, hãy tự test. 4. Chọn model theo tầng theo việc, kiểm soát 3 núm: 
>  chất lượng — độ trễ — chi phí. 5. Gọi API là điều khiển một vòng next-token từ xa." 
>  " 'Bên trong AI đang làm gì?' — một vòng lặp đoán token, được nuôi bằng dữ liệu, đang chờ bạn 
>  điều khiển. " 
>  "Một lời nhắc nhỏ mang theo: dữ liệu là mạch sống của model nhưng cũng là phần kém minh bạch nhất. 
>  Model nền là điểm đòn bẩy lớn — và cũng có thể là điểm lỗi lan xuống mọi ứng dụng. 
>  Evaluation, guardrails và system design không bao giờ là phần phụ. "

Năm ý này ánh xạ đúng vào năm chương chính, và đọc chúng theo thứ tự sẽ thấy một mạch: *cơ chế → cách tạo ra → giới hạn → cách chọn → cách dùng*.

*"Model nền là điểm đòn bẩy lớn — và cũng có thể là điểm lỗi lan xuống mọi ứng dụng."*

Đây là phát biểu ngắn gọn nhất về vì sao khoá học không dừng ở ngày 1. Cùng một model nền phục vụ 
 mọi tính năng của bạn, nên:

• Một cải tiến ở tầng đó lan xuống *mọi* tính năng — đòn bẩy. 
 • Một lỗi ở tầng đó cũng lan xuống *mọi* tính năng — rủi ro tập trung. 
 • Và nếu nhà cung cấp đó gặp sự cố, mọi thứ dừng cùng lúc — đúng điểm hỏng đơn mà [Ngày 25](track-3-day-25.html) mổ xẻ.

Câu *"Evaluation, guardrails và system design không bao giờ là phần 
 phụ"* chính là mục lục của Track 3, viết ở ngày đầu tiên.

"đừng tin benchmark, hãy tự test"

slide 71

lấy một prompt trong công việc của bạn, 
 chạy trên 2–3 model, so sánh

Ngày 24

### Slide 83 Tài liệu đọc thêm — thứ tự nên theo

> Trích slide 
>  "🎬 Nên xem & chơi trước: 3Blue1Brown — Transformers, the tech behind LLMs · 
>  3Blue1Brown — Attention in transformers, step-by-step · Transformer Explainer 
>  — chạy GPT-2 ngay trong trình duyệt · Karpathy — nanoGPT & State of GPT" 
>  "📄 Paper nền tảng: Attention Is All You Need (2017) · InstructGPT (2022) · 
>  Emergent World Representations — Othello-GPT (ICLR 2023) · 
>  On the Dangers of Stochastic Parrots (FAccT 2021) — phía phản biện" 
>  "📊 Bảng model & giá 7/2026: Fable 5 $10/$50 (tạm khóa export-control) · Opus 4.8 $5/$25 · 
>  Sonnet 4.6 $3/$15 · Haiku 4.5 $0.8/$4 · Gemini 3.1 Pro $2/$12 · Kimi K3 $3/$15 (open-weight)"

Danh mục này được sắp theo thứ tự đúng, và đáng theo đúng thứ tự đó:

| Thứ tự | Nguồn | Cho bạn cái gì | Tốn bao lâu |
| --- | --- | --- | --- |
| 1 | Transformer Explainer (chơi trong trình duyệt) | Trực giác về token, temperature, attention — bằng tay | 15 phút |
| 2 | 3Blue1Brown, hai video | Hình dung được cái đang xảy ra bên trong | ~1 giờ |
| 3 | Karpathy — nanoGPT | Code chạy được, ít dòng, đọc hết được | Vài buổi |
| 4 | Bốn paper nền tảng | Nguồn gốc và bằng chứng gốc | Đọc rải rác |

[Slide 48](#s47) đã biến nó thành một bài thực hành ba bước: ① gõ một câu, xem nó bị 
 cắt thành token thế nào ② vặn temperature, nhìn bảng xác suất đổi ra sao ③ mở attention map, bấm vào 
 một token, xem nó đang nhìn đâu.

Ba bước đó lần lượt cho bạn *chạm tay* vào ba khái niệm trừu tượng 
 nhất của bài: **token**, **phân bố xác suất**, và **attention**. 
 Cộng với hai mô-đun trong tài liệu này ( [temperature](#m-temp) và [hoá đơn](#m-cost) ), bạn có gần như toàn bộ chương 3 và chương 7 ở dạng nghịch được.

#### Ô kiểm tra — Chương 8 & 9

Trả lời thành tiếng trước khi mở đáp án.

**1.** Code của bạn gọi API rồi `json.loads()` kết quả, thỉnh thoảng 
 ném lỗi ở production mà không tái hiện được ở local. Nguyên nhân khả dĩ nhất và cách 
 sửa? Áp dụng

#### Đáp án

**Nhiều khả năng câu trả lời bị cắt giữa chừng vì đụng trần `max_tokens` — 
 và code không kiểm `finish_reason`.**

Khi `finish_reason == "length"`, JSON thiếu dấu đóng ngoặc nên parse hỏng. Ở local 
 bạn thử với câu hỏi ngắn nên không bao giờ chạm trần; production có câu hỏi dài hơn.

**Sửa:** ① kiểm `finish_reason` trước khi parse — một dòng `if`; ② nâng `max_tokens`, hoặc tốt hơn là ràng buộc độ dài ngay trong prompt 
 (lớp 4 của slide 75); ③ ghi `finish_reason` vào log để thấy tần suất.

**Ba giá trị cần phân biệt:** `stop` = hoàn chỉnh · `length` = bị cắt · `tool_calls` = model muốn gọi tool, chưa phải câu trả lời 
 cuối (nền của agent).

**2.** Model trả lời sai một câu hỏi kiến thức. Đồng nghiệp đề xuất "tăng 
 temperature lên cho nó sáng tạo hơn". Phản biện. Hiểu

#### Đáp án

**Temperature không thêm tri thức — nó chỉ đổi cách chọn từ trong một bảng xác suất 
 đã được tính xong.**

Bằng chứng trực quan từ [mô-đun temperature](#m-temp): kéo T từ 0,1 lên 2,0 thì phân 
 bố phẳng ra rõ rệt, nhưng *thứ tự các từ không bao giờ đổi* — "cà phê" vẫn đứng đầu ở mọi 
 mức T. Model không đổi ý về từ nào hợp lý hơn; nó chỉ đổi mức độ *chịu chọn* những từ kém 
 hợp lý hơn.

**Nên nếu model không biết câu trả lời đúng, tăng T chỉ đổi *kiểu sai*** — 
 và thường làm tệ hơn, vì nó tăng khả năng chọn những token có xác suất thấp.

**Cách sửa đúng, theo thứ tự:** ① đưa thông tin vào context (RAG, tool) — vì đây 
 là vấn đề *bong bóng thời gian* hoặc *thiếu dữ liệu*, không phải vấn đề chọn từ; 
 ② hạ T về 0 để kết quả ổn định và tái hiện được; ③ nếu vẫn sai, thử tầng model cao hơn.

*Khi nào tăng T mới đúng:* khi bạn cần **đa dạng** — sinh nhiều phương án 
 tiêu đề, brainstorm ý tưởng. Không phải khi bạn cần đúng.

**3.** "Model stateless" nghe như một hạn chế. Nêu ba kỹ thuật ở các bài sau chỉ 
 khả thi *nhờ* nó. Đánh giá

#### Đáp án

**Vì model không giữ trạng thái, lịch sử hội thoại là dữ liệu của BẠN — và bạn toàn quyền 
 sửa nó.**

① **Tóm tắt lịch sử** để tiết kiệm token và giữ "bàn làm việc" sạch (slide 36). 
 Nếu model tự giữ trạng thái bên trong, bạn không nén được. 
 ② **Chèn kết quả tra cứu vào giữa hội thoại** — đây chính là RAG (Ngày 8). Bạn thêm 
 được ngữ cảnh mà model chưa từng thấy, ngay giữa cuộc trò chuyện. 
 ③ **Thay một tin nhắn độc hại bằng "[đã bị gỡ]"** — phòng thủ Session Poisoning 
 (Ngày 24). Chỉ khả thi vì bạn sở hữu và sửa được lịch sử trước khi gửi.

*Cũng đúng nếu nêu:* checkpointing và khôi phục hội thoại trong LangGraph (Ngày 23), 
 hoặc chạy lại một lượt với model khác (fallback chain, Ngày 25) — cả hai đều dựa vào việc trạng 
 thái nằm ngoài model.

**Cái giá của sự tự do đó:** bạn phải trả tiền gửi lại lịch sử ở mỗi lượt, và 
 phải tự lo không vượt trần context.

---

<!-- chiron-source-span: {"source_span_id":"8762f1f5-76c1-5b12-b3e1-7dc929942c27","locator":{"kind":"html_section","section_id":"ladder","order":12,"heading":"▤ Luyện kỹ năng cốt lõi: quy hiện tượng về cơ chế","source_file":"day-1-ai-llm-foundation.html"},"checksum":"bf9ddac2c382a6976ab979a7525137472411d3253e1d726a65f0ca4424e13e91"} -->

## ▤ Luyện kỹ năng cốt lõi: quy hiện tượng về cơ chế

Ba bài giảm dần giàn giáo. Làm đúng thứ tự.

① Hiện tượng này là hệ quả của "chỉ đoán token tiếp theo" như thế nào?

context

hành vi

③ Sửa ở đâu rẻ nhất?

④ Tôi đo bằng gì để biết đã sửa được?

rất

#### Chatbot nội bộ trả lời sai về chính sách nghỉ phép của công ty — nói rất tự tin

Đọc cách *lập luận*, không chỉ đáp án.

1. Hệ quả của cơ chế: đây là hai giới hạn ở slide 44 cộng lại — 
 bong bóng thời gian (model chưa bao giờ đọc chính sách nội bộ của công ty bạn) và 
 nói chắc như đúng rồi (model tối ưu cho câu nghe hợp lý, không có cơ chế nào phân biệt 
 "biết" với "đoán"). Cách nhận ra: nếu thông tin đó không thể có trong dữ liệu công khai, 
 model chắc chắn đang bịa — dù nó nói tự tin đến đâu.
2. Vấn đề context, không phải hành vi. Model không sai cách nói — nó thiếu dữ kiện. 
 Đây là phân biệt quan trọng nhất, vì nó loại thẳng fine-tuning ra khỏi danh sách: 
 slide 37 nói tham số là thứ cố định, và Ngày 21 nói 
 "fine-tune không sửa knowledge gap".
3. Sửa ở đâu rẻ nhất — theo thứ tự: 
 ① Prompt: thêm chỉ dẫn "chỉ trả lời dựa trên tài liệu được cung cấp; nếu không có thì nói 
 không biết". Rẻ nhất, làm trong 2 phút, và một mình nó đã cắt được phần lớn ca bịa. 
 ② Context: đưa văn bản chính sách vào prompt. Nếu chính sách ngắn (vài trang) thì nhét 
 thẳng; nếu dài thì cần lấy đúng đoạn — tức RAG (Ngày 7–8). 
 ③ Không cần đụng tới tầng model hay fine-tune.
4. Đo bằng gì: ① dựng một bộ 20 câu hỏi về chính sách có đáp án đúng — 
 đây là golden set đầu tiên của bạn; ② đo tỷ lệ trả lời đúng trước và sau khi thêm context; 
 ③ đo riêng tỷ lệ nói "không biết" đúng lúc — vì một model trả lời đúng 100% câu có tài liệu 
 nhưng vẫn bịa khi thiếu tài liệu thì chưa xong việc.

Câu chốt kiểu vấn đáp "Model chưa bao giờ đọc chính sách nội bộ nên đây là knowledge gap, không phải lỗi hành vi — fine-tune 
 không giải được. Em sửa theo thứ tự rẻ dần: trước hết thêm chỉ dẫn 'chỉ dựa trên tài liệu, không có 
 thì nói không biết', rồi đưa văn bản chính sách vào context. Em đo bằng 20 câu hỏi có đáp án, và đo 
 thêm tỷ lệ nói 'không biết' đúng lúc — vì đó mới là thứ chứng minh model đã hết bịa."

#### Hoá đơn API tháng này gấp ba tháng trước, trong khi số người dùng chỉ tăng 20%

Hai bước đầu cho sẵn. Hai bước sau tự viết rồi mới mở.

1. Số người dùng không giải thích được mức tăng. Tăng 20% người dùng mà hoá đơn 
 gấp 3 nghĩa là chi phí mỗi người dùng đã tăng khoảng 2,5 lần. Vậy thứ đổi không phải lưu 
 lượng mà là số token mỗi lượt.
2. Ba nguồn khả dĩ, đều quy về "một núm vặn" ở slide 70: 
 ① câu trả lời dài ra (output — đắt gấp 3–5 lần), ② context nhét vào nhiều hơn (input), hoặc 
 ③ hội thoại dài hơn nên lịch sử tích luỹ nhiều hơn.
3. ③ Bạn cần dữ liệu gì để phân biệt ba nguồn trên, và nếu chưa có thì 
 sao? (gợi ý: có một trường trong mọi response mà slide 76 bảo phải đọc)
4. ④ Giả sử xác định được nguyên nhân là hội thoại dài hơn. Sửa thế nào, và 
 lợi ích có phải chỉ là tiền không?

#### Đáp án hai bước còn lại

**③ Cần `usage` tách theo tính năng, và cần nó được ghi từ trước.**

Ba con số `prompt_tokens`, `completion_tokens`, `total_tokens` có sẵn trong *mọi* response ( [slide 76](#s76) ). Nếu đã ghi vào log kèm nhãn tính 
 năng và ID hội thoại, bạn trả lời được ngay: input tăng hay output tăng, tính năng nào tăng.

**Nếu chưa ghi:** bạn chỉ có một con số tổng từ hoá đơn nhà cung cấp và *không khôi phục lại được*. Việc phải làm ngay hôm nay là bật ghi log — sau đó chờ vài ngày 
 mới có dữ liệu. Đây đúng lời cảnh báo của [Ngày 25](track-3-day-25.html): *"Đừng chỉ tổng cost theo ngày. Cần cost theo feature/user/model để tìm đường call đắt."*

*Cách tạm thời trong lúc chờ:* so độ dài trung bình của prompt và câu trả lời trong log 
 ứng dụng (nếu có), hoặc chạy lại một mẫu hội thoại thật rồi đo bằng tokenizer.

**④ Sửa: tóm tắt lịch sử — và lợi ích là kép.**

*Cơ chế:* model stateless nên toàn bộ lịch sử được gửi lại mỗi lượt; lượt thứ n phải trả 
 tiền cho tất cả n−1 lượt trước. Đây là tăng trưởng bậc hai, không phải tuyến tính — nên hội thoại 
 dài gấp đôi thì tốn *hơn* gấp đôi.

*Con số:* với system 300 + context 800, mỗi lượt hỏi 50 đáp 200, hội thoại 20 lượt tốn **74.500 token**. Bật tóm tắt còn **36.250** — tiết kiệm 51% 
 ( [mô-đun lịch sử](#m-hist) ).

**Lợi ích không chỉ là tiền — có ba:** 
 ① *Rẻ hơn* 51%. 
 ② *Chất lượng tốt hơn* — [slide 36](#s36): "context rác = attention rác". Lịch sử 
 cũ không liên quan làm loãng sự chú ý. 
 ③ *Không vượt trần context* — hội thoại đủ dài sẽ bị API từ chối. Tóm tắt làm chi phí mỗi lượt 
 gần như phẳng, nên hội thoại dài bao nhiêu cũng chạy được và *dự đoán được chi phí*.

**Việc nên làm song song:** rà lại system prompt. Nó được gửi lại mỗi lượt, nên cắt 
 200 token thừa ở đó nhân với số lượt và số người dùng.

#### Ước lượng chi phí và chọn tầng model cho SmartCheck AI

Không có gợi ý. Viết ra bốn câu trả lời rồi so với [mục áp dụng](#apply).

1. Bối cảnh: kiosk check-in khách sạn, khoảng 300 lượt check-in mỗi 
 ngày, mỗi lượt trung bình 4–6 lượt hội thoại. Agent LangGraph có node phân loại (đòi 
 structured output), node trả lời, node gọi tool. System prompt hiện khoảng 600 token; mỗi lượt trả 
 lời khoảng 150 token.
2. Câu hỏi ①: ước lượng số token mỗi tháng và chi phí ở ba tầng model. Dùng 
 mô-đun hoá đơn và mô-đun lịch sử.
3. Câu hỏi ②: node phân loại đòi JSON đúng schema. Điều đó ràng buộc gì lên việc 
 chọn tầng model, và bạn kiểm chứng ràng buộc đó bằng cách nào trước khi quyết?
4. Câu hỏi ③: ba việc rẻ nhất bạn làm được tuần này để giảm chi phí mà 
 không đổi model — xếp theo tác động.

không

khách đang đứng chờ

slide 70

cũng

---

<!-- chiron-source-span: {"source_span_id":"bf2c0ac8-f6c1-5b39-8cb7-042c593d94f9","locator":{"kind":"html_section","section_id":"misc","order":13,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"day-1-ai-llm-foundation.html"},"checksum":"3648f5a4b0fa59ef9e2c98f77796f570cf657fd4ca0bfc71350cc181af278d51"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Đây là bài nền, nên hiểu lầm ở đây kéo theo cả khoá. Mỗi thẻ: niềm tin phổ biến, 
 lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng.

*Vì sao nghe hợp lý:* mọi thứ được gọi là "AI" trên báo chí hai năm qua đều là LLM. Và LLM 
 thật sự là tầng nền của gần hết trải nghiệm AI bạn dùng hằng ngày.

LLM nằm ở **trong cùng** của năm tầng lồng nhau. Lọc spam Gmail, gợi ý phim Netflix, 
 nhận diện khuôn mặt — đều là AI, đều *không* phải LLM.

**Hệ quả thực hành:** câu hỏi đầu tiên cho một bài toán không phải "dùng LLM thế 
 nào" mà *"bài toán này thuộc tầng nào"*. Phân loại, dự đoán, chấm điểm — thường là machine 
 learning cổ điển: nhanh hơn, rẻ hơn, chính xác hơn, và giải thích được.

[Hình 1](#f1) — năm tầng lồng nhau · [Slide 7](#s7) — ba nhóm AI theo hình 
 dạng vào/ra.

*Vì sao nghe hợp lý:* trải nghiệm chat rất giống nói chuyện với người có trí nhớ. Bạn nhắc 
 "cái đó" và nó hiểu bạn đang nói gì.

Model **stateless** — không giữ gì giữa hai lần gọi. "Trí nhớ" là do *bạn* gửi lại toàn bộ lịch sử ở mỗi lượt.

Hai hệ quả trái ngược: *phiền* — càng chat càng đắt, tăng theo bậc hai, và có thể vượt trần 
 context. *Tiện* — lịch sử là dữ liệu của bạn, nên tóm tắt được, chèn được, sửa được. Không có 
 điều thứ hai thì không có RAG, không có phòng thủ Session Poisoning, không có checkpointing.

[Slide 78](#s78) — chữ `stateless` trong sơ đồ · [mô-đun lịch sử](#m-hist) — lượt 20 tốn gấp 4,5 lần lượt 1.

*Vì sao nghe hợp lý:* đó đúng là luật chơi 2020–2024 (scaling law), và số tham số là con 
 số duy nhất mà truyền thông hay nêu.

Tham số chỉ là **một trong ba trục** ( [slide 66](#s66) ). Chinchilla 70B 
 thắng cả ba model to hơn ở cùng ngân sách tính toán — vì cân đối tham số với dữ liệu. 
 InstructGPT 175B được ưa thích 85% so với 15% của GPT-3 175B — *cùng số tham số*, chỉ khác có 
 RLHF.

Thêm nữa: với **MoE**, số tham số không còn là chỉ báo tốt về giá hay tốc độ — mỗi 
 token chỉ kích hoạt vài "chuyên gia". So model bằng *giá mỗi triệu token* và *độ trễ đo 
 được*, không phải bằng số tham số.

[Slide 66](#s66) — ba trục · [Slide 37](#s37) — MoE, 2.800 tỷ mà chi phí 
 mỗi ca gần như không đổi.

*Vì sao nghe hợp lý:* nếu bàn làm việc đủ rộng để bày cả kho tài liệu, sao phải mất công 
 chọn đoạn nào? Nghe như một bước thừa.

Ba lý do, và lý do thứ ba là lý do phản trực giác nhất:

① **Tiền** — context là input token, trả tiền *mỗi lần gọi*. 
 ② **Tốc độ** — attention tốn theo bình phương độ dài. 
 ③ **Chất lượng có thể GIẢM** — thêm ngữ cảnh không liên quan làm loãng chú ý, cộng hiện 
 tượng "lost in the middle". Slide 36 gọi thẳng: *"context rác = attention rác"*.

Câu chốt: *"Agent mạnh không phải vì context khổng lồ — mà vì nó có tools để lấy đúng thứ vào 
 bàn làm việc đúng lúc."*

[Slide 31](#s31) — "bàn rộng không có nghĩa là dùng tốt" · [Slide 36](#s36) — câu kết.

*Vì sao nghe hợp lý:* chữ "temperature" và "sáng tạo" gợi ý rằng vặn lên thì model nghĩ 
 thoáng hơn. Và ở việc brainstorm, tăng T *thật sự* hữu ích.

Temperature **không thêm tri thức** — bảng xác suất đã được tính xong, nó chỉ đổi 
 cách đọc bảng đó. Bằng chứng: kéo T từ 0,1 lên 2,0 trong mô-đun, phân bố phẳng ra rõ rệt nhưng *thứ tự các từ không bao giờ đổi*.

Nếu model không biết đáp án đúng, tăng T chỉ đổi **kiểu sai** — và thường tệ hơn, 
 vì tăng khả năng chọn token xác suất thấp. Cách sửa đúng cho câu trả lời sai kiến thức là *đưa thông tin vào context*, và hạ T về 0 để kết quả tái hiện được.

[Mô-đun temperature](#m-temp) — kéo hết dải, thứ tự không đổi · [Slide 77](#s77) — "không làm model thông minh hơn".

*Vì sao nghe hợp lý:* benchmark là thứ khách quan duy nhất có sẵn, và ai cũng dùng nó để 
 so sánh. Không dùng nó thì dùng gì?

**Profile năng lực không phẳng.** GPT-4 (2023) đỗ Bar exam top 10% nhưng Codeforces 
 dưới 5% — cùng model, cùng thời điểm.

Ba cái bẫy: ① *học vẹt đường tắt* (model học "đếm hyperlink" thay vì hiểu spam); 
 ② *đề bão hoà* (SWE-bench Verified ~81%, chênh vài điểm là nhiễu); 
 ③ *học tủ đề* — **bẫy này gần như không phát hiện được từ bên ngoài**, vì bạn 
 không biết dữ liệu huấn luyện có chứa bộ đề hay không.

Kết luận đứng vững duy nhất: *bài test đáng tin là việc của chính bạn, trên dữ liệu của chính 
 bạn.*

[Slide 72](#s71) — ba cái bẫy · [Slide 45](#s44) — ba ví dụ học vẹt do 
 chính LLM tự phát hiện.

---

<!-- chiron-source-span: {"source_span_id":"533d8e48-1974-5401-ace3-0b3e85288cd3","locator":{"kind":"html_section","section_id":"apply","order":14,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"day-1-ai-llm-foundation.html"},"checksum":"86236c7cf68bb72ead156ebd0b1a008104f600ee9ce3e02531bac610256de6d0"} -->

## ◆ Áp dụng vào SmartCheck AI

Bài nền, nên phần áp dụng ở đây là *ước lượng chi phí* và *ba quyết định 
 kiến trúc* nên chốt sớm.

### Bước 1 — Ước lượng token và chi phí

Giả định làm việc, dựa trên mô tả dự án (con số của *bạn*, không phải của slide):

| Đại lượng | Giá trị giả định | Ghi chú |
| --- | --- | --- |
| Lượt check-in mỗi ngày | 300 | Từ mô tả dự án |
| Lượt hội thoại mỗi lần check-in | 5 | Trung bình — cần đo thật |
| Tổng lượt gọi model mỗi ngày | ~1.500 | 300 × 5 |
| System prompt | 600 token | Gửi lại mỗi lượt |
| Câu trả lời trung bình | 150 token | Kiosk nên trả lời ngắn |

Đặt vào [mô-đun hoá đơn](#m-cost) với input ~1.000 và output 150 ở 1.500 lượt/ngày:

| Tầng | Giá | Mỗi tháng (ước lượng) | Nhận xét |
| --- | --- | --- | --- |
| Frontier | $5 / $25 | ~$394 | Không có lý do — kiosk không làm việc khó |
| Chuẩn | $3 / $15 | ~$236 | Mặc định hợp lý để bắt đầu |
| Rẻ mà mạnh | $0,8 / $4 | ~$63 | Rẻ hơn 3,75 lần tầng chuẩn |

chưa ai đo

slide 30

usage

context.md

"chỉ cập nhật khi benchmark thực tế đã chạy"

### Bước 2 — Ba quyết định kiến trúc nên chốt sớm

Đừng rải `client.chat.completions.create(...)` khắp các node. Một hàm `call_model(messages, **kw)` duy nhất cho bạn **bốn thứ gần như miễn phí**:

• Đổi model khi giá rơi ( [slide 57](#s57): ~10 lần mỗi năm) 
 • Một chỗ duy nhất để ghi `usage` và `finish_reason` vào log 
 • Chỗ cắm sẵn cho fallback chain ( [Ngày 25](track-3-day-25.html) ) 
 • Chỗ cắm sẵn cho bôi đen PII trước khi gửi ( [Ngày 24](track-3-day-24.html), PDPL)

Cú pháp OpenAI và Anthropic tương đương về logic ( [slide 79](#s78) ), 
 nên lớp này thật sự mỏng. Đây là quyết định có tỷ lệ lợi ích trên công sức cao nhất trong cả danh sách.

[Slide 65](#s65): *"việc đơn giản mà gọi frontier → phí tiền"*. Các node của 
 SmartCheck AI không cùng độ khó:

| Node | Độ khó | Tầng đề xuất | Vì sao |
| --- | --- | --- | --- |
| Phân loại ý định | Thấp | Rẻ mà mạnh | Chọn một trong vài nhãn — việc điển hình của tầng 2/3. Chạy ở mọi lượt nên tiết kiệm ở đây nhân lên nhiều nhất |
| Trả lời khách | Trung bình | Rẻ mà mạnh → thử trước | Câu hỏi khách sạn phần lớn đơn giản. Nâng tầng chỉ khi đo được là chưa đủ |
| Xử lý ngoại lệ / khiếu nại | Cao | Chuẩn | Ít gặp nên tổng chi phí nhỏ, nhưng sai thì tốn kém |

**Nhưng có một ràng buộc phải kiểm trước:** node phân loại 
 đòi *structured output*. Không phải model nào ở tầng rẻ cũng đảm bảo JSON đúng schema — 
 đây đúng là bẫy "tương thích tính năng" mà [Ngày 25](track-3-day-25.html) cảnh báo. *Kiểm bằng cách nào:* chạy 50 câu hỏi thật qua model rẻ, đếm tỷ lệ parse được. Dưới 100% thì 
 hoặc giữ tầng chuẩn cho node đó, hoặc thêm bước sửa lỗi định dạng.

[Slide 47](#s47) xếp bốn cách chạm vào LLM theo mức kiểm soát. Kiosk xử lý họ tên, 
 số CCCD, số điện thoại — và điều đó biến lựa chọn giữa *API* và *self-host* thành một 
 câu hỏi có tầng pháp lý, không chỉ kỹ thuật.

**Cách dung hoà rẻ nhất:** ở lại với API (linh hoạt, không phải nuôi GPU) nhưng *bôi đen dữ liệu cá nhân trước khi gửi*. Bạn làm được điều này **chính vì** đang 
 ở hàng API chứ không phải hàng chat app — bạn kiểm soát được gửi gì.

Và nếu đã có lớp mỏng ở quyết định ①, chỗ cắm cho bước bôi đen đã sẵn 
 sàng. Ba quyết định này bổ trợ nhau — đó là lý do nên chốt cùng lúc, ngay bây giờ, khi codebase còn 
 nhỏ.

### Bước 3 — Ba việc rẻ nhất làm được tuần này

| # | Việc | Công sức | Đổi lại |
| --- | --- | --- | --- |
| 1 | Ghi usage + finish_reason vào log, kèm nhãn node | ~1 giờ | Không có nó thì mọi câu hỏi về chi phí đều không trả lời được. Không khôi phục được về sau |
| 2 | Thêm ràng buộc độ dài vào prompt trả lời khách ("tối đa 2–3 câu") | ~15 phút | Output đắt gấp 5 lần input. Với kiosk, câu ngắn còn tốt hơn về UX — khách đứng đọc màn hình |
| 3 | Rà system prompt 600 token, cắt phần thừa | ~30 phút | Gửi lại ở mỗi lượt. Cắt 200 token × 1.500 lượt/ngày × 30 = 9 triệu token/tháng |

input

output

Và có một lợi ích thứ hai chỉ việc 2 mới có:

nhanh hơn

slide 70

---

<!-- chiron-source-span: {"source_span_id":"48a2fa1c-6489-5c1c-a666-ecee2453cb06","locator":{"kind":"html_section","section_id":"numbers","order":15,"heading":"! Con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"day-1-ai-llm-foundation.html"},"checksum":"034661082fd63cd6ee67d4a0fec11865c09d3eb132f5769b41fa5175521c149e"} -->

## ! Con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này có hai loại con số rất khác nhau: *phép tính kiểm được* (đúng, dùng 
 thoải mái) và *số liệu thị trường* (mau cũ, phải tra lại).

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| Hoá đơn 1.150 in + 200 out @ $3/$15 = $0,0065 | 68 | Đúng chính xác — kiểm lại ra $0,00645 | Dùng làm mẫu tính. Công thức là thứ bền, giá thì không |
| 1.350 tok × 1.000 lượt × 30 ngày ≈ 40 triệu token/tháng | 69 | Đúng — ra 40,5 triệu | Dùng được |
| "Haiku $36 vs Sonnet $135 — gấp 4 lần" | 70 | Tỷ lệ đúng, số tuyệt đối không khớp với chính ví dụ ở slide 69 | Xem ô cảnh báo bên dưới |
| Output đắt gấp 3–5 lần input | 68 | Đúng với bảng giá hiện tại (tỷ lệ 5× ở Sonnet, 5× ở Haiku) | Dùng làm quy tắc ngón tay cái. Tra tỷ lệ thật của model bạn dùng |
| Giá rơi ~10 lần mỗi năm | 57 | Quan sát 2023–2026, không phải quy luật | Đúng ở bậc độ lớn cho giai đoạn đó. Đừng lập kế hoạch tài chính dựa vào việc nó tiếp tục |
| 128K token ≈ 300 trang · 1M ≈ 45 cuốn sách | 31 | Ước lượng thô, cho tiếng Anh | Tiếng Việt được ít trang hơn. Dùng để hình dung bậc độ lớn, không để lập kế hoạch |
| "Xin chào" ≈ 3–4 token | 30 | Phụ thuộc tokenizer từng model | Chạy tokenizer thật của model bạn dùng. Slide cũng tự ghi chú điều này |
| SWE-bench 33% → 81%; Verified 88,6% vs Pro 69,2% | 60, 66 | Vendor-reported; và cặp 88,6/69,2 là hai bộ đề khác nhau, không phải hai harness | Xem ô cảnh báo thứ hai bên dưới |
| InstructGPT 85% vs GPT-3 15% người ưa thích | 66 | Có nguồn (Ouyang 2022) | Trích được. Nhớ đây là tỷ lệ người ưa thích, không phải điểm chính xác |
| Bảng model & giá 7/2026 (Fable 5, Opus 4.8, Kimi K3…) | 83 | Ảnh chụp một thời điểm | Sẽ sai trong vài tháng. Slide 62 tự nhận: "bản đồ này sẽ cũ". Tra giá hiện tại trước khi dùng |
| Othello-GPT: sai luật chỉ 0,01% | 42 | Có nguồn (Li et al., ICLR 2023) | Trích được. Nhớ giới hạn: Othello luật đơn giản, trạng thái hữu hạn — không suy rộng ra thế giới thật |
| Mọi con số trong mô-đun lịch sử (74.500 · 36.250 · 51%) | — | Tính toán của tài liệu này | Đúng theo mô hình đã nêu. Ngưỡng tóm tắt 1.000 và kích thước bản tóm tắt 200 là giả định minh hoạ, không có trên slide |
| Phân bố 60/25/10/5 trong mô-đun temperature | — | Giả định minh hoạ | Slide chỉ vẽ bốn cột không ghi số. Công thức biến đổi thì đúng chuẩn |
| Ước lượng chi phí SmartCheck AI ở mục áp dụng | — | Ước lượng dựa trên giả định chưa đo | Thay bằng usage thật sau 20 lượt check-in |

Slide 69 lập ví dụ: 1.150 input + 200 output, 1.000 lượt/ngày, 30 ngày. Tính theo đúng ví dụ đó:

• Haiku ($0,8/$4): (1.150×0,8 + 200×4) ÷ 10⁶ × 30.000 = **$51,6** 
 • Sonnet ($3/$15): (1.150×3 + 200×15) ÷ 10⁶ × 30.000 = **$193,5**

Chứ không phải $36 và $135. **Nhưng hai cột trên slide nhất quán với nhau**: 
 135 ÷ 36 = 3,75 — đúng tỷ lệ giá giữa hai model. Nên biểu đồ dùng một tổ hợp token khác (ví dụ 
 ~1.000 in + 100 out) mà slide không nói ra.

**Điều đáng nhớ và luôn đúng:** tỷ lệ **3,75×** *không phụ thuộc* bạn đặt bao nhiêu token — vì giá input và giá output của hai model cùng tỷ lệ 
 với nhau ($3/$0,8 = $15/$4 = 3,75). Slide làm tròn thành "gấp 4 lần". Tự kiểm bằng [mô-đun hoá đơn](#m-cost): đổi tầng model, tỷ lệ ở cột cuối bảng luôn là 3,75×.

Slide 66 đặt chúng dưới nhãn *"Trục 3 — Test-time / agentic compute"* với chú thích 
 "chỉ đổi bộ đề / harness". Nhưng SWE-bench **Verified** (đề một file, đã bão hoà) và 
 SWE-bench **Pro** (đề đa file, khó hơn) là *hai bộ đề khác nhau*.

Nên kết luận đúng từ cặp số này là về **benchmark**: cùng một model, đổi độ khó của đề 
 thì điểm lệch 19 điểm — củng cố mạnh cho [slide 72](#s71) ("điểm số chỉ có nghĩa kèm tên bộ 
 đề"), chứ không phải bằng chứng cho test-time compute.

**Điều đó không làm trục 3 sai** — test-time compute là một 
 trục có thật, và bằng chứng đơn giản nhất nằm ngay trong bài: ví dụ Chain-of-Thought ở [slide 50](#s50), cùng model cùng câu hỏi, chỉ thêm giấy nháp mà từ sai thành đúng.

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực 
 tế đã chạy."

usage

bạn đo được

mục áp dụng

---

<!-- chiron-source-span: {"source_span_id":"4068de4f-2210-58dc-b575-41ef47d2571a","locator":{"kind":"html_section","section_id":"cheat","order":16,"heading":"✓ Cheat sheet ôn thi","source_file":"day-1-ai-llm-foundation.html"},"checksum":"1e091edafc8cc3686370f54ab03bc31aa68c457215204014da2c8006caf5213a"} -->

## ✓ Cheat sheet ôn thi

Nén 83 slide xuống một trang.

### Câu thần chú và sáu hệ quả

**"Model chỉ đoán token tiếp theo — mọi thứ khác là hệ quả."** Vòng lặp: `predict → append → rerun`.

| Hiện tượng | Vì sao |
| --- | --- |
| Bịa trích dẫn không có thật | Không tra cứu — chọn chuỗi token nghe hợp lý nhất |
| Quên yêu cầu ở giữa prompt dài | Chú ý phân bố không đều — "lost in the middle" |
| Hỏi lại y hệt ra câu khác | Đầu ra là phân bố xác suất, không phải một đáp án |
| "Nghĩ từng bước" thì đúng hơn | Token nháp được nối vào context → thành dữ kiện để đoán tiếp |
| Càng chat càng đắt | Model stateless — toàn bộ lịch sử gửi lại mỗi lượt (bậc hai) |
| Tiếng Việt tốn tiền hơn tiếng Anh | Tokenizer cắt thành nhiều mảnh hơn; tiền tính theo mảnh |

### Bốn bảng phải nhớ

**① Năm tầng lồng nhau:** AI ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI ⊃ LLM. *Câu hỏi đầu tiên cho một bài toán: nó thuộc tầng nào?*

**② Bốn bước tạo ra model:** Pre-training (kiến thức) → SFT (format) → 
 RLHF/DPO (hành vi) → Luyện suy luận (cách nghĩ). *Ba trục làm model giỏi hơn:* pretraining scale 
 (Chinchilla 70B thắng 3 model to hơn) · post-training (85% vs 15%, cùng 175B) · 
 test-time compute — **trục duy nhất bạn điều khiển được**.

**③ Bốn mức LLM → Agent:** L0 bộ não trần · L1 + tools · L2 + lập kế hoạch · 
 L3 + đội agent. *Agent = Goal + Reasoning + Tools + Memory + Action, chạy thành vòng lặp.*

**④ Ba tầng chọn model:** Frontier (chỉ việc thật khó) · **Rẻ mà mạnh ★ thử tầng này trước** · Self-host (kiểm soát dữ liệu, chi phí quy mô lớn). *Hai lỗi đối xứng: việc dễ gọi frontier = phí tiền; việc khó cố dùng rẻ = kết quả tệ.*

### Công thức tiền — thứ duy nhất cần tính được

```text
chi phí một lần gọi = (token_vào × giá_vào + token_ra × giá_ra) / 1.000.000

Ví dụ chuẩn (slide 68):  1.150 × $3 + 200 × $15  →  $0,00345 + $0,00300 = $0,0065
                          ↑ 85% số token              ↑ 15% số token
                            53% hoá đơn                 47% hoá đơn

Hội thoại n lượt:  token(lượt n) = system + context + (n−1)×(hỏi+đáp) + hỏi + đáp
                                                       └── phần này phình theo BẬC HAI
```

**Ba núm vặn, xếp theo tác động:** ① độ dài *output* (đắt gấp 3–5 lần) → 
 ② tầng model → ③ độ dài input. *Ngoại lệ:* trong hội thoại nhiều lượt, system prompt lên hàng 
 đầu vì được gửi lại mỗi lượt.

**Và nhớ:** chi phí với độ trễ là *cùng một núm vặn* — 
 tối ưu cái này là tối ưu cái kia.

### Năm câu hay ra đề — trả lời một dòng

| Câu hỏi | Trả lời gọn |
| --- | --- |
| Vì sao output đắt hơn input? | Input đọc một lượt (song song được); mỗi token output đòi một lượt chạy riêng, đọc lại cả ngữ cảnh |
| Vì sao Transformer thắng RNN? | Hai lý do, và lý do quyết định là song song hoá được → dùng hết GPU → scaling law tồn tại |
| Context 1M có thay được RAG không? | Không. Tiền · tốc độ (n²) · và chất lượng có thể giảm vì "context rác = attention rác" |
| Temperature làm model thông minh hơn? | Không. Bảng xác suất đã tính xong; nó chỉ đổi cách đọc bảng. Thứ tự các từ không đổi |
| Model nhớ cuộc trò chuyện? | Không — stateless. "Trí nhớ" là do bạn gửi lại lịch sử. Điều đó phiền (đắt) nhưng cũng là thứ cho bạn toàn quyền |

---

<!-- chiron-source-span: {"source_span_id":"3b1b1f13-dedc-5beb-a431-215b281a1dfe","locator":{"kind":"html_section","section_id":"gloss","order":17,"heading":"A–Z Từ điển thuật ngữ","source_file":"day-1-ai-llm-foundation.html"},"checksum":"6c3f9acf5df77c271378b95e10cf73eb03c6b737ff73dfd0e59ffe7246f9e320"} -->

## A–Z Từ điển thuật ngữ

Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"2d2facf2-cbdf-5849-9dec-6aef64ed578d","locator":{"kind":"html_section","section_id":"bloom","order":18,"heading":"◉ Bạn đang ở mức nào?","source_file":"day-1-ai-llm-foundation.html"},"checksum":"8c2740a6ca60e3987e6d130252294ed176643ebe8d8c4aa0364a49ab34bed89e"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Quiz kiểm tra mức 1–3; bài thực hành chiều 
 (gọi API + chatbot) kiểm tra mức 3–4.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được năm tầng AI, bốn bước tạo model, bốn mức LLM→Agent, ba tầng chọn model, và ba giới hạn 
 bẩm sinh. | Hình 1 · Hình 4 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao output đắt hơn input, và vì sao "nghĩ từng bước" làm 
 model đúng hơn — cả hai từ cùng một vòng lặp. | Hình 3 · slide 50 · ô kiểm tra chương 3 |
| 3 · Áp dụng | Ước lượng được chi phí tháng cho một ý tưởng sản phẩm, và chọn được tầng model kèm lý do. | mô-đun hoá đơn · mô-đun lịch sử · 
 Bài 3 |
| 4 · Phân tích | Cho một hiện tượng lạ (bịa, quên, đắt bất ngờ, sai bất thường), quy được về cơ chế và chỉ ra chỗ 
 sửa rẻ nhất. | Bảng sáu hệ quả · Bài 1 → 2 |
| 5 · Đánh giá | Đọc một bài báo hoặc một bảng benchmark về model mới và nói được: điều gì không suy ra 
 được từ nó. | Slide 72 · Con số cần kiểm chứng · 
 hiểu lầm 6 |

không phải

Benchmark Y đo cái gì và đã bão hoà chưa? Ai công bố con số 
 này? Việc của tôi có giống benchmark Y không?

không
