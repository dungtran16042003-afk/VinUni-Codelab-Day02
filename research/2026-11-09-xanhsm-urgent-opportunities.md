# Sáu cơ hội Xanh SM để chọn lại — mức cấp thiết và phần AI có thể làm tốt

- **Người làm:** Lê Thanh Tùng — **MSSV:** 2A202603819.
- **Phạm vi nguồn:** Việt Nam, kiểm tra đến 09/11/2026, Asia/Ho_Chi_Minh. Dùng nguồn chính thức Green SM/Xanh SM và Vingroup.
- **Mục đích:** Tìm thêm lựa chọn ngoài cân bằng cung–cầu và lịch sạc; không mặc định giữ đề xuất trước. Đây là discovery từ nguồn công khai, chưa có phỏng vấn, dữ liệu nội bộ hay kết quả thử nghiệm.

## 1. Kết luận có thể nói chắc đến đâu?

**Chưa có căn cứ để gọi cả sáu mục là những vấn đề Xanh SM “chưa giải quyết”.** Nhiều mục đã có tính năng hoặc quy trình xử lý. Cơ hội sản phẩm nằm ở chất lượng, tốc độ và độ chính xác của phần việc còn lại, nhưng phải xác minh bằng log và người vận hành.

Ba lựa chọn đáng khảo sát trước:

1. **Rút ngắn xác thực và cập nhật báo cáo đường thay đổi:** nguồn rất mới, nghiệp vụ cụ thể, ảnh hưởng trực tiếp hành trình; AI xử lý sự trùng lặp và diễn đạt đa dạng tốt hơn một nút báo cáo bổ sung.
2. **Chuẩn bị hồ sơ giải trình tài xế đủ chứng cứ trước hạn:** áp lực thời gian và hậu quả vận doanh được nêu rõ; phù hợp nhất nếu bài lab cần chứng minh giá trị LLM bằng đầu vào/đầu ra văn bản.
3. **Đối soát ngoại lệ thanh toán và hoàn tiền:** giá trị gắn với tiền của khách và công xử lý; lõi phải là dữ liệu giao dịch và rule, AI chỉ hỗ trợ chứng từ/diễn giải hoặc xếp ưu tiên ngoại lệ.

Đây là **đánh giá ưu tiên của người nghiên cứu**, không phải thứ hạng tổn thất hay mức cấp thiết do doanh nghiệp công bố. Chưa có số liệu để nói ứng viên nào gây thiệt hại lớn nhất.

## 2. Thang bằng chứng

| Mức | Ý nghĩa | Giới hạn khi dùng chữ “chưa xử lý” |
|---|---|---|
| **A — Sự việc đã ghi nhận** | Nguồn chính thức xác nhận tình huống đã xảy ra ở thời điểm/phạm vi cụ thể. | Sự việc quá khứ không chứng minh còn tiếp diễn ngày 09/11/2026. Chỉ gọi “đang tồn đọng” nếu có bằng chứng hiện tại về tồn đọng. |
| **B — Áp lực hoặc điểm lỗi của quy trình được mô tả** | Tài liệu nêu deadline, trường hợp sai/thiếu, hậu quả hoặc nhóm hỗ trợ cụ thể. | Chứng minh đây là tình huống nghiệp vụ được dự liệu/xử lý; không chứng minh tỷ lệ lỗi hoặc quy trình hiện đang kém. |
| **C — Khoảng trống cần kiểm chứng** | Giả thuyết rằng một bước còn chậm, sai, thiếu liên kết hoặc chưa được tự động hóa đủ. | Không được đổi “chưa tìm thấy công bố” thành “hãng chưa có chức năng”. |

Với sáu ứng viên bên dưới, **phần cải tiến đề xuất đều ở mức C**. Mức A/B chỉ mô tả sức mạnh bằng chứng về tình huống nền. Các workflow, AI, KPI và phạm vi MVP bên dưới là thiết kế đề xuất, không phải mô tả hệ thống nội bộ đã được quan sát.

## 3. So sánh nhanh

| # | Bài toán để chọn | Bằng chứng nền | Cấp thiết về nghiệp vụ | AI thực sự hữu ích ở đâu? | Khả thi lab |
|---|---|---|---|---|---|
| **1** | Xác thực/cập nhật báo cáo bản đồ nhanh hơn | **B, rất mới:** thông báo 05/11, tính năng từ 26/10/2026 | Đường cấm, ngập, chỉ dẫn sai có thể ảnh hưởng hành trình hiện tại; quy mô ảnh hưởng chưa đo | Gom cùng sự kiện, trích phạm vi/điều kiện, xếp thứ tự cần người kiểm tra | **Tốt** với báo cáo tổng hợp và bản đồ mô phỏng |
| **2** | Giải trình tài xế đủ chứng cứ trước hạn | **B, mới:** quy định 10/09 và cập nhật riêng 27/10/2026 | Có hạn phản hồi và khả năng tạm dừng phát cuốc | Trích timeline, liên kết bằng chứng, phát hiện thông tin thiếu/mâu thuẫn | **Rất tốt** cho LLM có kiểm soát |
| **3** | Đối soát ngoại lệ thanh toán/hoàn tiền | **B:** các mục FAQ; đã có auto-refund ở một phương thức | Liên quan tiền của khách; chưa có volume, số tiền treo hay tuổi ticket | Đọc chứng từ, liên kết nội dung khiếu nại với giao dịch, tóm tắt chứng cứ | **Tốt**, nhưng SQL/rule là lõi |
| **4** | Handoff đúng chủ xử lý khi sự cố vượt nhiều kênh | **B, rất mới:** hướng dẫn hỗ trợ 05/11/2026 | Sự cố phương tiện, pin, chuyến và thu nhập có thể cần các chủ xử lý khác nhau | Tách nhiều vấn đề trong một lời báo và chuẩn bị gói bàn giao đủ dữ liệu | **Tốt**, cần chứng minh hơn menu hỗ trợ |
| **5** | Phiếu bảo dưỡng hợp lệ ngay lần gửi đầu | **B:** thông báo 18/06/2026 nêu hậu quả nhập sai/thiếu | Xe đã bảo dưỡng nhưng hồ sơ không được ghi nhận có thể ảnh hưởng vận doanh | OCR/trích mã, kiểm tra ảnh và đối chiếu với hồ sơ xưởng | **Rất tốt**, nhưng scope nhỏ hơn và có phương án tích hợp trực tiếp tốt hơn |
| **6** | Khép vòng xử lý thiết bị/tín hiệu S2S không dùng được | **A lịch sử:** cảnh báo 27/05/2025; tình trạng hiện tại chưa xác minh | Hậu quả tiềm năng nghiêm trọng; chưa biết mức tồn đọng hiện nay | Phân biệt che/mờ/hỏng tín hiệu và gom cảnh báo cho người xác minh | **Khó hơn**, dễ trùng S2S hiện có |

Mức “cấp thiết” ở đây là đặc tính của workflow hoặc hậu quả tiềm năng, không phải bằng chứng doanh nghiệp đang thất bại. Không dùng bảng để tự suy ra ROI.

## 4. Ứng viên 1 — Từ phản ánh đường thay đổi đến bản đồ được cập nhật đúng

**Dữ kiện và phần đã có.** Thông báo 05/11/2026 giới thiệu “Đóng góp bản đồ”, triển khai từ 26/10 cho tài xế 2 bánh/4 bánh toàn quốc. Nguồn nêu dẫn đường sai, đường cấm, thi công, đường mới, ngập và kẹt xe; báo cáo đã được hệ thống kiểm tra/xác thực trước khi đủ điều kiện cập nhật. Tài xế được yêu cầu báo ngay tại vị trí xảy ra vấn đề. [Green SM: Đóng góp bản đồ](https://www.greensm.com/vn-vi/news/trien-khai-tinh-nang-dong-gop-ban-do-bac-tai-xanh-di-toi-dau-ban-do-green-sm-chuan-toi-do).

**Gap cần xác minh.** Có bao nhiêu báo cáo cùng một sự kiện nhưng khác cách viết? Thời gian từ báo cáo đầu tiên đến xác thực/cập nhật là bao lâu? Thông tin tạm thời có được hết hạn đúng lúc? **Chưa biết** các bước này đã có mô hình hay tự động hóa đến mức nào. Không làm lại nút báo cáo.

**Workflow MVP đề xuất.** Một nhóm quản trị bản đồ trong một quận nhận báo cáo có vị trí/thời gian → gom theo đoạn đường và chiều đi → AI trích loại sự kiện, loại xe, khung giờ, chứng cứ và điều chưa rõ → xếp hàng cần xác thực → nhân viên xác nhận với nguồn có thẩm quyền → cập nhật hoặc bác bỏ, có thời điểm kiểm tra lại/hết hạn. Ví dụ tổng hợp: hai báo cáo “cấm ô tô 7–9h” và “xe máy vẫn qua được” không được gộp thành “cấm mọi xe cả ngày”.

**AI so với rule.** Geofence, timestamp, quyền cập nhật và thời hạn hết hiệu lực dùng rule. Baseline là form có cấu trúc + gom gần nhau theo không gian/thời gian. NLP/LLM đáng thử khi cần hiểu mô tả tiếng Việt, gộp báo cáo khác cách diễn đạt và nhận ra mâu thuẫn; phải chỉ ra câu/ảnh làm căn cứ. Không cho LLM tự xác nhận một tuyến đường hợp pháp hoặc mở đường chỉ vì không còn báo cáo.

**KPI và dữ liệu.** P50/P90 từ báo cáo đến quyết định xác thực; số sự kiện được xác thực đúng trên giờ người kiểm tra; precision của cụm và trường “phạm vi cấm”; tỷ lệ cập nhật sai hoặc hết hạn sai. Theo dõi thêm số hành trình bị chỉ sai ở đoạn đã xử lý, nếu log cho phép. Cần báo cáo gốc, tọa độ/chiều đường, timestamp, bằng chứng đối chiếu và lịch sử quyết định. Dữ liệu tổng hợp chỉ kiểm thử logic, chưa chứng minh giảm đường vòng thật.

**Đánh giá:** Ưu tiên số 1 nếu muốn vấn đề gần vận hành thực và AI có công việc rõ. Gate trước pilot là bằng chứng có độ trễ/trùng lặp đáng kể mà cách đơn giản chưa xử lý tốt.

## 5. Ứng viên 2 — Hồ sơ giải trình đủ thông tin, không bị lỡ hạn vì thiếu chứng cứ

**Dữ kiện và phần đã có.** Thông báo 10/09/2026 áp dụng tính năng xác minh cho các nhóm tài xế toàn quốc, nêu thời hạn hai giờ, tạm dừng phát cuốc nếu chưa phản hồi và tiếp tục phát cuốc khi giải trình xong. Đã có thông báo, luồng phản hồi và hỗ trợ của Đội xe/hotline. [Green SM: quy trình ngày 10/09](https://www.greensm.com/vn-vi/news/trien-khai-tinh-nang-tam-dung-nhan-chuyen-de-xac-minh-thong-tin-1-2).

**Scope cập nhật phải giữ riêng.** Bài 27/10 quy định từ 24/10/2026 cho **Bike Platform tại TP.HCM**: hai giờ **không tính thời gian đang thực hiện đơn hàng**, có kênh Trung tâm hỗ trợ/Tài xế Thủ Lĩnh. Không khái quát ngoại lệ đồng hồ này cho mọi nhóm toàn quốc. [Green SM: cập nhật thời hạn phản hồi](https://greensm.com/vn-vi/news/cap-nhat-thoi-han-phan-hoi-tren-ung-dung-tai-xe-green-sm).

**Gap cần xác minh.** Tỷ lệ giải trình thiếu thông tin, số lần bị yêu cầu bổ sung và phút không được phát cuốc do gửi trễ là bao nhiêu? Việc đọc/tổng hợp chứng cứ đã được hỗ trợ như thế nào? Nguồn quy định không chứng minh tài xế đang bị xử oan hoặc hệ thống chưa có trợ lý.

**Workflow MVP đề xuất.** Chọn đúng phạm vi Bike Platform TP.HCM → tài xế mở một yêu cầu xác minh → backend lấy mã chuyến, thời điểm và chính sách đúng phiên bản → AI trích timeline từ lời trình bày/ảnh, đánh dấu câu nào là lời khai và dữ kiện nào đã xác minh → chỉ hỏi phần còn thiếu → tài xế kiểm tra, xác nhận và gửi → người xử lý xem bản đối chiếu có dẫn chứng. Mục tiêu là hồ sơ dễ kiểm tra, không tự soạn một câu chuyện để “qua vi phạm”.

**AI so với rule.** Đồng hồ hai giờ, trừ khoảng đang chạy chuyến, nhắc hạn và trường bắt buộc phải dùng rule/state machine. LLM hữu ích khi lời khai tự do, ảnh và mốc thời gian phân tán; nên so với form/checklist. Không tự kết luận lỗi, xử phạt, gỡ hạn chế hay bịa chứng cứ. Việc nhận giải trình và quyết định vụ việc phải được ghi log riêng.

**KPI và dữ liệu.** Tỷ lệ hồ sơ đủ điều kiện xem xét ngay lần đầu; số lượt hỏi bổ sung; thời gian tài xế chuẩn bị và nhân viên kiểm tra; tỷ lệ nộp đúng hạn theo đồng hồ đúng policy; phút bị dừng phát cuốc do chưa phản hồi. Đánh giá cả lỗi trích xuất/mâu thuẫn bị bỏ sót và không khuyến khích gửi một hồ sơ rỗng chỉ để đạt deadline. Cần thông báo, trạng thái chuyến, nội dung giải trình và nhãn đánh giá của người có nghiệp vụ; lab dùng tình huống tổng hợp, chưa đo công bằng ngoài thực tế.

**Đánh giá:** Lựa chọn tốt nhất nếu cần một MVP LLM có đầu vào/đầu ra và phép so sánh rõ. Giá trị lớn hơn “soạn tin nhanh” chỉ được xác nhận khi giảm vòng bổ sung hoặc thời gian gián đoạn mà không giảm chất lượng xác minh.

## 6. Ứng viên 3 — Làm rõ ca tiền đã trừ, trả hai lần hoặc hoàn tiền chưa khớp

**Dữ kiện và phần đã có.** Trung tâm giải đáp liệt kê các mục chuyến hủy vẫn trừ tiền, bị tính cước hai lần, đã trả tiền mặt cho chuyến cashless và trả nhiều hơn giá ban đầu; có luồng tạo yêu cầu trong ứng dụng. Việc có mục FAQ là bằng chứng tình huống được hãng hỗ trợ, không phải thống kê lỗi thực tế. [Green SM: Trung tâm giải đáp, mục 3.6–3.9 và 6.4](https://www.greensm.com/vn-vi/helps).

Phương thức liên kết ngân hàng nội địa đã được công bố có tự động hoàn tiền khi hủy chuyến/không tìm thấy tài xế. Vì vậy không đề xuất “xây auto-refund đầu tiên”. [Green SM: liên kết ngân hàng nội địa, 15/10/2025](https://www.greensm.com/vn-vi/news/xanh-sm-them-phuong-thuc-thanh-toan-lien-ket-ngan-hang-noi-dia).

**Gap cần xác minh.** Các ca ngoại lệ nào vẫn cần đối soát giữa trạng thái chuyến, ledger, nhà cung cấp thanh toán và lời khai trả tiền mặt? Tỷ lệ/tuổi ngoại lệ và số tiền bị ảnh hưởng chưa có trong nguồn công khai. Không coi khoản tạm giữ/ủy quyền thẻ là khoản đã ghi nợ cuối cùng.

**Workflow MVP đề xuất.** Một nhân viên payments mở ticket → hệ thống ghép đúng request/trip/transaction ID → rule phân loại authorized/captured/reversed/refunded và số tiền → OCR/LLM đọc chứng từ cùng lời báo, chỉ phần chưa khớp → hiển thị timeline và bộ chứng cứ → nhân viên quyết định bước kiểm tra/hoàn tiền theo thẩm quyền. Một giao dịch phải có cơ chế chống xử lý lặp, dù khách gửi nhiều ticket.

**AI so với rule.** SQL, phép cộng tiền, khóa duy nhất, state machine và callback thanh toán là lõi. Không dùng LLM để tính số tiền hoàn. AI chỉ đáng dùng ở chứng từ không đồng nhất, mô tả tự do hoặc xếp ưu tiên ca bất thường khi có nhãn đủ tốt; nếu API ghép ID giải quyết được thì không cần AI cho bước đó.

**KPI và dữ liệu.** Thời gian từ tiếp nhận đến xác định đúng trạng thái; thời gian đóng ngoại lệ; tỷ lệ tái liên hệ; tỷ lệ ghép nhầm/hoàn trùng; số tiền và tuổi ngoại lệ. Cần ledger, sự kiện cổng thanh toán, trạng thái chuyến và chứng từ được phép dùng. Phân tách thời gian xử lý nội bộ với thời gian ngân hàng ghi có; một demo không kiểm chứng được luồng ngân hàng thật.

**Đánh giá:** Giá trị kinh doanh dễ diễn giải nếu có dữ liệu ngoại lệ. Có thể là bài dữ liệu/rule rất tốt mà phần AI nhỏ, và đó vẫn là kết luận đúng.

## 7. Ứng viên 4 — Bàn giao sự cố đủ ngữ cảnh giữa xe/pin và chuyến/thu nhập

**Dữ kiện và phần đã có.** Thông báo 05/11/2026 cho Green SM Bike tách hỗ trợ phương tiện/pin ở VinFast, chuyến/cước/tình huống khẩn cấp ở Green SM, thu nhập/ví/thưởng qua Trung tâm hỗ trợ, cùng thông tin bảo hiểm. Hãng cũng nhắc chuẩn bị thông tin đăng ký, xe và sự cố. [Green SM: cập nhật kênh hỗ trợ Bike](https://www.greensm.com/vn-vi/news/cap-nhat-kenh-ho-tro-danh-cho-bac-tai-green-sm-bike).

**Gap cần xác minh.** Nhiều chủ xử lý không tự động đồng nghĩa hỗ trợ bị phân mảnh. Cần đo có bao nhiêu ca chuyển sai, phải kể lại hoặc đóng ở một đội nhưng phần việc khác chưa xong. Ví dụ giả định: lỗi đổi pin làm hỏng một chuyến và kéo theo thắc mắc thu nhập; đây là tình huống thiết kế, chưa phải case quan sát được.

**Workflow MVP đề xuất.** Nhân viên tiếp nhận một ca Bike có nhiều vấn đề → AI tách các phần việc và gắn bằng chứng → rule chọn chủ xử lý theo danh mục chính thức → dựng một gói bàn giao gồm mã xe/chuyến, sự kiện, dữ liệu còn thiếu và người chịu trách nhiệm → con người duyệt chuyển → theo dõi trạng thái từng phần dưới một hồ sơ liên kết. Không tự nhận đã tích hợp được hệ thống VinFast/Green SM.

**AI so với rule.** Menu hỗ trợ, bảng định tuyến và SLA dùng rule. AI có ích khi một lời báo chứa nhiều vấn đề/mô tả không theo mẫu, hoặc cần tóm tắt hồ sơ dài; phải thử đối chứng với form và macro. Không làm chatbot hỏi đáp chung, không để phân loại AI giữ một báo cáo khẩn cấp trong hàng đợi thông thường.

**KPI và dữ liệu.** Tỷ lệ định tuyến đúng lần đầu do người kiểm tra xác nhận; số lần chuyển đội/khách kể lại; thời gian đến đúng chủ xử lý; thời gian xử lý trọn ca; tỷ lệ phần việc chưa đóng. Cần lịch sử chuyển và kết quả thực, không chỉ nhãn phân loại. Lab mô phỏng được handoff; giá trị thực phụ thuộc quyền tích hợp giữa các bên.

**Đánh giá:** Đáng làm khi discovery chứng minh chuyển qua lại là tổn thất lớn. Nếu chỉ có vài nhóm rõ ràng, menu tốt có thể đủ và rẻ hơn AI.

## 8. Ứng viên 5 — Xe đã bảo dưỡng nhưng hồ sơ chưa được ghi nhận

**Dữ kiện và phần đã có.** Nguồn 18/06/2026 cho Bike công bố nhắc hạn, xác nhận bảo dưỡng trực tuyến; yêu cầu mã phiếu 22 ký tự, đơn vị xưởng phù hợp và ảnh rõ. FAQ nêu thông tin sai/thiếu hoặc ảnh không xác minh được sẽ không ghi nhận, có thể khiến xe tiếp tục hiện chưa bảo dưỡng và ảnh hưởng vận doanh/chính sách. Có kênh hỗ trợ khi trạng thái chưa đúng. [Green SM: nhắc lịch và xác nhận bảo dưỡng](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-nhac-lich-xac-nhan-bao-duong-tren-ung-dung-bac-tai-xanh-bike).

**Gap cần xác minh.** Tỷ lệ phiếu bị trả lại, thời gian chỉnh sửa và nguyên nhân là gì? Hiện đã có OCR hoặc đồng bộ trực tiếp từ xưởng chưa? Không có căn cứ từ tài liệu này để nói xe thường xuyên hỏng hoặc cần predictive maintenance.

**Workflow MVP đề xuất.** Tài xế chụp phiếu trước gửi → kiểm tra ảnh bị cắt/mờ → OCR lấy mã lệnh, xe, xưởng, ngày → rule kiểm tra định dạng và đối chiếu record xưởng nếu được cấp API → hiển thị điểm không khớp để tài xế sửa hoặc chuyển người xác minh → xác nhận theo quy trình hiện có. Không tự sửa mã mơ hồ thành một mã có thật.

**AI so với rule.** Kiểm tra mã 22 ký tự, danh sách xưởng và trường bắt buộc dùng rule. OCR/vision hữu ích khi đọc phiếu giấy; rule ảnh đơn giản có thể đủ cho mờ/cắt. Nếu xưởng đã có bản ghi điện tử chính xác, đồng bộ trực tiếp tốt hơn yêu cầu tài xế chụp giấy rồi dùng AI đọc lại.

**KPI và dữ liệu.** Tỷ lệ xác nhận hợp lệ lần đầu; số lần gửi lại; tỷ lệ mã OCR đúng tuyệt đối; thời gian xe đã bảo dưỡng còn bị ghi quá hạn; tỷ lệ chấp nhận nhầm phiếu không hợp lệ. Cần phiếu thật được phép dùng và quyết định chuẩn của xưởng/đội vận hành. Phiếu tổng hợp chỉ kiểm tra chức năng, chưa chứng minh giảm gián đoạn thực.

**Đánh giá:** MVP rõ và dễ đánh giá, chứng cứ về cơ chế lỗi khá cụ thể. Quy mô tác động có thể nhỏ hơn bản đồ/giải trình; chưa có volume để so sánh.

## 9. Ứng viên 6 — Thiết bị an toàn có tín hiệu nhưng ca lỗi cần được khép vòng

**Dữ kiện và phần đã có.** S2S được công bố có camera/cảm biến, AI phát hiện bất thường và tín hiệu về Trung tâm điều hành để huy động hỗ trợ. Vì vậy không được nói Xanh SM thiếu hệ thống phát hiện hoặc thiếu luồng ứng cứu. [Vingroup: S2S, 15/04/2025](https://www.vingroup.net/tin-tuc-su-kien/bai-viet/3411/xanh-sm-trang-bi-he-thong-an-toan-vuot-troi-cho-tre-em-phu-nu-nguoi-cao-tuoi-va-tai-xe).

Ngày 27/05/2025, Green SM nêu đã ghi nhận nhiều trường hợp cố tình can thiệp camera và đang rà soát; thông báo chỉ rõ taxi thuộc Depot Hà Nội/TP.HCM, không gồm Bình Dương/Bà Rịa–Vũng Tàu. Đây là **bằng chứng sự việc lịch sử**, chưa chứng minh còn tái diễn hoặc chưa được xử lý vào 09/11/2026. [Green SM: cảnh báo can thiệp S2S](https://www.greensm.com/vn-vi/news/canh-bao-can-thiep-he-thong-giam-sat-an-toan-s2s).

**Gap cần xác minh.** Thiết bị không dùng được được phát hiện và sửa trong bao lâu? Cảnh báo nào là che camera, ảnh mờ tự nhiên, lỗi kết nối hoặc bảo trì? Có ca mở chưa có người nhận hoặc chưa xác nhận sửa không? Các chức năng này có thể đã nằm trong S2S; cần xem hệ thống và log trước khi đề xuất mới.

**Workflow MVP đề xuất.** Tập cảnh báo thiết bị giả lập → rule phát hiện mất heartbeat → mô hình ảnh nhỏ gợi ý che/mờ/lệch khi có dữ liệu được phép → gom cảnh báo cùng xe thành một ca → nhân viên xác minh nguyên nhân và chọn chủ xử lý → chỉ đóng khi có tín hiệu kiểm tra lại đã phục hồi. Đây là quản lý độ sẵn sàng thiết bị và hồ sơ xử lý, không thay thế ứng cứu.

**AI so với rule.** Heartbeat, dedupe, người nhận và thời hạn phải dùng rule/workflow. Vision chỉ đáng thử khi cần phân loại chất lượng tín hiệu mà rule không đủ; không suy ra ý định gian lận từ một khung hình mờ, không tự xử phạt. Không thu thêm camera hành khách chỉ để làm demo; dùng dữ liệu tổng hợp hoặc dữ liệu đã được cho phép đúng mục đích.

**KPI và dữ liệu.** Thời gian từ mất chất lượng tín hiệu đến xác nhận nguyên nhân/khôi phục; tỷ lệ xe có thiết bị dùng được; false alarm trên giờ xe; tỷ lệ ca đóng nhưng kiểm tra lại vẫn lỗi. Cần nhãn nguyên nhân và log kết quả sửa, không chỉ video/cảnh báo. Khó đánh giá thực nếu không có chủ sở hữu S2S và bộ dữ liệu đủ đại diện.

**Đánh giá:** Mức nghiêm trọng tiềm năng cao, nhưng bằng chứng về khoảng trống hiện tại yếu và rủi ro trùng hệ thống lớn. Không chọn chỉ vì “an toàn” nghe cấp bách.

## 10. Những hướng không đưa vào sáu lựa chọn chính

- **Điểm đón/sảnh/cổng:** đáng khảo sát ở mức micro-location, nhưng đã có đổi điểm đón trong tài liệu 3.15.1 và Green Zone; không trình bày “cho đổi điểm đón” như tính năng mới. Nếu làm, phải chứng minh còn tỷ lệ nhầm sảnh/chiều đường cao sau các tính năng đó. [Green SM: cập nhật tính năng Bike 3.15.1](https://www.greensm.com/vn-vi/news/cap-nhat-cac-tinh-nang-moi-tren-ung-dung-tai-xe-green-sm), [Green SM: Green Zone](https://greensm.com/vn-vi/news/green-zone-khu-vuc-don-taxi-dien-green-sm).
- **Đồ bỏ quên:** FAQ có nhóm này nhưng chưa có bằng chứng nguồn gốc về backlog hoặc thất bại phối hợp. Không gọi là vấn đề chưa giải quyết chỉ vì cần nhiều bên liên hệ. [Green SM: Trung tâm giải đáp, mục 2.13](https://www.greensm.com/vn-vi/helps).
- **Dự báo hỏng xe:** chưa có nguồn trong đợt kiểm tra này chứng minh breakdown/downtime đang là pain lớn; không suy ra từ việc có chính sách bảo dưỡng.
- **Dữ liệu trạm/đổi pin không cập nhật:** bản đồ vị trí không chứng minh có hoặc thiếu tồn kho theo thời gian thực; cần kiểm tra API, timestamp và tỷ lệ đi tới nơi nhưng không đổi được. Không chọn thêm một biến thể sạc chỉ để tăng số lượng ý tưởng.

## 11. Cách chọn để AI tạo hiệu quả thật

Trước khi chốt, với mỗi ứng viên cần một chủ quy trình xác nhận vấn đề, một tập ca mẫu có kết quả chuẩn và baseline đủ tốt. Đo theo ba nhóm: **kết quả nghiệp vụ**, **công người dùng**, **lỗi do hệ thống gây ra**. Accuracy mô hình riêng lẻ chưa đủ.

Nếu cần chọn ngay cho Day 02, chọn **ứng viên 1 — xác thực báo cáo đường thay đổi** để có câu chuyện sản phẩm vận hành có nguồn mới và một điểm dùng AI cụ thể; chọn **ứng viên 2 — chuẩn bị hồ sơ giải trình** nếu yêu cầu trọng tâm là LLM. Cả hai bắt đầu bằng bản mẫu có con người duyệt và dữ liệu tổng hợp, sau đó mới xin dữ liệu phù hợp để xác minh tác động.

Không đặt các phần trăm cải thiện giả làm kết quả đã đạt. Chỉ chốt mục tiêu số và cỡ mẫu sau khi đo baseline. Nếu form/rule/tích hợp trực tiếp đạt kết quả tốt hơn với ít chi phí hơn, loại AI khỏi bước đó.
