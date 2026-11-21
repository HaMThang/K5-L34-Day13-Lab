# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: [điền tên nhóm] · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token và tool chia số yêu cầu (274,7 đ, đo từ trace). Làm lại chiếm 51,8% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất 1. Số ca làm lại gấp đôi +51,8% · 2. Xem lại gấp đôi +40,7% · 3. Lương +25% làm tăng +23,1%; giá token gấp đôi chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm Cả hệ thống (cộng phần nhân viên làm thay 222 yêu cầu): 7.037.585 đ / 1.200 = 5.865 đ/yêu cầu = 0,49× của 12.000 đ. Phạm vi `noi_dia` + `hang_nang` cộng cố định: 4.599 đ = 0,38×. `quoc_te` 1,88× và `doi_tac` 0,85× bị loại. Xem lại 100%: 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); số trong đợt chạy thử, không có đối chứng. Chi tiết: `chi_so.md` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận hai bộ nhãn độc lập 13/20 = 65%, dưới mục tiêu 80%, nên đã viết lại định nghĩa năm loại; 7 ca lệch đã thống nhất theo nguyên nhân gốc. Bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có ngưỡng đo được và một vai trò phụ trách. Chi tiết: `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên, ngẫu nhiên: 20 nhân viên dùng trợ lý + 20 đối chứng (20 cụm mỗi nhóm). Chỉ `noi_dia` + `hang_nang`. Mức chênh 6 điểm, n = 859 mỗi nhóm (hệ số thiết kế 6,96, m = 299 yêu cầu mỗi nhân viên); nếu tác động thật chỉ 5 điểm thì power còn 0,64. 3 luật dừng có ngưỡng và người có quyền dừng. Ngày quyết định 2027-01-05. Chi tiết: `pilot_plan.yaml` [simulated: ngưỡng chi phí 8.000 đ] | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế Làm lại gấp đôi: 6.787 đ (+51,8%) · xem lại 100%: 0,98× đến 1,03× · khối lượng giảm một nửa: cố định thành 2.370 đ/việc. Chi tiết: `chi_so.md` E2 [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chia theo nhân viên (20 + 20), chỉ `noi_dia` và `hang_nang`. Gate 2a chỉ duyệt kế hoạch pilot, chưa duyệt chạy chính thức.

Lý do: ở quy mô đầy đủ, chi phí cả hệ thống 0,49× và trong phạm vi pilot 0,38× của 12.000 đ [simulated]; `quoc_te` (1,88×) và `doi_tac` (0,85×) bị loại.

Con số bất lợi và cách xử lý:
- Xem lại 100% chỉ còn 0,98×, và 1,03× (đắt hơn nhân viên tự làm) nếu làm lại 15,3 phút/ca [simulated] → pilot phải đo phút thật và giảm xem lại theo bậc.
- Chỉ đủ mẫu cho mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power chỉ 0,64 → Giám đốc vận hành ký chấp nhận đánh đổi.
- `hang_nang` có chi phí 8.221 đ/việc [simulated], đã vượt ngưỡng dừng 8.000 đ của pilot → bước đầu chỉ chạy `noi_dia`, mở `hang_nang` khi chi phí đo thật dưới ngưỡng.
- Đồng thuận gắn nhãn lỗi chỉ 65% (13/20), dưới 80% → đã viết lại định nghĩa năm loại, cần gắn nhãn lại một mẫu ca mới trước khi pilot.

Điều kiện, người phụ trách, ngày kiểm tra (ngày là đề xuất, nhóm xác nhận lại với lịch thật):

| # | Điều kiện | Người phụ trách | Ngày kiểm tra |
| --: | --- | --- | --- |
| 1 | Sửa khoá chống trùng khi gửi lại yêu cầu (ca 20) và đối soát sổ cái trước khi báo "đã hoàn" (ca 7) | Kỹ sư trưởng agent | 2026-12-15 |
| 2 | Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm) | Giám đốc vận hành LogiX-VN | 2026-12-15 |
| 3 | Bật đủ 10 event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1 của pilot | PM trợ lý hoàn phí | 2026-12-22 |
| 4 | Có kế hoạch giảm tỉ lệ xem lại theo bậc (bỏ khi sửa + bỏ dưới 15%) vì xem lại 100% không tiết kiệm | Trưởng nhóm CSKH | 2026-12-22 |
| 5 | Chốt seed ngẫu nhiên và danh sách 20 + 20 nhân viên, phân tầng theo depot, trước ngày bắt đầu | PM trợ lý hoàn phí | 2026-12-29 |

Nếu điều kiện 1 hoặc 2 chưa đạt ở ngày kiểm tra thì không bắt đầu pilot (chuyển thành No-go cho tới khi đạt).
