# Báo cáo cá nhân — Hà Minh Thắng — 2A202603676

## 1. Thông tin thành viên

- Họ tên: Hà Minh Thắng
- MSSV: 2A202603676
- Email: haminhthang1213@gmail.com
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

- Phụ trách code mô hình phân tích chi phí trong `src/lab13.py`.
- Phối hợp hoàn thiện và rà soát bảng chi phí trong `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- Hoàn thiện các hàm A1 tính số lần chạy kỳ vọng, xác suất thành công và hệ số chi phí mỗi việc thành công.
- Triển khai hàm mô hình chi phí A2, gồm chi phí token, tool, xem lại, làm lại và chi phí trên mỗi việc thành công.
- Tính và trình bày kết quả theo loại yêu cầu ở A3, chi phí cố định ở A4, cùng các kịch bản độ nhạy B1–B4.
- Đối chiếu kết quả với dữ liệu CSV và các số tham khảo của hướng dẫn lab; ghi nhãn `simulated` cho các kết quả có dùng số phút giả lập.

## 4. Bằng chứng

- Code và các kết quả tính: `src/lab13.py`.
- Bảng kết quả A2–A4 và B1–B4: `report/team/bang_chi_phi.md`.
- Chương trình được chạy từ thư mục `src/`; ba phép thử A1 đạt. Kết quả A2 gồm 245.585 đ tiền token, 84.000 đ tiền tool, 1.780.000 đ xem lại (simulated), 2.264.000 đ làm lại (simulated), 978 việc thành công và khoảng 4.472 đ mỗi việc thành công.

## 5. Công cụ AI đã dùng

- Dùng Copilot để giải thích công thức, hỗ trợ triển khai và rà soát mã Python cũng như cách trình bày kết quả.
- Tự kiểm tra bằng cách chạy `lab13.py` với các tệp CSV, xác nhận ba phép thử A1, rồi đối chiếu kết quả A2–B4 với công thức và số tham khảo trong tài liệu lab.

## 6. Tự đánh giá

Qua phần code và phân tích chi phí, tôi hiểu rõ hơn vì sao phải tính chi phí của mọi lần chạy, kể cả lần lỗi, nhưng chỉ chia cho số việc thành công. Tôi cũng nhận ra cần xem chi phí nhân viên xem lại/làm lại và số yêu cầu phải chuyển cho nhân viên, thay vì chỉ nhìn hóa đơn token. Lần sau, tôi sẽ kiểm tra môi trường Python và thư viện sớm hơn, đồng thời kiểm thử từng phần ngay sau khi triển khai.
