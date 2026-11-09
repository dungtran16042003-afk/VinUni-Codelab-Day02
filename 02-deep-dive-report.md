# Phase 3 — DEEP-DIVE: Vinmec Discharge Summary (Tóm tắt xuất viện)

## 3.1. Current-State Workflow Mapping
Sơ đồ quy trình hiện tại (Tác vụ thủ công hoàn toàn):
- **Bước 1:** Bác sĩ ra quyết định xuất viện (⏱ 2 phút).
- **Bước 2:** Mở và đọc lại EMR, xét nghiệm, siêu âm (⏱ 8 phút).
- **Bước 3 (🔴 Bottleneck):** Gõ thủ công bản tóm tắt bệnh án và dặn dò (⏱ 15 phút).
- **Bước 4 (🔄 Handoff):** Ký duyệt bản cứng và bàn giao cho bệnh nhân (⏱ 5 phút).
=> **Tổng cộng = 30 phút/ca.**

## 3.2. Problem Statement (6-field)
| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Bác sĩ điều trị chính tại Vinmec. |
| **2. Current Workflow** | Bác sĩ tự tổng hợp và gõ tay bản tóm tắt quá trình điều trị từ hệ thống EMR để làm thủ tục xuất viện (mất ~30 phút/ca). |
| **3. Bottleneck** | Việc gõ tay và tổng hợp lượng lớn thông tin y khoa rải rác tốn nhiều thời gian, rủi ro bỏ sót thông tin cao khi mệt mỏi. |
| **4. Business Impact** | Giải pháp tiết kiệm ~18,250 giờ làm việc hành chính của bác sĩ/năm. Nếu chuyển hóa 40% số giờ này thành ca khám mới, dự kiến tạo ra thêm **14.6 Tỷ VNĐ doanh thu/năm**, đồng thời tăng CSAT do bệnh nhân không phải chờ đợi lâu. |
| **5. Success Metric** | Giảm thời gian soạn tóm tắt xuống < 5 phút (Efficiency). Tỉ lệ Bác sĩ giữ nguyên bản AI Draft đạt > 85% (Quality). |
| **6. Operational Boundary** | **CẤM:** Tự chẩn đoán, tự kê đơn, suy diễn ngoài EMR. Cấm sinh tóm tắt nếu sinh hiệu (vitals) nguy hiểm. **Bắt buộc:** HITL (Bác sĩ phải đọc và duyệt). |

## 3.3. Future-State Flow & AI Fit
* **AI Fit:** [x] LLM Feature
* **Future-State Flow:**
  - Bước 1: Quyết định xuất viện.
  - Bước 2: 🔵 **AI Step** - Hệ thống tự động kéo dữ liệu EMR và LLM draft sẵn bản tóm tắt.
  - Bước 3: 🟢 **Human Step** - Bác sĩ đọc, review và ký duyệt (HITL).
  - ↩️ **Fallback:** Nếu hệ thống lỗi hoặc AI sinh văn bản kém chất lượng, bác sĩ chuyển về quy trình gõ tay thủ công ban đầu.

---

# Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? (Hồ sơ bệnh án ẩn danh).
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát? (Có, vì bắt buộc qua bước duyệt của Bác sĩ).
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? (Có, vì bác sĩ rất muốn giảm tải việc hành chính).

### Quyết định cuối cùng:
[x] **GO (Bắt đầu xây dựng Prototype)**
*Justification:* Bài toán có ROI rõ ràng (14.6 Tỷ VNĐ/năm), ranh giới y khoa có thể kiểm soát chặt chẽ bằng System Prompt và Human-in-the-loop. Giải pháp công nghệ (LLM Feature) hoàn toàn khả thi và dễ triển khai trong thời gian ngắn.