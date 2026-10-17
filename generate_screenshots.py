import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    try:
        path = os.path.join("C:/Windows/Fonts", name)
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 22)
font_h2 = get_font("segoeuib.ttf", 16)
font_body = get_font("segoeui.ttf", 13)
font_body_b = get_font("segoeuib.ttf", 13)
font_small = get_font("segoeui.ttf", 11)
font_tab = get_font("segoeui.ttf", 12)
font_code = get_font("consola.ttf", 13)
font_item = get_font("segoeuib.ttf", 14)
font_badge = get_font("segoeuib.ttf", 11)

def draw_browser_frame(draw, width, height, title, url):
    draw.rectangle([0, 0, width, 70], fill="#e2e8f0")
    draw.ellipse([14, 12, 24, 22], fill="#ef4444")
    draw.ellipse([30, 12, 40, 22], fill="#f59e0b")
    draw.ellipse([46, 12, 56, 22], fill="#10b981")

    draw.rounded_rectangle([68, 6, 320, 36], radius=5, fill="#ffffff")
    draw.text((82, 12), title, fill="#1e293b", font=font_tab)

    draw.rectangle([0, 36, width, 70], fill="#ffffff")
    draw.line([0, 36, width, 36], fill="#cbd5e1", width=1)
    draw.line([0, 70, width, 70], fill="#e2e8f0", width=1)

    draw.polygon([(14, 53), (20, 48), (20, 58)], fill="#64748b")
    draw.polygon([(34, 53), (28, 48), (28, 58)], fill="#64748b")

    draw.rounded_rectangle([50, 41, width - 15, 65], radius=11, fill="#f1f5f9", outline="#cbd5e1", width=1)
    draw.text((65, 45), url, fill="#475569", font=font_small)

# 1. Screenshot Ví dụ 1 & 3: Main axis chiều ngang (px & %)
def render_example_px_percent(out_path):
    w, h = 950, 620
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "flex-basis với px và %", "http://localhost:5500/index.html#vi-du-1")

    # Card 1: px
    c1_y = 90
    draw.rounded_rectangle([40, c1_y, w - 40, c1_y + 220], radius=8, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.rounded_rectangle([56, c1_y + 14, 130, c1_y + 36], radius=11, fill="#2563eb")
    draw.text((68, c1_y + 17), "VÍ DỤ 1", fill="#ffffff", font=font_badge)
    draw.text((140, c1_y + 15), "flex-basis với đơn vị px (Main Axis chiều ngang)", fill="#0f172a", font=font_h2)
    draw.text((56, c1_y + 44), "Item 1: 200px | Item 2: 100px | Item 3: 150px (gap: 10px)", fill="#475569", font=font_body)

    # Box 1 demo
    bx = 56
    by = c1_y + 75
    boxes = [("Item 1 (200px)", 200), ("Item 2 (100px)", 100), ("Item 3 (150px)", 150)]
    for text, bw in boxes:
        draw.rounded_rectangle([bx, by, bx + bw, by + 75], radius=6, fill="lightblue", outline="#7dd3fc", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_item)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (bw - tw) // 2, by + (75 - th) // 2), text, fill="#0369a1", font=font_item)
        bx += bw + 10

    draw.text((56, c1_y + 175), "✓ flex-direction: row mặc định → flex-basis tác động trực tiếp vào chiều ngang (width cơ sở).", fill="#0369a1", font=font_small)

    # Card 2: %
    c2_y = 330
    draw.rounded_rectangle([40, c2_y, w - 40, c2_y + 220], radius=8, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.rounded_rectangle([56, c2_y + 14, 130, c2_y + 36], radius=11, fill="#f43f5e")
    draw.text((68, c2_y + 17), "VÍ DỤ 3", fill="#ffffff", font=font_badge)
    draw.text((140, c2_y + 15), "flex-basis với đơn vị phần trăm (50%)", fill="#0f172a", font=font_h2)
    draw.text((56, c2_y + 44), "Mỗi Item chiếm 50% kích thước Container → 2 cột đều nhau.", fill="#475569", font=font_body)

    # Box 2 demo
    b2x = 56
    b2y = c2_y + 75
    b2_w = (w - 80 - 32 - 10) // 2
    for text in ["Item 1 (50%)", "Item 2 (50%)"]:
        draw.rounded_rectangle([b2x, b2y, b2x + b2_w, b2y + 75], radius=6, fill="lightcoral", outline="#fda4af", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_item)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((b2x + (b2_w - tw) // 2, b2y + (75 - th) // 2), text, fill="#881337", font=font_item)
        b2x += b2_w + 10

    draw.text((56, c2_y + 175), "✓ flex-basis: 50% tính theo chiều rộng của Container.", fill="#881337", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

# 2. Screenshot Ví dụ 2 & 4: flex-direction column & flex-grow
def render_example_column_grow(out_path):
    w, h = 950, 680
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "flex-basis theo column & flex-grow", "http://localhost:5500/index.html#vi-du-2")

    # Left: Ví dụ 2 column (380px)
    c1_w = 410
    draw.rounded_rectangle([40, 90, 40 + c1_w, 640], radius=8, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.rounded_rectangle([56, 104, 130, 126], radius=11, fill="#10b981")
    draw.text((68, 107), "VÍ DỤ 2", fill="#ffffff", font=font_badge)
    draw.text((140, 105), "flex-direction: column", fill="#0f172a", font=font_h2)
    draw.text((56, 134), "flex-basis: 100px (Chiều dọc là Main Axis)", fill="#475569", font=font_small)

    cy = 165
    for text in ["Item 1 (Cao 100px)", "Item 2 (Cao 100px)", "Item 3 (Cao 100px)"]:
        draw.rounded_rectangle([56, cy, 56 + c1_w - 32, cy + 90], radius=6, fill="lightgreen", outline="#86efac", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_item)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((56 + (c1_w - 32 - tw) // 2, cy + (90 - th) // 2), text, fill="#15803d", font=font_item)
        cy += 100

    draw.text((56, 480), "Main Axis = Chiều dọc\nflex-basis quyết định chiều cao cơ sở.", fill="#15803d", font=font_small)

    # Right: Ví dụ 4 flex-grow (450px)
    c2_x = 470
    c2_w = w - c2_x - 40
    draw.rounded_rectangle([c2_x, 90, c2_x + c2_w, 640], radius=8, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.rounded_rectangle([c2_x + 16, 104, c2_x + 90, 126], radius=11, fill="#8b5cf6")
    draw.text((c2_x + 28, 107), "VÍ DỤ 4", fill="#ffffff", font=font_badge)
    draw.text((c2_x + 100, 105), "Kết hợp flex-grow", fill="#0f172a", font=font_h2)
    draw.text((c2_x + 16, 134), "Cùng flex-basis: 100px, grow tỷ lệ 1 : 2 : 1", fill="#475569", font=font_small)

    # Demo 3 items with grow: container 600px, in this mockup width is c2_w - 32
    # grow 1:2:1 => Item 1 (90px), Item 2 (180px), Item 3 (90px)
    gy = 175
    gw_items = [("Item 1\n(grow: 1)", 95, False), ("Item 2 (grow: 2)\n[Gấp đôi]", 190, True), ("Item 3\n(grow: 1)", 95, False)]
    gx = c2_x + 16
    for text, iw, is_double in gw_items:
        bg = "#93c5fd" if is_double else "lightblue"
        border = "#3b82f6" if is_double else "#7dd3fc"
        draw.rounded_rectangle([gx, gy, gx + iw, gy + 100], radius=6, fill=bg, outline=border, width=2)
        lines = text.split("\n")
        ly = gy + 25
        for l in lines:
            bbox = draw.textbbox((0, 0), l, font=font_small)
            tw = bbox[2] - bbox[0]
            draw.text((gx + (iw - tw) // 2, ly), l, fill="#1e3a8a", font=font_body_b)
            ly += 20
        gx += iw + 10

    # Explanation text inside card 4
    draw.rounded_rectangle([c2_x + 16, 310, c2_x + c2_w - 16, 520], radius=6, fill="#f8fafc", outline="#cbd5e1", width=1)
    exp = [
        "Phân bổ không gian còn trống:",
        "• Container: 600px",
        "• Tổng flex-basis ban đầu: 100px x 3 = 300px",
        "• Khoảng cách gap: 20px",
        "• Khoảng trống còn lại: ~280px",
        "• Phân chia theo tỷ lệ flex-grow 1 : 2 : 1:",
        "   + Item 1 nhận: +70px (Tổng ~170px)",
        "   + Item 2 nhận: +140px (Tổng ~240px)",
        "   + Item 3 nhận: +70px (Tổng ~170px)"
    ]
    ey = 325
    for e in exp:
        draw.text((c2_x + 28, ey), e, fill="#334155", font=font_small)
        ey += 20

    img.save(out_path)
    print(f"Saved: {out_path}")

# 3. Combined Overview Screenshot
def render_combined_overview(out_path):
    w, h = 1050, 920
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    # Header banner
    draw.rectangle([0, 0, w, 75], fill="#1e293b")
    draw.text((30, 22), "[Thực hành] Tổng quan 4 ví dụ về thuộc tính flex-basis", fill="#ffffff", font=font_title)

    # 4 Cards Layout (2x2)
    cards = [
        ("VÍ DỤ 1: Đơn vị px", "#2563eb", "flex-direction: row (chiều ngang)", [("Item 1 (200px)", 180), ("Item 2 (100px)", 90), ("Item 3 (150px)", 140)], "lightblue", "#0369a1", 30, 95),
        ("VÍ DỤ 2: flex-direction: column", "#10b981", "Trục chính là chiều dọc (chiều cao 100px)", [("Item 1", 100), ("Item 2", 100), ("Item 3", 100)], "lightgreen", "#15803d", 540, 95),
        ("VÍ DỤ 3: Đơn vị phần trăm (%)", "#f43f5e", "flex-basis: 50% (chia đôi container)", [("Item 1 (50%)", 215), ("Item 2 (50%)", 215)], "lightcoral", "#881337", 30, 480),
        ("VÍ DỤ 4: flex-basis + flex-grow", "#8b5cf6", "Cơ sở 100px, nhận thêm theo tỷ lệ 1:2:1", [("Item 1 (grow:1)", 110), ("Item 2 (grow:2)", 200), ("Item 3 (grow:1)", 110)], "#93c5fd", "#1e3a8a", 540, 480)
    ]

    cw, ch = 480, 360

    for title, badge_color, desc, items, bg_color, text_color, x, y in cards:
        draw.rounded_rectangle([x, y, x + cw, y + ch], radius=8, fill="#ffffff", outline="#cbd5e1", width=1)
        
        # Header of card
        draw.rounded_rectangle([x + 14, y + 14, x + 210, y + 38], radius=4, fill=badge_color)
        draw.text((x + 22, y + 17), title, fill="#ffffff", font=font_badge)
        draw.text((x + 16, y + 46), desc, fill="#475569", font=font_small)

        # Body demo
        demo_y = y + 74
        demo_h = ch - 90
        draw.rounded_rectangle([x + 14, demo_y, x + cw - 14, demo_y + demo_h], radius=6, fill="#f8fafc", outline="#e2e8f0", width=1)

        if "column" in title:
            # Draw vertically
            iy = demo_y + 12
            for iname, _ in items:
                draw.rounded_rectangle([x + 28, iy, x + cw - 28, iy + 65], radius=4, fill=bg_color, outline="#86efac", width=1)
                bbox = draw.textbbox((0, 0), iname, font=font_small)
                tw = bbox[2] - bbox[0]
                draw.text((x + 28 + (cw - 56 - tw) // 2, iy + 24), iname + " (Cao 100px)", fill=text_color, font=font_body_b)
                iy += 75
        else:
            # Draw horizontally
            ix = x + 24
            for iname, iw in items:
                draw.rounded_rectangle([ix, demo_y + 70, ix + iw, demo_y + 160], radius=4, fill=bg_color, outline="#cbd5e1", width=1)
                bbox = draw.textbbox((0, 0), iname, font=font_small)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                draw.text((ix + (iw - tw) // 2, demo_y + 70 + (90 - th) // 2), iname, fill=text_color, font=font_body_b)
                ix += iw + 8

    draw.text((w // 2 - 130, h - 35), "CSS Flexbox Practice • flex-basis Property", fill="#94a3b8", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\css-flex-basis"
    render_example_px_percent(os.path.join(base_dir, "screenshot_px_percent.png"))
    render_example_column_grow(os.path.join(base_dir, "screenshot_column_grow.png"))
    render_combined_overview(os.path.join(base_dir, "tat_ca_vi_du.png"))
