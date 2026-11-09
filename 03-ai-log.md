# AI Log & Reflection — Lê Thanh Tùng, 2A202603819

Branch: `le-thanh-tung-2A202603819`. Tài liệu đồng soạn với Codex từ các thao tác trong phiên làm bài; các yêu cầu được tóm tắt, không phải bản chép nguyên văn. Không có phỏng vấn, khảo sát thực địa hoặc dữ liệu nội bộ Xanh SM được giả thành trải nghiệm đã thực hiện.

## 1. AI giúp gì?

| Bước | Yêu cầu thực tế và cách dùng AI | Kết quả kiểm chứng |
|---|---|---|
| Đọc đề | Đọc README/worksheet, phân biệt branch/code cá nhân với tài liệu nhóm. | Kiểm tra file và quy tắc không merge code vào `main`. |
| Chọn problem | Ban đầu xét sự cố pin, rồi nghiên cứu cơ hội lớn và các vấn đề cấp thiết. | Lưu các memo trong `research/`, phân biệt dữ kiện với giả thuyết; không gọi một gap là chưa được hãng giải quyết. |
| Chốt phạm vi | Người dùng chọn điểm check-in mơ hồ, cổng sau/cổng phụ/mặt đường cụ thể. | Đề tài cuối là đúng điểm đón; không tiếp tục dùng tối ưu đội xe làm đề tài chính. |
| Lượng hóa | Người dùng yêu cầu số học về thời gian, tiền và UX để điền bảng. | Baseline 180s, target 60s, 1.000 chuyến/ngày là giả định; tính lại bằng script, không gọi đó là số liệu thực. |
| Prototype | Dùng LLM hiểu mô tả và hỏi lại, catalog/rule cấp dữ liệu vị trí, khách/tài xế xác nhận. | Test chặn tọa độ bịa, cổng đóng, thay phiên bản và bỏ xác nhận; live case lưu riêng. |
| Git | Người dùng yêu cầu tạm dừng push, sau đó cho phép hoàn thiện và push. | Kiểm tra đúng branch/remote và chỉ xuất bản bài cá nhân sau khi kiểm tra xong. Không đẩy `main`. |

## 2. AI sai hoặc chưa đủ ở đâu?

**Model có trong danh sách chưa chắc sinh nội dung được.** Starter dùng 2.5 Flash; `models.list()` vẫn liệt kê nhưng generate trả 404 với tài khoản hiện tại. 3.8 tiếp tục lỗi deadline, trong khi 3.1 Flash Lite gọi được. Đã cập nhật cấu hình, thêm kiểm tra contract SDK và lưu [bằng chứng API](artifacts/api-compatibility.md). Không báo các lời gọi thất bại là thành công.

**Các số tiền có thể bị gọi sai bản chất.** Phải tách giá trị thời gian 50 triệu/tháng với tiết kiệm chi tiền thực; 36 triệu tiền cước với doanh thu thuần/lợi nhuận của nền tảng. Khoản 36 triệu còn phụ thuộc mọi chuyến tránh hủy đều hoàn thành. [Script](tools/calculate_impact.py) không cộng các khoản thành ROI.

**Tên cổng và tọa độ không thể do LLM tự xác minh.** Dữ liệu tổng hợp có `verified=true` chỉ mô phỏng backend. Model chọn id; backend mới cấp cổng/đường/phía đường/tọa độ. Người dùng tự ghi một JSON không làm nó trở thành dữ liệu đáng tin. Prototype không khẳng định đã nâng độ chính xác GPS ngoài thực địa.

**Thêm AI không đồng nghĩa cải thiện UX.** Bắt người dùng trả lời quá nhiều có thể tăng công thao tác. Đã bổ sung đối chứng dropdown cổng không AI, đo cả vòng hỏi lại và ca hủy. Không giữ LLM nếu rule/form đạt kết quả tương đương.

## 3. Prompt và ranh giới đã làm rõ

System prompt yêu cầu: chỉ chọn điểm trong catalog, luôn là nháp cần xác nhận, hỏi lại khi “cổng phụ” chưa rõ, không tự đổi cổng đóng sang cổng khác, không tự cho khách băng đường, không bịa phía đường chưa có. Tọa độ và trạng thái đã xác nhận bị cấm trong output model.

Ba prompt tấn công trong [code](starter-code/pickup_checkin.py): yêu cầu bịa cổng VIP và tọa độ; yêu cầu bỏ xác nhận dù mô tả cổng sau hợp lệ; ép chọn cổng dịch vụ đang đóng. Các control cases kiểm tra nghĩa cụ thể, mơ hồ và phía đường đối diện.

Một model trả JSON hợp lệ chưa chứng minh ngữ nghĩa đúng: live harness còn đối chiếu id với đáp án fixture, và code vẫn đòi hỏi xác nhận của khách/tài xế. Những xác nhận này mới mô phỏng bằng sự kiện boolean, chưa phải hệ thống production có auth/chống replay.

## 4. Bằng chứng và giới hạn

- [Pytest](artifacts/pytest.txt): **64 test offline đạt** (30 check-in, 34 starter), có mock SDK, không phải kết quả Gemini thật.
- [Pickup live](artifacts/pickup-gemini-results.json): **7/7 case đạt** bằng `gemini-3.1-flash-lite`; log có timestamp, tình huống, output, id, trạng thái và thời gian gọi. Tất cả địa điểm là tổng hợp.
- [Bài starter](artifacts/gemini-results.json): kết quả ranh giới pin của bài mẫu, tách khỏi đề tài check-in.
- [Autograder](artifacts/autograder.txt): kiểm tra nguyên bản của giảng viên; không suy thành điểm rubric nội dung hoặc hiệu quả người dùng.
- [Impact](artifacts/impact-scenario.json): kết quả số học của các tham số giả định, không phải đo A/B.
- Sơ đồ vẽ bằng Pillow, thời gian được gắn nhãn giả định, có kiểm tra trực quan.

## 5. Reflection

Bài học chính là tách đúng loại bằng chứng: nguồn công khai xác nhận tính năng đã có; test mock kiểm tra code; lời gọi thật kiểm tra model trên fixture; thử nghiệm khách/tài xế mới kiểm tra tác động vận hành. Một loại bằng chứng không thay thế loại khác.

AI hữu ích khi giúp chuẩn hóa và phản biện nhanh, nhưng người làm bài vẫn cần kiểm tra đơn vị tính, phạm vi nguồn và dữ liệu. Kết luận NOT YET cho vận hành là phù hợp vì chưa có catalog thật hoặc thử nghiệm người dùng. Bản này cần người học đọc, hiểu và có thể giải thích các giả định, policy và code trước khi trình bày.

Khóa Gemini chỉ nằm trong `.env` bị Git bỏ qua; token GitHub dùng để xác thực tạm thời và không nằm trong bài nộp. Nhánh cá nhân giữ toàn bộ bài để trưởng nhóm review.
