## Final project segmentation-analysis

#### Data là các bình luận của các bài viết trên facebook.

#### Bài toán của bọn em là phân tích cảm xúc của các bình luận.

#### Kiến trúc: Bi RNN và Transformer.

#### Danh sách thành viên và công việc:

- Nguyễn Tuấn Thành - 22022624: Dùng selenium và pyautogui để thu thập và dùng pandas để trực quan và làm sạch dữ liệu.
- Vũ Đình Thọ - 22022580: Xây dựng kiến trúc và huấn luyện model Transformer.
- Đinh Văn Sinh - 22022625: Viết báo cáo, tổng hợp nội dung.
- Nguyễn Mạnh Hùng - 22022623: Xây dựng kiến trúc và huấn luyện model dùng Bi RNN.
- Nguyễn Công Thành - 22022630: Gán nhãn dữ liệu.

##### Khi crawl dat thì tạo file .env ở root dự án rồi thêm 2 biến có dạng:
```
EMAIL_FACEBOOK = <Email or SDT>
PASSWORD_FACEBOOK = <Password>
```
##### Rồi dùng các lệnh sau để crawl data:
```
cd crawl_data
```
```
python3 main.py
```
