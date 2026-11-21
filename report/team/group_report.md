# Báo cáo nhóm

Báo cáo tóm tắt kết quả Lab 13. Số liệu chi tiết nằm trong các hồ sơ nhóm; mọi kết quả dựa trên số phút có hậu tố `_simulated` được ghi nhãn `simulated`.

## 1. Thông tin nhóm

- Tên nhóm: STT
- Lớp: L3A
- Thành viên: Hà Minh Thắng, Lê Hoàng Sơn, Hồ Sỹ Tùng. Vai trò và đóng góp chi tiết được ghi trong `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá trợ lý hoàn phí LogiX-VN trên bộ dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy. Mục tiêu là ước tính chi phí mỗi việc thành công, xác định phạm vi xử lý phù hợp, phân loại lỗi và thiết kế pilot có đối chứng, cỡ mẫu cùng điều kiện dừng. Nhóm dùng `src/lab13.py` để tính toán, kiểm tra chéo kết quả với công thức và tài liệu lab.

## 3. Giải pháp

- **A — Chi phí:** tính token và tool trên mọi lần chạy; cộng thời gian xem lại/làm lại; chia cho số việc thành công. Phân tích thêm theo loại yêu cầu và phân bổ chi phí cố định. Chi tiết ở `bang_chi_phi.md`.
- **B — Độ nhạy:** thay đổi từng yếu tố, giới hạn số lần chạy và so sánh chi phí trợ lý với tổng chi phí công ty, bao gồm công việc nhân viên phải làm thay. Chi tiết ở `bang_chi_phi.md`.
- **C — Lỗi:** hai thành viên tạo bộ nhãn độc lập, sau đó đối chiếu, thống nhất quy tắc cho các ca bất đồng và đề xuất cách phát hiện/khắc phục. Chi tiết ở `bang_loi.md`.
- **D — Pilot:** so sánh cỡ mẫu theo yêu cầu, nhân viên và depot; lập kế hoạch phân nhóm theo nhân viên, đối chứng đồng thời, luật dừng và rollback. Chi tiết ở `pilot_plan.yaml`.
- **E — Chỉ số và hồ sơ:** đặc tả chỉ số chính, sử dụng, an toàn; thiết kế event có `trace_id`; ghi rủi ro kinh tế và lập hồ sơ Gate 2a. Chi tiết ở `chi_so.md` và `ho_so_launch_v0.md`.

## 4. Kết quả

Toàn bộ mẫu có 978/1.200 việc thành công. Chi phí là khoảng **4.472 đ/việc thành công (simulated)**; trong đó token 245.585 đ, tool 84.000 đ, xem lại 1.780.000 đ và làm lại 2.264.000 đ. Trong phạm vi `noi_dia` + `hang_nang`, chi phí gồm phân bổ chi phí cố định ước tính **4.599 đ/việc (simulated)** ở mức 45.000 yêu cầu/tháng. `quoc_te` có chi phí 22.515 đ/việc (1,88 lần mức 12.000 đ của nhân viên) và tỉ lệ thành công 27,3%, nên bị loại khỏi phạm vi pilot đề xuất.

Trong đợt chạy thử, chỉ số đóng trong 24 giờ và không mở lại trong 7 ngày là 82,83%; tỉ lệ bỏ qua gợi ý là 27,12%; tỉ lệ mở lại trong 7 ngày là 4,25%. Vì đợt chạy thử không có nhóm đối chứng, nhóm chỉ mô tả các chỉ số quan sát được, không kết luận trợ lý đã làm tăng chỉ số.

Hồ sơ launch đề xuất **Go có điều kiện** cho pilot `noi_dia` và `hang_nang`, phân nhóm ngẫu nhiên theo nhân viên (20 người dùng trợ lý, 20 đối chứng). Phương án chấp nhận MDE 6 điểm phần trăm và cần 859 yêu cầu mỗi nhóm; nếu tác động thật chỉ là 5 điểm, power ước tính còn khoảng 0,64. Điều kiện an toàn, người phụ trách và ngày kiểm tra được ghi trong `ho_so_launch_v0.md`. Kết quả hội đồng duyệt chéo chưa được cung cấp; cần cập nhật sau phiên trình bày.

## 5. Khó khăn và cách xử lý

Python mặc định ban đầu thiếu `pandas`, còn môi trường ảo cũ bị Windows chặn DLL NumPy. Nhóm tạo môi trường Python 3.12 riêng, cài thư viện theo `src/requirements.txt` và chạy lại chương trình; ba kiểm tra A1 cùng các phép tính A–D1 đạt kết quả đối chiếu. Đồng thuận nhãn lỗi ban đầu là 13/20 (65%), thấp hơn mục tiêu 80%; nhóm giữ nguyên hai bộ nhãn độc lập, thống nhất các ca bất đồng và viết lại quy tắc phân loại.

## 6. Tổng hợp đóng góp

Hà Minh Thắng phụ trách code `lab13.py` và tổng hợp bảng chi phí; Hồ Sỹ Tùng kiểm tra số, rà soát pilot và lập bộ nhãn lỗi thứ nhất; Lê Hoàng Sơn giữ hồ sơ, lập bộ nhãn lỗi thứ hai và tổng hợp chỉ số/kế hoạch pilot. Chi tiết bằng chứng được ghi trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Các phút xem lại/làm lại trong mô hình chi phí là `simulated`, chưa phải số đo vận hành; phân bổ chi phí cố định dựa trên giả định sản lượng tháng. Đợt chạy thử thiếu nhóm đối chứng nên chưa thể quy kết thay đổi chỉ số cho trợ lý. Với 40 nhân viên, thiết kế được chọn chưa đủ lực thống kê cho mức chênh 5 điểm theo giả định; nếu tác động thật chỉ là 5 điểm, power khoảng 0,64. Trước khi pilot, cần ghi nhận thời gian thực qua event, xác nhận đánh đổi với người có thẩm quyền và hoàn tất các điều kiện an toàn trong hồ sơ launch.

## 8. Tài liệu tham khảo

- Tài liệu đề bài, quy tắc, rubric và checkpoint Lab 13 trong repo.
- `docs/du_lieu_va_cong_thuc.md`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Google PAIR, *People + AI Guidebook*, mục “Errors + Graceful Failure”.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
