# Phase 1 — SCAN: Tìm kiếm cơ hội

Dưới đây là 5 bài toán/bottleneck thực tế được quét qua các hoạt động vận hành của các công ty thành viên Vingroup:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20-30 phút để đọc lại bệnh án điện tử (EMR) và tự gõ tay bản tóm tắt hồ sơ xuất viện cho mỗi bệnh nhân. |
| 2 | **Vinmec** | Pain từ người khác | Bệnh nhân không biết mô tả triệu chứng thuộc chuyên khoa nào, dẫn đến tổng đài viên xếp sai lịch hẹn khám ban đầu. |
| 3 | **Vinmec** | Lặp lại | Điều dưỡng phải gõ lại thủ công các chỉ số xét nghiệm/siêu âm từ bản giấy (của phòng khám vệ tinh) vào hệ thống nội bộ. |
| 4 | **Xanh SM** | Lặp lại | Điều phối viên xử lý thủ công các báo cáo sự cố hết pin giữa đường của tài xế xe điện. |
| 5 | **Vinhomes** | AI-upgrade | Phân loại và điều phối thủ công các khiếu nại của cư dân (ồn ào, mất nước, hỏng đèn) trên App Vinhomes Resident. |

---

# Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Dựa trên danh sách trên, nhóm quyết định chọn 3 bài toán tại Vinmec để đánh giá nhanh.

## QUICK PROBLEM CARD #1 (Bài toán được chọn để Deep-dive)
Bài toán: Bác sĩ tốn quá nhiều thời gian trích xuất thông tin từ bệnh án điện tử để soạn bản tóm tắt hồ sơ xuất viện.
Công ty thành viên: [x] Vinmec
Ai đang đau (Actor)? Bác sĩ điều trị (quá tải hành chính), Bệnh nhân (chờ đợi xuất viện lâu).
Workflow thủ công hiện tại: 
  1. Mở EMR ──> 2. Đọc lại xét nghiệm/ghi chú lâm sàng ──> 3. Gõ tay tóm tắt xuất viện ──> 4. Ký duyệt & In
Bước tốn thời gian nhất: Bước 2 & 3 (⏱ 25 phút/ca).
AI nhảy vào hỗ trợ ở bước nào? Bước 3 (LLM đọc hiểu EMR và tự động sinh bản Draft tóm tắt).
Đo thành công bằng gì (Metric)? Giảm thời gian soạn tóm tắt từ 25 phút ──> dưới 5 phút/ca.
Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

## QUICK PROBLEM CARD #2
Bài toán: Bệnh nhân mô tả triệu chứng mơ hồ khiến tổng đài xếp sai lịch khám chuyên khoa.
Công ty thành viên: [x] Vinmec
Ai đang đau (Actor)? Tổng đài viên CSKH, Bệnh nhân.
Workflow thủ công hiện tại: 
  1. BN gọi điện báo triệu chứng ──> 2. CSKH tra cứu/hỏi lại ──> 3. CSKH tự phán đoán chuyên khoa ──> 4. Book lịch
Bước tốn thời gian nhất: Bước 2 & 3 (⏱ 10 phút/lượt, dễ sai sót).
AI nhảy vào hỗ trợ ở bước nào? Bước 1 & 2 (Triage Chatbot tự động hỏi đáp triệu chứng và gợi ý chuyên khoa).
Đo thành công bằng gì (Metric)? Tỉ lệ gợi ý đúng chuyên khoa > 95%.
Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

## QUICK PROBLEM CARD #3
Bài toán: Nhập liệu thủ công kết quả xét nghiệm bản cứng vào hệ thống.
Công ty thành viên: [x] Vinmec
Ai đang đau (Actor)? Điều dưỡng hành chính.
Workflow thủ công hiện tại: 
  1. Nhận phiếu bản cứng ──> 2. Đọc từng chỉ số ──> 3. Gõ lại vào phần mềm HIS ──> 4. Lưu hồ sơ
Bước tốn thời gian nhất: Bước 2 & 3 (⏱ 15 phút/tờ, dễ gõ sai số).
AI nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (OCR + LLM đọc ảnh và chuẩn hóa ra định dạng bảng).
Đo thành công bằng gì (Metric)? Tỉ lệ nhận diện và nhập liệu chính xác > 99%, thời gian dưới 10s/phiếu.
Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent