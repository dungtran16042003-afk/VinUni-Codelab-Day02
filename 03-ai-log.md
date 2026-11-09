# Phase 6 — AI Log & Reflection (Nhật ký tương tác AI)

## 1. AI đã giúp tôi những gì?
- **Brainstorming & Scoping:** AI đóng vai trò "thought-partner", giúp tôi phân tích 3 bài toán tại Vinmec và chọn ra bài toán "Tự động hóa soạn tóm tắt hồ sơ xuất viện" với ROI cực cao.
- **Ranh giới y khoa:** AI hỗ trợ thiết kế System Prompt chặt chẽ (bắt buộc gắn thẻ `[DRAFT_ONLY_PENDING_MD_APPROVAL]`, cấm tự kê đơn thuốc, cảnh báo sinh hiệu xấu bằng JSON).
- **Tính toán Business Impact:** Hỗ trợ quy đổi 18,250 giờ làm việc tiết kiệm được thành doanh thu gia tăng 14.6 Tỷ VNĐ/năm.

## 2. Tôi gặp khó khăn gì và AI sai ở đâu?
- Khi tạo code prompt_prototype.py, tôi gặp lỗi `ImportError: cannot import name 'genai' from 'google'`.
- Sau đó, khi chạy API, hệ thống báo lỗi `404 models/gemini-3.8 is not found` do phiên bản model chưa hỗ trợ.

## 3. Tôi đã sửa đổi (Refine) như thế nào?
- **Gỡ lỗi Import:** Tôi đã cài lại thư viện `pip install google-generativeai` và trực tiếp sửa cú pháp import trong code thành `import google.generativeai as genai` để khắc phục lỗi.
- **Cấu hình Model:** Tôi đã cập nhật biến `GEMINI_MODEL = "gemini-3.8-flash"` cho phù hợp với API Key hiện tại.
- Bài học rút ra: LLM rất giỏi tạo framework, nhưng AI Product Engineer phải là người kiểm chứng mã nguồn, setup môi trường (API Key, `.venv`) và xử lý lỗi thực tế (Debugging) thì giải pháp mới hoạt động.