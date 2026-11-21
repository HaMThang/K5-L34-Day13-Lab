# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số ở bảng E1 tính trực tiếp từ `src/logix_requests.csv` (1.200 yêu cầu, đọc với `keep_default_na=False`). Ba chỉ số này không dùng cột `_simulated`. Số ở bảng E2 lấy từ `bang_chi_phi.md` (A4, B1, B4), do `src/lab13.py` tính.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: tỉ lệ yêu cầu của nhóm trợ lý có gợi ý được hiện cho nhân viên | số `agent_suggestion_shown` ÷ số `refund_request_created` có `arm` = trợ lý, theo tuần và theo `staff_id` | Không cần tính |
| An toàn | Nhóm tự đề xuất: tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | số `audit_sample_checked` có `so_tien_da_hoan` ≠ `so_tien_dung` ÷ số đơn được kiểm, mẫu 100 đơn mỗi tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng.

Số tham chiếu cho ngưỡng an toàn: tỉ lệ mở lại 7 ngày trong phạm vi `noi_dia` + `hang_nang` là 3,97% (39/982); tỉ lệ `lam_lai` trong phạm vi này là 4,89% (48/982). Chỉ số chính ở trên là 82,83%, cao hơn mốc baseline 0,70 của đề, nhưng chưa có đối chứng nên không kết luận là do trợ lý.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm (trợ lý/đối chứng), created_at, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| staff_review_decision | Nhân viên | staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn phí |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển cho nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** mỗi chỉ số và event dùng để tính.

- Chỉ số chính: `refund_request_created` (created_at) và `ticket_closed` (closed_at) cho điều kiện đóng trong 24 giờ; `ticket_reopened` cho điều kiện không mở lại trong 7 ngày. Nối bằng `trace_id`. Tính được.
- Chỉ số dùng (bỏ qua gợi ý): `agent_suggestion_shown` và `staff_review_decision` (quyet_dinh). Tính được.
- Chỉ số an toàn (mở lại 7 ngày): `ticket_reopened` chia số `ticket_closed`/`refund_request_created`. Tính được.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` theo `arm`. Tính được.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`. Tính được.
- Chi phí thật (phút xem lại, làm lại đo thật thay cho phút simulated): `staff_review_decision` và `staff_rework_completed`. Tính được từ tuần 1 của pilot.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Mọi số tiền dưới đây phụ thuộc cột `_simulated` nên phải ghi nhãn simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%: chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ (B1) [simulated] | Tỉ lệ `staff_rework_completed` theo tuần vượt 7% (đợt chạy thử: 4,89% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ/việc = 0,98× của 12.000 đ (làm lại 9 phút/ca); 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như dữ liệu (B4) [simulated] | % yêu cầu được xem lại còn trên 50% cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến, chi phí cố định 40 triệu đ/tháng chia cho ít việc | Cố định cộng thêm 1.185 đ/việc ở 45.000 yêu cầu/tháng (tổng 4.599 đ = 0,38×) và 2.370 đ/việc nếu còn một nửa (tổng 5.784 đ = 0,48×) (A4) [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
