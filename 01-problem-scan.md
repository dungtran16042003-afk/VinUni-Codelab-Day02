# Problem Scan & Quick Cards — Lê Thanh Tùng, 2A202603819

Branch cá nhân: `le-thanh-tung-2A202603819`. Đề tài cuối: **xác nhận đúng cổng/mặt đường đón khách Xanh SM**. Bài cá nhân đầy đủ để trưởng nhóm review, chọn lọc.

## Phase 1 — SCAN

Đây là các cơ hội nghiên cứu. Tính cấp thiết, tần suất và mức ảnh hưởng phải được kiểm chứng; không gọi chúng là vấn đề doanh nghiệp chưa giải quyết. Số phút và tỷ lệ trong các card là **giả định lab**.

| # | Công ty theo bối cảnh lab | Lens | Problem | Căn cứ và khoảng trống cần xác minh |
|---|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Khách/tài xế tìm nhầm cổng, mặt đường hoặc sảnh tại địa điểm nhiều lối vào. | Đã có nhập GPS, gọi/nhắn xác nhận. Khám phá hiệu quả xác nhận cổng cụ thể; không tuyên bố hệ thống chưa có chức năng tương tự. [Memo](research/2026-11-09-pickup-entrance-checkin.md). |
| 2 | Xanh SM | Pain từ người khác | Phản ánh dẫn đường sai, đường cấm hoặc ngập cần được xác minh kịp thời. | Đã có đóng góp bản đồ; cần đo thời gian và chất lượng cập nhật. [Nguồn](https://www.greensm.com/vn-vi/news/trien-khai-tinh-nang-dong-gop-ban-do-bac-tai-xanh-di-toi-dau-ban-do-green-sm-chuan-toi-do). |
| 3 | Xanh SM | Lặp lại | Hồ sơ xác nhận bảo dưỡng thiếu/sai thông tin khiến kết quả chưa được ghi nhận. | Đã có nhắc lịch/nộp phiếu; cần đo tỷ lệ phải nộp lại. [Nguồn](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-nhac-lich-xac-nhan-bao-duong-tren-ung-dung-bac-tai-xanh-bike). |
| 4 | Xanh SM | AI-upgrade | Chuẩn bị giải trình sự cố có đủ bằng chứng trước hạn. | Đã có quy trình giải trình; không suy ra cảnh báo sai. Bản cập nhật 27/10 áp dụng Bike Platform TP.HCM. [Nguồn](https://greensm.com/vn-vi/news/cap-nhat-thoi-han-phan-hoi-tren-ung-dung-tai-xe-green-sm). |
| 5 | Vinhomes | Lặp lại | Chuẩn hóa phản ánh cư dân để chuyển đúng bộ phận. | Gợi ý từ inspiration kit, chưa có dữ liệu phản ánh thực hoặc baseline. |
| 6 | Vinpearl | AI-upgrade | Trích thông tin đặt phòng đoàn và hỏi lại trường còn thiếu. | Gợi ý từ inspiration kit; cần so với form/template và dữ liệu quỹ phòng. |

## Phase 2 — QUICK-ASSESS

### Card #1 — Chọn: Đúng cổng, đúng mặt đường, đúng điểm đón

| Trường | Nội dung |
|---|---|
| Bài toán | Giảm công làm rõ vị trí gần đúng tại địa điểm nhiều cổng, giúp khách và tài xế gặp nhau đúng điểm đón được phép. |
| Subsidiary / Actor | Xanh SM; khách mô tả/xác nhận vị trí, tài xế xác nhận khả năng tiếp cận. |
| Workflow hiện tại cần khảo sát | Khách gửi vị trí → tài xế vào khu vực đón → gọi hỏi cổng/mốc → tìm đúng mặt đường → hai bên gặp nhau. Chưa xác nhận workflow thực. |
| Bottleneck giả định | Làm rõ cổng và mặt đường 105/180 giây của một lượt tìm nhau trong khu vực đón. |
| AI hỗ trợ | Chuẩn hóa mô tả tiếng Việt, khớp candidate có sẵn, hỏi câu làm rõ khi nhiều cổng cùng tên; backend cấp nhãn/đường/tọa độ từ catalog. |
| Metric có số | Thời gian 180→60 giây; đúng cổng lần đầu 75%→95%; cuộc gọi 2→≤1; hủy do không tìm được nhau 5%→3%. Tất cả là mục tiêu pilot. |
| Architecture | LLM Feature + catalog đã xác minh + rule + khách/tài xế xác nhận. |
| Boundary | Không bịa tọa độ/cổng, không chọn cổng đóng/cấm đón/không hợp xe, không tự xác nhận hoặc bắt khách băng đường. |
| Data & test | Catalog và tin nhắn tổng hợp; test cổng sau, cổng phụ mơ hồ, phía đường đối diện, cổng hạn chế và prompt injection. |

### Card #2 — Xử lý phản ánh bản đồ động

| Trường | Nội dung |
|---|---|
| Bài toán / Actor | Nhân viên xác minh phản ánh đường sai/cấm/ngập cần thông tin đủ rõ để cập nhật đúng điều kiện. |
| Công ty | Xanh SM. |
| Workflow | Nhận báo cáo → đọc vị trí/thời điểm → gom báo cáo liên quan → xác minh → cập nhật khi đủ điều kiện. Đã có tính năng báo cáo; chi tiết nội bộ cần khảo sát. |
| Bottleneck giả định | Đọc/làm rõ báo cáo 8/12 phút; chưa có baseline đo. |
| AI hỗ trợ | Trích loại sự cố và điều kiện theo giờ, gom mô tả tương đương, chỉ ra xung đột; người có thẩm quyền xác minh. |
| Metric mục tiêu | Chuẩn bị hồ sơ xác minh 12→5 phút/báo cáo; ≥95% trường bắt buộc đúng trên tập gán nhãn riêng. |
| Architecture / Boundary | LLM extraction + rule địa lý/thời gian + người duyệt; không tự đổi bản đồ từ một báo cáo chưa xác minh. |
| Lý do chưa chọn | Cần dữ liệu nguồn hiện trường và quyền cập nhật bản đồ, khó kiểm chứng tác động cuối trong lab. |

### Card #3 — Kiểm tra hồ sơ bảo dưỡng trước khi gửi

| Trường | Nội dung |
|---|---|
| Bài toán / Actor | Tài xế Bike đã bảo dưỡng cần nộp đúng mã phiếu và ảnh rõ để hệ thống ghi nhận. |
| Công ty | Xanh SM/Green SM Bike, đúng phạm vi nguồn. |
| Workflow | Nhận nhắc lịch → bảo dưỡng tại xưởng → nhập mã/chọn xưởng/tải ảnh → hệ thống đối chiếu → sửa/nộp lại nếu chưa đủ. |
| Bottleneck giả định | Nhập và kiểm tra 6/10 phút/hồ sơ; chưa đo số lần nộp lại. |
| AI hỗ trợ | OCR mã phiếu từ ảnh, kiểm tra ảnh mờ/thiếu, gợi ý điền; rule kiểm độ dài mã và tra xưởng/dữ liệu gốc nếu có API. |
| Metric mục tiêu | Chuẩn bị hồ sơ 10→4 phút; tỷ lệ đủ thông tin lần đầu ≥95%; exact-match mã phiếu ≥99% trên tập riêng. |
| Architecture / Boundary | OCR + rule + tài xế kiểm tra; không tự công nhận bảo dưỡng từ ảnh hoặc bịa mã. Nếu có API xưởng chuẩn, ưu tiên API. |
| Lý do chưa chọn | Phạm vi hẹp hơn trải nghiệm đón khách; vẫn là phương án dự phòng có vấn đề cụ thể được nguồn chính thức nêu. |

## Lựa chọn cuối và đối chứng

Chọn Card #1 theo yêu cầu cá nhân: cổng sau/cổng phụ/một mặt cụ thể. So sánh ba cách trên cùng tình huống: (A) pin + chat hiện có, (B) danh sách cổng có cấu trúc không AI, (C) danh sách cổng + AI hiểu mô tả. Chỉ giữ AI nếu tăng đúng cổng/giảm tổng công thao tác so với B, không chỉ so với A. [Báo cáo](02-deep-dive-report.md).
