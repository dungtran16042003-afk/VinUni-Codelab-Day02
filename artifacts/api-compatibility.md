# Bằng chứng kiểm tra model — đã loại thông tin xác thực

Các kết quả dưới đây đến từ lời gọi thật trong phiên làm bài, không phải output mẫu của worksheet. Không lưu khóa hoặc URL có thông tin xác thực.

| Phép thử | Kết quả quan sát | Kết luận có thể rút ra |
|---|---|---|
| `models.list()` | Có các tên 2.5 Flash, 3.8 Flash và 3.1 Flash Lite. | Chỉ chứng minh endpoint liệt kê được model, chưa chứng minh generate được. |
| 2.5 Flash, một case với cấu hình đầy đủ | HTTP 404, `NOT_FOUND`; thông báo model không còn khả dụng cho người dùng mới, đề nghị 3.8 Flash. | Không thể dùng cấu hình 2.5 của đề với tài khoản hiện tại. |
| 3.8 Flash, deadline 8 giây | HTTP 400, `INVALID_ARGUMENT`; yêu cầu deadline tối thiểu 10 giây. | Deadline 8 giây không hợp lệ. |
| 3.8 Flash, deadline 12 rồi 25 giây | HTTP 504, `DEADLINE_EXCEEDED`. | Tăng deadline vượt mức tối thiểu vẫn chưa giải quyết được. |
| 3.8 Flash, chỉ yêu cầu trả OK, deadline 60 giây | HTTP 504 sau **58,74 giây**. | Lỗi vẫn xảy ra khi bỏ schema và prompt dài; không đủ bằng chứng quy lỗi cho schema. |
| 3.1 Flash Lite, cùng lời gọi tối thiểu | Trả lời `OK.` sau **36,56 giây**. | Có thể sinh nội dung với model này, nhưng độ trễ có thể vượt timeout autograder. |
| 3.1 Flash Lite, case pin 2% và trạm 8 km với schema/validator đầy đủ | Trả `dispatch_mobile_charger`, giữ nhãn nháp và yêu cầu duyệt, station id null. | Đường gọi thật của prototype hoạt động với model này cho case đã thử. |

**Cấu hình cuối:** `gemini-3.1-flash-lite`, deadline mỗi lời gọi 120 giây; tối đa 3 lời gọi độc lập đồng thời. Kết quả bộ thử cuối nằm trong [gemini-results.json](gemini-results.json), gồm thời gian từng case. Không suy rộng một case thành độ an toàn của toàn bộ hệ thống.
