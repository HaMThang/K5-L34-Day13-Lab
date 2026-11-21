# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Người 2 của nhóm · Người gắn nhãn 2: Lê Hoàng Sơn (Người 3 của nhóm) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Ngầm | Không | Hệ thống |
| 3 | Ngữ cảnh | Do người dùng | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Ngữ cảnh | Không | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Giới hạn hệ thống | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Ngữ cảnh | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Giới hạn hệ thống | Không | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Do người dùng | Không | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |


**Tỉ lệ đồng thuận:** 13 / 20 = **65%**. Hai người bất đồng ở các ca 2, 3, 4, 10, 13, 16 và 19.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 2 (Hệ thống, không phải Ngầm):** trợ lý gọi sai tham số so với thiết kế, và sai đó đã lộ ra vì khách mở lại sau 2 ngày; Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- **Ca 3 (Ngữ cảnh, không phải Do người dùng):** khách không nhập hay chọn sai gì; trợ lý làm đúng thiết kế (ví LogiX trong 5 phút), chỉ giả định về nơi nhận tiền không khớp mong đợi của khách.
- **Ca 4 (Giới hạn hệ thống, không phải Ngữ cảnh):** trợ lý không có dữ liệu chặng do hãng nước ngoài giao nên không thể trả lời, dù có cố gắng.
- **Ca 10 (Ngữ cảnh, không phải Giới hạn hệ thống):** trợ lý làm đúng chính sách và làm được; khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ", tức giả định không khớp hoàn cảnh.
- **Ca 13 (Giới hạn hệ thống, không phải Ngữ cảnh):** bảo hiểm hàng hoá nằm ngoài phạm vi trợ lý; ngoài phạm vi là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 16 (Ngữ cảnh, không phải Giới hạn hệ thống):** trợ lý gửi đúng thiết kế "gửi ngay khi xong" và hoàn toàn làm được; chỉ giờ gửi 2:14 sáng không khớp hoàn cảnh của khách.
- **Ca 19 (Giới hạn hệ thống, không phải Do người dùng):** khách không sai gì; nguyên nhân gốc là trợ lý chỉ truy cập được dữ liệu 12 tháng, còn đơn đã 14 tháng.

**Đồng thuận 65% (13/20), thấp hơn 80%, nên viết lại định nghĩa.** Phần lớn bất đồng nằm ở ranh giới Ngữ cảnh với Giới hạn hệ thống và Do người dùng (ca 3, 4, 10, 13, 16, 19). Định nghĩa đã viết lại, thêm một câu hỏi phân biệt cho mỗi loại:

- **Do người dùng:** đầu vào của khách sai về sự thật (số tài khoản, mã đơn, nút bấm nhầm). Hỏi: "nếu khách nhập đúng thì lỗi có xảy ra không?" Nếu không xảy ra thì gắn loại này. Khách chỉ có kỳ vọng khác thiết kế thì không phải loại này.
- **Hệ thống:** trợ lý làm sai so với thiết kế hoặc chính sách, và có người nhìn thấy sai đó (nhân viên, khách, tin nhắn hiển thị sai).
- **Ngữ cảnh:** trợ lý làm được, kết quả đúng thiết kế và chính sách, nhưng khách thấy sai vì giả định mặc định (thời gian, kênh, cách trình bày, cam kết hiển thị) không khớp hoàn cảnh. Hỏi: "đổi giả định mặc định thì hết lỗi không?"
- **Giới hạn hệ thống:** trợ lý không thể làm được dù cố gắng, vì thiếu dữ liệu, thiếu quyền, ngoài phạm vi hoặc dạng đầu vào không xử lý được. Hỏi: "dù thiết kế đúng, trợ lý vẫn không làm được?"
- **Ngầm:** có sai nhưng không ai nhận ra, cả khách lẫn hệ thống; chỉ lộ ra khi kiểm tra mẫu hoặc nhìn số liệu (tiền, chi phí).

Bộ nhãn độc lập (hai cột đầu) giữ nguyên, không sửa sau khi so.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Thêm thuộc tính `error_type` = `ma_khong_hop_le` vào event `agent_run_completed`; cảnh báo khi quá 2% số yêu cầu mỗi ngày | Nhận diện mã đơn của sàn thương mại điện tử và gợi ý cách tra mã vận đơn; không tra được thì hướng dẫn kèm ảnh, không dừng im lặng | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` có `ket_qua` ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; nếu lỗi 503 sau 3 lần thì báo "đang xử lý" và gọi `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` có lý do liên quan đến số tiền mà kiểm tra thấy đúng, theo tuần; cảnh báo khi vượt 1% số yêu cầu tuần | Mẫu tin nhắn luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason` = `thieu_du_lieu`, theo loại yêu cầu; cảnh báo khi vượt 20% số yêu cầu của một loại trong tuần | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot (27,3% thành công, 1,88× so với 12.000 đ, simulated) | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn mỗi tuần (`audit_sample_checked`) so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới và ghi phiên bản bảng giá vào trace | Kế toán trưởng |

Năm ca trên đều có nhãn thống nhất khớp loại ở cột "Loại lỗi". Ngưỡng cảnh báo là đề xuất của nhóm cho pilot, cần đối chiếu lại với số đo thật sau tuần 1.
