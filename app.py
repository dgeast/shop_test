import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="아하 하모 칫솔 상세페이지 미리보기",
    page_icon="🦷",
    layout="wide",
)

st.title("🦷 아하 하모 칫솔 - 상세페이지 미리보기")
st.caption("네이버 스마트스토어 상세페이지 테스트")

html_file = Path(__file__).parent / "aha_hamo_toothbrush_detail_page.html"

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=6000, scrolling=True)
else:
    st.error("HTML 파일을 찾을 수 없습니다. `python save_page.py`를 먼저 실행해주세요.")
