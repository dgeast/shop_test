"""
아하 하모 칫솔 상세페이지용 플레이스홀더 이미지 생성
실제 제품 이미지로 교체 전 레이아웃 확인용
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "images"
IMAGES_DIR.mkdir(exist_ok=True)

# 색상 팔레트
TEAL = (0, 168, 168)
TEAL_DARK = (0, 120, 120)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

PURPLE = (155, 89, 182)
GREEN = (39, 174, 96)
RED = (231, 76, 60)
ORANGE = (243, 156, 18)

IMAGE_W = 860
IMAGE_H = 500


def draw_text_centered(draw, text, y, font_size, color, image_width):
    try:
        font = ImageFont.truetype("malgun.ttf", font_size)
    except Exception:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x = (image_width - text_w) // 2
    draw.text((x, y), text, fill=color, font=font)
    return font


def make_font(size):
    for path in ["malgun.ttf", "C:/Windows/Fonts/malgun.ttf", "C:/Windows/Fonts/gulim.ttc"]:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


# ── 이미지 1: 4가지 컬러 제품 ──────────────────────────────────────────────
def create_color_variants():
    img = Image.new("RGB", (IMAGE_W, IMAGE_H), WHITE)
    draw = ImageDraw.Draw(img)

    # 배경 그라데이션 느낌
    for y in range(IMAGE_H):
        r = int(240 + (255 - 240) * y / IMAGE_H)
        g = int(248 + (255 - 248) * y / IMAGE_H)
        b = int(248 + (255 - 248) * y / IMAGE_H)
        draw.line([(0, y), (IMAGE_W, y)], fill=(r, g, b))

    # 헤더
    draw.rectangle([0, 0, IMAGE_W, 80], fill=TEAL)
    f_lg = make_font(28)
    f_md = make_font(18)
    f_sm = make_font(14)

    bbox = draw.textbbox((0, 0), "아하 하모 칫솔 | 4가지 컬러", font=f_lg)
    tw = bbox[2] - bbox[0]
    draw.text(((IMAGE_W - tw) // 2, 25), "아하 하모 칫솔 | 4가지 컬러", fill=WHITE, font=f_lg)

    colors = [
        (PURPLE, "퍼플"),
        (GREEN, "그린"),
        (RED, "레드"),
        (ORANGE, "오렌지"),
    ]

    slot_w = IMAGE_W // 4
    for i, (color, name) in enumerate(colors):
        cx = slot_w * i + slot_w // 2
        # 칫솔 몸통
        handle_x1 = cx - 20
        handle_x2 = cx + 20
        draw.rectangle([handle_x1, 120, handle_x2, 360], fill=color, outline=WHITE, width=2)
        # 칫솔 헤드
        draw.ellipse([cx - 25, 100, cx + 25, 160], fill=color, outline=WHITE, width=2)
        # 모 표현 (작은 선들)
        for j in range(5):
            mx = cx - 15 + j * 8
            draw.line([(mx, 95), (mx, 75)], fill=GRAY, width=2)

        # 컬러 이름
        bbox = draw.textbbox((0, 0), name, font=f_md)
        tw = bbox[2] - bbox[0]
        draw.text((cx - tw // 2, 380), name, fill=color, font=f_md)

        # 컬러 원
        draw.ellipse([cx - 15, 410, cx + 15, 440], fill=color, outline=WHITE, width=2)

    # 하단 텍스트
    bbox = draw.textbbox((0, 0), "가족 모두 색깔별로 구분하여 사용하세요", font=f_sm)
    tw = bbox[2] - bbox[0]
    draw.text(((IMAGE_W - tw) // 2, 460), "가족 모두 색깔별로 구분하여 사용하세요", fill=(120, 120, 120), font=f_sm)

    path = IMAGES_DIR / "01_color_variants.jpg"
    img.save(path, "JPEG", quality=95)
    print(f"저장: {path}")


# ── 이미지 2: 투명 손잡이 디테일 ──────────────────────────────────────────
def create_handle_detail():
    img = Image.new("RGB", (IMAGE_W, IMAGE_H), (250, 252, 252))
    draw = ImageDraw.Draw(img)

    f_lg = make_font(26)
    f_md = make_font(17)
    f_sm = make_font(13)

    # 헤더
    draw.rectangle([0, 0, IMAGE_W, 80], fill=TEAL_DARK)
    text = "투명 ABS 손잡이 | 고급스러운 디자인"
    bbox = draw.textbbox((0, 0), text, font=f_lg)
    tw = bbox[2] - bbox[0]
    draw.text(((IMAGE_W - tw) // 2, 25), text, fill=WHITE, font=f_lg)

    # 좌측 - 큰 칫솔 이미지
    cx = 220
    # 손잡이 (투명감 표현 - 연한 틸)
    draw.rectangle([cx - 30, 100, cx + 30, 380],
                   fill=(180, 230, 230), outline=TEAL, width=3)
    # 투명 광택 효과
    draw.rectangle([cx - 20, 110, cx - 8, 370],
                   fill=(220, 245, 245), outline=None)
    # 헤드
    draw.ellipse([cx - 35, 80, cx + 35, 150],
                 fill=(200, 235, 235), outline=TEAL, width=3)
    # 모
    for j in range(6):
        mx = cx - 22 + j * 9
        draw.line([(mx, 78), (mx, 55)], fill=(150, 150, 150), width=2)

    # 우측 - 포인트 설명
    points = [
        (480, 130, "초극세모", "잇몸을 부드럽게 케어"),
        (480, 210, "투명 손잡이", "위생적이고 모던한 디자인"),
        (480, 290, "그립감", "미끄럼 방지 패턴 적용"),
        (480, 370, "국산 소재", "안전한 ABS 수지 사용"),
    ]
    for px, py, title, desc in points:
        # 연결선
        draw.line([(cx + 35, py + 10), (px - 10, py + 10)], fill=TEAL, width=1)
        draw.ellipse([px - 16, py + 4, px - 4, py + 16], fill=TEAL)
        draw.text((px, py), title, fill=TEAL_DARK, font=f_md)
        draw.text((px, py + 25), desc, fill=(100, 100, 100), font=f_sm)

    path = IMAGES_DIR / "02_handle_detail.jpg"
    img.save(path, "JPEG", quality=95)
    print(f"저장: {path}")


# ── 이미지 3: 벌크 패키징 ────────────────────────────────────────────────
def create_bulk_packaging():
    img = Image.new("RGB", (IMAGE_W, IMAGE_H), (245, 250, 245))
    draw = ImageDraw.Draw(img)

    f_lg = make_font(26)
    f_md = make_font(17)
    f_sm = make_font(13)

    # 헤더
    draw.rectangle([0, 0, IMAGE_W, 80], fill=(39, 174, 96))
    text = "벌크포장 | 포장비 절감으로 합리적인 가격"
    bbox = draw.textbbox((0, 0), text, font=f_lg)
    tw = bbox[2] - bbox[0]
    draw.text(((IMAGE_W - tw) // 2, 25), text, fill=WHITE, font=f_lg)

    # 박스 그리기
    box_colors = [PURPLE, GREEN, RED, ORANGE, TEAL, (100, 149, 237)]
    bx, by = 80, 110
    per_row = 6
    for i, c in enumerate(box_colors * 2):
        row = i // per_row
        col = i % per_row
        x = bx + col * 115
        y = by + row * 140
        # 칫솔 간략 표현
        draw.rectangle([x, y + 30, x + 30, y + 120], fill=c, outline=WHITE, width=2)
        draw.ellipse([x - 5, y + 10, x + 35, y + 55], fill=c, outline=WHITE, width=2)
        for j in range(4):
            draw.line([(x + 4 + j * 8, y + 8), (x + 4 + j * 8, y - 5)], fill=GRAY, width=2)

    # 우측 정보박스
    draw.rectangle([560, 100, 840, 420], fill=WHITE, outline=(39, 174, 96), width=2)

    info_lines = [
        ("💰 포장비 절감", TEAL_DARK, f_md, 125),
        ("개별 포장 없이 비용 절감", (80, 80, 80), f_sm, 160),
        ("", WHITE, f_sm, 175),
        ("📦 대량 구매 가능", TEAL_DARK, f_md, 190),
        ("치과·보건소 납품 실적", (80, 80, 80), f_sm, 225),
        ("학교·기업 단체 구매 환영", (80, 80, 80), f_sm, 248),
        ("", WHITE, f_sm, 263),
        ("✅ 식약처 인증", TEAL_DARK, f_md, 278),
        ("국가기관 위생검사 통과", (80, 80, 80), f_sm, 313),
        ("", WHITE, f_sm, 328),
        ("🇰🇷 전공정 국내생산", TEAL_DARK, f_md, 343),
        ("기획~제조 100% 국내", (80, 80, 80), f_sm, 378),
    ]
    for text, color, font, y in info_lines:
        if text:
            draw.text((580, y), text, fill=color, font=font)

    # 가격 배너
    draw.rectangle([0, 440, IMAGE_W, IMAGE_H], fill=TEAL)
    price_text = "9,000원  |  정가 12,000원 → 25% 할인"
    bbox = draw.textbbox((0, 0), price_text, font=f_md)
    tw = bbox[2] - bbox[0]
    draw.text(((IMAGE_W - tw) // 2, 462), price_text, fill=WHITE, font=f_md)

    path = IMAGES_DIR / "03_bulk_packaging.jpg"
    img.save(path, "JPEG", quality=95)
    print(f"저장: {path}")


if __name__ == "__main__":
    create_color_variants()
    create_handle_detail()
    create_bulk_packaging()
    print("\n완료! images/ 폴더에 3개 이미지가 생성되었습니다.")
    print("실제 제품 사진으로 교체하려면 같은 파일명으로 덮어쓰세요.")
