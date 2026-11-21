# Bảng lỗi Người 2 — phân loại độc lập theo đề Lab 13

**Nguồn:** `Ngay13_Lab13_De_bai_hoc_vien.docx`, Nhiệm vụ C, trang 4–5.  
**Mục đích:** Bộ nhãn độc lập của Người 2 để đối chiếu với Người 3. Không dùng bảng này làm kết quả đồng thuận trước khi hai người so sánh.

## 1. Quy tắc phân loại

- **Do người dùng:** Người dùng nhập sai hoặc chọn sai.
- **Hệ thống:** Hệ thống trả lời sai hoặc làm sai so với thiết kế/chính sách.
- **Ngữ cảnh:** Hệ thống làm đúng thiết kế nhưng giả định/ cách giao tiếp không khớp hoàn cảnh người dùng.
- **Giới hạn hệ thống:** Thiếu dữ liệu, ngoài phạm vi hoặc dạng đầu vào không xử lý được.
- **Ngầm:** Có sai sót nhưng cả người dùng lẫn hệ thống đều không nhận ra.

## 2. Nhãn độc lập cho 20 ca

| Ca | Nhãn Người 2 | Lý do ngắn |
|---:|---|---|
| 1 | Do người dùng | Khách nhập thiếu hai chữ số tài khoản nhận tiền. |
| 2 | Hệ thống | Trợ lý truyền sai loại kiện vào công cụ tra giá, dẫn đến hoàn thiếu. |
| 3 | Ngữ cảnh | Trợ lý làm đúng thiết kế (hoàn về ví), nhưng khách kỳ vọng tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | Không có dữ liệu chặng do hãng nước ngoài giao; trợ lý đã chuyển nhân viên. |
| 5 | Ngầm | Hoàn theo giá trước giảm gây trả thừa; khách không báo và hệ thống không cảnh báo. |
| 6 | Do người dùng | Khách chọn nhầm loại yêu cầu “giao trễ” trong khi mô tả là hàng bị vỡ. |
| 7 | Hệ thống | Ghi hoàn tiền thất bại 503 nhưng trợ lý vẫn thông báo đã hoàn thành. |
| 8 | Hệ thống | Trợ lý viện dẫn điều khoản không tồn tại, dù số tiền hoàn đúng. |
| 9 | Do người dùng | Khách nhập mã đơn của sàn thay vì mã vận đơn; đầu vào không đúng loại mã được yêu cầu. |
| 10 | Ngữ cảnh | Từ chối là đúng chính sách bất khả kháng, nhưng khách đối chiếu với cam kết giao 24 giờ trên ứng dụng. |
| 11 | Giới hạn hệ thống | Trợ lý không xử lý được tin nhắn thoại và yêu cầu nhập bằng chữ. |
| 12 | Ngầm | Tool thiếu trường; trợ lý vẫn ra kết quả đúng nhưng chi phí token tăng gấp 3 trong 3 tuần mà không ai phát hiện. |
| 13 | Giới hạn hệ thống | Yêu cầu bảo hiểm ngoài phạm vi trợ lý; câu trả lời chung chung không nêu rõ giới hạn. |
| 14 | Do người dùng | Khách bấm nhầm xác nhận đã nhận tiền khiến yêu cầu bị đóng. |
| 15 | Hệ thống | Trợ lý tính hoàn 100% thay vì 50%; nhân viên phát hiện trước khi gửi. |
| 16 | Ngữ cảnh | Gửi ngay theo thiết kế nhưng gửi lúc 2:14 sáng, không phù hợp hoàn cảnh khách. |
| 17 | Ngầm | Dùng bảng giá cũ trong cache, gây lệch tiền ở nhiều đơn mà không ai mở lại. |
| 18 | Ngữ cảnh | Số tiền tính đúng nhưng thiếu giải thích phép tính khiến khách nghĩ bị hoàn thiếu. |
| 19 | Giới hạn hệ thống | Dữ liệu vượt quá cửa sổ truy cập 12 tháng; trợ lý đã thông báo và chuyển nhân viên. |
| 20 | Hệ thống | Thiếu khóa chống trùng khiến cùng một đơn được hoàn hai lần. |

## 3. Tổng hợp nhãn

| Loại lỗi | Các ca | Số ca |
|---|---|---:|
| Do người dùng | 1, 6, 9, 14 | 4 |
| Hệ thống | 2, 7, 8, 15, 20 | 5 |
| Ngữ cảnh | 3, 10, 16, 18 | 4 |
| Giới hạn hệ thống | 4, 11, 13, 19 | 4 |
| Ngầm | 5, 12, 17 | 3 |
| **Tổng** | **1–20** | **20** |

## 4. Năm ca đại diện và cách khắc phục

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Người phụ trách |
|---:|---|---|---|---|
| 9 | Do người dùng | Theo dõi event `input_validation_failed`; cảnh báo nếu tỷ lệ vượt 2% yêu cầu/ngày. | Nhận diện mã đơn sàn thương mại điện tử; hướng dẫn khách nhập mã vận đơn hoặc gửi ảnh minh họa. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” phải có bản ghi ledger `ok` cùng `trace_id`; ngưỡng sai lệch là 0. | Chỉ thông báo hoàn tất khi ledger xác nhận thành công; sau 3 lần lỗi 503 thì báo đang xử lý và chuyển nhân viên. | Lead Agent Engineer |
| 18 | Ngữ cảnh | Theo dõi hàng tuần tỷ lệ mở lại do khách thắc mắc số tiền hoàn dù phép tính đúng. | Hiển thị phép tính rõ ràng: `30.000đ × 50% = 15.000đ`. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Ghi event `handoff_to_staff`, reason `thieu_du_lieu`; theo dõi số ca quốc tế cần chuyển. | Chuyển nhân viên kèm tóm tắt; loại `quoc_te` khỏi phạm vi pilot. | PM trợ lý hoàn phí |
| 17 | Ngầm | Đối soát 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu tỷ lệ sai giá vượt 1%. | Xóa cache khi cập nhật bảng giá và ghi phiên bản bảng giá được dùng trong trace. | Kế toán trưởng |

## 5. Bảng đối chiếu với Người 3

Điền nhãn của Người 3 sau khi hai người đã hoàn tất phân loại độc lập.

| Ca | Người 2 | Người 3 | Trùng? | Nhãn thống nhất / ghi chú |
|---:|---|---|---|---|
| 1 | Do người dùng |  |  |  |\n| 2 | Hệ thống |  |  |  |\n| 3 | Ngữ cảnh |  |  |  |\n| 4 | Giới hạn hệ thống |  |  |  |\n| 5 | Ngầm |  |  |  |\n| 6 | Do người dùng |  |  |  |\n| 7 | Hệ thống |  |  |  |\n| 8 | Hệ thống |  |  |  |\n| 9 | Do người dùng |  |  |  |\n| 10 | Ngữ cảnh |  |  |  |\n| 11 | Giới hạn hệ thống |  |  |  |\n| 12 | Ngầm |  |  |  |\n| 13 | Giới hạn hệ thống |  |  |  |\n| 14 | Do người dùng |  |  |  |\n| 15 | Hệ thống |  |  |  |\n| 16 | Ngữ cảnh |  |  |  |\n| 17 | Ngầm |  |  |  |\n| 18 | Ngữ cảnh |  |  |  |\n| 19 | Giới hạn hệ thống |  |  |  |\n| 20 | Hệ thống |  |  |  |

**Công thức đồng thuận:** `Số ca trùng / 20 × 100%`.  
**Ngưỡng yêu cầu:** từ 80% trở lên (ít nhất 16/20 ca). Nếu dưới 80%, nhóm cần thống nhất lại định nghĩa và ghi quy tắc phân biệt cho các ca bất đồng.
