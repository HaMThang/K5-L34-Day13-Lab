# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1.2 |
| Số lần chạy trung bình, chạy đến khi đúng | 1.25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1.25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` (tổng((tokens_in / 1000 × 26) + (tokens_out / 1000 × 130)) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi)(tổng(tool_calls) × 15) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) (phut_xem_lai_simulated × 2.000 đ/phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) (phut_lam_lai_simulated × 2.000 đ/phút) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua == thanh_cong` | |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | (token + tool) / 1.200 = 274,7 | đo từ trace |

- Chi phí mỗi việc thành công gấp khoảng **16,3 lần** hoá đơn token và tool chia cho số yêu cầu (4.472 / 274,7).
- Khoản lớn nhất là **làm lại: 51,8%** tổng chi phí; xem lại chiếm 40,7% (hai khoản tính từ phút `simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22x |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69x |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88x |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85x |

- **quoc_te** không đáng để trợ lý xử lý: chi phí 22.515 đ/việc, bằng 1,88x nhân viên, và chỉ 27,3% thành công.
- Chạy lại không giúp: tỉ lệ `ok` của `quoc_te` giảm từ 30,0% ở lần 1 xuống 11,4% ở lần 2 và 2,2% ở lần 3; nên loại này khỏi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38x |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48x |

- Cách tính: 45.000 × (900 / 1.200) = 33.750 việc thành công; 40.000.000 / 33.750 = 1.185 đ chi phí cố định/việc. Nửa khối lượng còn 16.875 việc thành công, nên chi phí cố định là 2.370 đ/việc.
- Chi phí cố định làm tăng chi phí thêm 1.185 đ/việc ở 45.000 yêu cầu/tháng và 2.370 đ/việc ở nửa khối lượng, nhưng chưa đổi kết luận: cả hai mức vẫn thấp hơn 12.000 đ/việc của nhân viên.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (simulated) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (simulated) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%) (simulated)**. Do mô hình cộng tuyến tính, mức tăng gần bằng tổng hai tác động riêng.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | 6.901.220 đ (simulated) | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ), nhưng không trùng với mức CPS thấp nhất: giới hạn **1 lần** có CPS 4.111 đ. Giới hạn 1 lần chuyển thêm 85 yêu cầu sang nhân viên so với giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

- Khi xem lại 100% (`noi_dia` + `hang_nang`): **11.743 đ/việc = 0,98×** mức 12.000 đ nếu làm lại mất 9 phút/ca; nếu dùng mức 15,3 phút/ca từ dữ liệu thì **12.415 đ/việc = 1,03× (simulated)**.
- Kết quả cho thấy xem lại 100% gần như mất hết lợi thế chi phí; pilot cần đo xem có thể giảm tỉ lệ xem lại an toàn đến đâu và thời lượng xem lại thực tế có thấp hơn mức hòa vốn khoảng 4,8–5,1 phút/ca không.
