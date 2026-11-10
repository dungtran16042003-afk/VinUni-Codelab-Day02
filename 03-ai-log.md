# Deliverable 03 — AI Collaboration Log & Reflection (Gate I3)

* **THÔNG TIN DỰ ÁN & NHÓM THỰC HIỆN**
* **Tên nhóm:** [Điền tên nhóm của bạn, ví dụ: Nhóm 02 / VinFast Operations]
* **Đề tài:** Tối ưu hóa phân luồng sự cố trạm sạc xe điện (VinFast & V-GREEN)
* **Danh sách thành viên:**
  1. **Nguyễn Tấn Dũng (Trưởng nhóm)** - dungtran16042003@gmail.com
  2. **Lê Thanh Tùng** - lethanhtung6803@gmail.com
  3. **Lê Huy Anh** - hanhfpt2226@gmail.com
  4. **Phạm Hoàng Huy** - huyclaynun@gmail.com
  5. **Cấn Xuân Nghĩa** - cannghia.xn@gmail.com

> 1. AI đã hỗ trợ hiệu quả ở những điểm nào? (What AI helped with)

Trong suốt quá trình thực hiện bài lab, AI đóng vai trò như một cộng sự tư duy phản hồi nhanh (rapid thought-partner), hỗ trợ giải phóng sức lao động ở các khâu:

* **Mở rộng danh mục quan sát với 4 Lenses:** AI hỗ trợ phân loại nhanh các hoạt động vận hành của Vingroup thành 4 lăng kính chuẩn (*Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác*), giúp tôi không bị tắc ý tưởng khi bắt đầu Phase 1.
* **Mô hình hóa tài chính định lượng (Quantitative Business Case):**
  * AI giúp tôi chuyển đổi các hiện tượng vận hành trừu tượng thành công thức toán học và con số tài chính có sức nặng thuyết phục:
    * Tiết kiệm chi phí lao động: $V_{labor} = 360.000 \times \left(\frac{25 - 0{,}5}{60}\right) \times 50.000 \approx \mathbf{7{,}35\text{ tỷ VNĐ/năm}}$.
    * Bảo toàn doanh thu bán điện: $V_{power} = 54.000 \times 4 \times 80 \times 0{,}10 \times 3.858 \approx \mathbf{66{,}66\text{ tỷ VNĐ/năm}}$.
    * Tổng giá trị đóng góp: $\mathbf{\sim 74\text{ tỷ VNĐ/năm}}$.
* **Soạn thảo khung kỹ thuật (Schema & Edge Cases):** AI đề xuất nhanh cấu trúc JSON schema chuẩn (`pillar_id`, `issue_category`, `priority_level`) và gợi ý các kịch bản kiểm thử tấn công (Adversarial test inputs) giúp rút ngắn đáng kể thời gian chuẩn bị cho phần code prototype.

---

## 2. Những sai sót và điểm mù của AI trong quá trình làm việc (Where AI failed)

Nếu quá phụ thuộc hoặc tin tưởng tuyệt đối vào AI mà không có chuyên môn phản biện, bài làm sẽ bị sai lệch nghiêm trọng do 4 lỗi điển hình của mô hình:

* **Lỗi 1 — Hiểu sai phân cấp cá nhân và nhóm:**
  * AI nhầm lẫn giữa phạm vi bài tập cá nhân trên branch riêng và bài tập nhóm trên branch `main`. AI tưởng nhầm việc chọn bài toán diễn ra ngay ở Phase 1 của cá nhân, dẫn đến cách trình bày lộn xộn giữa trách nhiệm cá nhân và quyết định của tập thể nhóm.
* **Lỗi 2 — Bẫy thu hẹp ngữ cảnh (Narrow Context Trap):**
  * Khi tôi yêu cầu tập trung vào VinFast, AI lập tức thu hẹp toàn bộ 3 thẻ Quick Problem Card vào riêng nội bộ VinFast. Điều này vi phạm nghiêm trọng yêu cầu của Phase 1 (buộc phải quét rộng trên toàn hệ sinh thái Vingroup gồm Vinhomes, Vinmec, Xanh SM rồi mới đối chiếu lựa chọn).
* **Lỗi 3 — Xáo trộn cấu trúc giai đoạn (Phase Bleeding):**
  * AI tự ý "lấn sân", nhồi nhét toàn bộ phần tính toán tài chính chuyên sâu, so sánh Rule vs LLM và ranh giới vận hành (nội dung của Phase 3 & 4 thuộc file `02-deep-dive-report.md`) dồn hết vào file `01-problem-scan.md`, làm sai lệch hoàn toàn format chuẩn của repo mẫu `02-deliverable-example.md`.
* **Lỗi 4 — Ảo tưởng quyền hạn tự trị (Over-automation & Zero-Tolerance Breach):**
  * AI ban đầu gợi ý để hệ thống tự động hoàn tiền vào ví tài xế hoặc gửi lệnh API reset ngắt điện trụ sạc. Đây là điểm mù cực kỳ nguy hiểm, vi phạm nghiêm trọng an toàn lưới điện và an toàn kiểm toán tài chính.

---

## 3. Quá trình tôi phản biện, điều hướng và chấn chỉnh AI (How I steered & corrected AI)

Để bảo vệ tính đúng đắn và chất lượng bài làm, tôi đã trực tiếp nắn chỉnh AI qua các bước cụ thể:

* **Bắt bẻ lại cấu trúc đề bài:** Tôi chỉ rõ cho AI thấy tài liệu mẫu `02-deliverable-example.md` và `01-worksheet.md` quy định tách biệt từng giai đoạn; buộc AI phải bóc tách nội dung, đưa Phase 1 & 2 về đúng file `01-problem-scan.md` và chuyển Phase 3, 4, 5 sang file `02-deep-dive-report.md`.
* **Ép AI mở rộng phạm vi quét Vingroup:** Tôi nhắc nhở AI rằng bài tập cá nhân phải thể hiện năng lực bao quát cả hệ sinh thái; yêu cầu AI tạo đủ 3 Card độc lập (VinFast trạm sạc, Vinhomes app cư dân, Vinmec tóm tắt bệnh án) để tạo cơ sở phản biện khách quan trước khi chọn bài toán của VinFast.
* **Thiết lập "Ranh giới đỏ" (Strict Guardrails & HITL):** Tôi kiên quyết bác bỏ các ý tưởng can thiệp vật lý/tài chính của AI. Tôi bắt buộc mô hình phải hoạt động theo cơ chế **LLM Feature có Human-in-the-loop (HITL)**: AI chỉ có nhiệm vụ trích xuất dữ liệu và tạo Draft Ticket; quyền phê duyệt cuối cùng và quyền điều động kỹ thuật viên 100% thuộc về điều phối viên con người.
* **Kiểm định tính xác thực của dữ liệu:** Tôi tra hỏi và yêu cầu AI giải trình từng con số giả định (công suất sạc 80 kW, tỷ lệ downtime 35%, đơn giá 3.858 VNĐ/kWh) để đảm bảo mọi luận điểm đưa ra hội đồng đều có căn cứ vững chắc, không phải số liệu bịa đặt.

---

## 4. Bài học đúc kết về tư duy AI Product Engineer (Key Takeaways)

1. **Problem-First, AI-Second:** Giá trị của một kỹ sư công nghệ không nằm ở việc áp dụng mô hình phức tạp (như Agentic hay Multi-Agent) vào mọi chỗ, mà nằm ở việc nhận biết khi nào bài toán chỉ cần **Rule-based/SQL** (như bài toán tính phí đỗ xe Idle Fee) và khi nào thật sự cần **LLM** (đọc hiểu văn bản lủng củng của tài xế).
2. **Kỹ sư là người cầm lái, AI chỉ là động cơ:** AI rất mạnh trong việc tạo sinh nội dung và gợi ý cấu trúc, nhưng con người bắt buộc phải là người đặt ra tiêu chuẩn nghiệm thu, kiểm soát ranh giới an toàn (Guardrails) và chịu trách nhiệm pháp lý cho sản phẩm.
3. **Quản trị rủi ro ảo giác (Hallucination Control):** Không bao giờ giao toàn bộ quy trình cho LLM mà không có cơ chế Fallback và sự giám sát của con người (Human-in-the-loop), đặc biệt là trong các hạ tầng kỹ thuật thực địa như lưới điện hay phương tiện giao thông.
