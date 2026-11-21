# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): STT
- Nhóm được chấm: 4TL
- Căn cứ: `presentation.html` (slide 1–9)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **0** | Nhóm nêu rõ các bất lợi như CPS quốc tế **22.515 đ (1,88×)**. Tuy nhiên, mô phỏng tương tác ghi “Reset (Kịch bản A2)” nhưng mặc định retry 2; khi tính lại, nó dùng **966** việc thành công và **4.093.220 đ**, khác baseline A2 là **978** việc và **4.373.585 đ**. Bảng B3 retry 2 là kịch bản riêng; vấn đề là nhãn/reset của mô phỏng khiến người xem hiểu nhầm baseline. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **5** | Slide A2 ghi CPS **4.472 đ [simulated]**; slide A3 có cột CPS [simulated] và nêu phạm vi, loại các yêu cầu quốc tế (**22.515 đ**) khỏi triển khai. Tuy nhiên nhãn simulated chưa gắn nhất quán với mọi số chi phí ở các bảng/kịch bản, ví dụ các giá trị A4 **4.599 đ/5.784 đ** và nhiều ô chi phí B3. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **5** | Có thiết kế Cluster-RCT theo nhân viên, **20 + 20** người, ngẫu nhiên theo seed; nêu MDE **6 điểm**, **859** yêu cầu/nhánh, khoảng **299** yêu cầu/nhân viên và power chỉ **64,2%** nếu hiệu ứng thật là 5 điểm. Ba luật dừng có ngưỡng/thời hạn và rollback **30 phút**; tuy vậy cần ghi rõ ai có quyền kích hoạt dừng/rollback và xác nhận rằng mẫu đủ cho MDE đã chọn. |
| **Tổng** | | | | **10 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Có cơ sở để thử nghiệm giới hạn, nhưng chưa nên mở rộng trước khi (1) sửa nhãn/reset mô phỏng để khớp cấu hình và số liệu; (2) gắn nhãn simulated xuyên suốt các bảng; và (3) ghi rõ người có quyền dừng/rollback cùng tiêu chí chốt kết quả. Duy trì giới hạn phạm vi theo đề xuất, không triển khai quốc tế; theo dõi riêng `noi_dia` và `hang_nang`, vì CPS simulated lần lượt là **2.696 đ** và **8.221 đ**, trong đó hàng nặng vượt ngưỡng tài chính **8.000 đ**.

**Câu hỏi cho đội trình:**

1. **Nguyễn Trọng Hưởng — Mô hình & code:** Vì sao nút “Reset (Kịch bản A2)” đặt mô phỏng ở retry 2, khiến kết quả sau khi tính lại thành **966 việc, 4.093.220 đ**, trong khi A2 ghi **978 việc, 4.373.585 đ**? Nút reset cần đưa về cấu hình nào?
2. **Lê Thành Đạt — Kiểm số độc lập:** `hang_nang` có CPS **8.221 đ**, cao hơn ngưỡng dừng **8.000 đ**. Nhóm sẽ vận hành điều kiện thu hẹp về `noi_dia` như thế nào, và ai có quyền quyết định thu hẹp?
3. **Trần Minh Tân — Gắn nhãn PAIR 1:** Slide C báo cáo đồng thuận độc lập **20/20 (100%)**. Tỉ lệ này được tính từ nhãn ban đầu trước khi thảo luận hay từ nhãn đã thống nhất? Nhóm lưu vết và phân xử bất đồng ra sao?
4. **Phạm Ngọc Trung Quân — Hồ sơ & Gắn nhãn 2:** Với MDE **6 điểm** nhưng power **64,2%** nếu hiệu ứng thật là 5 điểm, nhóm sẽ diễn giải kết quả không có khác biệt như thế nào để phân biệt “không có hiệu quả” với “chưa đủ bằng chứng”?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đã ghi nhận lúc phản biện
