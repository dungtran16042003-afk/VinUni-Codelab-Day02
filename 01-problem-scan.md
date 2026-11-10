<!-- ============================================================================== -->
<!-- TÊN NHÓM: Nhóm X                                          -->
<!-- TÊN THÀNH VIÊN:                                                         -->
<!-- 1. Nguyễn Tấn Dũng - [Email: dungtran16042003@gmail.com]                                                   
============================================================================== -->

# Deliverable 01 — Problem Scan (VinFast / V-GREEN Use Case)

> **Mục tiêu của file này:** Thực hiện quét cơ hội (Phase 1 — SCAN) và hoàn thiện đầy đủ 3 Thẻ bài toán nhanh (Phase 2 — QUICK-ASSESS) theo đúng tiêu chuẩn Rubric của Vin Smart Future.
>
> **Mảng kinh doanh lựa chọn:** **VinFast & V-GREEN — Mạng lưới trạm sạc xe điện & Dịch vụ hậu mãi toàn quốc.**

---

## 🏛️ Bối cảnh: Tôi là ai?

Tôi đóng vai là một AI Engineer tại **Vin Smart Future**. Nhóm chúng tôi phối hợp cùng Khối Vận hành Dịch vụ Khách hàng & Hạ tầng Trạm sạc của **VinFast / V-GREEN** nhằm tìm kiếm cơ hội tối ưu hóa quy trình tiếp nhận và xử lý sự cố mạng lưới trạm sạc bằng mô hình ngôn ngữ lớn (LLM).

Qua khảo sát thực tế tại Trung tâm Điều hành Vận hành (NOC), các điều phối viên và nhân viên CSKH đang gặp áp lực rất lớn khi xử lý hàng nghìn tin nhắn báo lỗi dạng văn bản tự do mỗi ngày từ tài xế. Tình trạng nhập liệu thủ công kéo dài gây nghẽn điều phối, khiến trụ sạc hỏng chậm được khắc phục và ứng dụng hiển thị trạng thái khả dụng ảo. Bài toán này được chọn để giải quyết dứt điểm nút thắt đó.

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Sử dụng **4 Lenses** quét qua các mảng vận hành của VinFast và hạ tầng V-GREEN để ghi nhận 6 bài toán thực tế:

| # | Subsidiary / Unit | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | **VinFast (Charging)** | **Tốn thời gian** | CSKH đọc hiểu tin nhắn tự do lủng củng của tài xế để lập ticket điều phối kỹ thuật sửa trụ sạc (mất 25 phút/ticket). |
| 2 | **VinFast (Charging)** | **Lặp lại** | Tính phí phạt chiếm chỗ sau khi sạc đầy (Idle fee) và trừ tiền tự động trên ví tài xế qua dữ liệu telemetry. |
| 3 | **VinFast (Aftersales)** | **Pain từ người khác** | Kỹ thuật viên xưởng dịch vụ mất 30 phút tra cứu mã lỗi chẩn đoán OBD-II và tài liệu hướng dẫn sửa chữa PDF cồng kềnh. |
| 4 | **V-GREEN** | **AI-upgrade** | Dự báo nhu cầu phụ tải điện tại các trạm sạc cao tốc vào dịp lễ tết để điều phối trạm sạc lưu động. |
| 5 | **VinFast (Battery)** | **Lặp lại** | Đối soát hóa đơn tiêu thụ điện năng định kỳ giữa trụ sạc đối tác nhượng quyền và dữ liệu tổng trạm V-GREEN. |
| 6 | **VinFast (CSKH)** | **Tốn thời gian** | Tóm tắt nguyên nhân khiếu nại chất lượng dịch vụ sạc từ log ghi âm cuộc gọi hotline tổng đài để phân loại lỗi hệ thống. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn top 3 bài toán từ danh sách SCAN: **#1 (Sự cố trạm sạc), #2 (Phí phạt đỗ sạc), #3 (Tra cứu lỗi kỹ thuật xưởng dịch vụ).**

---

### QUICK PROBLEM CARD #1: VinFast Phân Luồng Sự Cố Trạm Sạc Bằng LLM

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Bóc tách thực thể và phân luồng sự cố trạm sạc    │
│ từ phản ánh dạng văn bản tự do của tài xế xe điện.          │
│ Công ty thành viên: [x] VinFast / V-GREEN                   │
│                                                             │
│ Ai đang đau? Tài xế (ức chế vì trụ ảo), CSKH (quá tải gõ tay)│
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận tin nhắn/cuộc gọi báo sự cố từ khách qua app      │
│   → 2. Đọc hiểu, làm rõ trạm sạc và số trụ gặp vấn đề       │
│   → 3. Tra cứu mã định danh trụ trên hệ thống CMS trạm sạc  │
│   → 4. Phân loại lỗi, gán nhãn ưu tiên và gõ form ticket    │
│   → 5. Bắn phiếu điều phối sang app kỹ thuật viên hiện trường│
│                                                             │
│ Bước nào tốn nhất? Bước 2, 3, 4 (⏱ 20/25 phút/lượt) 🔴      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3, 4          │
│ (LLM đọc hiểu text phi cấu trúc -> trích xuất JSON chuẩn -> │
│ tự động điền sẵn bản Draft Ticket trong 5 giây)             │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Giảm thời gian xử lý ticket từ 25 phút ──> 30 giây (-98%)│
│ 2. Tiết kiệm 147.000 giờ công/năm (~7,35 tỷ VNĐ)            │
│ 3. Giảm 35% downtime trụ, bảo toàn 66,6 tỷ VNĐ bán điện    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Trích xuất & phân loại)│
└─────────────────────────────────────────────────────────────┘
```

---

### QUICK PROBLEM CARD #2: VinFast Tính Phí Chiếm Chỗ Sau Khi Sạc Đầy (Idle Fee)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Tính toán phí phạt chiếm chỗ sau khi pin xe đã đầy│
│ 100% quá 15 phút tại trạm sạc công cộng và trừ ví tự động. │
│ Công ty thành viên: [x] VinFast / V-GREEN                   │
│                                                             │
│ Ai đang đau? Tài xế đến sau không có chỗ sạc, Kế toán đối soát│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Trụ sạc bắn tín hiệu pin đầy 100% về máy chủ trung tâm │
│   → 2. Hệ thống đếm thời gian xe tiếp tục cắm súng sạc      │
│   → 3. Kế toán kiểm tra đối chiếu log thời gian và trạng thái│
│   → 4. Tạo lệnh trừ tiền trên ví VinFast của chủ xe         │
│                                                             │
│ Bước nào tốn nhất? Bước 3 (⏱ 5-10 phút đối soát chéo)       │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Không cần thiết        │
│ (Toàn bộ dữ liệu pin và thời gian đã có cấu trúc chuẩn)     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Tự động hóa 100% khâu tính phí và gạch nợ trong < 1 giây.    │
│ Độ chính xác số học tuyệt đối (100% không sai lệch số dư).  │
│                                                             │
│ Quick Architecture: [x] Rule-Based / Backend Cron-job (No AI)│
└─────────────────────────────────────────────────────────────┘
```

---

### QUICK PROBLEM CARD #3: VinFast Trợ Lý Tra Cứu Mã Lỗi OBD-II Xưởng Dịch Vụ

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Tra cứu mã lỗi kỹ thuật OBD-II và trích xuất quy   │
│ trình sửa chữa khuyến nghị từ cẩm nang kỹ thuật cho thợ máy.│
│ Công ty thành viên: [x] VinFast (Khối Dịch vụ Hậu mãi)     │
│                                                             │
│ Ai đang đau? Kỹ thuật viên xưởng dịch vụ (mất thời gian tra)│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cắm thiết bị chẩn đoán vào xe quét ra danh sách mã lỗi │
│   → 2. Mở file PDF cẩm nang kỹ thuật nội bộ (dày 500 trang) │
│   → 3. Đọc sơ đồ mạch điện và quy trình kiểm tra từng bước   │
│   → 4. Soạn biên bản sửa chữa và đề xuất linh kiện thay thế │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 25 phút/ca chẩn đoán phức tạp)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (RAG)      │
│ (Trợ lý RAG tra cứu nhanh cẩm nang kỹ thuật theo mã lỗi)     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Rút ngắn thời gian tra cứu từ 25 phút xuống 3 phút (-88%).   │
│                                                             │
│ Quick Architecture: [x] LLM Feature (RAG Tra cứu tài liệu)  │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn của nhóm

Nhóm quyết định chọn bài toán **"Card #1 — VinFast Xử lý & Phân luồng sự cố trạm sạc bằng LLM"** để thực hiện báo cáo chuyên sâu (Deep-Dive).

## Bảng so sánh đánh giá lựa chọn:

| Tiêu chí đánh giá | Card #1: Sự cố trạm sạc | Card #2: Phí phạt đỗ sạc | Card #3: Tra cứu lỗi OBD-II |
|---|:---:|:---:|:---:|
| **1. Bản chất dữ liệu đầu vào** | **Phi cấu trúc** (Văn bản tự do, viết tắt, tiếng lóng) | **Cấu trúc 100%** (Timestamp, % Pin, ID xe) | **Bán cấu trúc** (Mã lỗi chuẩn + PDF tài liệu) |
| **2. Mức độ phù hợp với LLM** | **Tối ưu tuyệt đối** (LLM đọc hiểu & trích xuất JSON) | **Không phù hợp** (Vi phạm nguyên tắc dùng AI) | **Phù hợp** (Cần xây dựng hệ thống RAG) |
| **3. Tác động tài chính trực tiếp** | **Rất lớn** (~74 tỷ VNĐ/năm) | Trung bình (Thu phí phạt cục bộ) | Trung bình (Tăng năng suất cục bộ thợ máy) |
| **4. Tính khả thi trong Lab (Prototype)** | **Rất cao** (Schema rõ ràng, test nhanh bằng API) | Không cần prototype AI | Phức tạp (Cần nhúng kho vector tài liệu PDF) |
| **Quyết định** | **CHỌN (Winner)** | **LOẠI (Dùng Rule)** | **LOẠI (Để giai đoạn sau)** |

## Lý do chi tiết:
* **Loại Card #2 (Phí phạt đỗ sạc):** Bài toán tính phí chiếm chỗ dựa trên thời gian thực ngắt sạc là bài toán logic xác định (Deterministic). Toàn bộ dữ liệu pin và thời gian đã được trụ sạc bắn về qua giao thức OCPP chuẩn. Bài toán này giải quyết bằng **Rule-based (Backend / SQL cron-job)** với chi phí gần như bằng 0 và độ chính xác 100%, tuyệt đối không được dùng LLM vì nguy cơ ảo giác gây sai lệch tài chính.
* **Loại Card #3 (Tra cứu lỗi OBD-II):** Mặc dù phù hợp với LLM, nhưng việc xây dựng giải pháp RAG đòi hỏi dữ liệu cẩm nang kỹ thuật độc quyền dày hàng nghìn trang và quy trình nhúng vector database phức tạp, vượt quá phạm vi triển khai nhanh của một buổi lab prompt prototype.
* **Chọn Card #1 (VinFast Sự cố trạm sạc):** Đầu vào là ngôn ngữ tự nhiên không có cấu trúc (viết tắt, tiếng lóng, sai lỗi chính tả) — đây là thế mạnh cốt lõi của LLM. Quy trình áp dụng cơ chế Human-in-the-loop đảm bảo an toàn vận hành, đồng thời mang lại giá trị tài chính đo lường được lên tới **~74 tỷ VNĐ/năm**.