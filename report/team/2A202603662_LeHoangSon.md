# Báo cáo cá nhân — Lê Hoàng Sơn - 2A202603662

## 1. Thông tin thành viên

- Họ tên: Lê Hoàng Sơn
- MSSV: 2A202603662
- Email: leson121105@gmail.com
- Vai trong nhóm: người gắn nhãn 2 kiêm giữ hồ sơ (Người 3 trong bản phân công nhóm 3 người)

## 2. Phần việc phụ trách

- Giữ hồ sơ: điền dần `report/team/ho_so_launch_v0.md` từ đầu buổi, tổng hợp số từ các nhiệm vụ A–D.
- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi (bộ nhãn thứ hai), sau đó cùng người gắn nhãn 1 so nhãn, thống nhất ca không trùng và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Nhiệm vụ D: soạn `report/team/pilot_plan.yaml` (đối chứng, cách chia, đánh đổi, ba luật dừng, rollback), dùng cỡ mẫu D1 do người viết code tính.
- Nhiệm vụ E: soạn `report/team/chi_so.md` (đặc tả chỉ số, danh sách event, rủi ro kinh tế) và hoàn thiện `ho_so_launch_v0.md`, gồm đề xuất cuối.

## 3. Đóng góp cụ thể

- **`chi_so.md`:**
  - Ba chỉ số E1 tính trực tiếp từ `src/logix_requests.csv`: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200).
  - Đề xuất thêm một chỉ số dùng và một chỉ số an toàn.
  - Lập danh sách 10 event, mỗi event có `trace_id`, kèm phần kiểm tra chéo chỉ số với event.
  - Ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy: làm lại gấp đôi +51,8% (6.787 đ), xem lại 100% 0,98× đến 1,03×, chi phí cố định 1.185 đến 2.370 đ/việc (đều simulated).
- **`bang_loi.md`:**
  - Gắn bộ nhãn độc lập thứ hai cho 20 ca. Đồng thuận với bộ nhãn thứ nhất là 13/20 = 65%, dưới mục tiêu 80%.
  - Viết lại định nghĩa năm loại, ghi quy tắc phân biệt cho 7 ca lệch (2, 3, 4, 10, 13, 16, 19).
  - Điền bảng khắc phục 5 ca (9, 7, 18, 4, 17) với cách phát hiện đo được và vai trò phụ trách.
- **`pilot_plan.yaml`:**
  - Điền D1 a–e (1.251 · 3.103 · 1.000 · 300 · m ≥ 299), D2 năm câu và đánh đổi mức chênh 6 điểm. Tự tính lại power: 0,64 ở mức 5 điểm, 0,80 ở mức 6 điểm.
  - Ba luật dừng đủ bốn vế (an toàn, chi phí, mức độ sử dụng), rollback 30 phút, ngày quyết định.
- **`ho_so_launch_v0.md`:** điền bảy mục (con số, trạng thái, vai trò phụ trách), soạn đề xuất **Go có điều kiện** kèm bốn con số bất lợi và năm điều kiện có người phụ trách và ngày kiểm tra.
- **Rà soát:** phát hiện ô A1 dòng 2 trong `bang_chi_phi.md` ghi `1` thay vì `1,25`; phát hiện lệnh kiểm tra YAML của đề lỗi trên Windows do bảng mã cp1258 (cần `encoding='utf-8'`).

## 4. Bằng chứng

- Commit (Son0709): `b7bd5f7`, `e814894`, `26323f4`, `bdaba4a`, `2243aea`, `87ecb55`, `33d52b0`, `1039cdf`.
- File: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/pilot_plan.yaml`, `report/team/bang_loi.md`.
- Con số tự tính hoặc kiểm tra: 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%; phạm vi `noi_dia` + `hang_nang` (982 yêu cầu) mở lại 3,97%, làm lại 4,89%; power 0,641 (mức 5 điểm) và 0,800 (mức 6 điểm) với n = 859 mỗi nhóm; chi phí cả hệ thống 7.037.585 đ / 1.200 = 5.865 đ/yêu cầu = 0,49×.

## 5. Công cụ AI đã dùng

- Công cụ: Claude Code (trong VS Code).
- Dùng vào việc: đọc đề và tài liệu để nắm phần việc, dựng khung và soạn nháp `chi_so.md`, `ho_so_launch_v0.md`, `pilot_plan.yaml`, phần quy tắc và bảng khắc phục trong `bang_loi.md`, và bản nháp báo cáo này.
- Cách tự kiểm tra:
  - Ba chỉ số E1 và power được tính lại bằng đoạn code chạy trực tiếp trên CSV, rồi đối chiếu số trong tài liệu hướng dẫn; đều khớp.
  - Số A, B, D1 trong hồ sơ được đối chiếu với output thực của `python lab13.py`.
  - Đã chạy `yaml.safe_load` với `encoding='utf-8'` để kiểm tra `pilot_plan.yaml`, và grep toàn bộ `report/team` để kiểm tra không dùng từ bị cấm theo quy tắc 5 của lab.
- Lưu ý về độc lập (C): bộ nhãn độc lập của tôi do tôi tự gắn, không nhờ AI. Tuy nhiên AI đã đọc tài liệu hướng dẫn (có nhãn tham khảo) khi soạn phần quy tắc phân biệt và nhãn thống nhất, nên phần đó tôi và Người 2 đã rà lại theo định nghĩa của đề.
- Ngưỡng cảnh báo trong bảng khắc phục (2%, 20%, 1%) và các ngày kiểm tra điều kiện là đề xuất của nhóm, không phải số đo từ dữ liệu.

## 6. Tự đánh giá

- **Làm tốt:** hồ sơ nêu cả con số bất lợi (xem lại 100% đạt 1,03×, power 0,64, `hang_nang` 8.221 đ chạm ngưỡng dừng 8.000 đ, đồng thuận nhãn 65%) cùng cách xử lý, thay vì chỉ đưa số có lợi. Mọi số simulated đều có nhãn và mọi người phụ trách là một vai trò cụ thể.
- **Chưa tốt:** đồng thuận gắn nhãn chỉ 65%, chưa đạt 80%; hai bên chưa phân biệt rõ ranh giới Ngữ cảnh với Giới hạn hệ thống ngay từ đầu. Ngưỡng cảnh báo và ngày kiểm tra chưa có số đo thật làm cơ sở.
- **Bài học:** gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa; tử số chi phí phải tính mọi lần chạy, kể cả lần lỗi; so với 12.000 đ phải dùng chi phí cả hệ thống chứ không chỉ chi phí mỗi việc thành công; và một đề xuất có nêu số bất lợi đáng tin hơn một đề xuất chỉ nêu số tốt.
