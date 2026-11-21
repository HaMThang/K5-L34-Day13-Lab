# K5 · L34 · Day 13 Lab — Định giá agent và lập kế hoạch pilot

Lab buổi chiều Ngày 13 (Launch & Economics) của chương trình VinUni AI 20k. Mỗi nhóm dựng một bộ **hồ sơ launch v0** cho trợ lý hoàn phí của công ty giả định **LogiX-VN**, rồi bảo vệ hồ sơ trước một nhóm khác đóng vai hội đồng **Gate 2a**.

Bộ hồ sơ phải trả lời bốn câu hỏi:

1. **Có đáng chạy không?** Chi phí thật cho mỗi việc thành công, so với nhân viên tự làm.
2. **Nhân viên có dùng không?** Chỉ số sử dụng và danh sách event cần ghi.
3. **Khi hỏng thì sao?** Phân loại lỗi và cách khắc phục, mỗi cách có người phụ trách.
4. **Pilot thiết kế thế nào để ra được quyết định?** Có nhóm đối chứng, đủ cỡ mẫu, có luật dừng.

> Toàn bộ dữ liệu là **giả lập**. Lab không cần khoá API và không cần mạng trong lúc làm.

## Bối cảnh

| Thông tin | Giá trị |
| --- | --- |
| Quy mô LogiX-VN | 12 depot, khoảng 40 nhân viên CSKH |
| Lượng yêu cầu hoàn phí | khoảng 45.000 / tháng (1.500 / ngày) |
| Đợt chạy thử | 2 tuần ở 6 depot |
| Dữ liệu được phát | mẫu ngẫu nhiên 1.200 yêu cầu, 1.624 lần chạy của agent |

## Nội dung repo

| File | Nội dung |
| --- | --- |
| [`Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](Lab13_Huong_dan_chi_tiet_buoi_chieu.md) | Hướng dẫn từng bước cho 5 nhiệm vụ A–E: cách làm, code mẫu, số để tự đối chiếu, lỗi hay gặp |
| `Ngay13_Lab13_De_bai_hoc_vien.docx` | Đề bài Lab 13 bản gốc |
| `Ngay13_Huong_dan_hoc_vien.docx` | Hướng dẫn học viên cả ngày: lịch, công thức, cách tổ chức nhóm, cách chấm |
| `Ngay13_Slide_Launch_Economics.pdf` | Slide buổi sáng |
| `lab13_starter.py` | File khởi đầu: hằng số giá, khung hàm và ba phép thử đáp án biết trước |
| `logix_runs.csv` | 1.624 lần chạy của agent: `run_id, request_id, trace_id, attempt, tokens_in, tokens_out, tool_calls, status` |
| `logix_requests.csv` | 1.200 yêu cầu: `depot, staff_id, loai, so_tien_vnd, so_lan_chay, ket_qua, duoc_xem_lai, quyet_dinh_xem_lai, phut_xem_lai_simulated, phut_lam_lai_simulated, dong_trong_24h, mo_lai_trong_7_ngay` |

### Giá trị của một số cột

- `loai`: `noi_dia` (nội địa thường), `hang_nang` (hàng nặng, cồng kềnh), `quoc_te` (quốc tế), `doi_tac` (khách đối tác có điều khoản riêng).
- `ket_qua`: `thanh_cong` (đã đóng, không mở lại trong 7 ngày, không sai tiền), `lam_lai` (trả lời sai, nhân viên phải làm lại), `chuyen_nhan_vien` (chạy hết 3 lần vẫn lỗi, chuyển cho nhân viên).
- `quyet_dinh_xem_lai`: `giu`, `sua`, `bo`; để trống nếu không được xem lại.
- Hai cột đuôi `_simulated` là số phút giả lập. **Mọi con số tính từ hai cột này phải ghi nhãn `simulated`** trong hồ sơ.

## Bắt đầu nhanh

Cần Python 3.10 trở lên.

```bash
git clone https://github.com/VinUni-AI20k/K5-L34-Day13-Lab.git
cd K5-L34-Day13-Lab

python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install pandas numpy scipy statsmodels pyyaml
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"

python lab13_starter.py              # sẽ báo NotImplementedError cho tới khi bạn viết xong các hàm
```

Đọc dữ liệu luôn kèm `keep_default_na=False`, nếu không ô trống trong `quyet_dinh_xem_lai` sẽ thành `NaN` và các phép so sánh phía sau sai:

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

## Số liệu dùng chung (giả định của lab)

| Khoản | Giá trị |
| --- | --- |
| Token đầu vào | 26 đ / 1.000 token |
| Token đầu ra | 130 đ / 1.000 token |
| Gọi tool | 15 đ / lần |
| Thời gian nhân viên | 2.000 đ / phút (đã gồm bảo hiểm, văn phòng) |
| Nhân viên tự làm một yêu cầu | 6 phút = 12.000 đ |
| Chi phí cố định của trợ lý | 40 triệu đ / tháng |

## Năm nhiệm vụ

| Giờ | Nhiệm vụ | Thời gian | Sản phẩm |
| --- | --- | --- | --- |
| 14:10 | **A · Mô hình chi phí mỗi việc thành công**: ba phép thử A1, bảng chi phí từ trace (A2), tách theo loại yêu cầu (A3) | 40 + 3 phút | `lab13.py`, `bang_chi_phi.md` |
| 14:53 | **B · Bảng độ nhạy**: đổi từng yếu tố, đổi một cặp, giới hạn chạy lại, kịch bản xem lại 100% | 25 + 2 phút | `bang_chi_phi.md` |
| 15:35 | **C · Bảng lỗi và cách khắc phục**: gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, đồng thuận ≥ 80%, bảng khắc phục 5 ca | 30 + 3 phút | `bang_loi.md` |
| 16:08 | **D · pilot_plan.yaml**: cỡ mẫu theo ba cách chia, năm câu "tách được tác động", luật dừng | 25 + 3 phút | `pilot_plan.yaml` |
| 16:36 | **E · Chỉ số, rủi ro kinh tế, hồ sơ launch v0**: đặc tả chỉ số, danh sách event có `trace_id`, risk register, trang hồ sơ 7 mục | 20 + 4 phút | `chi_so.md`, `ho_so_launch_v0.md` |
| 17:00 | **Duyệt chéo Gate 2a**: nhóm n chấm nhóm n + 1 | 45 phút | `phieu_cham.md` |
| 17:45 | Đóng gói, nộp (hạn 18:00) | 15 phút | |

Chi tiết từng bước nằm trong [`Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## Sáu công thức của cả ngày

| Tên | Công thức |
| --- | --- |
| Chi phí mỗi việc thành công | (token + tool + xem lại + làm lại) ÷ số việc thành công. Tử số tính **mọi** lần chạy, kể cả lần lỗi |
| Số lần chạy trung bình, tối đa k lần | (1 − (1 − p)^k) ÷ p |
| Tỉ lệ thành công sau tối đa k lần | 1 − (1 − p)^k |
| Cỡ mẫu mỗi nhóm, so hai tỉ lệ | (z₁₋α/₂·√(2p̄(1 − p̄)) + z₁₋β·√(p₁(1 − p₁) + p₂(1 − p₂)))² ÷ (p₂ − p₁)² |
| Hệ số thiết kế | 1 + (m − 1) × ICC, với m là số yêu cầu mỗi cụm |
| Cỡ mẫu hiệu dụng khi chia theo cụm | c × m ÷ hệ số thiết kế, luôn nhỏ hơn c ÷ ICC |

## Nộp bài

Nộp một thư mục tên `lop_nhom` (ví dụ `L3A_nhom04`) trước 18:00:

| File | Nội dung | Nhiệm vụ |
| --- | --- | --- |
| `lab13.py` | Code chạy được từ đầu đến cuối, in ra các bảng | A, B, D1 |
| `bang_chi_phi.md` | Bảng A2, A3, bảng độ nhạy, câu trả lời B3 và B4 | A, B |
| `bang_loi.md` | Hai bộ nhãn, tỉ lệ đồng thuận, bảng khắc phục 5 ca | C |
| `pilot_plan.yaml` | Kế hoạch pilot, không còn dấu `?` | D |
| `chi_so.md` | Đặc tả chỉ số, danh sách event, các dòng rủi ro kinh tế | E |
| `ho_so_launch_v0.md` | Một trang, bảy mục, dòng cuối là đề xuất Go / Go có điều kiện / No-go | E |
| `phieu_cham.md` | Phiếu nhóm bạn chấm nhóm khác | Duyệt chéo |

**Kiểm tra trước khi nộp**

- [ ] `python3 lab13.py` chạy hết trên một máy khác trong nhóm
- [ ] Ba phép thử A1 ra đúng 1,20 · 1,25 · 1,25
- [ ] Mọi con số giả lập có nhãn `simulated`
- [ ] Mỗi mục hồ sơ có người phụ trách là một vai trò, không ghi "cả đội"
- [ ] Đề xuất là một trong ba: Go, Go có điều kiện, No-go
- [ ] Không dùng từ "production": Gate 2a chỉ duyệt kế hoạch pilot

## Cách chấm

| Phần | Điểm | Ai chấm |
| --- | --- | --- |
| Đối chiếu đáp án: A 20 · B 15 · C 10 · D 15 · E 10 (số được nhận nếu lệch không quá 2%) | 70 | Trợ giảng |
| Hội đồng: đề xuất khớp bằng chứng · số giả lập và phạm vi · pilot ra được quyết định (mỗi tiêu chí 0 / 5 / 10) | 30 | Nhóm khác |

Một đề xuất **No-go có lý do bằng số** được điểm cao hơn một đề xuất **Go bỏ qua con số bất lợi**.

## Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
