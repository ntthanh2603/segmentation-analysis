## Final project segmentation-analysis
Phân tích cảm xúc (Sentiment Analysis) là một ứng dụng phổ biến trong Xử lý ngôn ngữ tự nhiên (NLP), nhằm
xác định cảm xúc (tích cực, tiêu cực, hoặc trung tính) trong văn bản. Dự án này tập trung triển khai và so 
sánh hai mô hình deep learning hiện đại: Transformer và Bi-RNN (Mạng nơ-ron hồi tiếp hai chiều), nhằm giải
quyết bài toán phân tích cảm xúc trên các tập dữ liệu thực tế.
<br>
Trong bài báo cáo, chúng em đã thực hiện phân tích và so sánh hai mô hình deep learning hiện đại là Transformer (PhoBERT, DistilBERT) và Bi-RNN (với các lớp LSTM) trong bài toán phân tích cảm xúc dựa trên đánh giá phim bằng tiếng Việt.

#### Danh sách thành viên và công việc:
- Nguyễn Tuấn Thành - 22022624: Dùng Selenium và Pyautogui để thu thập và dùng pandas để trực quan và làm sạch dữ liệu.
- Vũ Đình Thọ - 22022580: Xây dựng kiến trúc và huấn luyện model Transformer.
- Đinh Văn Sinh - 22022625: Viết báo cáo, tổng hợp nội dung.
- Nguyễn Mạnh Hùng - 22022623: Xây dựng kiến trúc và huấn luyện model dùng Bi RNN.
- Nguyễn Công Thành - 22022630: Gán nhãn dữ liệu.

#### Mục Tiêu
- Xây dựng và triển khai mô hình: Phát triển hai mô hình deep learning là Transformer và Bi-RNN để phân tích cảm xúc.
- Đánh giá và so sánh: So sánh hiệu suất của hai mô hình thông qua các chỉ số như độ chính xác (Accuracy), F1-Score, độ chính xác (Precision) và độ nhạy (Recall).
- Ứng dụng thực tiễn: Ứng dụng kết quả phân tích vào các lĩnh vực như quản lý phản hồi khách hàng, theo dõi đánh giá sản phẩm hoặc giám sát cảm xúc trên mạng xã hội.

#### Data:
Là các bình luận của các bài viết trên facebook được thu thập bằng thư viện Selenium và Pyautogui.
Và dùng Pandas và các thư viện hỗ trợ như emoji, unicodedata, regex, pyvi để chuyển data thành chữ thường, tách từ tiếng việt, 
chuẩn hóa từ tiếng việt, chuẩn hóa câu, loại bỏ link, loại bỏ số, loại bỏ các icon và trực quan hóa dữ liệu.

#### Kết luận chung: 
- PhoBERT (Transformer) với độ chính xác cao nhất 90.93% là lựa chọn phù hợp cho các bài toán xử lý ngôn ngữ tiếng Việt nhờ khả năng xử lý toàn cục và hiệu suất cao, đặc biệt trong các tập dữ liệu phức tạp. Nhưng hạn chế khi  thời gian huấn luyện của dài hơn so với Bi-RNN khi batch size tăng.
- Bi-RNN (với LSTM) với 95.26% độ chính xác vẫn là một phương pháp mạnh mẽ và hiệu quả, đặc biệt khi tài nguyên huấn luyện hạn chế. Khó khăn khi chuỗi dài và có tốc độ huấn luyện chậm hơn khi số lượng layer tăng.
Kết quả mang lại thể hiện hiệu quả của các mô hình deep learning trong bài toán phân tích cảm xúc và góp phần đóng góp thực tiễn cho phát triển các ứng dụng NLP.

#### Thanks for watching!!!
