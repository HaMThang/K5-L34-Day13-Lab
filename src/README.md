# Source code

Code khởi đầu và dữ liệu giả lập của Lab 13. **Mọi lệnh chạy trong thư mục `src/`.**

- File bắt đầu chạy: `lab13_starter.py` (file mẫu). Bài nộp là `lab13.py`, copy từ file mẫu ở CP1.
- Cách chạy: `python3 lab13.py` (khi chưa copy: `python3 lab13_starter.py`).
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, đọc bằng `pd.read_csv(..., keep_default_na=False)` cho file yêu cầu.
- Output: in ra stdout ba phép thử A1, các bảng A2, A3, độ nhạy (B) và cỡ mẫu (D1). Nhóm chép số vào các file trong `report/team/`.
- File học viên được sửa: `lab13.py`. Không sửa hai file CSV.

## Cài đặt

Cần Python 3.10 trở lên. Lab không cần khoá API và không cần mạng trong lúc làm.

macOS / Linux:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
cp lab13_starter.py lab13.py
python lab13.py                      # báo NotImplementedError cho tới khi viết xong các hàm
```

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
Copy-Item lab13_starter.py lab13.py
python lab13.py
```

Dòng `python -c ...` phải in ra `san sang`.

## File trong thư mục

| File | Nội dung |
| --- | --- |
| `lab13_starter.py` | File mẫu: hằng số giá, khung hàm A1, A2 và ba phép thử đáp án biết trước. Chỗ cần viết có dòng `VIẾT Ở ĐÂY` và `TODO CP1`, `TODO CP2`, `TODO CP4` |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu hoàn phí |
| `requirements.txt` | Thư viện cần cài |

Ý nghĩa từng cột và các công thức: [docs/du_lieu_va_cong_thuc.md](../docs/du_lieu_va_cong_thuc.md).

## Đọc dữ liệu đúng cách

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Thiếu `keep_default_na=False`, ô trống trong cột `quyet_dinh_xem_lai` bị đọc thành `NaN` và các phép so sánh phía sau sai.
