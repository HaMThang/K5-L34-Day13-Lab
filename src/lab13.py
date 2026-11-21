"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[
            vuot_gioi_han,
            ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']
        ] = 0

    tien_token = (
        runs['tokens_in'] / 1000 * gia_vao
        + runs['tokens_out'] / 1000 * gia_ra
    )
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = (
        reqs['phut_xem_lai_simulated'].sum()
        * luong_phut
        * he_so_xem_lai
    )
    lam_lai = (
        reqs['phut_lam_lai_simulated'].sum()
        * luong_phut
        * he_so_lam_lai
    )
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    if thanh_cong == 0:
        raise ValueError('Không có yêu cầu thành công để tính chi phí mỗi việc.')

    return {
        'token': tien_token.sum(),
        'tool': tien_tool.sum(),
        'chay_lai': (tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': (tien_token.sum() + tien_tool.sum()) / len(reqs),
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\nA2 · Mô hình chi phí')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')

    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f'{"loai":12s} {"so_yc":>8s} {"thanh_cong":>12s} '
          f'{"ty_le":>9s} {"lan_chay/yc":>13s} {"cps":>12s} {"so_voi_12000":>14s}')
    for loai in reqs['loai'].unique():
        reqs_loai = reqs[reqs['loai'] == loai]
        ket_qua_loai = mo_hinh(runs, reqs_loai)
        so_yc = len(reqs_loai)
        ty_le = ket_qua_loai['thanh_cong'] / so_yc
        lan_chay_moi_yc = reqs_loai['so_lan_chay'].sum() / so_yc
        print(f'{loai:12s} {so_yc:8,d} {ket_qua_loai["thanh_cong"]:12,d} '
              f'{ty_le:8.1%} {lan_chay_moi_yc:13.2f} '
              f'{ket_qua_loai["cps"]:12,.0f} '
              f'{ket_qua_loai["cps"] / BASELINE:13.2f}x')

    print('\nB1 · Độ nhạy (chi phí mỗi việc thành công)')
    kich_ban = {
        'Giá token gấp đôi': {'gia_vao': 52, 'gia_ra': 260},
        'Giá token giảm một nửa': {'gia_vao': 13, 'gia_ra': 65},
        'Xem lại gấp đôi': {'he_so_xem_lai': 2},
        'Xem lại giảm một nửa': {'he_so_xem_lai': 0.5},
        'Làm lại gấp đôi': {'he_so_lam_lai': 2},
        'Làm lại giảm một nửa': {'he_so_lam_lai': 0.5},
        'Lương tăng 25%': {'luong_phut': 2500},
        'Tối đa 2 lần chạy': {'max_lan_chay': 2},
        'Chỉ 1 lần chạy': {'max_lan_chay': 1},
    }
    cps_goc = ket_qua['cps']
    print(f'{"Kịch bản":26s} {"cps":>12s} {"thay_doi":>11s}')
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi = (cps / cps_goc - 1) * 100
        print(f'{ten:26s} {cps:12,.0f} {thay_doi:+10.1f}%')

    print('\nB2 · Giá token gấp đôi và xem lại gấp đôi')
    cps_cap = mo_hinh(
        runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2
    )['cps']
    print(f'{cps_cap:,.0f} đ ({(cps_cap / cps_goc - 1) * 100:+.1f}%)')

    print('\nB3 · Chi phí cả hệ thống theo giới hạn số lần chạy')
    print(f'{"gioi_han":>10s} {"tong_tro_ly":>16s} '
          f'{"khong_thanh_cong":>18s} {"tong_he_thong":>16s} {"cps":>12s}')
    for gioi_han in (1, 2, 3):
        ket_qua_gioi_han = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua_gioi_han['thanh_cong']
        tong_he_thong = (
            ket_qua_gioi_han['tong'] + khong_thanh_cong * BASELINE
        )
        print(f'{gioi_han:10d} {ket_qua_gioi_han["tong"]:16,.0f} '
              f'{khong_thanh_cong:18,d} {tong_he_thong:16,.0f} '
              f'{ket_qua_gioi_han["cps"]:12,.0f}')

    print('\nB4 · Xem lại 100% (noi_dia + hang_nang)')
    pham_vi = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    reqs_pham_vi = reqs[pham_vi]
    runs_pham_vi = runs[runs['request_id'].isin(reqs_pham_vi['request_id'])]
    ids_co_lan_chay_ok = runs_pham_vi.loc[
        runs_pham_vi['status'] == 'ok', 'request_id'
    ].unique()
    so_ca_xem_lai = len(ids_co_lan_chay_ok)
    so_ca_lam_lai = (reqs_pham_vi['ket_qua'] == 'lam_lai').sum()
    ket_qua_pham_vi = mo_hinh(runs, reqs_pham_vi)
    chi_phi_token_tool = ket_qua_pham_vi['token'] + ket_qua_pham_vi['tool']
    viec_thanh_cong = ket_qua_pham_vi['thanh_cong']
    for phut_lam_lai in (9, 15.3):
        chi_phi_xem_lai_100 = so_ca_xem_lai * 5 * LUONG_PHUT
        chi_phi_lam_lai = so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        cps_xem_lai_100 = (
            chi_phi_token_tool + chi_phi_xem_lai_100 + chi_phi_lam_lai
        ) / viec_thanh_cong
        print(f'Làm lại {phut_lam_lai:g} phút/ca: '
              f'{cps_xem_lai_100:,.0f} đ/việc '
              f'({cps_xem_lai_100 / BASELINE:.2f}x nhân viên)')

    print('\nD1 · Cỡ mẫu')
    from statistics import NormalDist

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
        z_power = NormalDist().inv_cdf(power)
        p_trung_binh = (p1 + p2) / 2
        tu_so = (
            z_alpha * math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
            + z_power * math.sqrt(
                p1 * (1 - p1) + p2 * (1 - p2)
            )
        ) ** 2
        return math.ceil(tu_so / (p2 - p1) ** 2)

    n_5_diem = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * 0.02
    n_nhan_vien_75 = math.ceil(n_5_diem * de_75)
    n_6_diem = co_mau(0.70, 0.76)
    m_20_nhan_vien = 1
    while (
        20 * m_20_nhan_vien
        / (1 + (m_20_nhan_vien - 1) * 0.02)
        < n_6_diem
    ):
        m_20_nhan_vien += 1
    de_6_diem = 1 + (m_20_nhan_vien - 1) * 0.02

    print(f'a) Chia theo yêu cầu, +5 điểm: {n_5_diem:,} mỗi nhóm')
    print(f'b) Theo nhân viên, 75 yêu cầu/người: DE={de_75:.2f}, '
          f'{n_nhan_vien_75:,} mỗi nhóm, '
          f'{math.ceil(n_nhan_vien_75 / 75)} nhân viên mỗi nhóm')
    print(f'c) 20 nhân viên mỗi nhóm: tối đa {20 / 0.02:,.0f} mẫu hiệu dụng')
    print(f'd) 6 depot mỗi nhóm: tối đa {6 / 0.02:,.0f} mẫu hiệu dụng')
    print(f'e) +6 điểm, {n_6_diem:,} mỗi nhóm: '
          f'{m_20_nhan_vien} yêu cầu/nhân viên, DE={de_6_diem:.2f}')
