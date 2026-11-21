# Báo cáo cá nhân — Lê Hoàng Sơn - 2A202603662

## 1. Thông tin thành viên

- Họ tên: Lê Hoàng Sơn
- MSSV: 2A202603662
- Email: leson121105@gmail.com
- Vai trong nhóm: người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Giữ hồ sơ: điền dần `report/team/ho_so_launch_v0.md` từ đầu buổi, tổng hợp số từ các nhiệm vụ A–D.
- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi (bộ nhãn thứ hai), sau đó cùng người gắn nhãn 1 so nhãn, thống nhất ca không trùng và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Nhiệm vụ D: soạn `report/team/pilot_plan.yaml` (đối chứng, cách chia, đánh đổi, ba luật dừng, rollback), dùng cỡ mẫu D1 do người viết code tính.
- Nhiệm vụ E: soạn `report/team/chi_so.md` (đặc tả chỉ số, danh sách event, rủi ro kinh tế).
- Cuối buổi: soạn `report/team/group_report.md` và nhắc các thành viên tạo báo cáo cá nhân.

## 3. Đóng góp cụ thể

Đã làm đến thời điểm viết báo cáo này:

- `chi_so.md`: điền bảng E1 với ba chỉ số tính trực tiếp từ `src/logix_requests.csv`: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200). Đề xuất thêm một chỉ số dùng và một chỉ số an toàn. Lập danh sách 10 event, mỗi event có `trace_id`, và phần kiểm tra chéo chỉ số với event. Dựng 3 dòng rủi ro kinh tế.
- `ho_so_launch_v0.md`: dựng khung bảy mục, trạng thái và người phụ trách là vai trò cụ thể. Mục 4 đã có số. Các mục còn lại chờ số từ người viết code (A, B) và từ CP3, CP4.

Chưa làm (sẽ cập nhật khi xong): gắn nhãn 20 ca lỗi, `pilot_plan.yaml`, `group_report.md`, điền các số còn lại trong hồ sơ và rủi ro kinh tế.

## 4. Bằng chứng

- File: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
- Con số tự tính từ CSV: 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%. Trong phạm vi `noi_dia` + `hang_nang` (982 yêu cầu): mở lại 7 ngày 3,97%, làm lại 4,89%.
- Chưa có commit. Cập nhật mã commit khi đã push.

## 5. Công cụ AI đã dùng

- Công cụ: Claude Code (trong VS Code).
- Dùng vào việc: đọc đề và các file hướng dẫn để nắm phần việc, dựng khung `chi_so.md` và `ho_so_launch_v0.md`, và điền bản nháp báo cáo này.
- Cách tự kiểm tra: ba chỉ số E1 được tính bằng một đoạn pandas chạy trực tiếp trên CSV, rồi đối chiếu với số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; cả ba khớp. Các số phụ thuộc cột `_simulated` hoặc `src/lab13.py` chưa được điền; để `[chờ Người 1]` cho tới khi người viết code chốt. Đã chạy `grep -rni production report/team`, không có kết quả.

## 6. Tự đánh giá

[Tự viết sau khi hoàn thành: điều làm tốt, điều chưa tốt, bài học.]
