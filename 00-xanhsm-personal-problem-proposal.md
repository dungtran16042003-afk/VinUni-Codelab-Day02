# Đề tài cá nhân đã chốt — Xác nhận đúng cổng và mặt đường đón khách

**Lê Thanh Tùng — MSSV 2A202603819 — branch `le-thanh-tung-2A202603819`.**

## Problem

Điểm check-in gần đúng hoặc thiếu cổng/mặt đường khiến tài xế và khách khó tìm nhau tại địa điểm nhiều lối vào. Đề xuất làm rõ vị trí đến mức **đúng cổng, đúng phía đường, đúng mốc nhận diện**, sau đó hai bên xác nhận trước khi chốt điểm đón.

AI hiểu mô tả như “cổng sau, cạnh hiệu thuốc” và chọn trong danh mục điểm đón được xác minh. Nếu “cổng phụ” có nhiều nghĩa hoặc khách ở phía đường chưa có trong danh mục, phải hỏi lại. Tọa độ do backend tra từ danh mục; mô hình không tự bịa tọa độ.

## Impact — giả định và mục tiêu pilot, chưa phải số liệu Xanh SM

| Chỉ số | Baseline giả định | Mục tiêu | Chênh lệch |
|---|---:|---:|---:|
| Thời gian làm rõ/tìm điểm đón trong khu vực đón, gồm xác nhận | 180 giây/chuyến | 60 giây/chuyến | −120 giây, −66,7% |
| Cuộc gọi xác nhận trung bình | 2/chuyến | ≤1/chuyến | Giảm ≥50% |
| Đón đúng cổng lần đầu | 75% | 95% | +20 điểm phần trăm |
| Hủy vì không tìm được nhau | 5% | 3% | −2 điểm phần trăm |

Kịch bản **1.000 chuyến thuộc nhóm điểm đón mơ hồ/ngày**, 30 ngày/tháng: giải phóng **1.000 giờ tài xế/tháng**. Giá trị thời gian giả định 50.000đ/giờ cho ra **50 triệu đồng/tháng giá trị cơ hội**, chưa phải giảm chi tiền thực tế. Nếu 20 chuyến giữ lại mỗi ngày đều hoàn thành, cước trung bình 60.000đ thì có **36 triệu đồng/tháng giá trị cước tăng thêm**; chưa phải doanh thu thuần/lợi nhuận của nền tảng. Không cộng hai khoản thành ROI. [Tham số](data/impact_assumptions.json), [kết quả tính](artifacts/impact-scenario.json).

## Bài nộp và bằng chứng

- [Problem Scan & 3 Cards](01-problem-scan.md).
- [Deep-Dive Report](02-deep-dive-report.md), [workflow](04-workflow-diagram.png), [AI Log](03-ai-log.md).
- [Prototype đúng cổng](starter-code/pickup_checkin.py), [catalog tổng hợp](data/pickup_catalog.json), [test](tests/test_pickup_checkin.py), [log Gemini thật](artifacts/pickup-gemini-results.json).
- [Memo nguồn chính thức](research/2026-11-09-pickup-entrance-checkin.md). Những memo cơ hội khác trong `research/` ghi quá trình chọn bài, không phải đề tài cuối.

**Trạng thái:** prototype trong sandbox, dữ liệu địa điểm tổng hợp. Chưa tích hợp Xanh SM, chưa có bản đồ thật, chưa đo hiệu quả trên hành khách thật. Đánh giá **NOT YET cho pilot vận hành**, tiếp tục kiểm chứng dữ liệu và tác động.
