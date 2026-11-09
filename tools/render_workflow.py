"""Render the classroom workflow with Pillow; no external service is needed."""

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", help="Path to a Unicode TrueType font, if not auto-detected.")
    args = parser.parse_args()
    candidates = [args.font,
                  "/System/Library/Fonts/Supplemental/Arial.ttf",
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                  "C:/Windows/Fonts/arial.ttf"]
    font_path = next((p for p in candidates if p and Path(p).exists()), None)
    if not font_path:
        parser.error("Provide --font with a Vietnamese-capable TrueType font.")

    def font(size):
        return ImageFont.truetype(font_path, size)

    canvas = Image.new("RGB", (2400, 1570), "#f5f7fb")
    draw = ImageDraw.Draw(canvas)
    ink, muted, blue, red = "#17283d", "#486079", "#176b93", "#b8273c"
    draw.rounded_rectangle((60, 45, 2340, 240), radius=28, fill="#102b46")
    draw.text((105, 75), "CURRENT-STATE WORKFLOW", font=font(48), fill="white")
    draw.text((105, 140), "Xanh SM · Tìm đúng cổng / mặt đường · Mô hình giả định cho lab", font=font(34), fill="#d6e8f6")
    draw.text((105, 192), "Lê Thanh Tùng  |  MSSV 2A202603819", font=font(25), fill="#c1d5e8")

    positions = [(90, 330), (900, 330), (1710, 330),
                 (1710, 850), (900, 850), (90, 850)]
    steps = [
        ("Đối chiếu ghim GPS", "20 giây", ["Ai: Khách / tài xế", "Công cụ: App / bản đồ", "Vào: Ghim GPS và địa chỉ", "Ra: Khu vực cần tìm"]),
        ("Nhận diện hiện trường", "20 giây", ["Ai: Tài xế đã vào khu vực đón", "Công cụ: Bản đồ / quan sát", "Vào: Khu vực gần đúng", "Ra: Các cổng có thể có"]),
        ("Hỏi vị trí khách", "60 giây", ["Ai: Khách / tài xế", "Công cụ: Gọi / chat", "Vào: Mô tả gần đúng", "Ra: Thông tin bổ sung"]),
        ("Làm rõ cổng / phía đường", "45 giây", ["Ai: Khách / tài xế", "Công cụ: Gọi / chat / bản đồ", "Vào: Cổng phụ / cổng sau", "Ra: Điểm hai bên hiểu giống nhau"]),
        ("Tìm đúng điểm", "25 giây", ["Ai: Khách / tài xế", "Công cụ: Quan sát / bản đồ", "Vào: Điểm đã làm rõ", "Ra: Hai bên tiếp cận"]),
        ("Xác nhận gặp nhau", "10 giây", ["Ai: Khách / tài xế", "Công cụ: App / đối chiếu", "Vào: Đúng cổng và đúng khách", "Ra: Đón khách thành công"]),
    ]
    width, height = 600, 340
    for number, ((x, y), (title, duration, lines)) in enumerate(zip(positions, steps), 1):
        bottleneck = number in (3, 4)
        accent = red if bottleneck else blue
        draw.rounded_rectangle((x, y, x + width, y + height), radius=22,
                               fill="#fff1f2" if bottleneck else "white", outline=accent, width=3)
        draw.rounded_rectangle((x + 20, y + 18, x + 78, y + 76), radius=14, fill=accent)
        draw.text((x + 37, y + 28), str(number), font=font(30), fill="white")
        draw.text((x + 96, y + 28), title, font=font(30), fill=ink)
        draw.text((x + 28, y + 101), duration + ("  ·  BOTTLENECK" if bottleneck else ""),
                  font=font(29), fill=accent)
        for offset, line in enumerate(lines):
            draw.text((x + 28, y + 162 + offset * 37), line, font=font(25), fill=muted)

    def arrow(start, end, label=None):
        draw.line((start, end), fill=blue, width=7)
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        points = [end]
        for delta in (-0.55, 0.55):
            points.append((end[0] - 22 * math.cos(angle + delta),
                           end[1] - 22 * math.sin(angle + delta)))
        draw.polygon(points, fill=blue)
        if label:
            center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
            draw.rounded_rectangle((center[0] - 45, center[1] - 65,
                                    center[0] + 45, center[1] - 20), radius=12, fill="#dcecf8")
            draw.text((center[0] - 25, center[1] - 59), label, font=font(24), fill=blue)

    arrow((700, 495), (890, 495), "H1")
    arrow((1510, 495), (1700, 495), "H2")
    arrow((2010, 682), (2010, 835))
    arrow((1700, 1015), (1510, 1015))
    arrow((890, 1015), (700, 1015), "H3")
    draw.text((103, 735), "Handoff = điểm chuyển giao thông tin giữa người / hệ thống", font=font(31), fill=ink)
    draw.text((103, 785), "Đi theo thứ tự 1 → 2 → 3 → 4 → 5 → 6", font=font(29), fill=muted)
    draw.rounded_rectangle((90, 1245, 2310, 1515), radius=24, fill="#e5edf6")
    draw.text((125, 1270), "180 giây/lượt  =  20 + 20 + 60 + 45 + 25 + 10", font=font(40), fill=ink)
    draw.text((125, 1330), "Điểm nghẽn: hỏi vị trí + làm rõ cổng / phía đường = 105 giây (giả định).", font=font(30), fill=red)
    draw.text((125, 1380), "H1: Khách gửi vị trí → tài xế   |   H2: Hỏi / đáp hai bên   |   H3: Xác nhận gặp đúng khách", font=font(27), fill=muted)
    draw.text((125, 1430), "Chỉ tính làm rõ / tìm nhau trong khu đón. Chưa đo thực tế; mục tiêu thử nghiệm: 180 → 60 giây.", font=font(27), fill=muted)
    output = ROOT / "04-workflow-diagram.png"
    canvas.save(output, optimize=True)
    print(output)


if __name__ == "__main__":
    main()
