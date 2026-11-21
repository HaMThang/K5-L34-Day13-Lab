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
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
