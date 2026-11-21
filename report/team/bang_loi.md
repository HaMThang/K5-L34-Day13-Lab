# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Ngầm | Không | Hệ thống |
| 3 | Ngữ cảnh | Do người dùng | Không | Do người dùng |
| 4 | Giới hạn hệ thống | Ngữ cảnh | Không | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Ngữ cảnh | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Do người dùng | Không | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |


**Tỉ lệ đồng thuận:** 13 / 20 = **65%**. Hai người bất đồng ở các ca 2, 3, 4, 10, 13, 16 và 19.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Các ca bất đồng chưa được tự động gán nhãn thay cho người gắn nhãn. Sau khi hai người đã lưu nhãn độc lập, cả nhóm cần xem nguyên nhân gốc của từng ca, thống nhất nhãn cuối và ghi quy tắc phân biệt; hiện tại đồng thuận 65%, thấp hơn mục tiêu 80%.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
|---:|---|---|---|---|
| 9 | Do người dùng | Theo dõi event `input_validation_failed`; cảnh báo nếu tỷ lệ vượt 2% yêu cầu/ngày. | Nhận diện mã đơn sàn thương mại điện tử; hướng dẫn khách nhập mã vận đơn hoặc gửi ảnh minh họa. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” phải có bản ghi ledger `ok` cùng `trace_id`; ngưỡng sai lệch là 0. | Chỉ thông báo hoàn tất khi ledger xác nhận thành công; sau 3 lần lỗi 503 thì báo đang xử lý và chuyển nhân viên. | Lead Agent Engineer |
| 18 | Ngữ cảnh | Theo dõi hàng tuần tỷ lệ mở lại do khách thắc mắc số tiền hoàn dù phép tính đúng. | Hiển thị phép tính rõ ràng: `30.000đ × 50% = 15.000đ`. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Ghi event `handoff_to_staff`, reason `thieu_du_lieu`; theo dõi số ca quốc tế cần chuyển. | Chuyển nhân viên kèm tóm tắt; loại `quoc_te` khỏi phạm vi pilot. | PM trợ lý hoàn phí |
| 17 | Ngầm | Đối soát 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu tỷ lệ sai giá vượt 1%. | Xóa cache khi cập nhật bảng giá và ghi phiên bản bảng giá được dùng trong trace. | Kế toán trưởng |
