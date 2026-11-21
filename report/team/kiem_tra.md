# Tổng kiểm tra công việc Người 2 — Lab 13

**Mục tiêu:** Hoàn tất tất cả phần Người 2 có thể làm độc lập; sau đó chỉ còn buổi đối chiếu và thống nhất với Người 3.

## 1. Kết luận nhanh

Các phần A/B và phép tính D1 đã có kết quả kiểm tra trong hồ sơ. Kế hoạch Pilot đã được rà soát và có danh sách chỉnh sửa gửi Người 3. Bảng khắc phục 5 loại lỗi đã được điền trong bản chuẩn bị.

**Chưa thể xác nhận chỉ còn việc gặp Người 3**, vì bộ nhãn hiện tại của Người 2 đang được ghi nhận là nhãn tham khảo từ đáp án/hướng dẫn, chưa chứng minh được tính độc lập. Cần đọc lại đúng 20 tình huống gốc và tự xác nhận nhãn trước khi khóa bộ nhãn.

Ngoài ra, tệp ZIP hiện có trong lượt tải lên là bộ **Day 12**, không chứa tài liệu 20 ca lỗi Lab 13. Cần có `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` hoặc ZIP Lab 13 để hoàn tất bước này.

## 2. Kiểm tra A/B

Các kết quả dưới đây khớp với kết quả chạy đã được lưu trong hồ sơ nhóm/cuộc trao đổi trước đó. Trong lượt kiểm tra này không có source `src/lab13.py` và CSV Lab 13 để chạy lại từ dữ liệu gốc, vì vậy đây là kiểm tra chéo trên kết quả đã ghi, không phải lần chạy độc lập mới.

| Hạng mục | Kết quả kiểm tra |
|---|---|
| A2 | Tổng chi phí 4.373.585đ; 978 việc thành công; CPS 4.472đ |
| A4 | Dùng mẫu số 900 việc thành công trong 1.200 yêu cầu của `noi_dia` + `hang_nang`; kết quả 45.000 yêu cầu/tháng: 4.599đ/CPS; nửa khối lượng: 5.784đ/CPS |
| B1 | Tác động lớn nhất: làm lại gấp đôi (+51,8%); xem lại gấp đôi (+40,7%); lương +25% (+23,1%) |
| B2 | Token gấp đôi + xem lại gấp đôi: CPS 6.543đ, tăng 46,3% |
| B3 | Tổng chi phí hệ thống thấp nhất ở giới hạn 2 lần chạy: 6.901.220đ; CPS thấp nhất ở giới hạn 1 lần: 4.111đ |
| B4 | Xem lại 100%, giả định làm lại 9 phút: CPS 11.743đ; thay bằng trung bình simulated 15,3 phút: CPS khoảng 12.414đ |

Lưu ý:
- B3 phải trình bày riêng hai tiêu chí: tổng chi phí hệ thống và CPS. Không kết luận một giới hạn chạy tối ưu cho cả hai.
- B4 với 15,3 phút là kịch bản dựa trên dữ liệu `simulated`, không phải số đo vận hành thực tế.
- Nếu cộng chi phí nhân viên xử lý các ca chuyển tiếp, phải ghi rõ mẫu số là mỗi yêu cầu hay mỗi việc thành công; không trộn hai cách tính.

## 3. Kiểm tra độc lập D1

### 3.1. So sánh hai tỷ lệ với MDE 5 điểm

Với `p1 = 0,70`, `p2 = 0,75`, `alpha = 0,05`, `power = 0,80`, công thức xấp xỉ hai tỷ lệ độc lập cho khoảng 1.250,72 yêu cầu/nhóm, làm tròn lên **1.251 yêu cầu/nhóm**.

### 3.2. Điều chỉnh theo cụm với m = 75

`DE = 1 + (75 - 1) × 0,02 = 2,48`

`1.251 × 2,48 = 3.102,48`, làm tròn lên **3.103 yêu cầu/nhóm**.

`3.103 / 75 = 41,37`, do đó cần **42 nhân viên/nhóm**, tổng 84 người; vượt quá 40 người hiện có.

### 3.3. Giới hạn 20 nhân viên/nhóm

`20 / 0,02 = 1.000` yêu cầu hiệu dụng tối đa/nhóm, thấp hơn 1.251; không đủ cho MDE 5 điểm theo giả định này.

### 3.4. Giới hạn 6 depot/nhóm

`6 / 0,02 = 300` yêu cầu hiệu dụng tối đa/nhóm; thấp hơn 1.251 và chỉ có 6 cụm, không đạt yêu cầu 20 cụm/nhóm.

### 3.5. Chấp nhận MDE 6 điểm

Với `p1 = 0,70`, `p2 = 0,76`, công thức xấp xỉ cho khoảng 858,27 yêu cầu/nhóm, làm tròn lên **859**.

Giải bất đẳng thức:

`20m / [1 + (m - 1) × 0,02] >= 859`

cho kết quả `m >= 298,52`, do đó cần tối thiểu **299 yêu cầu/nhân viên**.

Kiểm tra:

`DE = 1 + (299 - 1) × 0,02 = 6,96`

`20 × 299 / 6,96 ≈ 859,2`

**Kết luận D1:** Các kết quả 1.251, 3.103, 1.000, 300, 859, DE 6,96 và 299 yêu cầu/nhân viên nhất quán theo các giả định nêu trên. Đánh đổi là nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64; Giám đốc vận hành phải chấp nhận trước Pilot.

## 4. Rà soát `pilot_plan.yaml`

### 4.1. Phần đã có

- YAML đọc được.
- Chọn `noi_dia` và `hang_nang`; loại `quoc_te` và `doi_tac` có nêu lý do.
- Chia theo nhân viên, 20 người nhóm trợ lý và 20 người đối chứng.
- Có ngẫu nhiên hóa, seed và phân tầng theo depot.
- Có chỉ số chính, MDE, alpha, power và cỡ mẫu.
- Có ba luật dừng, người có quyền dừng, rollback và ngày quyết định.
- Có liệt kê các đầu vào `_simulated`.

### 4.2. Các điểm Người 3 cần xử lý

1. **CPS:** 4.472đ là kết quả A2 toàn bộ mẫu, không phải CPS riêng của phạm vi Pilot. Chi phí Pilot phải tính đúng `noi_dia` + `hang_nang`, và cần nói rõ có/không bao gồm chi phí nhân viên xử lý chuyển tiếp.
2. **Rollout:** `rollout: [0.10, 0.25, 0.50]` trên tổng 40 nhân viên tương ứng 4, 10, 20 nhân viên được mở trợ lý; không phải 4, 10, 20 người ở mỗi nhóm. Cần sửa chú thích để không mâu thuẫn với thiết kế 20 treatment + 20 control.
3. **Cỡ mẫu/thời gian:** ghi rõ thời gian dự kiến để mỗi người đạt 299 yêu cầu; không kết luận hiệu quả nếu chưa đủ mẫu.
4. **Hoàn tiền trùng:** viết lại điều kiện để biết một giao dịch hoàn trùng đã xác nhận kích hoạt dừng ngay hay phải theo dõi trong cửa sổ 3 ngày. Khuyến nghị an toàn: một ca hoàn trùng đã xác nhận là trigger độc lập để tắt trợ lý.
5. **Định nghĩa metric:** định nghĩa mẫu số, điều kiện thành công trong 24 giờ, thời điểm bắt đầu đồng hồ và cách xác định không mở lại trong 7 ngày; áp dụng giống nhau cho hai nhóm.
6. **Ngưỡng CPS 8.000đ:** cần ghi rõ CPS dùng mẫu số nào và có tính chi phí nhân viên làm thay hay không.

### 4.3. Nhãn simulated

Các số phút xem lại/làm lại từ `phut_xem_lai_simulated` và `phut_lam_lai_simulated`, CPS tính từ các dữ liệu mô phỏng, và các tỷ lệ so sánh với 12.000đ dựa trên dữ liệu mô phỏng phải được đánh dấu `simulated`. Không mô tả là số đo vận hành thật.

