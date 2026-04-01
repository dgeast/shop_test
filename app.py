import base64
import re
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


def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def get_product_images() -> list[str]:
    """images/ 폴더에서 실제 제품 사진(타임스탬프 파일명)을 날짜순으로 반환."""
    images_dir = BASE_DIR / "images"
    photos = sorted(images_dir.glob("2026*.jpg")) + sorted(images_dir.glob("2025*.jpg"))
    if photos:
        return [f"data:image/jpeg;base64,{img_to_base64(p)}" for p in photos]
    # 플레이스홀더 이미지로 폴백
    placeholders = sorted(images_dir.glob("0*.jpg"))
    return [f"data:image/jpeg;base64,{img_to_base64(p)}" for p in placeholders]


def inject_images(html: str, data_uris: list[str]) -> str:
    """HTML 내 img-placeholder div를 실제 <img> 태그로 교체."""
    img_tag_tpl = (
        '<div class="image-section" style="padding:20px;">'
        '<img src="{src}" style="width:100%;border-radius:10px;" />'
        "</div>"
    )
    placeholder_pattern = re.compile(
        r'<div class="image-section">.*?</div>', re.DOTALL
    )
    matches = list(placeholder_pattern.finditer(html))

    # 뒤에서부터 교체해야 인덱스가 밀리지 않음
    for i, match in reversed(list(enumerate(matches))):
        if i < len(data_uris):
            replacement = img_tag_tpl.format(src=data_uris[i])
        else:
            replacement = match.group(0)
        html = html[: match.start()] + replacement + html[match.end() :]

    return html


if not html_file.exists():
    st.error("HTML 파일을 찾을 수 없습니다. `python save_page.py`를 먼저 실행해주세요.")
    st.stop()

html_content = html_file.read_text(encoding="utf-8")

data_uris = get_product_images()
if data_uris:
    html_content = inject_images(html_content, data_uris)
    st.success(f"제품 이미지 {len(data_uris)}장이 삽입되었습니다.")
else:
    st.warning("images/ 폴더에 제품 사진이 없습니다. 플레이스홀더로 표시됩니다.")

st.components.v1.html(html_content, height=7000, scrolling=True)
