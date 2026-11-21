# Báo cáo kiểm tra kế hoạch Pilot — Vai trò Người 2

**Tài liệu được kiểm tra:** `pilot_plan.yaml`  
**Phạm vi:** Kiểm tra công thức, giả định, chi phí, phạm vi Pilot, luật dừng và dữ liệu mô phỏng.  
**Kết luận:** YAML đọc được và các phép tính D1 được ghi trong kế hoạch nhất quán về số học. Tuy nhiên, cần làm rõ một số nội dung trước khi chốt kế hoạch Pilot.

---

## 1. Kết quả kiểm tra

| Hạng mục | Kết quả | Nhận xét |
|---|---|---|
| Cú pháp YAML | Đạt | File đọc được bằng `yaml.safe_load`. |
| Phạm vi Pilot | Đạt về lập luận | Chọn `noi_dia` và `hang_nang`; loại `quoc_te` và `doi_tac` có nêu lý do. |
| Chia nhóm | Đạt về mô tả | 20 nhân viên nhóm trợ lý và 20 nhân viên nhóm đối chứng. |
| Ngẫu nhiên hóa | Đạt về mô tả | Có ghi ngẫu nhiên bằng code, seed và phân tầng theo depot. |
| Cỡ mẫu D1 | Đạt về số học | MDE 6 điểm, 859 yêu cầu hiệu dụng/nhóm, DE 6,96 và 299 yêu cầu/nhân viên. |
| Luật dừng | Cần làm rõ | Điều kiện hoàn tiền trùng và cách áp dụng mốc 3 ngày chưa đủ rõ. |
| Chi phí Pilot | Cần làm rõ | CPS 4.472đ là kết quả A2 toàn bộ mẫu, không phải CPS riêng của phạm vi Pilot. |
| Dữ liệu mô phỏng | Đã nhận diện | Các kết quả dựa trên cột `_simulated` phải được ghi rõ là simulated. |

## 2. Kiểm tra phép tính D1

Thông số trong kế hoạch:

- Baseline: 0,70.
- Mục tiêu: tăng 6 điểm phần trăm.
- Alpha: 0,05.
- Power: 0,80.
- ICC: 0,02.
- Số nhân viên: 40, chia thành 20 người mỗi nhóm.

Kiểm tra hệ số thiết kế:

\[
DE = 1 + (299 - 1) \times 0,02 = 6,96
\]

Kiểm tra cỡ mẫu hiệu dụng:

\[
n_{eff} = \frac{20 \times 299}{6,96} \approx 859
\]

**Kết luận:** Các con số 299 yêu cầu/nhân viên, DE = 6,96 và khoảng 859 yêu cầu hiệu dụng mỗi nhóm nhất quán về số học theo giả định trong file.

Kế hoạch cũng ghi rõ đánh đổi: nếu tác động thực tế chỉ là 5 điểm phần trăm thì power giảm còn khoảng 0,64. Giám đốc vận hành cần chấp nhận đánh đổi này trước ngày bắt đầu Pilot.

## 3. Các điểm cần chỉnh sửa hoặc xác nhận

### 3.1. CPS 4.472đ chưa đại diện riêng cho phạm vi Pilot

Trong `pilot_plan.yaml`, chi phí 4.472đ được liệt kê trong `simulated_inputs`. Đây là CPS A2 của toàn bộ mẫu, không phải CPS tính riêng cho hai nhóm `noi_dia` và `hang_nang`.

Các kết quả đã đối chiếu trước đó:

| Nhóm yêu cầu | CPS |
|---|---:|
| `noi_dia` | 2.696đ |
| `hang_nang` | 8.221đ |
| Hai nhóm gộp theo kết quả đã tính | Khoảng 3.414đ chi phí biến đổi/việc thành công |

**Đề nghị:** Ghi rõ 4.472đ là số liệu A2 toàn bộ mẫu. Khi đánh giá Pilot, cần tính CPS theo đúng phạm vi Pilot và tính cả chi phí chuyển nhân viên xử lý. Không dùng 4.472đ như thể đó là CPS riêng của Pilot.

### 3.2. Làm rõ cách diễn đạt rollout

File ghi:

```yaml
rollout: [0.10, 0.25, 0.50]
```

Chú thích mô tả lần lượt là 4, 10 và 20 nhân viên mỗi nhóm. Cần ghi rõ các tỷ lệ này áp dụng cho nhóm dùng trợ lý hay tổng số nhân viên tham gia ở từng giai đoạn, để tránh hiểu nhầm về quy mô rollout.

### 3.3. Bổ sung thời gian dự kiến đạt cỡ mẫu

Theo phương án đã chọn, mỗi nhóm cần tối thiểu 859 yêu cầu hiệu dụng; với 20 nhân viên mỗi nhóm và m = 299, tương ứng 299 yêu cầu/nhân viên theo kế hoạch.

**Đề nghị:** Bổ sung thời gian dự kiến để mỗi nhân viên đạt đủ số yêu cầu. Nếu kết thúc giai đoạn đo khi chưa đạt cỡ mẫu, không nên kết luận Pilot đã đạt yêu cầu kiểm định đã đặt ra.

### 3.4. Làm rõ luật dừng khi có hoàn tiền trùng

Luật hiện tại ghi: có ít nhất một ca hoàn trùng trong 3 ngày liên tiếp thì dừng.

Cần xác nhận ý định của nhóm:

- Nếu chỉ cần phát hiện một ca hoàn tiền trùng đã xác nhận là phải dừng ngay, hãy ghi rõ điều kiện này là độc lập và không phải chờ hết 3 ngày.
- Nếu muốn dùng cửa sổ theo dõi 3 ngày, hãy định nghĩa rõ cửa sổ đó và cách xác nhận sự kiện hoàn trùng.

Không nên để cách diễn đạt khiến người thực hiện hiểu rằng phải chờ đủ 3 ngày mới xử lý một ca hoàn trùng.

### 3.5. Định nghĩa chỉ số chính

Chỉ số chính hiện ghi là:

`dong_trong_24h_khong_mo_lai_7_ngay`

Cần bổ sung định nghĩa vận hành thống nhất, tối thiểu gồm:

- Mẫu số gồm những yêu cầu nào.
- Điều kiện để một yêu cầu được tính là thành công.
- Thời điểm bắt đầu tính 24 giờ.
- Cách xác định một yêu cầu không bị mở lại trong 7 ngày.
- Cách xử lý yêu cầu thiếu dữ liệu hoặc bị hủy.

Cần áp dụng cùng một cách tính cho nhóm trợ lý và nhóm đối chứng.

## 4. Dữ liệu cần gắn nhãn `simulated`

Các nội dung sau trong kế hoạch cần tiếp tục được ghi rõ là dữ liệu mô phỏng:

- `phut_xem_lai_simulated` — 890 phút trong mẫu.
- `phut_lam_lai_simulated` — 1.132 phút trong mẫu.
- CPS 4.472đ nếu lấy từ kết quả A2 mô phỏng.
- So sánh 0,22× và 0,69× với mức 12.000đ nếu được suy ra từ dữ liệu mô phỏng.

Không trình bày các số liệu này như số đo vận hành thực tế. Khi Pilot chạy, thay bằng số liệu đo thực tế và ghi rõ thời điểm, phạm vi đo.

## 5. Nội dung gửi Người 3

Có thể gửi nội dung sau để Người 3 cập nhật kế hoạch:

> Mình đã kiểm tra `pilot_plan.yaml`. YAML hợp lệ và các thông số D1 (859 yêu cầu hiệu dụng/nhóm, DE = 6,96, 299 yêu cầu/nhân viên) nhất quán về số học.
>
> Có 5 điểm cần rà soát:
>
> 1. CPS 4.472đ là kết quả A2 toàn bộ mẫu, không đại diện riêng cho phạm vi Pilot `noi_dia` + `hang_nang`. Cần ghi rõ phạm vi của số liệu và tính CPS Pilot theo đúng nhóm yêu cầu, bao gồm chi phí nhân viên làm thay.
> 2. Chú thích rollout 4, 10, 20 nhân viên mỗi nhóm cần diễn đạt rõ hơn.
> 3. Bổ sung thời gian dự kiến đạt 299 yêu cầu/nhân viên, tránh kết thúc đo khi chưa đủ cỡ mẫu.
> 4. Làm rõ điều kiện phát hiện hoàn tiền trùng trong luật dừng.
> 5. Bổ sung định nghĩa, mẫu số và cách tính chỉ số chính `dong_trong_24h_khong_mo_lai_7_ngay`.
>
> Các phần còn lại có thể giữ nguyên sau khi kiểm tra chéo.

## 6. Trạng thái bàn giao Người 2

| Công việc | Trạng thái |
|---|---|
| Kiểm tra A/B | Đã hoàn thành theo kết quả đã đối chiếu |
| Kiểm tra D1 | Đã kiểm tra phép tính và giả định được ghi trong kế hoạch |
| Rà soát phạm vi Pilot | Đã kiểm tra |
| Rà soát chi phí Pilot | Đã phát hiện điểm cần làm rõ |
| Rà soát luật dừng | Đã phát hiện điểm cần làm rõ |
| Kiểm tra dữ liệu `_simulated` | Đã xác định các số liệu cần gắn nhãn |
| Bộ nhãn lỗi Người 2 | Cần bảo đảm đây là bộ nhãn độc lập, không chỉ sao chép đáp án tham khảo |
| Đối chiếu với Người 3 | Chờ Người 3 hoàn thành và lưu bộ nhãn độc lập |

**Kết luận:** Phần rà soát Pilot của Người 2 đã có kết quả kiểm tra và danh sách điểm cần phản hồi. Người 3 là người phụ trách chính cập nhật `pilot_plan.yaml`. Người 2 tiếp tục theo dõi các chỉnh sửa và xác nhận lại trước khi nhóm chốt hồ sơ.
