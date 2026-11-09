# Chọn vấn đề Xanh SM cho Day 02 — AI Product Scoping

- **Người làm:** Lê Thanh Tùng — **MSSV:** 2A202603819.
- **Ngày chốt nguồn:** 09/11/2026, múi giờ Asia/Ho_Chi_Minh.
- **Mục đích:** Chọn một cơ hội có tác động kinh doanh lớn, rồi thu hẹp thành giả thuyết có thể kiểm chứng. Đây là nghiên cứu nguồn công khai cho bài cá nhân; chưa phỏng vấn, chưa có dữ liệu nội bộ, chưa đo baseline.

## 1. Khuyến nghị

Chọn bài toán **đảm bảo đủ xe điện sẵn sàng phục vụ đúng vùng, đúng giờ cao điểm**. Kết quả cần cải thiện là khả năng đáp ứng yêu cầu và đón khách tin cậy. Dự báo nhu cầu, điều chuyển xe và kế hoạch sạc là các cách can thiệp cần kiểm chứng.

**Problem statement đề xuất:** Trong một vùng thí điểm tại Hà Nội vào cao điểm chiều, người phụ trách vận hành cần biết trước nơi nào có nguy cơ thiếu xe đủ điều kiện phục vụ trong 30 phút tới, để chọn điều chuyển xe rảnh hoặc dời một số lượt sạc phù hợp, nhằm tăng tỷ lệ yêu cầu được phục vụ và giảm thời gian đón khách mà không làm giảm thu nhập theo giờ của tài xế.

Đây là **ứng viên ưu tiên cho bài lab**, chưa phải kết luận rằng Xanh SM đang thiếu năng lực điều phối, sạc là nguyên nhân chính của hủy chuyến, hoặc bài toán này gây thiệt hại lớn nhất doanh nghiệp. Không có nguồn đã kiểm tra nào công bố dữ liệu đủ để kết luận các điều đó.

Lý do chọn: kết nối trực tiếp trải nghiệm khách với năng suất đội xe; có thể đo bằng sự kiện chuyến đi và trạng thái xe; có giả thuyết kỹ thuật rõ để so sánh với rule đơn giản. Hướng này mở rộng giá trị so với việc chỉ tiết kiệm vài phút soạn tin hỗ trợ, nhưng phải bắt đầu bằng discovery và mô phỏng thay vì tự nhận đã tìm thấy bottleneck thật.

## 2. Những gì nguồn chính thức xác nhận

Các nguồn doanh nghiệp dưới đây chứng minh **chính sách, tính năng hoặc ưu tiên mà doanh nghiệp công bố**. Chúng không phải kiểm toán độc lập về hiệu quả thực tế.

| Bằng chứng công khai | Điều có thể sử dụng | Điều chưa thể suy ra |
|---|---|---|
| Ngày 11/02/2026, Xanh SM công bố chương trình thưởng nhận và hoàn thành chuyến theo khung giờ tại Hà Nội/TP.HCM dịp Tết; chính sách kèm yêu cầu nhận chuyến, hạn chế hủy và hỗ trợ khách khi chuyến đã ghép không thực hiện được. [Nguồn Vingroup: chương trình giữ chuyến](https://www.vingroup.net/vi/tin-tuc-su-kien/bai-viet/3825/xanh-sm-nang-chuan-giu-chuyen-thuong-lon-cho-bac-tai-nhan-chuyen-deu-dip-tet-2026). | Giữ chuyến và độ ổn định khi nhu cầu cao là ưu tiên vận hành được nêu rõ. | Không có tỷ lệ hủy, phân bố nguyên nhân, chi phí thất bại hoặc mức cải thiện sau chương trình. Không được coi chương trình Tết đã kết thúc là chính sách còn áp dụng ngày 09/11. |
| Thông báo ngày 08/11/2026 gắn ưu đãi sạc với km vận doanh; FAQ định nghĩa km này từ điểm đón đến điểm trả, không gồm quãng đường đón khách. Thông báo khuyến khích vận doanh cao điểm, duy trì nhận/hoàn thành và hạn chế hủy. [Nguồn Green SM: chính sách sạc](https://www.greensm.com/vn-vi/news/cap-nhat-chinh-sach-uu-dai-sac-xe-danh-cho-bac-tai-xanh-green-sm). | Sạc, km có khách và hiệu suất nhận/hoàn thành cùng nằm trong chính sách vận hành hiện hành tại thời điểm nghiên cứu. | Không chứng minh thiếu trạm, hàng đợi sạc dài, hay sạc đang gây mất cung. Quyền lợi có hạn mức và phụ thuộc nhóm tài xế; không được suy rộng mọi tài xế đều được sạc không giới hạn. |
| Ngày 07/11/2026, Green SM công bố chương trình từ 08/11/2026 đến 28/02/2027 gồm ưu đãi cước và hỗ trợ doanh số/phí nền tảng/sạc cho những nhóm tài xế tương ứng. [Nguồn Vingroup: Mùa đông Xanh](https://vingroup.net/tin-tuc-su-kien/bai-viet/10117/green-sm-trien-khai-chuong-trinh-mua-dong-xanh-vi-tuong-lai-xanh-ho-tro-dac-biet-cho-khach-hang-va-tai-xe). | Thu nhập tài xế và tăng hoạt động là các chủ đề doanh nghiệp đang đầu tư. Đây cũng là một thay đổi chính sách cần kiểm soát khi đánh giá pilot. | Dự báo thu nhập tăng trong thông cáo chưa phải kết quả đo. Không chứng minh churn cao hay biên lợi nhuận hiện tại. |
| Bài ngày 12/01/2026 mô tả đầu tư vào back-end, chuẩn hóa thông tin chuyến, hỗ trợ/phản hồi và công cụ thời gian thực cho tài xế. [Nguồn Vingroup: công nghệ và trải nghiệm khách hàng](https://vingroup.net/tin-tuc-su-kien/bai-viet/3781/xanh-sm-nhan-3-giai-thuong-ve-cong-nghe-va-trai-nghiem-khach-hang-xuat-sac-nhat-viet-nam-va-chau-a). | Phải khám phá khả năng hiện có trước khi thiết kế một sản phẩm vận hành bổ sung. | Không được viết quy trình hiện tại là điều phối thủ công, thiếu dashboard hay chưa dùng AI. Giải thưởng không phải bằng chứng về baseline của bài toán đề xuất. |
| Thông báo 23/09/2026 giới thiệu tính năng theo dõi tỷ lệ nhận/hoàn thành, gợi ý và cảnh báo trên Trợ lý Tài xế, với phạm vi nêu rõ là Bike Platform tại Hà Nội theo địa giới cũ. [Nguồn Green SM: theo dõi tỷ lệ vận doanh](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-moi-theo-doi-ty-le-van-doanh-tren-tro-ly-tai-xe). | Một trợ lý theo dõi hiệu suất đã có trong ít nhất phạm vi được công bố; ý tưởng mới phải tránh trùng tính năng. | Không suy rộng tính năng này sang toàn bộ taxi ô tô hoặc coi nó đã giải quyết dự báo cung và lịch sạc. |
| Ngày 15/04/2025, Xanh SM công bố kế hoạch triển khai S2S trên đội taxi cơ hữu, gồm cảm biến/camera, nút khẩn cấp và AI phát hiện bất thường; đối tác Platform được khuyến khích trang bị sau đó. [Nguồn Vingroup: hệ thống S2S](https://www.vingroup.net/tin-tuc-su-kien/bai-viet/3411/xanh-sm-trang-bi-he-thong-an-toan-vuot-troi-cho-tre-em-phu-nu-nguoi-cao-tuoi-va-tai-xe). | An toàn là hướng có sản phẩm và đầu tư công bố sẵn. | Kế hoạch công bố không chứng minh tỷ lệ hoàn tất triển khai, độ chính xác cảnh báo hoặc xu hướng sự cố. |

## 3. So sánh các bài toán có tác động lớn

**Các mức ưu tiên dưới đây là đánh giá định tính của người làm bài**, không phải xếp hạng của Xanh SM. Tiêu chí: độ gần với giá trị kinh doanh, sức mạnh bằng chứng công khai, khả năng kiểm chứng trong phạm vi cá nhân, độ phù hợp của AI và khả năng khác biệt với tính năng hiện có. Không gán điểm số vì thiếu dữ liệu tổn thất và độ khả thi triển khai thực.

| Ứng viên | Đánh giá tác động tiềm năng | Bằng chứng và khoảng trống | AI và khả năng thu hẹp | Ưu tiên cho bài |
|---|---|---|---|---|
| **Cân bằng cung–cầu, mức sử dụng xe, có ràng buộc pin/sạc** | Gắn đồng thời với số chuyến thực hiện, thời gian đón, km rỗng và thời gian xe phục vụ được. Đây là lập luận cơ chế, chưa phải mức tác động đã đo. | Chính sách giữ chuyến/sạc làm hướng này đáng khảo sát; chưa có dữ liệu chứng minh mất cân bằng hay sạc là nguyên nhân chính. | Dự báo chuỗi thời gian và tối ưu có ràng buộc phù hợp về cấu trúc; thu hẹp được vào một vùng và một khung giờ. | **Chọn làm hướng khám phá**, với pickup/fulfillment là kết quả. |
| **Hủy chuyến và đón khách thiếu tin cậy** | Rất gần giá trị khách nhận được; dễ định nghĩa sự kiện thất bại. | Nguồn giữ chuyến có bằng chứng ưu tiên trực tiếp mạnh nhất; thiếu tỷ lệ và nguyên nhân. | Có thể bắt đầu bằng phân tích log/rule. Không cần AI nếu nguyên nhân chủ yếu là lỗi bản đồ, quy định đón hoặc sự cố thanh toán. | **Ưu tiên cao; dùng làm kết quả và chẩn đoán** cho hướng được chọn. |
| **Thu nhập và giữ chân tài xế** | Có thể ảnh hưởng quy mô cung, chi phí tuyển mới và tính bền vững đội xe; mức tác động chưa biết. | Có bằng chứng hỗ trợ doanh số/phúc lợi, nhưng không có churn, thu nhập ròng theo giờ hoặc khảo sát lý do rời bỏ. | Dự báo churn chỉ hữu ích khi có biện pháp hỗ trợ có tác dụng; cần dữ liệu dài hạn và kiểm chứng can thiệp, khó hơn một lab ngắn. | **Theo dõi như chỉ số bảo vệ**; chưa chọn làm bài chính. |
| **An toàn và chất lượng dịch vụ** | Hậu quả tiềm năng nghiêm trọng, không nên xếp thấp chỉ vì số sự cố có thể ít. | S2S đã được công bố; không có dữ liệu tần suất, cảnh báo sai hay năng lực xử lý để xác định phần việc còn thiếu. | Cần dữ liệu/đánh giá chuyên môn và quy trình ứng cứu; scope cá nhân khó chứng minh giá trị mới. | **Chưa chọn**, cần discovery riêng với chủ sở hữu S2S. |
| **CSKH, phân loại phản ánh, soạn nháp hỗ trợ** | Có thể giảm thời gian xử lý; tác động thường cần quy đổi qua khối lượng thực và chất lượng giải quyết. | Đã có back-end và công cụ hỗ trợ được doanh nghiệp mô tả; chưa có volume, AHT hay tỷ lệ tái liên hệ. | LLM phù hợp với văn bản; scope hẹp dễ làm nhưng cần so với form/rule/template. | **Ứng viên dự phòng**, không đủ căn cứ để gọi là vấn đề lớn nhất. |

Không diễn giải bảng thành “tối ưu đội xe chắc chắn đem lại nhiều tiền nhất”. Muốn kết luận đó cần dữ liệu kinh tế và ước lượng tác động so sánh giữa các hướng.

## 4. Phân biệt dữ kiện, giả thuyết và giả định lab

| Loại | Nội dung |
|---|---|
| **Dữ kiện có nguồn** | Doanh nghiệp công bố ưu tiên giữ chuyến, hỗ trợ tài xế và chính sách sạc; có hệ thống back-end và một số trợ lý/tính năng hiệu suất. Các phạm vi/thời hạn nằm trong bảng nguồn phía trên. |
| **Giả thuyết nghiệp vụ H1** | Một phần yêu cầu thất bại hoặc đón lâu vào cao điểm có thể được giảm bằng bố trí lại xe sẵn sàng theo vùng trước khi nhu cầu đến. |
| **Giả thuyết H2 về sạc** | Một phần thiếu cung có thể trùng với thời điểm xe phải sạc; phối hợp lịch sạc và điều chuyển có thể cải thiện H1. Không có bằng chứng hiện tại chứng minh quan hệ nhân quả này tại Xanh SM. |
| **Giả thuyết H3 về AI** | Dự báo có xét độ bất định cộng tối ưu ràng buộc tạo giá trị cao hơn một rule theo giờ/vùng và ngưỡng pin đơn giản. |
| **Giả định thiết kế lab** | Một depot/đội xe thuộc một vùng Hà Nội, khung 16–19h, cập nhật mỗi 15 phút, nhìn trước 30 phút, một người vận hành duyệt. Quy mô 50 ô tô mô phỏng và 6 ô địa lý liền kề chỉ là một cấu hình thử tùy chọn, chưa chốt cho MVP. Đây không phải quy mô, cấu trúc tổ chức hay quy trình hiện hành của Xanh SM. |

## 5. Discovery trước khi xác nhận giải pháp

Đề nghị phỏng vấn một người phụ trách vận hành vùng/depot, một người phụ trách matching hoặc dữ liệu, và 5–8 tài xế trong cùng phạm vi. Đây là kế hoạch nghiên cứu; chưa có ai được phỏng vấn. Cần làm rõ:

1. Hệ thống hiện dự báo nhu cầu và điều chuyển/sạc như thế nào? Phần nào đã tự động? Ai có quyền thay đổi và ai được từ chối đề xuất?
2. Bao nhiêu yêu cầu không ghép được, bao nhiêu chuyến đã ghép rồi thất bại, và nguyên nhân nào chiếm tổn thất lớn nhất theo vùng/giờ?
3. Xe được đánh dấu rảnh có thật sự sẵn sàng nhận chuyến không? Ca làm, nghỉ, loại dịch vụ, pin và dữ liệu trạm ảnh hưởng ra sao?
4. Tài xế có quyền chủ động chọn sạc/đổi vùng như thế nào? Khoản thu nhập và chi phí nào họ thực chịu? Đề xuất điều chuyển có làm họ chạy rỗng hoặc bỏ lỡ quyền lợi không?
5. Khi nào dữ liệu pin/trạm bị trễ hoặc sai? Có API quyền truy cập phù hợp hay chỉ có dữ liệu tổng hợp? Chi phí tích hợp có vượt lợi ích kỳ vọng không?

**Dữ liệu tối thiểu cần xin có thẩm quyền:** thời điểm yêu cầu, vùng đón/trả, loại dịch vụ, các trạng thái matching/accept/cancel/pickup/complete, mã lý do hủy, vị trí và trạng thái xe theo thời gian, ca/nghỉ, SoC có timestamp, năng lượng tiêu thụ, sự kiện vào/chờ/sạc/rời trạm, dữ liệu cổng tương thích/hoạt động, và thu nhập/chi phí phục vụ đánh giá theo giờ. Dùng mã định danh giả, vùng tổng hợp và quyền truy cập cần thiết; lab chưa có các dữ liệu này.

**Không trộn các hiện tượng:**

- **Trước ghép:** không tìm được xe, hết thời gian chờ ghép, hoặc khách hủy khi chưa được ghép. Khách hủy trước ghép không tự động đồng nghĩa “không đủ cung”.
- **Sau ghép, trước đón:** tài xế/khách/hệ thống hủy, xe không tới, phải ghép lại. Cần actor, timestamp và lý do; ghép lại phải giữ liên kết với cùng yêu cầu gốc.
- **Sau đón:** chuyến dở dang và vấn đề chất lượng khác, đo riêng.
- **Mất cung do sạc:** chỉ xác nhận khi có trạng thái xe và thời gian sạc/chờ tương ứng; lời ghi chú “pin yếu” không tự chứng minh đây là nguyên nhân hệ thống hoặc nguyên nhân của mọi hủy chuyến.

Nếu dữ liệu cho thấy lỗi điểm đón, hành vi tài xế, quy tắc khuyến mại hoặc nguyên nhân khác chiếm phần lớn mất chuyến, cần đổi can thiệp theo nguyên nhân đó. Nếu sạc không đóng góp đáng kể, bỏ thành phần tối ưu sạc và giữ bài toán cung–cầu.

## 6. MVP: gợi ý bố trí xe sẵn sàng trước cao điểm

MVP là **màn hình hỗ trợ quyết định cho người vận hành vùng**, chưa thay matching thực tế và chưa tự điều khiển tài xế. Trong lab dùng dữ liệu tổng hợp có ghi nhãn rõ. Một vòng quyết định:

1. Lấy snapshot có timestamp của nhu cầu lịch sử/hiện tại, xe rảnh/đang chuyến/sạc và năng lực trạm; chặn hoặc đánh dấu dữ liệu thiếu/trễ.
2. Dự báo số yêu cầu theo vùng trong 30 phút tới, kèm khoảng dự báo. Ước lượng số xe thực sẵn sàng, không đồng nhất mọi xe online với xe đủ điều kiện.
3. So sánh phương án giữ nguyên, chuyển một số xe rảnh sang vùng lân cận, hoặc sạc trong một khoảng cho phép. Tính cả quãng đường rỗng, pin dự kiến, năng lực cổng và thời gian tài xế sẵn sàng.
4. Hiển thị tối đa ba đề xuất cùng tác động dự kiến, ràng buộc và độ tin cậy. Người vận hành duyệt/sửa/từ chối; tài xế được thông báo theo cơ chế đã thống nhất trong pilot thật.
5. Ghi nhận quyết định và kết quả để đánh giá. Dữ liệu thực tế khác dự báo phải được phản ánh ở vòng sau.

Ví dụ minh họa, hoàn toàn tổng hợp: mô hình năng lực phục vụ ước lượng vùng A thiếu tương đương 8 xe trong 30 phút, vùng B có thể điều chuyển 5 xe rảnh; đề xuất chuyển 3 xe từ B sang A sau khi kiểm tra thời gian đi và đủ năng lượng. Ước lượng năng lực phải tính số chuyến mỗi xe có thể phục vụ, thời gian chuyến, vị trí và khả năng xe quay lại, không lấy số yêu cầu trừ số xe. Một xe cần sạc không được chuyển chỉ vì đang gần A. Không coi ví dụ là kết quả thuật toán đã chạy.

**Giới hạn MVP:** chỉ một vùng vận hành gồm các ô lân cận và một khung cao điểm; không tối ưu toàn quốc, không thay đổi giá/thu nhập, không xử phạt tài xế, không tự đặt cổng sạc và không coi dữ liệu cổng trống là cam kết giữ chỗ. Ngưỡng năng lượng dự phòng phải do kỹ thuật/vận hành xác lập theo xe, hành trình và độ tin cậy dữ liệu; không lấy ngưỡng 5% của starter lab làm chuẩn kỹ thuật thực.

## 7. AI phù hợp ở đâu?

Phần lõi là **dự báo nhu cầu + tối ưu có ràng buộc**, không phải chatbot. ML có thể dự báo nhu cầu/khả năng xe quay lại phục vụ khi có dữ liệu phù hợp; solver hoặc heuristic chọn phương án khả thi. Tối ưu toán học tự nó không chứng minh cần AI.

Nghiên cứu gốc của Li, Wang và Huang đề xuất kết hợp dự báo nhu cầu, điều chuyển, matching và lựa chọn trạm sạc, đánh giá bằng case New York. Nguồn này hỗ trợ tính hợp lý của hướng phương pháp, không chứng minh tác động tại Hà Nội và không được chuyển các phần trăm cải thiện của nghiên cứu thành mục tiêu chắc đạt của Xanh SM. [Bài gốc, arXiv v2 ngày 09/01/2024](https://arxiv.org/html/2401.03300v2).

Một tiền lệ sản phẩm là hướng dẫn chính thức của Uber về khuyến nghị sạc tại Mỹ/Canada, sử dụng dữ liệu pin, giá sạc lân cận và thu nhập sắp tới; tài xế có thể bỏ qua và vẫn cần kiểm tra giá/tính sẵn có tại trạm. Đây là bằng chứng về cách thiết kế một chức năng tương tự ở thị trường khác, không phải dữ liệu vận hành của Xanh SM. [Uber Help: Charging recommendations for EV drivers](https://help.uber.com/driving-and-delivering/article/charging-recommendations-for-ev-drivers?nodeId=bf23f907-3a93-4bb6-bf04-9a3c43dc1568).

So sánh bắt buộc trên cùng tập đánh giá:

- **Baseline 0:** quy trình/chính sách hiện có, sau khi được khám phá và ghi nhận.
- **Baseline 1:** dự báo theo cùng thứ/giờ gần nhất hoặc trung bình đơn giản + rule thiếu/dư vùng + ràng buộc năng lượng.
- **Ứng viên:** mô hình dự báo được học từ dữ liệu quá khứ + tối ưu có ràng buộc với cùng dữ liệu đầu vào.

LLM chỉ là tùy chọn để giải thích đề xuất hoặc tổng hợp ghi chú đã kiểm chứng; không để LLM tự tính tầm hoạt động, chọn xe hoặc bịa dữ liệu trạm. Nếu baseline đơn giản đạt mục tiêu với chi phí thấp hơn, chọn baseline đó. Starter soạn tin pin hiện có không kiểm chứng được giả thuyết tối ưu cung–cầu này.

## 8. Đo hiệu quả và thiết kế thí nghiệm

**Mọi mục tiêu số trong mục này đều là đề xuất lab**, cần hiệu chỉnh sau baseline và phân tích cỡ mẫu; chưa phải kết quả thực hoặc KPI nội bộ.

| Nhóm | Chỉ số và cách tính | Vai trò |
|---|---|---|
| **Kết quả chính** | **Tỷ lệ được đón đúng SLA = số yêu cầu hợp lệ được đón trong ngưỡng T / tổng yêu cầu hợp lệ trong vùng/giờ đã định.** Chốt T với vận hành trước thử nghiệm. Khử trùng yêu cầu thử lại theo quy tắc công bố trước; giữ cả không ghép được và hủy trong mẫu số. | Đo khả năng đón tin cậy trên toàn bộ nhu cầu quan sát được; không chỉ tính trên chuyến đã nhận. Mục tiêu thử: tăng ≥5 điểm phần trăm so với đối chứng, không phải tăng 5% tương đối. |
| Kết quả toàn hành trình | Fulfillment = số yêu cầu hợp lệ có chuyến hoàn thành / tổng yêu cầu hợp lệ. Tập yêu cầu được xác định theo thời điểm gửi yêu cầu; theo dõi đến kết quả cuối kể cả đón/hoàn thành sau khi khung đo kết thúc. | Chỉ số thứ cấp để kiểm tra đón đúng SLA có dẫn tới chuyến hoàn thành; không đếm chuyến hoàn thành trong khung giờ rồi chia cho một tập yêu cầu khác. |
| Thời gian đón | P50/P90 thời gian từ yêu cầu đến đón cho chuyến thực đón, đọc cùng tỷ lệ đón đúng SLA trên mọi yêu cầu. | Tránh P90 trông tốt hơn chỉ vì chuyến chờ lâu bị hủy. Mục tiêu lab: P90 giảm ≥10% tương đối cùng fulfillment không giảm. |
| Năng suất đội xe | Chuyến hoàn thành / tổng giờ xe theo ca trong phạm vi, tính cả thời gian sạc, chờ và chạy rỗng trong ca. | Theo dõi sử dụng tài sản, không làm đẹp số bằng loại xe đang sạc ra khỏi mẫu. |
| Chẩn đoán | Tỷ lệ không ghép được; hủy trước ghép; hủy sau ghép theo actor/lý do; số lượt ghép lại; phút sạc/chờ; km rỗng trên chuyến. | Xác định cơ chế, không tự quy toàn bộ cải thiện cho sạc. |
| Tài xế | Thu nhập ròng trên giờ theo ca, cả phân bố giữa tài xế; số phút nghỉ và mức chấp nhận đề xuất. | Không tối ưu tổng số chuyến bằng cách chuyển chi phí hoặc giảm thu nhập của một nhóm tài xế. Thu nhập ròng phải thống nhất các khoản thực nhận/thực trả theo từng loại hợp đồng. |
| Ràng buộc | Không có đề xuất vi phạm dự phòng năng lượng/cổng/ca trong bộ đánh giá; dữ liệu trễ phải bị chặn; km rỗng/chuyến không tăng so với baseline trong mục tiêu lab. | Kiểm tra tính khả thi và chi phí can thiệp. “0 lỗi trong bộ thử” không phải bảo đảm 0 lỗi ngoài thực tế. |

Thứ tự đánh giá: (1) dữ liệu tổng hợp để kiểm tra logic và ca biên; (2) replay theo thời gian với log được phép dùng, so trên cùng nhu cầu và cùng giả định; (3) chạy shadow để xem đề xuất mà chưa thực thi; (4) pilot có người duyệt nếu bằng chứng đủ. Tách train/test theo thời gian để tránh rò rỉ tương lai. Không dùng kết quả mô phỏng làm bằng chứng đã giảm thời gian đón khách thật.

Pilot thực cần cân nhắc thử nghiệm luân phiên theo khung thời gian cho cả cụm vùng, có thời gian chuyển tiếp và giám sát xe tràn giữa cụm; không ngẫu nhiên từng tài xế rồi coi các nhóm độc lập khi họ cùng phục vụ một thị trường. Theo dõi thời tiết, sự kiện, giao thông và khuyến mại. Chương trình mới bắt đầu 08/11/2026 là lý do không so trước/sau một cách giản đơn. Quy mô mẫu và thời lượng chỉ chốt sau khi biết baseline, độ biến động và hiệu ứng tối thiểu cần phát hiện.

Giá trị kinh tế chỉ ước lượng sau khi có dữ liệu: **lãi đóng góp tăng thêm từ chuyến hoàn thành − chi phí km rỗng/sạc/thưởng tăng thêm − chi phí hệ thống và vận hành**. Cước chuyến không đồng nghĩa doanh thu thuần hoặc lợi nhuận nền tảng; tránh cộng hai lần lợi ích từ “tăng chuyến” và “tăng sử dụng xe”.

## 9. Quyết định cho bài cá nhân

**GO cho discovery và prototype mô phỏng** của bài toán xe sẵn sàng theo vùng/giờ; **chưa đủ căn cứ cho pilot vận hành**. Đầu ra Day 02 nên là problem card, sơ đồ vòng quyết định, hợp đồng dữ liệu, baseline và kế hoạch đánh giá rõ ràng. Bản demo chỉ cần cho thấy người vận hành hiểu và kiểm tra được một đề xuất hợp lệ.

Ba bằng chứng có thể đổi quyết định: nguyên nhân mất chuyến chủ yếu không thuộc phân bố cung; hệ thống hiện tại đã giải quyết tốt phần đề xuất; hoặc dữ liệu pin/trạm/ca không đủ tin cậy để tạo đề xuất khả thi. Khi đó giữ mục tiêu đón khách tin cậy và chọn can thiệp khác theo dữ liệu, thay vì bảo vệ một giải pháp AI đã định sẵn.
