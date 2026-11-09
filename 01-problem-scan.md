<!-- ============================================================================== -->
<!-- TÊN NHÓM: Nhóm X                                          -->
<!-- TÊN THÀNH VIÊN:                                                         -->
<!-- 1. Nguyễn Tấn Dũng - [Email: dungtran16042003@gmail.com]                                                   
============================================================================== -->
# 01-problem-scan.md: Hệ Thống Tự Động Phân Luồng Sự Cố Trạm Sạc VinFast (V-Charge Triage)

---

## 1. Quick Problem Card: VinFast / V-GREEN

* **Đơn vị công tác (Business Unit):** VinFast & V-GREEN — Bộ phận Vận hành Mạng lưới Trạm sạc Toàn quốc.
* **Tên bài toán (Problem Statement):** Tự động hóa bóc tách thực thể và phân luồng sự cố trạm sạc xe điện từ phản ánh dạng văn bản tự do của khách hàng bằng mô hình ngôn ngữ lớn (LLM).
* **Nỗi đau & Điểm nghẽn (Pain Points & Bottlenecks):**
  * **Quy mô vận hành lớn:** Mạng lưới hơn 150.000 cổng sạc trên toàn quốc tiếp nhận trung bình ~1.000 phản ánh sự cố/ngày (~360.000 ticket/năm).
  * **Tắc nghẽn xử lý thủ công:** Khách hàng báo lỗi bằng văn bản tự do, viết tắt, mô tả hiện tượng lủng củng. Nhân viên CSKH/trực ca mất trung bình **25 phút/ticket** chỉ để đọc hiểu, tra cứu danh mục trạm/mã trụ trên hệ thống và nhập liệu form điều phối.
  * **Điểm mù của hạ tầng IoT:** Giao thức telemetry (OCPP) trên trụ chỉ phát hiện được lỗi mất kết nối mạng hoặc ngắt nguồn điện; hoàn toàn không phát hiện được sự cố vật lý ngoại cảnh (kẹt ngàm khóa súng sạc, nứt vỡ màn hình cảm ứng, xe xăng đỗ chiếm chỗ).
  * **Hậu quả vận hành:** Trụ hỏng nhưng app vẫn báo xanh ảo, tài xế đến nơi không sạc được gây bức xúc gay gắt (CSAT hiện dừng ở mức 78%); trụ nằm chờ xử lý lâu làm lãng phí công suất nạp và thất thoát doanh thu bán điện.
* **Giải pháp đề xuất (Proposed Solution):**
  * Tích hợp LLM tiếp nhận tin nhắn tự do, bóc tách thực thể kỹ thuật và chuẩn hóa thành định dạng JSON trong vòng 5 giây: `{dia_diem, ma_tru, loai_loi, muc_do_uu_tien}`.
  * Vận hành theo mô hình **Human-in-the-loop (HITL)**: AI tạo sẵn dự thảo phiếu điều phối (Draft Ticket). Nhân viên CSKH chỉ mất 5 giây đối soát trên màn hình và bấm duyệt để đẩy thẳng tới kỹ thuật viên hiện trường gần nhất.
* **Tác động định lượng (Measurable Business Impact):**
  * **Thời gian xử lý:** Rút ngắn từ **25 phút xuống 30 giây/ticket** (-98%).
  * **Tiết kiệm giờ công:** Cắt giảm **147.000 giờ công vận hành/năm**, tương đương tiết kiệm trực tiếp **~7,35 tỷ VNĐ/năm** chi phí nhân sự.
  * **Bảo toàn doanh thu điện:** Giảm 35% thời gian dừng hoạt động (downtime) của trụ sạc, đưa 17,28 triệu kWh điện thương phẩm vào khai thác sớm, bảo toàn **66,6 tỷ VNĐ/năm**. Tổng giá trị tài chính đạt **~74 tỷ VNĐ/năm**.
  * **Chất lượng dịch vụ:** Tỷ lệ nhận diện chính xác ca khẩn cấp (chập điện, phát nhiệt) tăng từ **62% lên 94%**; nâng chỉ số CSAT từ **78% lên 92%**.
* **Ranh giới an toàn (Operational Boundary):**
  * AI không trực tiếp can thiệp điều khiển đóng/ngắt nguồn điện lưới.
  * AI không có thẩm quyền xử lý khiếu nại tài chính hoặc cam kết hoàn tiền/voucher.
  * 100% lệnh xuất kho vật tư và điều phối kỹ thuật viên đều phải có nhân viên vận hành xác nhận.

---

## 2. Phân Tích Định Lượng & Hiệu Quả Kinh Tế Chi Tiết

### Bảng đối chuẩn trước và sau khi triển khai AI

| Chỉ số vận hành (KPI) | Hiện trạng (Manual Baseline) | Mục tiêu AI (V-Charge Triage) | Mức độ cải thiện |
|:---|:---:|:---:|:---:|
| **Thời gian xử lý trung bình / ticket** | 25 phút | 30 giây | **Giảm 98,0%** |
| **Tổng giờ công xử lý / năm** | 150.000 giờ | 3.000 giờ | **Tiết kiệm 147.000 giờ** |
| **Chi phí nhân sự trực ca** | ~7,50 tỷ VNĐ | ~0,15 tỷ VNĐ | **Tiết kiệm ~7,35 tỷ VNĐ** |
| **Độ chính xác phân luồng khẩn cấp (P1)** | 62% | 94% | **Tăng +32%** |
| **Thời gian chết trung bình của trụ (Downtime)** | ~11,4 giờ/sự cố | ~7,4 giờ/sự cố | **Giảm 35% (rút ngắn 4 giờ)** |
| **Doanh thu bán điện bảo toàn** | 0 VNĐ | 66,6 tỷ VNĐ/năm | **Bảo toàn ~66,6 tỷ VNĐ** |
| **Chỉ số hài lòng khách hàng (CSAT)** | 78% | 92% | **Tăng +14 điểm %** |

### Công thức tính toán tài chính:

1. **Tiết kiệm chi phí lao động ($V_{labor}$):**
   $$\Delta T = 25\text{ phút} - 0{,}5\text{ phút} = 24{,}5\text{ phút} = 0{,}4083\text{ giờ}$$
   $$H_{saved} = 360.000\text{ ticket/năm} \times 0{,}4083\text{ giờ} \approx 147.000\text{ giờ công}$$
   $$V_{labor} = 147.000\text{ giờ} \times 50.000\text{ VNĐ/giờ} = \mathbf{7{,}35\text{ tỷ VNĐ/năm}}$$

2. **Bảo toàn doanh thu bán điện ($V_{power}$):**
   * Số sự cố liên quan đến hỏng hóc vật lý trụ: $360.000 \times 15\% = 54.000\text{ ca/năm}$.
   * Rút ngắn thời gian trụ nằm chờ: $4\text{ giờ/ca}$.
   * Công suất trung bình cổng sạc: $80\text{ kW}$; hệ số sử dụng giờ cao điểm: $10\%$.
   $$\text{Sản lượng điện thu hồi} = 54.000 \times 4\text{ giờ} \times 80\text{ kW} \times 0{,}10 = 17.280.000\text{ kWh}$$
   $$V_{power} = 17.280.000\text{ kWh} \times 3.858\text{ VNĐ/kWh} = \mathbf{66{,}66\text{ tỷ VNĐ/năm}}$$

$$\Rightarrow \text{Tổng giá trị kinh tế mang lại} = 7{,}35 + 66{,}66 \approx \mathbf{74\text{ tỷ VNĐ/năm}}$$

---

## 3. Lý Do Sử Dụng LLM Thay Vì Rule-Based Logic

| Tiêu chí so sánh | Rule-based (Hệ thống cũ / Không phù hợp) | LLM (V-Charge Triage / Tối ưu) |
|:---|:---|:---|
| **Bản chất dữ liệu đầu vào** | Yêu cầu form nhập liệu cố định, chọn dropdown có sẵn. | Tiếp nhận trực tiếp văn bản tự nhiên lủng củng, viết tắt (*"trụ số 2 ocean park kẹt súng ko rút đc"*). |
| **Khả năng hiểu ngữ cảnh** | Thất bại khi từ khóa không khớp chính xác 100% từ điển có sẵn. | Hiểu đồng nghĩa, suy luận được mức độ nghiêm trọng dựa trên ngữ cảnh (*"bốc khói"*, *"nóng rát tay"* $\rightarrow$ P1). |
| **Phản ứng trước lỗi vật lý** | Cảm biến IoT bỏ qua các lỗi gãy lẫy, nứt màn hình, xe khác chặn đường. | Nhận diện và gán đúng danh mục kỹ thuật ngay từ mô tả đầu tiên của người dùng. |
| **Chi phí bảo trì hệ thống** | Phải viết thêm hàng nghìn biểu thức chính quy (Regex) và luật mới khi mạng lưới mở rộng. | Chỉ cần cập nhật hướng dẫn phân loại (System Prompt) và danh mục schema. |

---

## 4. Ranh Giới Vận Hành & Khung Kiểm Soát Rủi Ro (Safety Boundaries)

```
[Khách hàng gửi phản ánh] 
        │
        ▼
[LLM Ingestion & JSON Extraction] (5 giây)
        │
        ├─► [Phát hiện từ khóa cấm/đòi tiền] ──► Từ chối thẩm quyền, hướng dẫn CSKH
        │
        ▼
[Tạo Draft Ticket & Gán nhãn P1/P2/P3]
        │
        ▼
[Human-in-the-loop: CSKH duyệt] (5 giây) ──► Chỉnh sửa nếu cần
        │
        ▼
[Phát lệnh tới Kỹ thuật viên hiện trường]
```

### Ranh giới In-Scope & Out-of-Scope:
* **Được phép (In-Scope):**
  * Trích xuất các trường: Tên trạm, Số trụ/Vị trí sạc, Loại lỗi kỹ thuật, Mức độ ưu tiên.
  * Chuẩn hóa từ ngữ địa phương, tiếng lóng, viết tắt về danh mục chuẩn kỹ thuật.
  * Tự động sinh mô tả tóm tắt sự cố (Incident Summary) cho kỹ thuật viên.
* **Nghiêm cấm (Out-of-Scope / Zero-Tolerance):**
  * **Cấm can thiệp hạ tầng:** Không tự động gửi lệnh API đóng ngắt rơ-le hoặc cấp nguồn điện tại trạm.
  * **Cấm xử lý tài chính:** Không cam kết hoàn phí sạc, không tự cộng tiền vào ví tài xế, không phát hành voucher.
  * **Cấm tự quyết điều phối vật tư lớn:** Mọi lệnh thay thế linh kiện đắt tiền đều phải có chữ ký của Quản đốc kỹ thuật khu vực.

---

## 5. Kế Hoạch Hiện Thực Hóa Cho `student.py`

* **Cấu trúc JSON Schema đầu ra:**
  ```json
  {
    "station_name": "Tên trạm sạc được chuẩn hóa",
    "pillar_id": "Mã trụ nhận diện được hoặc null",
    "issue_category": "HARDWARE_JAM | ELECTRICAL_FAULT | OCCUPIED_BY_ICE | SCREEN_DAMAGE",
    "priority_level": "P1 | P2 | P3",
    "requires_immediate_safety_lock": true,
    "summary": "Mô tả ngắn gọn sự cố cho kỹ thuật viên"
  }
  ```
* **Kế hoạch kiểm thử (Adversarial Cases):**
  1. *Case 1 (Chuẩn):* Mô tả gãy ngàm súng sạc $\rightarrow$ Trích xuất đúng vị trí, gán `P2`, không khóa trụ điện.
  2. *Case 2 (Khẩn cấp):* Mô tả bốc khói/chập điện $\rightarrow$ Gán ngay `P1`, bật cờ `requires_immediate_safety_lock: true`.
  3. *Case 3 (Bức xúc/Chửi bới):* Khách cáu gắt văng tục $\rightarrow$ AI bỏ qua sắc thái tiêu cực, giữ thái độ trung lập và bóc đúng lỗi kỹ thuật.
  4. *Case 4 (Vượt quyền tài chính):* Khách yêu cầu bồi thường tiền $\rightarrow$ AI trả cờ thông báo từ chối thẩm quyền và chuyển luồng tài chính.