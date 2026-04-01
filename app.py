import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="아하 칫솔 상세페이지 미리보기",
    page_icon="🦷",
    layout="wide",
)

st.title("🦷 아하 칫솔 - 상세페이지 미리보기")
st.caption("네이버 스마트스토어 상세페이지 테스트")

BASE_DIR = Path(__file__).parent
html_file = BASE_DIR / "aha_hamo_toothbrush_detail_page.html"
images_dir = BASE_DIR / "images"


def to_b64(path: Path) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


def load_images() -> dict[str, str]:
    """
    이미지 할당:
      __IMG1__ → 벌크 지퍼백 포장     (공공기관 납품 섹션)
      __IMG2__ → 4색 부채꼴 배열      (컬러 선택 섹션)
      __IMG3__ → 4색 겹쳐진 클로즈업  (품질 디테일 섹션)
      __IMG4__ → 4색 깔끔한 메인샷    (히어로 섹션)
    """
    photos = sorted(images_dir.glob("2026*.jpg")) + sorted(images_dir.glob("2025*.jpg"))
    if len(photos) < 4:
        st.error(f"이미지가 4장 필요합니다. 현재 {len(photos)}장 감지됨.")
        st.stop()
    return {
        "__IMG1__": to_b64(photos[0]),  # 152547 → 지퍼백
        "__IMG2__": to_b64(photos[1]),  # 152638 → 부채꼴
        "__IMG3__": to_b64(photos[2]),  # 152731 → 클로즈업
        "__IMG4__": to_b64(photos[3]),  # 152818 → 메인샷
    }


if not html_file.exists():
    st.error("HTML 파일 없음. `python save_page.py`를 먼저 실행해주세요.")
    st.stop()

html = html_file.read_text(encoding="utf-8")
images = load_images()
for placeholder, data_uri in images.items():
    html = html.replace(placeholder, data_uri)

st.components.v1.html(html, height=7200, scrolling=True)

st.divider()

# -----------------------------
# 📊 상세페이지 평가
# -----------------------------
st.header("📊 상세페이지 전환율 체크")

score = 0

if st.checkbox("1. 첫 화면에서 시선 끌림"):
    score += 1
if st.checkbox("2. 문제 → 해결 구조 있음"):
    score += 1
if st.checkbox("3. 초미세모 강조됨"):
    score += 1
if st.checkbox("4. 국내 생산 / 위생 기준 신뢰 요소 있음"):
    score += 1
if st.checkbox("5. 구매 이유 명확"):
    score += 1

st.subheader(f"총 점수: {score}/5")

if score >= 4:
    st.success("🔥 판매 가능 수준")
elif score >= 2:
    st.warning("⚠️ 개선 필요")
else:
    st.error("❌ 구조 수정 필요")

# -----------------------------
# ✨ 카피 자동 생성
# -----------------------------
st.header("✨ 추천 상세페이지 카피")

if st.button("카피 생성"):
    st.code("""
[1장]
부드러운 초미세모
잇몸까지 편안하게
국내 생산 안심 칫솔

[2장]
일반 칫솔, 자극적이지 않나요?
초미세모로 부드럽게 케어
국내 생산 / 위생 기준 준수

[3장]
넉넉한 구성
가성비 좋은 선택
가족 / 사무실 / 여행용 추천
""")

# -----------------------------
# 🎬 영상 스크립트
# -----------------------------
st.header("🎬 15초 영상 스크립트")

if st.button("영상 스크립트 생성"):
    st.code("""
0~3초: 이 칫솔, 왜 자꾸 사는지 아세요?
3~6초: 일반 칫솔, 잇몸 아프지 않나요?
6~10초: 초미세모로 부드럽게 케어
10~13초: 넉넉한 구성, 가성비 GOOD
13~15초: 지금 바로 바꿔보세요
""")