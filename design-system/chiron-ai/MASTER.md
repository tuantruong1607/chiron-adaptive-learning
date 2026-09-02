# Chiron AI UI system

Hệ thống này là chuẩn triển khai cho giao diện học tập Chiron AI. Nó tổng hợp audit bằng `ui-ux-pro-max` ngày 2026-09-01 với nhận diện hiện có của dự án.

## Hướng thiết kế

- Phong cách: editorial tối giản, rõ ràng như một công cụ học tập chuyên nghiệp.
- Cảm hứng Hy Lạp chỉ xuất hiện ở tên gọi, serif display và nhịp bố cục; không dùng họa tiết trang trí làm giảm khả năng đọc.
- Không dùng claymorphism, glassmorphism dày, gradient tím AI đại trà hoặc shadow nặng.
- Một màn hình chỉ có một hành động chính nổi bật. Thông tin học tập và bằng chứng phải quan trọng hơn trang trí.

## Màu sắc

| Vai trò | Light | Dark | Ghi chú |
| --- | --- | --- | --- |
| Canvas | `#edf1f2` | `#111819` | Nền ứng dụng |
| Surface | `#f8faf9` | `#182223` | Khối nội dung |
| Text | `#172522` | `#edf4f1` | Nội dung chính |
| Muted | `#61706d` | `#a9b8b4` | Nội dung phụ |
| Brand | `#0c7067` | `#62c8bb` | CTA, trạng thái active |
| Focus | `#0b766d` | `#86e0d4` | Focus ring rõ trên mọi surface |
| Danger | `#a33b35` | `#ff9a90` | Lỗi và hành động nguy hiểm |

- Văn bản thường phải đạt tương phản tối thiểu 4.5:1.
- Không truyền đạt mastery, quan hệ hoặc lỗi chỉ bằng màu; luôn có nhãn, icon hoặc nội dung tương ứng.

## Typography

- Display và heading: `Lora`, serif, dùng vừa phải để giữ nét học thuật.
- Body và UI: `Manrope`, sans-serif, hỗ trợ tiếng Việt đầy đủ.
- Body tối thiểu 15px trên mobile và 16px cho nội dung dài.
- Metadata tối thiểu 12px; không dùng chữ 9–10px ngoài nhãn ngắn trong đồ thị desktop.
- Heading dùng sentence case, không viết hoa toàn bộ đoạn dài.
- Giữ độ dài dòng nội dung trong khoảng 55–75 ký tự.

## Spacing và hình học

- Base unit: 4px. Khoảng cách chuẩn: 4, 8, 12, 16, 24, 32, 48, 64.
- Control chính cao tối thiểu 44px; mục tiêu tương tác web tuyệt đối không nhỏ hơn 24×24px.
- Khoảng cách giữa các touch target liền kề tối thiểu 8px.
- Radius: 8px cho control, 12px cho card, 16–20px cho surface cấp trang.
- Border 1px giúp phân lớp; shadow chỉ dùng nhẹ cho overlay và drawer.

## Interaction và accessibility

- Mọi tương tác phải dùng được bằng bàn phím và có focus ring tối thiểu 2px với offset rõ.
- Có skip link tới nội dung chính. Menu mobile mở phải chuyển focus vào menu; Escape hoặc đóng menu phải trả focus về nút mở.
- Hover chỉ là tín hiệu bổ sung, không phải cách duy nhất để khám phá hành động.
- Không di chuyển layout khi press; dùng thay đổi màu hoặc độ sáng.
- Overlay không được che phần tử đang focus.
- Tôn trọng `prefers-reduced-motion`; animation chức năng dưới 220ms và không dùng parallax.

## Knowledge Map

- SVG graph chỉ là chế độ trực quan cho tập dưới 100 node.
- Mũi tên và nhãn quan hệ phải biểu diễn rõ nguồn → đích; khi chọn node, làm nổi quan hệ trực tiếp.
- Luôn có chế độ danh sách adjacency làm nguồn sự thật dễ đọc và tương thích screen reader.
- Mobile mặc định mở danh sách; graph vẫn là lựa chọn phụ.
- Chọn node mở drawer có heading nhận focus; đóng drawer trả focus về node đã chọn.
- Citation phải mở đúng source locator, không chỉ mở tài liệu gốc.

## Responsive

- Các breakpoint kiểm tra bắt buộc: 375, 768, 1024 và 1440px.
- Không cho phép horizontal overflow ở cấp trang. Toolbar rộng phải cuộn bên trong chính nó.
- Sidebar chuyển thành drawer ở tablet/mobile; nội dung chính không bị nén dưới 320px.
- Card và dashboard chuyển 1 cột ở mobile nhưng giữ thứ tự ưu tiên hành động.

## Pre-delivery gate

- Kiểm tra keyboard path, focus return, Escape, dark mode và reduced motion.
- Kiểm tra console không có lỗi client-side hoặc hydration.
- Kiểm tra font tiếng Việt hiển thị đúng, không có mojibake hoặc ký tự thay thế.
- Kiểm tra touch target, tương phản, overflow và trạng thái loading/error/empty.
- Chạy typecheck, lint, test và production build trước khi phát hành.
