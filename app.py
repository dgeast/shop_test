import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="아하 하모 칫솔 상세페이지 미리보기",
    page_icon="🦷",
    layout="wide",
)

st.title("🦷 아하 하모 칫솔 - 상세페이지 미리보기")
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
