"""
아하 하모 칫솔 상세페이지 HTML 파일 저장 스크립트
이미지 플레이스홀더: __IMG1__ ~ __IMG4__ (app.py에서 base64로 교체)
"""

import os
from pathlib import Path

save_dir = Path(r'F:\dev\projects\shop_test')
save_dir.mkdir(parents=True, exist_ok=True)

html_content = """<!-- 네이버 스마트스토어용 상세페이지 -->

<style>
.pp * { margin:0; padding:0; box-sizing:border-box; }

.pp {
    font-family: 'Malgun Gothic', '맑은 고딕', sans-serif;
    color: #333;
    max-width: 860px;
    margin: 0 auto;
    background: #fff;
}

/* ── 히어로 ── */
.hero {
    display: table;
    width: 100%;
    background: linear-gradient(135deg, #00a8a8 0%, #00c8c8 100%);
    color: #fff;
}
.hero-text { display: table-cell; width: 52%; vertical-align: middle; padding: 50px 30px 50px 40px; }
.hero-img  { display: table-cell; width: 48%; vertical-align: bottom; padding: 0; }
.hero-img img {
    display: block;
    width: 100%;
    height: 380px;
    object-fit: cover;
    object-position: center;
}
.hero-badge {
    background: rgba(255,255,255,0.25);
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 12px;
    margin-bottom: 18px;
    font-weight: bold;
    letter-spacing: 0.5px;
}
.hero-title { font-size: 34px; font-weight: bold; line-height: 1.35; margin-bottom: 12px; }
.hero-sub   { font-size: 15px; opacity: .9; margin-bottom: 28px; line-height: 1.6; }
.price-box {
    background: rgba(0,0,0,0.18);
    border-radius: 12px;
    padding: 18px 22px;
    display: inline-block;
}
.price-original { font-size: 14px; text-decoration: line-through; opacity: .75; margin-bottom: 4px; }
.price-current  { font-size: 38px; font-weight: bold; color: #ffd700; line-height: 1; margin-bottom: 8px; }
.price-badge {
    background: #ff4757; color: #fff;
    padding: 5px 14px; border-radius: 20px;
    font-size: 13px; font-weight: bold;
}

/* ── 이유 3가지 ── */
.reasons { padding: 60px 30px; background: #fff; }
.sec-hd   { text-align: center; margin-bottom: 45px; }
.sec-title { font-size: 28px; font-weight: bold; color: #1a2533; margin-bottom: 10px; }
.sec-sub   { font-size: 14px; color: #888; }
.reason-row { display: table; width: 100%; }
.reason-cell { display: table-cell; width: 33.33%; padding: 15px; text-align: center; vertical-align: top; }
.r-icon {
    width: 88px; height: 88px;
    background: linear-gradient(135deg, #00a8a8, #00d4d4);
    border-radius: 50%; margin: 0 auto 18px;
    line-height: 88px; font-size: 42px;
}
.r-title { font-size: 18px; font-weight: bold; color: #1a2533; margin-bottom: 10px; }
.r-desc  { font-size: 14px; color: #555; line-height: 1.7; }

/* ── 컬러 섹션 (이미지 + 컬러 정보) ── */
.color-split { display: table; width: 100%; background: #f4fbfb; }
.cs-img  { display: table-cell; width: 50%; vertical-align: middle; padding: 0; }
.cs-img img {
    display: block; width: 100%;
    height: 360px; object-fit: cover; object-position: center;
}
.cs-info { display: table-cell; width: 50%; vertical-align: middle; padding: 40px 35px; }
.cs-title { font-size: 24px; font-weight: bold; color: #1a2533; margin-bottom: 8px; line-height: 1.4; }
.cs-sub   { font-size: 14px; color: #666; margin-bottom: 28px; line-height: 1.6; }
.color-list { list-style: none; }
.color-list li {
    display: flex; align-items: center; gap: 14px;
    padding: 10px 0; border-bottom: 1px solid #e0f0f0;
    font-size: 15px; font-weight: bold; color: #333;
}
.color-list li:last-child { border-bottom: none; }
.c-dot { width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0; border: 3px solid #fff; box-shadow: 0 2px 6px rgba(0,0,0,.2); }
.c-pink   { background: #e74c7d; }
.c-teal   { background: #00b09b; }
.c-yellow { background: #f0c040; }
.c-purple { background: #8e44ad; }

/* ── 신뢰 배지 ── */
.trust {
    padding: 45px 30px;
    background: linear-gradient(135deg, #27ae60, #2ecc71);
    color: #fff; text-align: center;
}
.trust-icon  { font-size: 52px; margin-bottom: 16px; }
.trust-title { font-size: 24px; font-weight: bold; margin-bottom: 12px; }
.trust-desc  { font-size: 15px; opacity: .95; line-height: 1.8; }

/* ── 품질 디테일 (이미지 + 포인트) ── */
.detail-split { display: table; width: 100%; background: #fff; }
.ds-info { display: table-cell; width: 50%; vertical-align: middle; padding: 40px 35px; }
.ds-img  { display: table-cell; width: 50%; vertical-align: middle; padding: 30px 20px 30px 0; }
.ds-img img {
    display: block; width: 100%; border-radius: 14px;
    box-shadow: 0 8px 30px rgba(0,0,0,.12);
    object-fit: cover; height: 320px; object-position: center;
}
.ds-title { font-size: 24px; font-weight: bold; color: #1a2533; margin-bottom: 20px; line-height: 1.4; }
.point-list { list-style: none; }
.point-list li {
    display: flex; align-items: flex-start; gap: 12px;
    padding: 10px 0; border-bottom: 1px solid #f0f0f0;
    font-size: 14px; color: #444; line-height: 1.6;
}
.point-list li:last-child { border-bottom: none; }
.pt-num {
    min-width: 26px; height: 26px; background: #00a8a8;
    color: #fff; border-radius: 50%; text-align: center;
    line-height: 26px; font-size: 12px; font-weight: bold; flex-shrink: 0;
}

/* ── 공공기관 납품 (이미지 + 텍스트) ── */
.inst-split { display: table; width: 100%; background: #f8f9fa; }
.is-img  { display: table-cell; width: 46%; vertical-align: middle; padding: 30px 0 30px 30px; }
.is-img img {
    display: block; width: 100%; border-radius: 14px;
    box-shadow: 0 6px 24px rgba(0,0,0,.1);
    object-fit: cover; height: 300px; object-position: center;
}
.is-info { display: table-cell; width: 54%; vertical-align: middle; padding: 40px 35px; }
.is-title { font-size: 24px; font-weight: bold; color: #1a2533; margin-bottom: 6px; line-height: 1.4; }
.is-sub   { font-size: 14px; color: #777; margin-bottom: 24px; }
.inst-row { display: table; width: 100%; margin-bottom: 10px; }
.inst-cell { display: table-cell; width: 33.33%; text-align: center; padding: 10px 6px; }
.inst-icon  { font-size: 32px; margin-bottom: 8px; }
.inst-label { font-size: 13px; font-weight: bold; color: #00a8a8; margin-bottom: 4px; }
.inst-desc  { font-size: 12px; color: #666; line-height: 1.5; }
.contact-box {
    background: #fff; border-radius: 10px;
    padding: 16px 20px; margin-top: 18px;
    border-left: 4px solid #00a8a8;
    font-size: 13px; color: #444; line-height: 1.8;
}
.contact-box strong { color: #00a8a8; }

/* ── 스펙 ── */
.spec { padding: 60px 30px; background: #fff; }
.spec-table {
    width: 100%; max-width: 680px;
    margin: 0 auto; border-collapse: collapse;
    border-radius: 10px; overflow: hidden;
    box-shadow: 0 4px 18px rgba(0,0,0,.08);
}
.spec-table tr { border-bottom: 1px solid #e8f4f4; }
.spec-table tr:last-child { border-bottom: none; }
.spec-table td { padding: 16px 20px; font-size: 15px; }
.spec-table tr:nth-child(even) { background: #f4fbfb; }
.sl { font-weight: bold; color: #555; width: 38%; }
.sv { color: #00a8a8; font-weight: bold; }

/* ── 후기 ── */
.review { padding: 60px 30px; background: #f8f9fa; }
.review-row { display: table; width: 100%; margin-top: 35px; }
.review-cell { display: table-cell; width: 33.33%; padding: 10px; vertical-align: top; }
.review-card {
    background: #fff; padding: 26px 20px;
    border-radius: 12px; text-align: center;
    box-shadow: 0 3px 14px rgba(0,0,0,.07);
}
.rv-stars { color: #ffc107; font-size: 18px; margin-bottom: 12px; }
.rv-text  { font-size: 14px; color: #555; line-height: 1.7; margin-bottom: 12px; }
.rv-auth  { font-size: 13px; color: #00a8a8; font-weight: bold; }

/* ── FAQ ── */
.faq { padding: 60px 30px; background: #fff; }
.faq-item { background: #f4fbfb; padding: 22px 24px; border-radius: 10px; margin-bottom: 12px; }
.fq { font-size: 16px; font-weight: bold; color: #1a2533; margin-bottom: 8px; }
.fa { font-size: 14px; color: #555; line-height: 1.75; }

/* ── 보증 ── */
.guarantee {
    background: linear-gradient(135deg, #f093fb, #f5576c);
    color: #fff; padding: 40px 30px;
    text-align: center; border-radius: 14px; margin: 20px;
}
.gu-title { font-size: 26px; font-weight: bold; margin-bottom: 10px; }
.gu-text  { font-size: 15px; opacity: .95; line-height: 1.7; }

/* ── CTA ── */
.cta {
    padding: 60px 30px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: #fff; text-align: center;
}
.cta-title { font-size: 32px; font-weight: bold; margin-bottom: 14px; }
.cta-sub   { font-size: 16px; opacity: .9; margin-bottom: 28px; }
.cta-box {
    background: rgba(255,255,255,0.15); border-radius: 14px;
    padding: 28px; max-width: 560px; margin: 0 auto 30px;
}
.cta-price   { font-size: 44px; font-weight: bold; color: #ffd700; margin-bottom: 12px; }
.cta-benefit { font-size: 15px; margin: 6px 0; }
.cta-contact { font-size: 14px; opacity: .85; line-height: 2; }

/* ── 모바일 ── */
@media (max-width: 640px) {
    .hero, .color-split, .detail-split, .inst-split { display: block; }
    .hero-text, .hero-img, .cs-img, .cs-info,
    .ds-info, .ds-img, .is-img, .is-info {
        display: block; width: 100%;
    }
    .hero-img img, .cs-img img { height: 240px; }
    .ds-img { padding: 0 20px 20px; }
    .is-img { padding: 20px 20px 0; }
    .hero-title { font-size: 26px; }
    .cta-title  { font-size: 24px; }
    .reason-cell, .review-cell, .inst-cell { display: block; width: 100%; }
}
</style>

<div class="pp">

    <!-- ① 히어로: 텍스트 + 메인 제품샷 -->
    <div class="hero">
        <div class="hero-text">
            <div class="hero-badge">🇰🇷 전공정 국내생산 &nbsp;|&nbsp; ✅ 식약처 인증 &nbsp;|&nbsp; 🏥 기관 납품</div>
            <h1 class="hero-title">딱 3가지만<br>기억하세요<br>아하 하모 칫솔</h1>
            <p class="hero-sub">국산 &nbsp;·&nbsp; 식약처 인증 &nbsp;·&nbsp; 합리적 가격</p>
            <div class="price-box">
                <div class="price-original">정가 12,000원</div>
                <div class="price-current">9,000원</div>
                <span class="price-badge">지금 25% 할인</span>
            </div>
        </div>
        <div class="hero-img">
            <img src="__IMG4__" alt="아하 하모 칫솔 4가지 컬러" />
        </div>
    </div>

    <!-- ② 핵심 이유 3가지 -->
    <div class="reasons">
        <div class="sec-hd">
            <h2 class="sec-title">왜 아하 하모 칫솔인가요?</h2>
            <p class="sec-sub">단 3가지 이유면 충분합니다</p>
        </div>
        <div class="reason-row">
            <div class="reason-cell">
                <div class="r-icon">🇰🇷</div>
                <h3 class="r-title">100% 국산</h3>
                <p class="r-desc">기획부터 제조까지<br>전공정 국내생산<br>믿을 수 있는 품질</p>
            </div>
            <div class="reason-cell">
                <div class="r-icon">✅</div>
                <h3 class="r-title">식약처 인증</h3>
                <p class="r-desc">국가기관 검증 완료<br>위생검사 통과<br>안심하고 사용</p>
            </div>
            <div class="reason-cell">
                <div class="r-icon">💰</div>
                <h3 class="r-title">합리적 가격</h3>
                <p class="r-desc">벌크포장으로<br>포장비 절감<br>25% 할인가</p>
            </div>
        </div>
    </div>

    <!-- ③ 컬러 선택: 제품 사진 + 컬러 정보 -->
    <div class="color-split">
        <div class="cs-img">
            <img src="__IMG2__" alt="4가지 컬러 칫솔" />
        </div>
        <div class="cs-info">
            <h2 class="cs-title">우리 가족<br>색깔별로 골라요</h2>
            <p class="cs-sub">투명 손잡이 디자인으로<br>각자 색상을 구분해 위생적으로 사용하세요.</p>
            <ul class="color-list">
                <li><span class="c-dot c-pink"></span> 핑크 — 감각적인 포인트</li>
                <li><span class="c-dot c-teal"></span> 틸 — 신선하고 청량한 느낌</li>
                <li><span class="c-dot c-yellow"></span> 옐로 — 밝고 에너지 넘치는</li>
                <li><span class="c-dot c-purple"></span> 퍼플 — 고급스러운 컬러</li>
            </ul>
        </div>
    </div>

    <!-- ④ 신뢰 배지 -->
    <div class="trust">
        <div class="trust-icon">🏅</div>
        <h3 class="trust-title">식품의약안전처 위생검사 통과</h3>
        <p class="trust-desc">국가기관의 엄격한 검사를 통과한 검증된 제품입니다<br>전공정 국내생산으로 안전을 보장합니다</p>
    </div>

    <!-- ⑤ 품질 디테일: 포인트 설명 + 제품 클로즈업 -->
    <div class="detail-split">
        <div class="ds-info">
            <h2 class="ds-title">작은 디테일에서<br>느껴지는 품질</h2>
            <ul class="point-list">
                <li><span class="pt-num">1</span><span><strong>초극세모</strong> — 잇몸을 부드럽게 케어하는 미세모 설계</span></li>
                <li><span class="pt-num">2</span><span><strong>투명 ABS 손잡이</strong> — 위생적이고 모던한 프리미엄 소재</span></li>
                <li><span class="pt-num">3</span><span><strong>그립감</strong> — 미끄럼 방지 패턴으로 편안한 사용감</span></li>
                <li><span class="pt-num">4</span><span><strong>국산 소재</strong> — 안전성 검증된 재료만 사용</span></li>
            </ul>
        </div>
        <div class="ds-img">
            <img src="__IMG3__" alt="칫솔 품질 디테일" />
        </div>
    </div>

    <!-- ⑥ 공공기관 납품: 벌크 패키징 사진 + 설명 -->
    <div class="inst-split">
        <div class="is-img">
            <img src="__IMG1__" alt="벌크 포장 제품" />
        </div>
        <div class="is-info">
            <h2 class="is-title">치과·보건소도<br>선택한 칫솔</h2>
            <p class="is-sub">공공기관이 믿고 사용하는 품질</p>
            <div class="inst-row">
                <div class="inst-cell">
                    <div class="inst-icon">🏥</div>
                    <div class="inst-label">보건소 납품</div>
                    <div class="inst-desc">전국 보건소<br>구강보건 사업용</div>
                </div>
                <div class="inst-cell">
                    <div class="inst-icon">🦷</div>
                    <div class="inst-label">치과 공급</div>
                    <div class="inst-desc">치과에서 직접<br>환자에게 권하는</div>
                </div>
                <div class="inst-cell">
                    <div class="inst-icon">🏢</div>
                    <div class="inst-label">대량 공급</div>
                    <div class="inst-desc">학교·기업·단체<br>별도 문의 환영</div>
                </div>
            </div>
            <div class="contact-box">
                📞 공공기관·대량구매 전용 상담<br>
                <strong>☎ 1588-0000</strong> &nbsp;|&nbsp; 📧 business@ahabrand.co.kr
            </div>
        </div>
    </div>

    <!-- ⑦ 제품 스펙 -->
    <div class="spec">
        <div class="sec-hd">
            <h2 class="sec-title">제품 정보</h2>
        </div>
        <table class="spec-table">
            <tr><td class="sl">브러시</td><td class="sv">초극세모 (부드러운 미세모)</td></tr>
            <tr><td class="sl">손잡이</td><td class="sv">투명 ABS 소재</td></tr>
            <tr><td class="sl">컬러</td><td class="sv">4종 (핑크·틸·옐로·퍼플)</td></tr>
            <tr><td class="sl">원산지</td><td class="sv">대한민국 (전공정 국내생산)</td></tr>
            <tr><td class="sl">인증</td><td class="sv">식품의약안전처 위생검사 통과</td></tr>
            <tr><td class="sl">사용 연령</td><td class="sv">전 연령 (어린이~성인)</td></tr>
        </table>
    </div>

    <!-- ⑧ 후기 -->
    <div class="review">
        <div class="sec-hd">
            <h2 class="sec-title">실제 구매자 후기</h2>
            <p class="sec-sub">만족도 98% 실제 사용 후기</p>
        </div>
        <div class="review-row">
            <div class="review-cell">
                <div class="review-card">
                    <div class="rv-stars">★★★★★</div>
                    <p class="rv-text">"보건소에서 받아본 그 칫솔이네요! 역시 품질 좋아요"</p>
                    <p class="rv-auth">김○○님</p>
                </div>
            </div>
            <div class="review-cell">
                <div class="review-card">
                    <div class="rv-stars">★★★★★</div>
                    <p class="rv-text">"가족 모두 색깔별로 사용하고 있어요. 가성비 최고!"</p>
                    <p class="rv-auth">이○○님</p>
                </div>
            </div>
            <div class="review-cell">
                <div class="review-card">
                    <div class="rv-stars">★★★★★</div>
                    <p class="rv-text">"치과에서 권해줘서 직접 구매했어요. 만족합니다!"</p>
                    <p class="rv-auth">박○○님</p>
                </div>
            </div>
        </div>
    </div>

    <!-- ⑨ FAQ -->
    <div class="faq">
        <div class="sec-hd">
            <h2 class="sec-title">자주 묻는 질문</h2>
        </div>
        <div class="faq-item">
            <div class="fq">Q. 정말 전공정 국내생산인가요?</div>
            <div class="fa">A. 네! 기획부터 제조까지 모든 공정을 대한민국에서 진행합니다. 식약처 위생검사도 통과한 검증된 제품입니다.</div>
        </div>
        <div class="faq-item">
            <div class="fq">Q. 치과나 보건소에 실제로 납품되나요?</div>
            <div class="fa">A. 네! 전국 치과, 보건소 등 공공기관에 납품되고 있는 검증된 제품입니다.</div>
        </div>
        <div class="faq-item">
            <div class="fq">Q. 컬러를 선택할 수 있나요?</div>
            <div class="fa">A. 핑크, 틸, 옐로, 퍼플 4가지 컬러 중 선택 가능합니다. (재고 상황에 따라 랜덤 발송될 수 있습니다)</div>
        </div>
        <div class="faq-item">
            <div class="fq">Q. 어린이도 사용 가능한가요?</div>
            <div class="fa">A. 네! 부드러운 초극세모로 어린이부터 성인까지 전 연령이 안전하게 사용 가능합니다.</div>
        </div>
        <div class="faq-item">
            <div class="fq">Q. 대량 구매(학교, 기업 등)도 가능한가요?</div>
            <div class="fa">A. 네! 전용 상담 라인(1588-0000)으로 문의 주시면 최적의 조건으로 안내해드립니다.</div>
        </div>
    </div>

    <!-- ⑩ 보증 -->
    <div class="guarantee">
        <div class="gu-title">🛡️ 100% 만족 보장</div>
        <p class="gu-text">제품이 마음에 들지 않으시면<br>14일 내 무조건 전액 환불해드립니다</p>
    </div>

    <!-- ⑪ 최종 CTA -->
    <div class="cta">
        <h2 class="cta-title">지금 바로 시작하세요</h2>
        <p class="cta-sub">건강한 구강케어의 첫걸음</p>
        <div class="cta-box">
            <div class="cta-price">9,000원</div>
            <div class="cta-benefit">✓ 전공정 국내생산</div>
            <div class="cta-benefit">✓ 식약처 위생검사 통과</div>
            <div class="cta-benefit">✓ 4가지 컬러 선택</div>
            <div class="cta-benefit">✓ 무료배송 (3만원 이상)</div>
        </div>
        <p class="cta-contact">
            📞 고객센터: 1588-0000 (평일 09:00~18:00)<br>
            📧 support@ahabrand.co.kr
        </p>
    </div>

</div>
"""

file_path = save_dir / 'aha_hamo_toothbrush_detail_page.html'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Saved: {file_path}  ({os.path.getsize(file_path):,} bytes)")
