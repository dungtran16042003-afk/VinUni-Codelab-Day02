# Bằng chứng và phạm vi — xác nhận đúng cổng/sảnh đón Green SM

**Lê Thanh Tùng — 2A202603819.** Kiểm tra nguồn chính thức đến 09/11/2026, Việt Nam. Đây là nghiên cứu phục vụ bài lab; chưa có phỏng vấn hoặc dữ liệu vận hành nội bộ.

## Dữ kiện đã xác minh

| Nguồn chính thức | Nội dung được hỗ trợ và giới hạn |
|---|---|
| [Green SM: Trung tâm giải đáp, mục 2.1](https://www.greensm.com/vn-vi/helps) | Khách đã có thể nhập/xác nhận điểm đón hoặc dùng GPS. Sau khi ghép, khách có thể gọi hoặc nhắn tài xế trong ứng dụng để xác nhận điểm đón và chi tiết khác. Nguồn không cung cấp tỷ lệ nhầm cổng, số cuộc gọi hoặc hiệu quả của luồng hiện có. |
| [Green SM: cập nhật tính năng 3.15.1, 08/09/2026](https://www.greensm.com/vn-vi/news/cap-nhat-cac-tinh-nang-moi-tren-ung-dung-tai-xe-green-sm) | Bài viết trong bối cảnh **Green SM Bike** nêu từ 11/09/2026 khách có thể đổi điểm đón sau khi tài xế nhận chuyến và đang tới đón. Không dùng nguồn này để khẳng định đã kiểm chứng cùng phạm vi cho toàn bộ Car hoặc mọi thị trường. |
| [Green SM: Điều khoản chung Hợp đồng dịch vụ, mục 2.1.5 và 2.2.8](https://www.greensm.com/vn-vi/terms-policies/service-agreement) | Điều khoản cho dịch vụ **ô tô** mô tả điểm đón/trả là gần đúng; tài xế có thể chọn điểm gần đó nếu xác định hợp lý rằng điểm ban đầu nguy hiểm hoặc bị cấm. Điều khoản cũng có bước xác nhận điểm đón và thông báo thời gian dự kiến. Đây là mô tả điều khoản doanh nghiệp, không phải xác nhận một điểm cụ thể được phép dừng đón. |

**Không kết luận:** Green SM chưa có dữ liệu cổng/sảnh, chưa có xử lý ngữ nghĩa phía backend hoặc chưa giải quyết vấn đề này. Nguồn công khai trên không đủ để xác định năng lực nội bộ đó.

## Phần đề xuất mới và giả thuyết cần đo

Đề xuất cá nhân là **làm rõ mô tả tự nhiên thành một điểm gặp có mã định danh đã xác minh**: cổng sau/cổng hông, sảnh nào, mặt tòa nhà hướng ra đường nào, cùng bên hay đối diện đường và mốc nhận biết. Không coi việc thêm nút đổi điểm đón hoặc chat là tính năng mới.

Giả thuyết: với một số tòa nhà nhiều lối vào, tọa độ gần đúng và mô tả thiếu rõ ràng khiến khách và tài xế chưa thống nhất cùng một điểm gặp. Chọn và xác nhận đúng cổng/sảnh có thể giảm vòng gọi lại, đi nhầm và thời gian làm rõ. **Chưa có baseline chứng minh tần suất hoặc mức tổn thất tại Green SM.** Theo suy luận thiết kế, một tọa độ đơn lẻ cũng không tự chứng minh tên cổng, phía đường hay quyền tiếp cận của xe.

## Dữ liệu và vòng xác nhận tối thiểu

Registry điểm đón cần có `entrance_id`, tòa nhà, tên/biệt danh cổng–sảnh, tọa độ, mặt đường/đoạn đường và phía đường, loại xe tiếp cận được, điều kiện dừng đón/giờ mở cửa, mốc nhận biết, nguồn xác minh và thời điểm cập nhật. Thông tin thiếu hoặc hết hạn phải được đánh dấu; tọa độ GPS của khách chỉ là một tín hiệu hỗ trợ.

Luồng MVP đề xuất: lấy tập điểm ứng viên đã xác minh → đọc lời mô tả khách → chỉ ra ứng viên phù hợp hoặc hỏi một câu phân biệt → khách xác nhận điểm có tên/mốc rõ → gửi cùng một thẻ điểm gặp cho khách và tài xế. Nếu không có điểm hợp lệ hoặc mô tả còn mâu thuẫn, quay lại liên hệ thủ công. “Check-in” ở đây là khách xác nhận **điểm hẹn**, không phải xác nhận tài xế đã tới, đã đón đúng người hoặc đã bắt đầu chuyến.

Ví dụ hoàn toàn tổng hợp: “Em ở cửa sau gần hiệu thuốc” chưa đủ nếu registry có hai cửa phía sau. Hệ thống hỏi khách đang ở mặt đường A hay đường B; chỉ sau khi xác nhận mới chọn ID tương ứng. Không tự dịch chuyển pin sang cổng gần nhất rồi coi là đúng.

## AI, rule và cách kiểm chứng

LLM phù hợp để hiểu cách gọi cổng/sảnh tiếng Việt, phủ định, mốc nhận biết và câu diễn đạt thiếu dấu; đối chiếu với **tập ứng viên được cấp**, trích lý do và soạn câu hỏi ngắn. Lời nhắn khách là dữ liệu, không được ghi đè registry hoặc quy tắc hệ thống. LLM không tạo cổng, tọa độ, quyền tiếp cận, đường đi hay tính hợp pháp của điểm đón.

Map/geospatial xử lý khoảng cách và quan hệ đường; rule kiểm tra ID, tính mới dữ liệu, loại xe, điều kiện đón và trạng thái xác nhận. Khách xác nhận điểm hẹn; tài xế đánh giá điều kiện thực tế. Một điểm được khách gọi tên chưa tự động trở thành điểm xe có thể đón. Không suy ra chỉ dẫn sang đường hoặc lối đi bộ an toàn từ mô tả ngôn ngữ.

Đối chứng tối thiểu: form chọn cổng/sảnh + rule so với cùng form có LLM hỗ trợ. Đo độ chính xác chọn điểm trên ca có đáp án chuẩn, tỷ lệ hỏi lại đúng lúc khi mơ hồ, thời gian thống nhất điểm gặp, số lần gọi/nhắn bổ sung và tỷ lệ đổi cổng/đón thất bại. Đọc thời gian đón cùng các ca hủy để tránh loại mất những ca khó. Cần log được phép dùng và xác minh thực địa cho pilot; dữ liệu tổng hợp chỉ kiểm chứng chức năng, chưa chứng minh hiệu quả kinh doanh. Nếu form/rule đạt kết quả tốt hơn với ít chi phí hơn, chọn phương án đó.
