import base64
from pathlib import Path

# 이미지를 Base64로 인코딩
images = {
    'images/20260401_152547.jpg': '20260401_152547',
    'images/20260401_152638.jpg': '20260401_152638',
    'images/20260401_152731.jpg': '20260401_152731'
}

encoded_images = {}
for img_path, name in images.items():
    if Path(img_path).exists():
        with open(img_path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode()
            encoded_images[name] = f'data:image/jpeg;base64,{encoded}'
            print(f'✓ {name}: encoded ({len(encoded)} bytes)')

# HTML 파일 읽기
html_file = Path('aha_hamo_toothbrush_detail_page.html')
html_content = html_file.read_text(encoding='utf-8')

# 이미지 경로를 Base64로 치환
html_content = html_content.replace(
    'src="images/20260401_152547.jpg"',
    f'src="{encoded_images["20260401_152547"]}"'
)
html_content = html_content.replace(
    'src="images/20260401_152638.jpg"',
    f'src="{encoded_images["20260401_152638"]}"'
)
html_content = html_content.replace(
    'src="images/20260401_152731.jpg"',
    f'src="{encoded_images["20260401_152731"]}"'
)

# HTML 파일 저장
html_file.write_text(html_content, encoding='utf-8')
print('\n✓ HTML 파일 업데이트 완료!')
print('배포 환경에서 이미지가 정상적으로 표시됩니다.')
