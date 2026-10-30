"""원소 실험실 시뮬레이터 - Streamlit 앱
실행: streamlit run app.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="원소 실험실 시뮬레이터", page_icon="🧪", layout="wide")

st.markdown(
    "<style>.block-container{padding:0.5rem 0.5rem 0 0.5rem;max-width:100%}"
    "header[data-testid='stHeader']{display:none}</style>",
    unsafe_allow_html=True,
)

GAME_HTML = r"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>원소 실험실 시뮬레이터</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
*{box-sizing:border-box}body{margin:0;font-family:system-ui,'Malgun Gothic',sans-serif;background:#0f172a;color:#e2e8f0}
header{padding:12px 18px;background:#1e293b;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
h1{margin:0;font-size:19px}h2{font-size:15px;margin:0 0 8px;color:#93c5fd}
.panel{background:#1e293b;border-radius:12px;padding:12px;margin:12px}
#pt{display:grid;grid-template-columns:repeat(18,minmax(0,1fr));gap:3px}
.el{border-radius:5px;padding:3px 1px;text-align:center;cursor:pointer;border:2px solid transparent;user-select:none;min-height:44px;line-height:1.1}
.el:hover{border-color:#fff;transform:scale(1.12);z-index:3;position:relative}
.el i{font-size:9px;opacity:.8;font-style:normal;display:block}.el b{font-size:14px;display:block}.el small{font-size:8px;display:block;white-space:nowrap;overflow:hidden}
.c-alkali{background:#b91c1c}.c-alkaline{background:#c2410c}.c-trans{background:#7c3aed}.c-post{background:#475569}.c-metalloid{background:#0f766e}
.c-nonmetal{background:#059669}.c-halogen{background:#a16207}.c-noble{background:#be185d}.c-lan{background:#4338ca}.c-act{background:#6d28d9;outline:1px dashed #fde047}
.legend span{display:inline-block;padding:2px 7px;border-radius:4px;margin:2px;font-size:11px}
.row{display:grid;grid-template-columns:1fr 1.1fr 1fr;gap:0}@media(max-width:1000px){.row{grid-template-columns:1fr}}
#bench{display:flex;flex-direction:column;align-items:center}
#beaker{width:220px;height:230px;border:4px solid #cbd5e1;border-top:none;border-radius:0 0 30px 30px;position:relative;overflow:hidden;margin:8px 0;background:#0b1220}
#liquid{position:absolute;bottom:0;width:100%;height:30%;background:#38bdf855;transition:all .6s}
#contents{position:absolute;top:10px;width:100%;text-align:center;font-size:22px;font-weight:bold;z-index:2}
#fx{position:absolute;inset:0;pointer-events:none;z-index:1}
.bubble{position:absolute;bottom:0;width:10px;height:10px;border-radius:50%;background:#fff8;animation:up 1.2s linear forwards}
@keyframes up{to{transform:translateY(-240px);opacity:0}}.shake{animation:sh .1s 8}@keyframes sh{50%{transform:translateX(-6px)}}
.btns{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}
button{background:#334155;color:#fff;border:0;border-radius:8px;padding:8px 11px;cursor:pointer;font-size:13px}button:hover{background:#475569}button.on{background:#2563eb}
#log{margin-top:8px;width:100%;min-height:100px;background:#0b1220;border-radius:8px;padding:10px;font-size:14px;line-height:1.5}
#info{font-size:13px;line-height:1.6}
#disc{max-height:430px;overflow:auto}.disc{padding:5px 8px;border-radius:6px;background:#0b1220;margin-bottom:4px;font-size:12px}.disc.no{opacity:.35}
.bar{height:8px;background:#0b1220;border-radius:4px;overflow:hidden;margin:4px 0 8px}.bar div{height:100%;background:#22c55e;transition:.4s}

.ov{position:fixed;inset:0;z-index:50;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 30%,#1e3a8a,#020617 75%);overflow:auto;padding:20px}
.ov.hide{display:none}.card{max-width:640px;width:100%;text-align:center}
.logo{font-size:72px;animation:float 3s ease-in-out infinite}@keyframes float{50%{transform:translateY(-12px) rotate(-6deg)}}
.card h1{font-size:40px;margin:6px 0;background:linear-gradient(90deg,#38bdf8,#a78bfa,#f472b6);-webkit-background-clip:text;background-clip:text;color:transparent}
.card p{color:#cbd5e1;line-height:1.6}.big{font-size:18px;padding:13px 28px;margin:6px;background:#2563eb}.big:hover{background:#1d4ed8}
.how{text-align:left;background:#0f172acc;border-radius:12px;padding:14px 18px;margin:16px 0;font-size:14px;line-height:1.8}
.floatel{position:absolute;font-weight:bold;opacity:.15;font-size:30px;animation:float 5s ease-in-out infinite;pointer-events:none}
#over{background:radial-gradient(circle,#7f1d1d,#0b0000 80%)}#over h1{background:none;color:#fca5a5;font-size:46px}
.stat{display:inline-block;background:#0f172acc;border-radius:10px;padding:10px 18px;margin:5px;font-size:14px}.stat b{display:block;font-size:24px;color:#fff}
#safe.low{color:#f87171;animation:blink .6s infinite}@keyframes blink{50%{opacity:.3}}
#quiz .card{background:#1e293bee;border-radius:16px;padding:20px}.opt{display:block;width:100%;margin:6px 0;text-align:left;font-size:15px;padding:11px}
.opt.ok{background:#16a34a}.opt.bad{background:#dc2626}#safe.up{color:#4ade80}
#battle{background:radial-gradient(circle at 50% 20%,#3b0764,#020617 80%);align-items:flex-start}
#battle .card{max-width:900px}.bcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;max-height:300px;overflow:auto;text-align:left}
.cc{background:#1e293b;border:2px solid #334155;border-radius:10px;padding:8px;font-size:12px;cursor:pointer;line-height:1.5}.cc.sel{border-color:#facc15;background:#422006}.cc b{font-size:13px}
.arena{display:grid;grid-template-columns:1fr auto 1fr;gap:10px;align-items:center;margin:10px 0}
.fighter{background:#0f172acc;border-radius:12px;padding:12px;text-align:left;min-height:130px}.fighter .nm{font-size:16px;font-weight:bold}
.hp{height:12px;background:#334155;border-radius:6px;overflow:hidden;margin:6px 0}.hp div{height:100%;background:#22c55e;transition:width .4s}
.team{font-size:20px;letter-spacing:2px}.hit{animation:sh .1s 5}
#blog{background:#0b1220;border-radius:8px;padding:8px;height:120px;overflow:auto;text-align:left;font-size:13px;line-height:1.5}
.tp{display:inline-block;padding:1px 6px;border-radius:4px;font-size:11px;background:#475569}
.proj{position:absolute;top:40%;font-size:34px;z-index:5;pointer-events:none;filter:drop-shadow(0 0 8px #fff)}
.proj.toR{animation:flyR .42s ease-in forwards}.proj.toL{animation:flyL .42s ease-in forwards}.proj.big{font-size:56px}
@keyframes flyR{from{left:18%;transform:scale(.6) rotate(0)}to{left:72%;transform:scale(1.2) rotate(360deg)}}
@keyframes flyL{from{left:72%;transform:scale(.6) rotate(0)}to{left:18%;transform:scale(1.2) rotate(-360deg)}}
.pop{position:absolute;top:25%;z-index:6;pointer-events:none;font-weight:900;animation:popUp .9s ease-out forwards;text-shadow:0 0 6px #000,0 0 2px #000}
.pop.atR{left:70%}.pop.atL{left:12%}@keyframes popUp{0%{transform:translateY(10px) scale(.5);opacity:0}20%{transform:translateY(0) scale(1.3);opacity:1}100%{transform:translateY(-50px) scale(1);opacity:0}}
.boomfx{position:absolute;top:20%;font-size:90px;z-index:4;pointer-events:none;animation:bm .6s ease-out forwards}.boomfx.atR{left:66%}.boomfx.atL{left:8%}
@keyframes bm{0%{transform:scale(.2);opacity:1}100%{transform:scale(2.2);opacity:0}}
.fighter.hit{animation:hitA .45s}@keyframes hitA{0%,100%{transform:translateX(0);background:#0f172acc}20%{transform:translateX(-10px);background:#7f1d1dcc}40%{transform:translateX(10px)}60%{transform:translateX(-6px)}80%{transform:translateX(6px)}}
.fighter.guardfx{box-shadow:0 0 0 3px #38bdf8,0 0 25px #38bdf8}.fighter.ko{animation:ko .6s}@keyframes ko{50%{opacity:.1;transform:scale(.9) rotate(-4deg)}}
.arena.flashA{animation:fl .3s}@keyframes fl{0%{background:#fff8}100%{background:transparent}}
.sw{height:56px;border-radius:8px;margin:6px 0;border:1px solid #fff3;position:relative;overflow:hidden}.sw i{position:absolute;width:18px;height:18px;border-radius:50%;top:19px}
.toast{position:fixed;right:18px;top:70px;z-index:99;background:linear-gradient(135deg,#16a34a,#0d9488);color:#fff;border-radius:14px;padding:12px 16px;min-width:240px;max-width:330px;box-shadow:0 10px 30px #0008;animation:tin .4s,tout .5s 3.2s forwards;font-size:14px;line-height:1.5}
.toast b.big{font-size:17px}@keyframes tin{from{transform:translateX(120%)}}@keyframes tout{to{opacity:0;transform:translateX(120%)}}
#toasts{position:fixed;right:18px;top:70px;z-index:99;display:flex;flex-direction:column;gap:8px}#toasts .toast{position:static}

/* ===== v7 세련된 UI 레이어 ===== */
:root{--bg:#0b0f1a;--glass:rgba(255,255,255,.045);--line:rgba(255,255,255,.09);--txt:#e6e9f2;--mute:#8b93a7;--acc:#7c9cff;--acc2:#b98cff;--ok:#34d399;--r:16px}
body{font-family:'Pretendard',system-ui,-apple-system,'Malgun Gothic',sans-serif;background:var(--bg);color:var(--txt);letter-spacing:-.01em;
 background-image:radial-gradient(900px 500px at 10% -10%,rgba(124,156,255,.16),transparent 60%),radial-gradient(800px 500px at 110% 10%,rgba(185,140,255,.12),transparent 60%);background-attachment:fixed}
header{position:sticky;top:0;z-index:20;background:rgba(11,15,26,.72);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line);padding:12px 22px}
header h1{font-size:18px;font-weight:800;background:linear-gradient(90deg,#fff,#b9c6ff);-webkit-background-clip:text;background-clip:text;color:transparent}
h2{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);margin-bottom:12px}
.panel{background:var(--glass);border:1px solid var(--line);border-radius:var(--r);padding:16px;margin:14px;box-shadow:0 10px 30px rgba(0,0,0,.25);backdrop-filter:blur(10px)}
.row{gap:0}
/* 주기율표 타일 */
#pt{gap:4px}
.el{border-radius:8px;border:1px solid rgba(255,255,255,.08);min-height:48px;transition:transform .15s,box-shadow .15s,filter .15s;position:relative;
 background-image:linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,0) 55%);box-shadow:inset 0 -2px 0 rgba(0,0,0,.18)}
.el:hover{transform:translateY(-3px) scale(1.12);border-color:rgba(255,255,255,.6);box-shadow:0 8px 20px rgba(0,0,0,.45);filter:brightness(1.15);z-index:3}
.el b{font-weight:800}.el i{opacity:.65}.el small{opacity:.8}
.c-alkali{background-color:#c2415d}.c-alkaline{background-color:#d0743c}.c-trans{background-color:#6d5bd0}.c-post{background-color:#4b5872}.c-metalloid{background-color:#15938a}
.c-nonmetal{background-color:#1fa37a}.c-halogen{background-color:#b8892b}.c-noble{background-color:#c0508f}.c-lan{background-color:#4a5bd4}.c-act{background-color:#7b48c9;outline:none;box-shadow:inset 0 0 0 1px #fde68a88}
.legend span{border-radius:999px;padding:3px 10px;font-weight:600}
/* 버튼 */
button{font-family:inherit;font-weight:600;background:rgba(255,255,255,.07);border:1px solid var(--line);color:var(--txt);border-radius:10px;padding:9px 14px;transition:all .15s}
button:hover{background:rgba(255,255,255,.14);transform:translateY(-1px)}button:active{transform:translateY(0) scale(.97)}
button.on,.big{background:linear-gradient(135deg,var(--acc),var(--acc2));border-color:transparent;color:#fff;box-shadow:0 6px 18px rgba(124,156,255,.35)}
.big{border-radius:14px;font-size:17px;padding:14px 30px}.big:hover{filter:brightness(1.1);background:linear-gradient(135deg,var(--acc),var(--acc2))}
/* 비커 */
#beaker{border:2px solid rgba(255,255,255,.35);border-top:none;border-radius:0 0 38px 38px;background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,.07));
 box-shadow:inset 8px 0 18px rgba(255,255,255,.05),0 20px 40px rgba(0,0,0,.35)}
#beaker::after{content:'';position:absolute;left:16px;top:12px;width:8px;height:70%;border-radius:8px;background:linear-gradient(rgba(255,255,255,.25),transparent);z-index:3}
#liquid{border-radius:0 0 36px 36px;box-shadow:0 -4px 16px currentColor}
#contents{font-weight:800;text-shadow:0 2px 10px rgba(0,0,0,.6)}
#log,#blog,.disc{background:rgba(0,0,0,.25);border:1px solid var(--line);border-radius:12px}
#log{padding:12px 14px}.disc{border-radius:10px;padding:7px 10px;margin-bottom:6px;transition:background .15s}.disc:hover{background:rgba(255,255,255,.06)}
.bar{height:6px;background:rgba(255,255,255,.08);border-radius:99px}.bar div{background:linear-gradient(90deg,var(--ok),#5eead4);border-radius:99px}
#info{color:#cfd5e4}
/* 스크롤바 */
*::-webkit-scrollbar{width:8px;height:8px}*::-webkit-scrollbar-thumb{background:rgba(255,255,255,.15);border-radius:8px}*::-webkit-scrollbar-track{background:transparent}
/* 오버레이 */
.ov{background:radial-gradient(1000px 600px at 50% 0%,#1d2a5c,#070a12 70%);backdrop-filter:blur(6px)}
.card h1{font-weight:900;letter-spacing:-.03em;background:linear-gradient(90deg,#9db4ff,#c9a4ff,#ff9ecf)}
.how,.stat,#quiz .card,.fighter{background:rgba(255,255,255,.05);border:1px solid var(--line);border-radius:var(--r);backdrop-filter:blur(10px)}
.stat b{font-weight:800}
.cc{background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:12px;transition:all .15s}.cc:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.3)}
.cc.sel{border-color:#fbbf24;background:rgba(251,191,36,.12);box-shadow:0 0 0 1px #fbbf24,0 8px 22px rgba(251,191,36,.18)}
.tp{border-radius:999px;padding:1px 8px;font-weight:600}
canvas{border-radius:var(--r);box-shadow:0 20px 50px rgba(0,0,0,.5);border:1px solid var(--line)}
.toast{background:rgba(16,24,40,.85);backdrop-filter:blur(14px);border:1px solid rgba(52,211,153,.45);border-left:4px solid var(--ok);border-radius:14px}
</style></head><body>
<div class="ov" id="menu"><div id="bgel"></div><div class="card">
<div class="logo">🧪</div><h1>원소 실험실</h1><p>118개 원소로 숨겨진 화학 반응을 찾아 도감을 완성하세요!<br>☢ 우라늄·플루토늄 같은 핵물질도 자유롭게 실험할 수 있어요.</p>
<div id="menuRec"></div>
<button class="big" onclick="startGame()">▶ 게임 시작</button><button class="big" style="background:#9333ea" onclick="openBattle()">⚔️ 원소 배틀</button><button class="big" style="background:#d97706" onclick="openShop()">🛒 테마 상점</button><button class="big" style="background:#475569" onclick="resetAll()">🗑 기록 초기화</button>
<div class="how"><b>🎮 게임 방법</b><br>
① 원소를 <b>화학식 개수만큼</b> 클릭해 넣어요 (예: H₂O = H 2번 + O 1번)<br>
② ⚗️ 혼합 · 💧 물 · 🔥 불꽃 버튼으로 실험해요<br>
③ 새로운 반응을 발견하면 도감에 등록돼요<br>
④ 도감 화합물로 ⚔️ 배틀 → 💎 배틀 포인트 획득 → 🛒 상점에서 테마 구매!</div>
<small style="color:#64748b">※ 교육용으로 단순화한 시뮬레이션입니다. 위험 반응은 절대 따라 하지 마세요.</small></div></div>
<div class="ov hide" id="quiz" style="background:#020617dd"><div class="card"><div class="logo" style="font-size:48px">🥽</div><h2 style="font-size:20px">실험실 안전 퀴즈</h2><p id="qq" style="font-size:17px"></p><div id="qo"></div><p id="qr"></p><button id="qclose" class="big" style="display:none" onclick="$('quiz').classList.add('hide')">계속 실험하기</button></div></div>
<div class="ov hide" id="battle"><div class="card">
<h1 style="font-size:32px;margin:4px">⚔️ 원소 배틀</h1><p>💎 배틀 포인트: <b id="bp">0</b> · 전적 <span id="brec"></span></p>
<div id="bSetup"><p>도감에서 발견한 화합물 중 <b>최대 5개</b>를 골라 팀을 만드세요! (<span id="selN">0</span>/5)</p>
<div class="bcards" id="pool"></div>
<div class="how" style="font-size:13px"><b>📘 배틀 규칙</b><br>
· 능력치는 반응 특성에서 나와요: 💥폭발 반응 = 공격형, ✨섬광 반응 = 균형형, 🫧거품 반응 = 방어형 (구성 원소가 많을수록 HP↑)<br>
· 타입 상성(공격 ×1.5): 🔥산화 → 🌿할로젠화 → 💧물 반응 → 🔥산화 / 🟡황화 ↔ ⚙️특수·공업 / 🧬유기 ↔ 🧂염·생활 / 🎆불꽃은 무상성<br>
· 🎱 <b>공 튕기기 배틀</b>: 화합물이 공이 되어 경기장을 튕겨 다녀요. 상대 공과 부딪히면 서로 피해! (자동 전투, 45초 제한 — 시간 초과 시 남은 HP 비율로 판정)<br>
· 💥폭발형은 빠르고 쓰러질 때 주변에 폭발 피해, 🫧거품형은 크고 무거워 잘 밀리지 않아요<br>
· 타입 스킬(약 5초마다): 🔥화염 폭발 · 🌿독침 발사 · 💧회복 파동 · 🟡가시 돌기 · ⚙️강철 보호막 · 🎆폭죽 3연발 · 🧪돌진 · 🧬성장 · 🧂결정 감속장<br>
· ☢️핵·방사성: 방사선 오라(반경 넓은 범위 피해) · 상성: ☢️ → ⚙️특수·공업 / 🧪비금속 → ☢️ (차폐!)<br>· 📣응원: 10초마다 내 팀 공 전체 2초 가속 · ⏩속도 조절 가능<br>
· 승리 시 💎 BP = 20 + 남은 화합물 수×10 + 상대 팀 수×5 (패배 시 참가상 3 BP)</div>
<button class="big" onclick="startBattle()">⚔️ 배틀 시작</button><button class="big" style="background:#475569" onclick="closeBattle()">↩ 돌아가기</button></div>
<div id="bFight" style="display:none">
<div id="bHud" style="display:flex;justify-content:space-between;font-weight:bold;margin:4px 0"><span style="color:#60a5fa" id="hMe"></span><span id="hTime"></span><span style="color:#f87171" id="hEn"></span></div>
<canvas id="bc" width="880" height="500" style="width:100%;max-width:880px;border-radius:14px;border:2px solid #475569;background:#0b1120;display:block;margin:0 auto"></canvas>
<div class="btns" id="bAct" style="justify-content:center"><button onclick="setSpd()" id="spdB">⏩ 속도 ×1</button><button onclick="cheer()" id="cheerB">📣 응원 (가속)</button><button onclick="giveUp()" style="background:#475569">🏳 항복</button></div>
<div id="blog" style="margin-top:8px"></div>
<div id="bEnd" style="display:none"><button class="big" onclick="openBattle()">🔁 다시 배틀</button><button class="big" style="background:#475569" onclick="closeBattle()">↩ 돌아가기</button></div>
</div></div></div>
<div class="ov hide" id="over"><div class="card"><div class="logo">💥</div><h1>GAME OVER</h1>
<p>안전점수가 0이 되어 실험실이 폐쇄되었습니다!<br><span id="overWhy"></span></p>
<div id="overStat"></div>
<button class="big" onclick="startGame()">🔄 다시 도전</button><button class="big" style="background:#475569" onclick="toMenu()">🏠 메인 화면</button></div></div>
<div class="ov hide" id="shop" style="background:#020617ee;align-items:flex-start"><div class="card" style="max-width:900px">
<h1 style="font-size:32px;margin:4px">🛒 테마 상점</h1><p>💎 보유 배틀 포인트: <b id="shopBP">0</b> · 배틀에서 이겨서 BP를 모으세요!</p>
<div class="bcards" id="shopList" style="max-height:none;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))"></div><p id="shopMsg"></p>
<button class="big" style="background:#475569" onclick="closeShop()">↩ 돌아가기</button></div></div>
<div id="toasts"></div><header><h1><button onclick="toMenu()" style="padding:4px 8px">🏠</button> 🧪 원소 실험실 시뮬레이터 v5</h1><div>발견 <b id="score">0</b>/<span id="total"></span><b id="safe" style="display:none">100</b> · 칭호 <b id="title">견습 연구원</b> · 💎 BP <b id="bpTop">0</b> <button onclick="openShop()" style="padding:3px 8px;background:#d97706">🛒 상점</button></div></header>
<div class="panel"><h2>① 주기율표 — 화학식의 원자 개수만큼 클릭! (H₂O = H 2번 + O 1번 · 최대 4종/90개 · Shift+클릭 = 5개)</h2><div id="pt"></div>
<div class="legend" id="legend"></div></div>
<div class="row">
 <div class="panel"><h2>원소 정보</h2><div id="info">원소에 마우스를 올리면 정보가 보여요.</div></div>
 <div class="panel" id="bench"><h2>② 실험대</h2>
  <div id="beaker"><div id="contents">비어 있음</div><div id="liquid"></div><div id="fx"></div></div>
  <div class="btns"><button onclick="act('mix')">⚗️ 혼합/가열·점화</button><button onclick="act('water')">💧 물에 넣기</button><button onclick="act('flame')">🔥 불꽃 반응</button><button onclick="hint()">💡 힌트</button><button onclick="openBattle()" style="background:#7e22ce">⚔️ 배틀</button><span id="qbtn" style="display:none"></span><button onclick="undoB()">↩ 하나 빼기</button><button onclick="clearB()">🧹 비우기</button></div>
  <div id="log">원소를 골라 실험해 보세요!<br><small>※ 교육용으로 단순화한 시뮬레이션입니다. 실제 반응 조건(온도·촉매 등)은 설명을 참고하고, 위험 반응은 절대 따라 하지 마세요.</small></div></div>
 <div class="panel"><h2>③ 발견 도감</h2><div class="btns" id="tabs" style="justify-content:flex-start;margin-bottom:6px"></div><div class="bar"><div id="prog"></div></div><div id="disc"></div></div>
</div>
<script>
const SYM="H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og".split(' ');
const KO="수소 헬륨 리튬 베릴륨 붕소 탄소 질소 산소 플루오린 네온 나트륨 마그네슘 알루미늄 규소 인 황 염소 아르곤 칼륨 칼슘 스칸듐 타이타늄 바나듐 크로뮴 망가니즈 철 코발트 니켈 구리 아연 갈륨 저마늄 비소 셀레늄 브로민 크립톤 루비듐 스트론튬 이트륨 지르코늄 나이오븀 몰리브데넘 테크네튬 루테늄 로듐 팔라듐 은 카드뮴 인듐 주석 안티모니 텔루륨 아이오딘 제논 세슘 바륨 란타넘 세륨 프라세오디뮴 네오디뮴 프로메튬 사마륨 유로퓸 가돌리늄 터븀 디스프로슘 홀뮴 어븀 툴륨 이터븀 루테튬 하프늄 탄탈럼 텅스텐 레늄 오스뮴 이리듐 백금 금 수은 탈륨 납 비스무트 폴로늄 아스타틴 라돈 프랑슘 라듐 악티늄 토륨 프로트악티늄 우라늄 넵투늄 플루토늄 아메리슘 퀴륨 버클륨 캘리포늄 아인슈타이늄 페르뮴 멘델레븀 노벨륨 로렌슘 러더포듐 더브늄 시보귬 보륨 하슘 마이트너륨 다름슈타튬 뢴트게늄 코페르니슘 니호늄 플레로븀 모스코븀 리버모륨 테네신 오가네손".split(' ');
const CAT={alkali:'알칼리 금속',alkaline:'알칼리 토금속',trans:'전이 금속',post:'전이후 금속',metalloid:'준금속',nonmetal:'비금속',halogen:'할로젠',noble:'비활성 기체',lan:'란타넘족',act:'악티늄족'};
const sets={alkali:[3,11,19,37,55,87],alkaline:[4,12,20,38,56,88],metalloid:[5,14,32,33,51,52],nonmetal:[1,6,7,8,15,16,34],halogen:[9,17,35,53,85,117],noble:[2,10,18,36,54,86,118],post:[13,31,49,50,81,82,83,84,113,114,115,116]};
const STATE={1:'기체',2:'기체',7:'기체',8:'기체',9:'기체',10:'기체',17:'기체',18:'기체',36:'기체',54:'기체',86:'기체',35:'액체',80:'액체'};
const RADIO=z=>z==43||z==61||z>=84;
function cat(z){for(const k in sets)if(sets[k].includes(z))return k;if(z>=57&&z<=71)return'lan';if(z>=89&&z<=103)return'act';return'trans'}
function pos(z){ // [row,col]
 const P=[[1,1],[1,18]];if(z<=2)return P[z-1];
 const per=[[3,10,2],[11,18,3],[19,36,4],[37,54,5],[55,86,6],[87,118,7]];
 for(const [a,b,p] of per)if(z>=a&&z<=b){
  if(p<=3){let i=z-a;return[p,i<2?i+1:i+11]}
  if(p<=5)return[p,z-a+1];
  if(z>=a+2&&z<=a+16)return[p+3,z-a+1]; // La/Ac 계열 아래줄 (col 3~17)
  let i=z-a;return[p,i<2?i+1:i-13]}}
const E={};SYM.forEach((s,i)=>{const z=i+1;E[s]={z,n:KO[i],c:cat(z)}});
const DESC={H:'가장 가볍고 우주에서 가장 풍부한 원소.',He:'풍선·초저온 냉각에 쓰이는 비활성 기체.',C:'유기물의 뼈대. 다이아몬드·흑연은 같은 탄소.',N:'공기의 약 78%.',O:'공기의 약 21%. 연소를 도움.',F:'반응성이 가장 큰 원소.',Na:'물과 격렬히 반응하는 무른 금속.',Mg:'연소 시 눈부신 흰 빛.',Al:'지각에 가장 많은 금속.',Si:'반도체의 핵심 재료.',Cl:'황록색 유독 기체, 소독에 사용.',Fe:'강철의 주성분. 녹슬기 쉬움.',Cu:'전선에 쓰이는 붉은 금속.',Ag:'전기 전도도가 가장 높은 금속.',Au:'산화되지 않는 귀금속.',Hg:'상온에서 액체인 유일한 금속.',Br:'상온에서 액체인 비금속.',Pt:'촉매로 쓰이는 귀금속.',U:'원자력 발전의 연료.',Xe:'비활성 기체지만 플루오린과는 화합물을 만듦.',Og:'가장 무거운 인공 원소.'};
// ---------- 반응 데이터 생성 ----------
const sub=s=>s.replace(/([A-Za-z\)])(\d+)/g,(_,a,m)=>a+[...m].map(d=>'₀₁₂₃₄₅₆₇₈₉'[d]).join(''));
const R=[];const add=(els,a,p,eq,fx,col,msg,cat)=>R.push({k:[...els].sort().join(','),a,p,eq:sub(eq),fx,col,msg,cat});
// 금속: [기호, 산화수, 이름표기, 산화물 여부]
const M=[['Li',1,'리튬',1],['Na',1,'나트륨',0],['K',1,'칼륨',0],['Rb',1,'루비듐',0],['Cs',1,'세슘',0],['Be',2,'베릴륨',1],['Mg',2,'마그네슘',1],['Ca',2,'칼슘',1],['Sr',2,'스트론튬',1],['Ba',2,'바륨',1],['Al',3,'알루미늄',1],['Zn',2,'아연',1],['Fe',3,'철(III)',1],['Cu',2,'구리(II)',1],['Ni',2,'니켈(II)',1],['Pb',2,'납(II)',1],['Sn',4,'주석(IV)',1],['Ti',4,'타이타늄(IV)',1],['Cr',3,'크로뮴(III)',1],['Hg',2,'수은(II)',1],['Ag',1,'은',0]];
const oxSpecial={Na:['Na2O2','과산화 나트륨','2Na + O2 → Na2O2'],K:['KO2','초과산화 칼륨','K + O2 → KO2'],Rb:['RbO2','초과산화 루비듐','Rb + O2 → RbO2'],Cs:['CsO2','초과산화 세슘','Cs + O2 → CsO2']};
const oxEq=(m,n)=>[[`M2O`,`4M + O2 → 2M2O`],[`MO`,`2M + O2 → 2MO`],[`M2O3`,`4M + 3O2 → 2M2O3`],[`MO2`,`M + O2 → MO2`]][n-1];
const OXCOL={Fe:'#b45309',Cu:'#1f2937',Cr:'#15803d',Hg:'#dc2626',Ni:'#4d7c0f',Pb:'#facc15'};
for(const [m,n,nm,ox] of M){
 if(ox){const [f,e]=oxEq(m,n);add([m,'O'],'mix',`${f.replace(/M/g,m)} 산화 ${nm}`,e.replace(/M/g,m),m=='Mg'?'flash':'bub',OXCOL[m]||'#f1f5f9',m=='Mg'?'눈부신 흰 빛과 함께 흰 가루 생성!':'금속이 산소와 결합해 산화물이 되었어요(가열 시).','산화')}
 else if(oxSpecial[m]){const [f,k,e]=oxSpecial[m];add([m,'O'],'mix',`${f} ${k}`,e,'flash','#fde68a','알칼리 금속은 연소 시 단순 산화물이 아닌 과산화물/초과산화물을 주로 만들어요.','산화')}}
const HAL=[['F','플루오린화','#fef9c3'],['Cl','염화','#f1f5f9'],['Br','브로민화','#fdba74'],['I','아이오딘화','#a8a29e']];
const halEq=n=>[`2M + X2 → 2MX`,`M + X2 → MX2`,`2M + 3X2 → 2MX3`,`M + 2X2 → MX4`][n-1];
const halF=(m,x,n)=>n==1?m+x:m+x+n;
const skipHal={'Fe,I':1,'Cu,I':1,'Hg,F':1};
for(const [m,n,nm] of M)for(const [x,xn,col] of HAL){if(skipHal[m+','+x])continue;
 add([m,x],'mix',`${sub(halF(m,x,n))} ${xn} ${nm}`,halEq(n).replace(/M/g,m).replace(/X/g,x),['alkali'].includes(E[m].c)?'flash':'bub',m=='Ag'?(x=='I'?'#fde047':x=='Br'?'#fef08a':'#f8fafc'):col,
 m=='Ag'&&x!='F'?'은 할로젠화물은 빛에 민감해 옛 사진 필름에 쓰였어요.':'금속과 할로젠이 이온 결합 화합물(염)을 만들었어요.','할로젠화')}
add(['Fe','I'],'mix','FeI₂ 아이오딘화 철(II)','Fe + I2 → FeI2','bub','#57534e','아이오딘은 산화력이 약해 철(III)이 아닌 철(II) 화합물이 생겨요.','할로젠화');
add(['Cu','I'],'mix','CuI 아이오딘화 구리(I)','2Cu + I2 → 2CuI','bub','#f5f5f4','구리와 아이오딘은 구리(I) 화합물을 만들어요.','할로젠화');
// 물 반응
const W=[['Li',1,'리튬','bub','비교적 잔잔하게 거품을 내며 반응.'],['Na',1,'나트륨','boom','물 위를 돌아다니며 쉭쉭 수소 발생!'],['K',1,'칼륨','boom','보라색 불꽃을 내며 격렬히 반응!'],['Rb',1,'루비듐','boom','칼륨보다 더 격렬하게 폭발적으로 반응!'],['Cs',1,'세슘','boom','닿자마자 폭발! 알칼리 금속 중 반응성 최고 수준.'],['Ca',2,'칼슘','bub','거품이 나며 용액이 뿌옇게 흐려져요.'],['Sr',2,'스트론튬','bub','칼슘보다 활발하게 수소 발생.'],['Ba',2,'바륨','bub','활발하게 수소 발생.']];
for(const [m,n,nm,f,msg] of W)add([m],'water',n==1?`${m}OH 수산화 ${nm}`:sub(`${m}(OH)2 수산화 ${nm}`),n==1?`2${m} + 2H2O → 2${m}OH + H2`:`${m} + 2H2O → ${m}(OH)2 + H2`,f,'#f9a8d4',msg+' 용액은 염기성.','물 반응');
add(['Mg'],'water','Mg(OH)₂ 수산화 마그네슘','Mg + 2H2O → Mg(OH)2 + H2','bub','#e2e8f0','찬물에선 거의 반응하지 않고 뜨거운 물에서 천천히 반응해요.','물 반응');
add(['Cl'],'water','HCl + HClO 염소수','Cl2 + H2O ⇌ HCl + HClO','bub','#ecfccb','차아염소산(HClO)이 생겨 소독 작용을 해요.','물 반응');
add(['F'],'water','HF + O₂','2F2 + 2H2O → 4HF + O2','boom','#fef9c3','플루오린은 물까지 산화시켜 산소를 내보내요!','물 반응');
// 황화물
[['Fe','FeS 황화 철(II)','Fe + S → FeS','#334155'],['Zn','ZnS 황화 아연','Zn + S → ZnS','#f8fafc'],['Cu','Cu₂S 황화 구리(I)','2Cu + S → Cu2S','#1e293b'],['Na','Na₂S 황화 나트륨','2Na + S → Na2S','#fef3c7'],['Ag','Ag₂S 황화 은','2Ag + S → Ag2S','#0f172a'],['Pb','PbS 황화 납(II)','Pb + S → PbS','#1f2937'],['Hg','HgS 황화 수은(II)','Hg + S → HgS','#dc2626'],['Mg','MgS 황화 마그네슘','Mg + S → MgS','#f1f5f9'],['Al','Al₂S₃ 황화 알루미늄','2Al + 3S → Al2S3','#fef9c3']]
 .forEach(([m,p,e,c])=>add([m,'S'],'mix',p,e,m=='Zn'||m=='Al'?'flash':'bub',c,m=='Hg'?'붉은 황화 수은은 천연 광물 진사(주사)와 같아요.':m=='Ag'?'은 식기가 검게 변하는 이유가 바로 황화 은!':'가열하자 금속과 황이 결합해 황화물이 생겼어요.','황화'));
// 비금속 반응
[[['H','O'],'H₂O 물','2H2 + O2 → 2H2O','boom','#38bdf8','펑! 수소가 연소하며 물이 생성.'],
[['C','O'],'CO₂ 이산화 탄소','C + O2 → CO2','bub','#94a3b8','탄소가 연소하며 이산화 탄소 발생.'],
[['O','S'],'SO₂ 이산화 황','S + O2 → SO2','bub','#a5b4fc','푸른 불꽃과 자극적인 냄새의 기체.'],
[['O','P'],'P₄O₁₀ 십산화 사인','P4 + 5O2 → P4O10','flash','#f8fafc','인이 밝게 타며 흰 연기 발생.'],
[['O','Si'],'SiO₂ 이산화 규소','Si + O2 → SiO2','bub','#e7e5e4','모래·유리·수정의 주성분.'],
[['B','O'],'B₂O₃ 삼산화 이붕소','4B + 3O2 → 2B2O3','flash','#d9f99d','붕소는 초록빛 불꽃으로 타요.'],
[['N','O'],'NO 일산화 질소','N2 + O2 → 2NO','flash','#fca5a5','번개나 엔진 같은 고온에서만 일어나요.'],
[['H','N'],'NH₃ 암모니아','N2 + 3H2 ⇌ 2NH3','bub','#e0f2fe','고온·고압·철 촉매가 필요한 하버-보슈법.'],
[['H','S'],'H₂S 황화 수소','H2 + S → H2S','bub','#fef08a','달걀 썩는 냄새의 유독 기체.'],
[['H','F'],'HF 플루오린화 수소','H2 + F2 → 2HF','boom','#fef9c3','어두운 곳에서도 폭발적으로 반응!'],
[['Cl','H'],'HCl 염화 수소','H2 + Cl2 → 2HCl','boom','#d9f99d','빛을 받으면 폭발적으로 반응.'],
[['Br','H'],'HBr 브로민화 수소','H2 + Br2 → 2HBr','bub','#fed7aa','가열하면 반응해요.'],
[['H','I'],'HI 아이오딘화 수소','H2 + I2 ⇌ 2HI','bub','#d6d3d1','가역 반응 — 평형의 대표 예시!'],
[['C','H'],'CH₄ 메테인','C + 2H2 → CH4','bub','#cbd5e1','고온·촉매 조건(단순화).'],
[['C','S'],'CS₂ 이황화 탄소','C + 2S → CS2','bub','#fef9c3','고온에서 생기는 휘발성 액체.'],
[['C','Si'],'SiC 탄화 규소','Si + C → SiC','flash','#334155','매우 단단한 연마재(카보런덤).'],
[['C','Ca'],'CaC₂ 탄화 칼슘','Ca + 2C → CaC2','flash','#64748b','물과 만나면 아세틸렌을 내는 카바이드.'],
[['F','Xe'],'XeF₂ 이플루오린화 제논','Xe + F2 → XeF2','flash','#f5f3ff','“비활성” 기체도 반응할 수 있다는 증거!'],
[['Mg','N'],'Mg₃N₂ 질화 마그네슘','3Mg + N2 → Mg3N2','flash','#fef9c3','마그네슘은 질소 속에서도 타요.'],
[['Li','N'],'Li₃N 질화 리튬','6Li + N2 → 2Li3N','bub','#7f1d1d','상온에서 질소와 반응하는 유일한 알칼리 금속.'],
[['Al','N'],'AlN 질화 알루미늄','2Al + N2 → 2AlN','bub','#f1f5f9','열전도가 좋은 세라믹 재료.'],
[['Cl','P'],'PCl₃ 삼염화 인','2P + 3Cl2 → 2PCl3','bub','#f8fafc','염소가 충분하면 PCl₅까지 생겨요.'],
[['Na','H'],'NaH 수소화 나트륨','2Na + H2 → 2NaH','bub','#f1f5f9','수소가 음이온(H⁻)이 되는 특이한 화합물.'],
[['Ca','H'],'CaH₂ 수소화 칼슘','Ca + H2 → CaH2','bub','#f1f5f9','건조제·수소 저장 물질.'],
[['Cl','F'],'ClF 플루오린화 염소','Cl2 + F2 → 2ClF','bub','#fef08a','할로젠끼리도 결합할 수 있어요(할로젠 간 화합물).'],
[['C','H','O'],'CO₂ + H₂O 완전 연소','CH4 + 2O2 → CO2 + 2H2O','boom','#7dd3fc','탄화수소의 완전 연소.'],
[['H','N','O'],'HNO₃ 질산','(오스트발트법) NH3 → NO → NO2 → HNO3','bub','#fde68a','암모니아를 산화시켜 질산을 만드는 공업 공정(단순화).'],
[['H','O','S'],'H₂SO₄ 황산','(접촉법) S → SO2 → SO3 → H2SO4','bub','#fef9c3','“화학 공업의 피”라 불리는 황산(단순화).'],
[['Ca','C','O'],'CaCO₃ 탄산 칼슘','CaO + CO2 → CaCO3','bub','#f8fafc','석회암·조개껍데기·분필의 성분.'],
[['Al','Fe','O'],'테르밋 반응','2Al + Fe2O3 → Al2O3 + 2Fe','boom','#f97316','2000℃가 넘는 열로 녹은 철이 생겨요! 철로 용접에 사용.'],
[['Cu','Zn'],'황동(놋쇠) 합금','Cu + Zn → 황동(합금)','flash','#eab308','금빛 합금. 악기·동전에 사용.'],
[['Cu','Sn'],'청동 합금','Cu + Sn → 청동(합금)','flash','#b45309','인류 문명을 바꾼 청동기 시대의 금속.'],
[['C','Fe'],'강철 합금','Fe + C(약 2% 이하) → 강철','flash','#94a3b8','철에 탄소를 조금 넣으면 단단한 강철!'],
[['Cr','Fe','Ni'],'스테인리스강','Fe + Cr + Ni → 스테인리스강','flash','#e2e8f0','크로뮴 산화막 덕분에 녹슬지 않아요.'],
[['Au','Hg'],'금 아말감','Au + Hg → 아말감','bub','#fde047','수은은 금·은을 녹여 아말감을 만들어요(옛 금 채굴법, 유독!).'],
[['Ag','Hg'],'은 아말감','Ag + Hg → 아말감','bub','#e5e7eb','과거 치과 충전재로 쓰였어요.'],
[['Na','K'],'NaK 합금','Na + K → NaK(액체 합금)','bub','#cbd5e1','상온에서 액체! 원자로 냉각재로 연구됨.']]
.forEach(([els,p,e,f,c,msg])=>add(els,'mix',p,e,f,c,msg,els.length==3||/합금|아말감/.test(p)?'특수·공업':'비금속·기타'));
// 불꽃 반응
const FL={Li:['#dc2626','빨간색'],Na:['#facc15','노란색'],K:['#c084fc','연보라색'],Rb:['#a21caf','적자색'],Cs:['#818cf8','청자색'],Ca:['#f97316','주황빛 빨간색'],Sr:['#b91c1c','진한 빨간색'],Ba:['#84cc16','황록색'],Cu:['#14b8a6','청록색'],B:['#22c55e','초록색'],In:['#6366f1','남색'],Tl:['#4ade80','초록색']};
for(const s in FL)R.push({k:s,a:'flame',p:`${E[s].n} 불꽃: ${FL[s][1]}`,eq:'',cat:'불꽃 반응'});

// ---------- 추가 조합 ----------
[[['C','O'],'CO 일산화 탄소','2C + O2 → 2CO','bub','#9ca3af','산소가 부족할 때(불완전 연소) 생기는 무색·무취의 유독 기체.','비금속·기타'],
[['O','S'],'SO3 삼산화 황','2SO2 + O2 ⇌ 2SO3 (촉매)','bub','#e0e7ff','황산을 만드는 중간 물질.','비금속·기타'],
[['N','O'],'NO2 이산화 질소','2NO + O2 → 2NO2','bub','#b45309','적갈색 유독 기체. 대기 오염·산성비의 원인.','비금속·기타'],
[['N','O'],'N2O 일산화 이질소','NH4NO3 → N2O + 2H2O (가열)','bub','#e0f2fe','“웃음 가스”로 불리는 마취 기체.','비금속·기타'],
[['H','O'],'H2O2 과산화 수소','H2 + O2 → H2O2 (단순화, 실제는 안트라퀴논법)','bub','#bae6fd','소독약으로 쓰이는 강한 산화제.','비금속·기타'],
[['O'],'O3 오존','3O2 → 2O3 (방전·자외선)','flash','#93c5fd','성층권에서 자외선을 막아 주는 기체. 지표면에선 유해.','비금속·기타'],
[['Fe','O'],'FeO 산화 철(II)','2Fe + O2 → 2FeO','bub','#1c1917','산소가 부족한 조건에서 생기는 검은 산화물.','산화'],
[['Fe','O'],'Fe3O4 사산화 삼철','3Fe + 2O2 → Fe3O4','flash','#0c0a09','철을 태우면 생기는 검은 자철석 성분. 자석에 붙어요!','산화'],
[['Cu','O'],'Cu2O 산화 구리(I)','4Cu + O2 → 2Cu2O','bub','#b91c1c','붉은색 구리 산화물.','산화'],
[['Cl','Fe'],'FeCl2 염화 철(II)','Fe + 2HCl → FeCl2 + H2','bub','#bbf7d0','철을 염산에 녹이면 생겨요(연두색 용액).','할로젠화'],
[['Cl','P'],'PCl5 오염화 인','PCl3 + Cl2 → PCl5','bub','#fef9c3','염소가 충분할 때 생겨요.','비금속·기타'],
[['Cl','Si'],'SiCl4 사염화 규소','Si + 2Cl2 → SiCl4','bub','#f1f5f9','고순도 반도체용 규소를 만드는 원료.','할로젠화'],
[['C','Cl'],'CCl4 사염화 탄소','CH4 + 4Cl2 → CCl4 + 4HCl','bub','#f8fafc','옛 소화기·세척제. 독성 때문에 지금은 사용 제한.','할로젠화'],
[['F','S'],'SF6 육플루오린화 황','S + 3F2 → SF6','flash','#e0f2fe','전기 절연 가스. 강력한 온실가스이기도 해요.','할로젠화'],
[['C','H'],'C2H6 에테인','2C + 3H2 → C2H6 (단순화)','bub','#e2e8f0','천연가스에 들어 있는 탄화수소.','유기 화합물'],
[['C','H'],'C2H4 에텐(에틸렌)','C2H6 → C2H4 + H2 (열분해)','bub','#d9f99d','과일을 익게 하는 식물 호르몬, 플라스틱(폴리에틸렌) 원료.','유기 화합물'],
[['C','H'],'C2H2 아세틸렌','CaC2 + 2H2O → C2H2 + Ca(OH)2','flash','#fef3c7','산소 용접 불꽃은 3000℃가 넘어요.','유기 화합물'],
[['C','H'],'C3H8 프로페인','(석유·천연가스에서 분리)','bub','#e2e8f0','LPG의 주성분.','유기 화합물'],
[['C','H'],'C4H10 뷰테인','(석유·천연가스에서 분리)','bub','#e2e8f0','휴대용 가스레인지 연료.','유기 화합물'],
[['C','H'],'C6H6 벤젠','3C2H2 → C6H6 (촉매)','bub','#fef9c3','육각 고리 모양의 방향족 화합물(발암성).','유기 화합물'],
[['C','H','O'],'CH3OH 메탄올','CO + 2H2 → CH3OH (촉매)','bub','#e0f2fe','연료·용매. 마시면 실명할 수 있는 유독 물질!','유기 화합물'],
[['C','H','O'],'C2H5OH 에탄올','C6H12O6 → 2C2H5OH + 2CO2 (발효)','bub','#f0f9ff','술의 성분이자 소독용 알코올.','유기 화합물'],
[['C','H','O'],'CH3COOH 아세트산','C2H5OH + O2 → CH3COOH + H2O','bub','#fef3c7','식초의 신맛을 내는 산.','유기 화합물'],
[['C','H','O'],'C6H12O6 포도당','6CO2 + 6H2O → C6H12O6 + 6O2 (광합성)','flash','#bbf7d0','식물이 햇빛으로 만드는 에너지원!','유기 화합물'],
[['C','H','N','O'],'CO(NH2)2 요소','CO2 + 2NH3 → CO(NH2)2 + H2O','bub','#f8fafc','최초로 실험실에서 합성된 유기물(뵐러, 1828). 비료 원료.','유기 화합물'],
[['C','H','N'],'HCN 사이안화 수소','2CH4 + 2NH3 + 3O2 → 2HCN + 6H2O (촉매)','bub','#e0f2fe','맹독성 기체. 아크릴 섬유 원료.','유기 화합물'],
[['C','H','Na','O'],'NaHCO3 탄산수소 나트륨','NaOH + CO2 → NaHCO3','bub','#f8fafc','베이킹소다! 가열하면 CO₂를 내며 빵을 부풀려요.','염·생활 화학'],
[['C','Na','O'],'Na2CO3 탄산 나트륨','2NaOH + CO2 → Na2CO3 + H2O','bub','#f8fafc','세탁 소다·유리 원료.','염·생활 화학'],
[['Cl','Na','O'],'NaClO 하이포아염소산 나트륨','Cl2 + 2NaOH → NaClO + NaCl + H2O','bub','#ecfccb','락스(표백제)의 주성분. 산성 세제와 섞으면 염소 가스 발생!','염·생활 화학'],
[['K','N','O'],'KNO3 질산 칼륨','KOH + HNO3 → KNO3 + H2O','flash','#f8fafc','흑색 화약과 비료의 원료(초석).','염·생활 화학'],
[['H','N','O'],'NH4NO3 질산 암모늄','NH3 + HNO3 → NH4NO3','boom','#f8fafc','질소 비료. 대량으로 쌓이면 폭발 위험!','염·생활 화학'],
[['Cl','H','N'],'NH4Cl 염화 암모늄','NH3 + HCl → NH4Cl','bub','#f8fafc','두 기체가 만나면 흰 연기가 피어올라요.','염·생활 화학'],
[['Ca','O','S'],'CaSO4 황산 칼슘','Ca(OH)2 + H2SO4 → CaSO4 + 2H2O','bub','#f8fafc','석고·깁스·두부 응고제.','염·생활 화학'],
[['Cu','O','S'],'CuSO4 황산 구리(II)','CuO + H2SO4 → CuSO4 + H2O','bub','#2563eb','물에 녹으면 파란색! 결정 키우기 실험 단골.','염·생활 화학'],
[['Ag','N','O'],'AgNO3 질산 은','Ag + 2HNO3 → AgNO3 + NO2 + H2O','bub','#f8fafc','염화 이온 검출 시약. 피부에 닿으면 검게 변해요.','염·생활 화학'],
[['K','Mn','O'],'KMnO4 과망가니즈산 칼륨','(공업적 제조, 단순화) MnO2 → K2MnO4 → KMnO4','bub','#7e22ce','진한 보라색 산화제·소독제.','염·생활 화학'],
[['H','O','P'],'H3PO4 인산','P4O10 + 6H2O → 4H3PO4','bub','#f0fdf4','콜라의 새콤한 맛, 비료 원료.','비금속·기타'],
[['Ca','O','P'],'Ca3(PO4)2 인산 칼슘','3Ca(OH)2 + 2H3PO4 → Ca3(PO4)2 + 6H2O','bub','#fefce8','뼈와 치아를 이루는 성분.','염·생활 화학'],
[['As','Ga'],'GaAs 비소화 갈륨','Ga + As → GaAs','flash','#475569','고속 반도체·태양전지 재료.','특수·공업'],
[['Ga','N'],'GaN 질화 갈륨','2Ga + 2NH3 → 2GaN + 3H2','flash','#60a5fa','파란 LED의 핵심 재료(2014 노벨 물리학상).','특수·공업'],
[['Co','Li','O'],'LiCoO2 코발트산 리튬','6Li2CO3 + 4Co3O4 + O2 → 12LiCoO2 + 6CO2','flash','#1e3a8a','스마트폰 리튬 이온 배터리 양극재.','특수·공업']]
.forEach(([els,p,e,f,c,msg,ct])=>add(els,'mix',p,e,f,c,msg,ct));
// ---------- 레시피(원소 개수) ----------
const NEED={'테르밋 반응':{Al:2,Fe:2,O:3},'황동(놋쇠) 합금':{Cu:2,Zn:1},'청동 합금':{Cu:3,Sn:1},'강철 합금':{Fe:5,C:1},'스테인리스강':{Fe:7,Cr:2,Ni:1},
 '금 아말감':{Au:1,Hg:2},'은 아말감':{Ag:1,Hg:1},'NaK 합금':{Na:1,K:2},'CO₂ + H₂O 완전 연소':{C:1,H:4,O:4}};
function parseF(f){f=f.replace(/[₀-₉]/g,c=>'₀₁₂₃₄₅₆₇₈₉'.indexOf(c));const st=[{}];let i=0;
 while(i<f.length){const c=f[i];
  if(c=='('){st.push({});i++}
  else if(c==')'){i++;const m=f.slice(i).match(/^\d+/),n=m?+m[0]:1;if(m)i+=m[0].length;const t=st.pop(),o=st[st.length-1];for(const k in t)o[k]=(o[k]||0)+t[k]*n}
  else{const m=f.slice(i).match(/^([A-Z][a-z]?)(\d*)/);if(!m||!E[m[1]])return null;i+=m[0].length;const o=st[st.length-1];o[m[1]]=(o[m[1]]||0)+(m[2]?+m[2]:1)}}
 return st[0]}
const recStr=n=>Object.keys(n).sort().map(s=>`${s}×${n[s]}`).join(' + ');
// ---------- 조합 추가 (v4) : 화학식에서 원소를 자동 추출 ----------
[['MnO2 이산화 망가니즈','(천연 연망간석)','bub','#292524','과산화 수소 분해 촉매, 건전지 재료.','산화'],
['TiO2 이산화 타이타늄','Ti + O2 → TiO2','flash','#f8fafc','흰색 페인트·선크림·광촉매.','산화'],
['Cr2O3 산화 크로뮴(III)','4Cr + 3O2 → 2Cr2O3','flash','#15803d','초록색 안료. 스테인리스가 녹슬지 않는 비밀 막.','산화'],
['SnO2 산화 주석(IV)','Sn + O2 → SnO2','bub','#f1f5f9','투명 전극·가스 센서 재료.','산화'],
['Ag2O 산화 은','4Ag + O2 → 2Ag2O (단순화)','bub','#44403c','시계용 산화은 전지의 재료.','산화'],
['HgO 산화 수은(II)','2Hg + O2 → 2HgO (가열)','bub','#dc2626','프리스틀리가 가열해 산소를 발견한 물질(1774).','산화'],
['NiO 산화 니켈(II)','2Ni + O2 → 2NiO','bub','#166534','초록빛 산화물. 배터리·세라믹 재료.','산화'],
['V2O5 오산화 바나듐','4V + 5O2 → 2V2O5','flash','#ea580c','황산 공업(접촉법)의 촉매.','산화'],
['WO3 삼산화 텅스텐','2W + 3O2 → 2WO3','flash','#facc15','스마트 유리(전기변색 유리) 재료.','산화'],
['ZrO2 산화 지르코늄','Zr + O2 → ZrO2','flash','#f8fafc','큐빅 지르코니아(인조 다이아몬드), 치과 보철.','산화'],
['N2H4 하이드라진','2NH3 + NaClO → N2H4 + NaCl + H2O','boom','#e0f2fe','로켓·인공위성 추진제.','비금속·기타'],
['PH3 포스핀','P4 + 3NaOH + 3H2O → PH3 + 3NaH2PO2','bub','#f1f5f9','맹독성 기체. 반도체 도핑 가스.','비금속·기타'],
['SiH4 실레인','SiCl4 + LiAlH4 → SiH4 + LiCl + AlCl3','boom','#f8fafc','공기 중에서 저절로 불붙는 기체. 반도체 공정용.','비금속·기타'],
['B2H6 다이보레인','(BF3 + NaBH4 반응, 단순화)','boom','#f1f5f9','공기와 만나면 불붙는 붕소 수소 화합물.','비금속·기타'],
['CS2 이황화 탄소','C + 2S → CS2 (고온)','bub','#fef9c3','레이온 섬유 제조 용매. 인화성 매우 높음.','비금속·기타'],
['ClO2 이산화 염소','2NaClO2 + Cl2 → 2ClO2 + 2NaCl','bub','#fde047','수돗물·펄프 소독제.','비금속·기타'],
['OF2 이플루오린화 산소','2F2 + 2NaOH → OF2 + 2NaF + H2O','bub','#fef3c7','산소가 + 산화수를 갖는 드문 화합물.','할로젠화'],
['XeF4 사플루오린화 제논','Xe + 2F2 → XeF4 (가열)','flash','#e0e7ff','“비활성” 기체도 화합물을 만든다는 증거!','할로젠화'],
['KrF2 이플루오린화 크립톤','Kr + F2 → KrF2 (저온 방전)','flash','#ede9fe','가장 강력한 산화제 중 하나.','할로젠화'],
['H2CO3 탄산','CO2 + H2O ⇌ H2CO3','bub','#e0f2fe','탄산음료의 톡 쏘는 맛! 불안정해서 곧 분해돼요.','비금속·기타'],
['HClO 하이포아염소산','Cl2 + H2O ⇌ HCl + HClO','bub','#ecfccb','염소 소독의 실제 살균 성분.','비금속·기타'],
['HNO2 아질산','(NaNO2 + HCl, 단순화)','bub','#e0f2fe','불안정한 약산.','비금속·기타'],
['CH2O 폼알데하이드','2CH3OH + O2 → 2CH2O + 2H2O','bub','#f1f5f9','새집증후군의 원인 물질.','유기 화합물'],
['HCOOH 폼산(개미산)','CO + H2O → HCOOH (단순화)','bub','#fef3c7','개미에 물렸을 때 따끔한 이유!','유기 화합물'],
['C3H6O 아세톤','(큐멘법, 단순화)','bub','#f0f9ff','매니큐어 리무버.','유기 화합물'],
['C2H6O2 에틸렌 글라이콜','C2H4O + H2O → C2H6O2','bub','#bae6fd','자동차 부동액.','유기 화합물'],
['C3H8O3 글리세롤','(유지의 가수 분해)','bub','#f8fafc','화장품 보습제. 니트로글리세린의 원료.','유기 화합물'],
['C3H6O3 젖산','C6H12O6 → 2C3H6O3 (젖산 발효)','bub','#fefce8','요구르트의 신맛, 운동 후 근육에 쌓이는 물질.','유기 화합물'],
['C6H8O7 시트르산','(곰팡이 발효)','bub','#fef08a','레몬의 신맛.','유기 화합물'],
['C9H8O4 아스피린','C7H6O3 + C4H6O3 → C9H8O4 + C2H4O2','flash','#f8fafc','1897년 합성된 대표 해열·진통제.','유기 화합물'],
['C7H6O3 살리실산','(콜베-슈미트 반응, 단순화)','flash','#f8fafc','버드나무 껍질 성분에서 유래. 여드름 치료제.','유기 화합물'],
['C8H10N4O2 카페인','(천연 추출)','flash','#f5f5f4','커피·차의 각성 성분.','유기 화합물'],
['C2H5NO2 글라이신','(가장 간단한 아미노산)','flash','#f8fafc','단백질을 이루는 가장 작은 아미노산.','유기 화합물'],
['C3H7NO2 알라닌','(아미노산)','flash','#f8fafc','단백질을 이루는 아미노산.','유기 화합물'],
['C10H8 나프탈렌','(콜타르에서 분리)','bub','#f8fafc','옛날 좀약 냄새의 정체.','유기 화합물'],
['C8H18 옥테인','(석유 정제)','boom','#fef3c7','휘발유 품질(옥테인가)의 기준 물질.','유기 화합물'],
['C12H22O11 설탕(수크로스)','(사탕수수·사탕무에서 추출)','bub','#ffffff','포도당 + 과당이 결합한 이당류.','유기 화합물'],
['CaCO3 탄산 칼슘','Ca(OH)2 + CO2 → CaCO3 + H2O','bub','#f8fafc','석회수가 뿌옇게! 대리석·조개껍데기·분필.','염·생활 화학'],
['Na2SO4 황산 나트륨','2NaOH + H2SO4 → Na2SO4 + 2H2O','bub','#f8fafc','세제 첨가제, 글라우버염.','염·생활 화학'],
['MgSO4 황산 마그네슘','MgO + H2SO4 → MgSO4 + H2O','bub','#f8fafc','입욕제 엡섬 솔트.','염·생활 화학'],
['BaSO4 황산 바륨','BaCl2 + H2SO4 → BaSO4 + 2HCl','bub','#f8fafc','위장 X선 촬영 조영제(물에 거의 안 녹아 안전).','염·생활 화학'],
['FeSO4 황산 철(II)','Fe + H2SO4 → FeSO4 + H2','bub','#a7f3d0','빈혈 치료용 철분제.','염·생활 화학'],
['ZnSO4 황산 아연','Zn + H2SO4 → ZnSO4 + H2','bub','#f8fafc','아연 보충제.','염·생활 화학'],
['Al2(SO4)3 황산 알루미늄','2Al(OH)3 + 3H2SO4 → Al2(SO4)3 + 6H2O','bub','#f8fafc','정수장의 응집제.','염·생활 화학'],
['(NH4)2SO4 황산 암모늄','2NH3 + H2SO4 → (NH4)2SO4','bub','#f8fafc','질소 비료(유안).','염·생활 화학'],
['K2CO3 탄산 칼륨','2KOH + CO2 → K2CO3 + H2O','bub','#f8fafc','옛날엔 나무 재(잿물)에서 얻었어요.','염·생활 화학'],
['NaNO3 질산 나트륨','NaOH + HNO3 → NaNO3 + H2O','bub','#f8fafc','칠레 초석. 비료·식품 보존제.','염·생활 화학'],
['KClO3 염소산 칼륨','(전기 분해, 단순화)','boom','#f8fafc','성냥 머리의 산화제.','염·생활 화학'],
['CaCl2 염화 칼슘','CaCO3 + 2HCl → CaCl2 + H2O + CO2','bub','#f8fafc','겨울철 도로 제설제, 제습제.','염·생활 화학'],
['NaHSO4 황산수소 나트륨','NaCl + H2SO4 → NaHSO4 + HCl','bub','#f8fafc','변기 세정제 성분.','염·생활 화학'],
['Mg(OH)2 수산화 마그네슘','MgO + H2O → Mg(OH)2','bub','#f8fafc','제산제(위산 중화)·변비약.','염·생활 화학'],
['Al(OH)3 수산화 알루미늄','AlCl3 + 3NaOH → Al(OH)3 + 3NaCl','bub','#f8fafc','제산제·난연제.','염·생활 화학'],
['Mg2SiO4 감람석','(마그마에서 결정화)','flash','#84cc16','맨틀의 주성분 광물. 보석 이름은 페리도트.','특수·공업'],
['Be3Al2Si6O18 녹주석(에메랄드)','(페그마타이트에서 결정화)','flash','#10b981','크로뮴이 섞이면 에메랄드, 철이 섞이면 아쿠아마린!','특수·공업'],
['CaTiO3 페로브스카이트','CaO + TiO2 → CaTiO3 (고온)','flash','#78350f','차세대 태양전지 구조의 이름이 된 광물.','특수·공업'],
['BN 질화 붕소','B2O3 + 2NH3 → 2BN + 3H2O','flash','#f8fafc','다이아몬드급으로 단단한 구조도 있어요.','특수·공업'],
['Si3N4 질화 규소','3Si + 2N2 → Si3N4 (고온)','flash','#64748b','엔진 부품·베어링용 세라믹.','특수·공업'],
['WC 탄화 텅스텐','W + C → WC (고온)','flash','#52525b','절삭 공구·드릴 날 재료.','특수·공업'],
['TiN 질화 타이타늄','2Ti + N2 → 2TiN','flash','#eab308','금빛 코팅. 공구를 단단하게 해요.','특수·공업'],
['InP 인화 인듐','In + P → InP','flash','#334155','광통신 레이저 반도체.','특수·공업'],
['CdTe 텔루르화 카드뮴','Cd + Te → CdTe','flash','#1f2937','박막 태양전지 재료.','특수·공업'],
['MoS2 이황화 몰리브데넘','Mo + 2S → MoS2','bub','#475569','고체 윤활제. 2차원 반도체로도 연구 중.','황화'],
['FeS2 황철석','Fe + 2S → FeS2 (단순화)','flash','#ca8a04','“바보의 금”! 금처럼 반짝이지만 철 + 황.','황화'],
['CuFeS2 황동석','(열수 광상에서 생성)','flash','#b45309','구리를 얻는 가장 중요한 광석.','황화'],
['Ag2S 황화 은','4Ag + 2H2S + O2 → 2Ag2S + 2H2O','bub','#1c1917','은 수저가 검게 변하는 이유.','황화'],
['YBa2Cu3O7 YBCO 초전도체','(고상 반응, 단순화)','flash','#0f172a','액체 질소 온도(−196℃)에서 전기 저항 0!','특수·공업'],
['Nd2Fe14B 네오디뮴 자석','(분말 소결, 단순화)','flash','#71717a','세상에서 가장 강한 영구 자석.','특수·공업'],
['LiFePO4 인산 철 리튬','(고상 합성, 단순화)','flash','#1e293b','전기차 LFP 배터리 양극재.','특수·공업']]
.forEach(([p,e,f,c,msg,ct])=>{const n=parseF(p.split(' ')[0]);if(!n){console.warn('파싱 실패',p);return}
 const sig=recStr(n);if(R.some(x=>x.a=='mix'&&recStr(NEED[sub(x.p)]||parseF(x.p.split(' ')[0])||{})==sig)){console.warn('중복 생략',p);return}
 add(Object.keys(n),'mix',p,e,f,c,msg,ct)});
[['UO2 이산화 우라늄','U + O2 → UO2 (단순화)','flash','#1c1917','원자력 발전소 핵연료 펠릿의 주성분.','핵·방사성'],
['U3O8 팔산화 삼우라늄','3U + 4O2 → U3O8','flash','#14532d','우라늄 광석 정제 산물 “옐로케이크”의 주요 성분.','핵·방사성'],
['UO3 삼산화 우라늄','2U + 3O2 → 2UO3 (단순화)','flash','#facc15','주황·노란색 우라늄 산화물.','핵·방사성'],
['UF6 육플루오린화 우라늄','U + 3F2 → UF6','bub','#f8fafc','56℃에서 승화하는 기체. 원심분리기로 U-235를 농축할 때 사용.','핵·방사성'],
['UF4 사플루오린화 우라늄','UO2 + 4HF → UF4 + 2H2O','bub','#16a34a','“그린 솔트”. UF6와 금속 우라늄 제조의 중간 물질.','핵·방사성'],
['UCl4 사염화 우라늄','U + 2Cl2 → UCl4','flash','#15803d','맨해튼 계획의 전자기 동위원소 분리(칼루트론) 원료.','핵·방사성'],
['UC 탄화 우라늄','U + C → UC (고온)','flash','#3f3f46','고온 원자로용 차세대 핵연료 후보.','핵·방사성'],
['UN 질화 우라늄','2U + N2 → 2UN','flash','#44403c','열전도도가 높은 차세대 핵연료 후보.','핵·방사성'],
['UH3 수소화 우라늄','2U + 3H2 → 2UH3','boom','#18181b','공기 중에서 저절로 불붙을 수 있는 검은 가루.','핵·방사성'],
['PuO2 이산화 플루토늄','Pu + O2 → PuO2','flash','#78350f','Pu-238 형태는 보이저·큐리오시티 탐사선의 원자력 전지(RTG) 열원.','핵·방사성'],
['PuF4 사플루오린화 플루토늄','Pu + 2F2 → PuF4 (단순화)','bub','#b45309','금속 플루토늄 제조의 중간 물질.','핵·방사성'],
['ThO2 이산화 토륨','Th + O2 → ThO2','flash','#f8fafc','녹는점 3350℃! 옛 캠핑 랜턴 맨틀 재료, 토륨 원자로 연료.','핵·방사성'],
['ThF4 사플루오린화 토륨','Th + 2F2 → ThF4','bub','#e2e8f0','용융염 원자로(MSR) 연료 성분.','핵·방사성'],
['RaCl2 염화 라듐','Ra + Cl2 → RaCl2','flash','#a5f3fc','마리 퀴리가 라듐을 분리할 때 얻은 화합물. 어둠 속에서 희미하게 빛나요.','핵·방사성'],
['RaSO4 황산 라듐','(Ra2+ + SO4 2− 침전, 단순화)','bub','#e0f2fe','물에 거의 녹지 않는 라듐 화합물.','핵·방사성'],
['AmO2 이산화 아메리슘','Am + O2 → AmO2','flash','#78350f','가정용 연기 감지기 속 Am-241의 화학 형태.','핵·방사성'],
['NpO2 이산화 넵투늄','Np + O2 → NpO2','flash','#365314','Pu-238 생산을 위한 표적 물질.','핵·방사성'],
['CmO2 이산화 퀴륨','Cm + O2 → CmO2 (단순화)','flash','#1c1917','강한 열을 내는 퀴륨 산화물.','핵·방사성'],
['Es2O3 산화 아인슈타이늄','4Es + 3O2 → 2Es2O3','flash','#fef9c3','수소폭탄 실험 낙진에서 처음 발견된 원소의 산화물.','핵·방사성'],
['PoO2 이산화 폴로늄','Po + O2 → PoO2','flash','#fde68a','폴로늄은 마리 퀴리가 조국 폴란드의 이름을 따 지었어요.','핵·방사성'],
['Tc2O7 칠산화 이테크네튬','4Tc + 7O2 → 2Tc2O7','flash','#fef08a','테크네튬은 최초의 인공 원소. Tc-99m은 의료 영상에 쓰여요.','핵·방사성'],
['RnF2 이플루오린화 라돈','Rn + F2 → RnF2','flash','#e9d5ff','라돈도 플루오린과는 반응해요!','핵·방사성'],
['Ac2O3 산화 악티늄','4Ac + 3O2 → 2Ac2O3','flash','#f8fafc','어둠 속에서 푸르게 빛나는 악티늄의 산화물.','핵·방사성'],
['Pa2O5 오산화 프로탁티늄','4Pa + 5O2 → 2Pa2O5','flash','#f1f5f9','매우 희귀한 악티늄족 원소의 산화물.','핵·방사성'],
['Cs2O 산화 세슘','4Cs + O2 → 2Cs2O (산소 부족)','flash','#f97316','Cs-137은 원전 사고 때 주요 방사성 오염 물질.','핵·방사성'],
['SrTiO3 타이타늄산 스트론튬','SrO + TiO2 → SrTiO3','flash','#f8fafc','다이아몬드 모조품. Sr-90 형태는 등대·위성용 RTG 열원으로 쓰였어요.','핵·방사성']]
.forEach(([p,e,f,c,msg,ct])=>{const n=parseF(p.split(' ')[0]);if(!n){console.warn('파싱 실패',p);return}
 const sig=recStr(n);if(R.some(x=>x.a=='mix'&&recStr(NEED[sub(x.p)]||parseF(x.p.split(' ')[0])||{})==sig)){console.warn('중복 생략',p);return}
 add(Object.keys(n),'mix',p,e,f,c,msg,ct)});
[['Na2O 산화 나트륨','4Na + O2 → 2Na2O (산소 부족)','flash','#f8fafc','흰색 고체. 유리 원료 성분.','산화'],
['K2O 산화 칼륨','4K + O2 → 2K2O (산소 부족)','flash','#fef3c7','비료 성분 표시에 쓰이는 “K₂O 함량”의 그 물질.','산화'],
['BaO 산화 바륨','2Ba + O2 → 2BaO','flash','#f8fafc','물과 반응해 수산화 바륨이 돼요.','산화'],
['BaO2 과산화 바륨','Ba + O2 → BaO2','flash','#f1f5f9','옛날 산소 제조(브린 공정)에 쓰인 과산화물.','산화'],
['SrO 산화 스트론튬','2Sr + O2 → 2SrO','flash','#f8fafc','브라운관 유리에 X선 차단용으로 쓰였어요.','산화'],
['BeO 산화 베릴륨','2Be + O2 → 2BeO','flash','#f8fafc','전기는 안 통하지만 열은 매우 잘 통하는 세라믹.','산화'],
['B2O3 삼산화 이붕소','4B + 3O2 → 2B2O3','flash','#e0f2fe','내열 유리(붕규산 유리)의 핵심 성분.','산화'],
['P4O10 십산화 사인','P4 + 5O2 → P4O10','boom','#f8fafc','흰인이 타면서 생기는 흰 연기. 강력한 건조제.','산화'],
['Sb2O3 삼산화 이안티모니','4Sb + 3O2 → 2Sb2O3','flash','#f8fafc','난연제(불에 잘 안 타게 하는 첨가제).','산화'],
['Bi2O3 삼산화 이비스무트','4Bi + 3O2 → 2Bi2O3','flash','#fde047','노란 안료. 비스무트 결정은 무지개빛!','산화'],
['GeO2 이산화 저마늄','Ge + O2 → GeO2','flash','#f8fafc','광섬유 코어의 굴절률을 높이는 재료.','산화'],
['Ga2O3 산화 갈륨','4Ga + 3O2 → 2Ga2O3','flash','#f8fafc','차세대 전력 반도체 소재.','산화'],
['In2O3 산화 인듐','4In + 3O2 → 2In2O3','flash','#fef9c3','스마트폰 터치스크린 투명 전극(ITO)의 주성분.','산화'],
['Y2O3 산화 이트륨','4Y + 3O2 → 2Y2O3','flash','#f8fafc','붉은 형광체·레이저 결정 재료.','산화'],
['La2O3 산화 란타넘','4La + 3O2 → 2La2O3','flash','#f8fafc','고급 카메라 렌즈 유리 첨가제.','산화'],
['CeO2 이산화 세륨','Ce + O2 → CeO2','flash','#fef3c7','유리 연마제, 자동차 촉매 변환기 재료.','산화'],
['Nd2O3 산화 네오디뮴','4Nd + 3O2 → 2Nd2O3','flash','#e9d5ff','유리를 보라색으로 물들여요.','산화'],
['Eu2O3 산화 유로퓸','4Eu + 3O2 → 2Eu2O3','flash','#fecaca','유로화 지폐 위조 방지 형광 잉크의 원소!','산화'],
['Gd2O3 산화 가돌리늄','4Gd + 3O2 → 2Gd2O3','flash','#f8fafc','MRI 조영제로 유명한 원소의 산화물.','산화'],
['Er2O3 산화 어븀','4Er + 3O2 → 2Er2O3','flash','#fbcfe8','분홍색. 광섬유 증폭기에 쓰여요.','산화'],
['HfO2 이산화 하프늄','Hf + O2 → HfO2','flash','#f8fafc','최신 반도체 트랜지스터의 절연막(High-k).','산화'],
['Ta2O5 오산화 이탄탈럼','4Ta + 5O2 → 2Ta2O5','flash','#f8fafc','스마트폰 콘덴서의 유전체.','산화'],
['MoO3 삼산화 몰리브데넘','2Mo + 3O2 → 2MoO3','flash','#f8fafc','촉매와 윤활제 원료.','산화'],
['RuO2 이산화 루테늄','Ru + O2 → RuO2','flash','#1e293b','칩 저항기에 쓰이는 전도성 산화물.','산화'],
['OsO4 사산화 오스뮴','Os + 2O2 → OsO4','bub','#fef9c3','매우 독성이 강한 휘발성 산화물. 지문 감식·전자현미경 염색용.','산화'],
['IrO2 이산화 이리듐','Ir + O2 → IrO2','flash','#1e3a8a','수전해(물 분해) 촉매.','산화'],
['Mn3O4 사산화 삼망가니즈','3Mn + 2O2 → Mn3O4','flash','#44403c','망가니즈를 태우면 생기는 갈흑색 산화물.','산화'],
['Co3O4 사산화 삼코발트','3Co + 2O2 → Co3O4','flash','#0f172a','코발트 블루 안료와 배터리 재료.','산화'],
['SeO2 이산화 셀레늄','Se + O2 → SeO2','flash','#f8fafc','유기 합성에 쓰이는 산화제.','산화'],
['TeO2 이산화 텔루륨','Te + O2 → TeO2','flash','#f8fafc','음향광학 소자용 결정.','산화'],
['Tl2O 산화 탈륨','4Tl + O2 → 2Tl2O','flash','#1c1917','탈륨은 독성이 매우 강해요.','산화'],
['Rb2O 산화 루비듐','4Rb + O2 → 2Rb2O (산소 부족)','flash','#fde68a','공기 중에선 보통 초과산화물이 생겨요.','산화'],
['Li2O2 과산화 리튬','2Li + O2 → Li2O2','flash','#f8fafc','우주선에서 CO₂ 흡수·산소 공급에 쓰여요.','산화'],
['CaO2 과산화 칼슘','Ca + O2 → CaO2','flash','#fef9c3','양식장·토양에 산소를 천천히 공급.','산화'],
['ZnO2 과산화 아연','Zn + O2 → ZnO2 (단순화)','flash','#f8fafc','불꽃놀이 산화제.','산화'],
['MgH2 수소화 마그네슘','Mg + H2 → MgH2','flash','#f1f5f9','수소 저장 소재로 연구 중.','비금속·기타'],
['CaH2 수소화 칼슘','Ca + H2 → CaH2','flash','#f8fafc','물과 만나면 수소를 내는 건조제.','비금속·기타'],
['LiH 수소화 리튬','2Li + H2 → 2LiH','flash','#f8fafc','가장 가벼운 이온성 화합물 중 하나.','비금속·기타'],
['KH 수소화 칼륨','2K + H2 → 2KH','flash','#f8fafc','유기 합성의 강염기.','비금속·기타'],
['AsH3 아르신','(As + 3H 단순화)','bub','#f8fafc','반도체 도핑 기체. 맹독성.','비금속·기타'],
['H2Se 셀레늄화 수소','H2 + Se → H2Se','bub','#f8fafc','썩은 무 냄새의 독성 기체.','비금속·기타'],
['H2Te 텔루륨화 수소','H2 + Te → H2Te (단순화)','bub','#f8fafc','불안정한 기체.','비금속·기타'],
['NCl3 삼염화 질소','(NH3 + 3Cl2 → NCl3 + 3HCl)','boom','#fde047','충격에 민감한 폭발성 액체. 실내 수영장 냄새의 원인 중 하나.','비금속·기타'],
['NF3 삼플루오린화 질소','N2 + 3F2 → 2NF3','bub','#f8fafc','반도체 챔버 세정 기체.','비금속·기타'],
['BF3 삼플루오린화 붕소','2B + 3F2 → 2BF3','bub','#f8fafc','유기 합성의 루이스산 촉매.','할로젠화'],
['BCl3 삼염화 붕소','2B + 3Cl2 → 2BCl3','bub','#f8fafc','반도체 식각 기체.','할로젠화'],
['SCl2 이염화 황','S + Cl2 → SCl2','bub','#dc2626','붉은 액체. 고무 가황에 쓰여요.','할로젠화'],
['S2Cl2 일염화 황','2S + Cl2 → S2Cl2','bub','#facc15','노란 액체.','할로젠화'],
['SiF4 사플루오린화 규소','Si + 2F2 → SiF4','flash','#f8fafc','플루오린이 유리를 녹일 때 생기는 기체.','할로젠화'],
['GeCl4 사염화 저마늄','Ge + 2Cl2 → GeCl4','bub','#f8fafc','광섬유 제조 원료.','할로젠화'],
['TiCl4 사염화 타이타늄','Ti + 2Cl2 → TiCl4','bub','#f8fafc','공기 중에서 흰 연기를 내뿜어 스카이라이팅에 쓰였어요.','할로젠화'],
['WF6 육플루오린화 텅스텐','W + 3F2 → WF6','bub','#f8fafc','반도체 텅스텐 배선 증착용 기체.','할로젠화'],
['IF5 오플루오린화 아이오딘','I2 + 5F2 → 2IF5','bub','#fef9c3','강력한 플루오린화제.','할로젠화'],
['IF7 칠플루오린화 아이오딘','I2 + 7F2 → 2IF7','bub','#f8fafc','원자 하나에 플루오린 7개가 붙는 희귀 구조.','할로젠화'],
['ClF3 삼플루오린화 염소','Cl2 + 3F2 → 2ClF3','boom','#bef264','콘크리트와 모래도 태우는 초강력 산화제.','할로젠화'],
['BrF3 삼플루오린화 브로민','Br2 + 3F2 → 2BrF3','boom','#fde68a','강력한 플루오린화제.','할로젠화'],
['ICl 일염화 아이오딘','I2 + Cl2 → 2ICl','flash','#7f1d1d','적갈색. 위이스 시약.','할로젠화'],
['IBr 브로민화 아이오딘','I2 + Br2 → 2IBr','flash','#57534e','할로젠끼리 만든 화합물.','할로젠화'],
['NaBrO3 브로민산 나트륨','(Br2 + NaOH → NaBrO3, 단순화)','flash','#f8fafc','파마약 2제(산화제).','염·생활 화학'],
['KI 아이오딘화 칼륨','2K + I2 → 2KI','flash','#f8fafc','방사선 사고 때 갑상선 보호약! 요오드 소금 성분.','염·생활 화학'],
['NaF 플루오린화 나트륨','2Na + F2 → 2NaF','flash','#f8fafc','불소 치약 성분.','염·생활 화학'],
['KF 플루오린화 칼륨','2K + F2 → 2KF','flash','#f8fafc','유기 합성에서 플루오린 공급원.','염·생활 화학'],
['Na2SiO3 규산 나트륨','Na2O + SiO2 → Na2SiO3','bub','#e0f2fe','“물유리”. 실리카겔 원료.','염·생활 화학'],
['Na3PO4 인산 나트륨','(H3PO4 + 3NaOH → Na3PO4 + 3H2O)','bub','#f8fafc','세척제·식품 첨가물.','염·생활 화학'],
['Na2B4O7 붕사','(단순화)','bub','#f8fafc','슬라임 만들 때 쓰는 그 붕사!','염·생활 화학'],
['NaNO2 아질산 나트륨','(단순화)','flash','#fef9c3','햄·소시지의 발색제.','염·생활 화학'],
['KCN 사이안화 칼륨','(단순화)','bub','#f8fafc','맹독. 금 채굴(시안화법)에 쓰여요.','염·생활 화학'],
['Na2S2O3 싸이오황산 나트륨','(단순화)','bub','#f8fafc','“하이포”. 사진 정착액, 수돗물 염소 제거제.','염·생활 화학'],
['CaF2 플루오린화 칼슘','Ca + F2 → CaF2','flash','#c4b5fd','형석. 자외선에 빛나요(형광의 어원!).','염·생활 화학'],
['MgCO3 탄산 마그네슘','(MgO + CO2 → MgCO3)','bub','#f8fafc','클라이밍·체조 선수가 손에 바르는 초크.','염·생활 화학'],
['SrCO3 탄산 스트론튬','(SrO + CO2 → SrCO3)','bub','#f8fafc','빨간 불꽃놀이 재료.','염·생활 화학'],
['BaCO3 탄산 바륨','(BaO + CO2 → BaCO3)','bub','#f8fafc','쥐약·도자기 유약.','염·생활 화학'],
['Li2CO3 탄산 리튬','(Li2O + CO2 → Li2CO3)','bub','#f8fafc','배터리 원료이자 조울증 치료제.','염·생활 화학'],
['CuCO3 탄산 구리','(단순화)','bub','#4ade80','구리 지붕이 초록색이 되는 녹청 성분.','염·생활 화학'],
['Cu(NO3)2 질산 구리','Cu + 4HNO3 → Cu(NO3)2 + 2NO2 + 2H2O','bub','#2563eb','구리를 질산에 넣으면 파랗게 변해요.','염·생활 화학'],
['Pb(NO3)2 질산 납','(단순화)','bub','#f8fafc','KI와 섞으면 “황금비” 침전!','염·생활 화학'],
['PbI2 아이오딘화 납','Pb(NO3)2 + 2KI → PbI2 + 2KNO3','flash','#facc15','황금비 실험의 노란 결정. 페로브스카이트 태양전지 원료.','염·생활 화학'],
['AgCl 염화 은','2Ag + Cl2 → 2AgCl','flash','#f8fafc','빛에 검게 변해요 — 사진 필름 원리.','할로젠화'],
['CH3Cl 클로로메테인','CH4 + Cl2 → CH3Cl + HCl','bub','#f8fafc','실리콘 고무 제조 원료.','유기 화합물'],
['CHCl3 클로로폼','(CH4 + 3Cl2 → CHCl3 + 3HCl)','bub','#f8fafc','옛 마취제.','유기 화합물'],
['C2H3Cl 염화 비닐','(단순화)','bub','#f8fafc','PVC 플라스틱 원료.','유기 화합물'],
['C2F4 테트라플루오로에틸렌','(단순화)','bub','#f8fafc','테플론 프라이팬 코팅의 원료.','유기 화합물'],
['C3H6 프로펜','(단순화)','bub','#f8fafc','폴리프로필렌(PP) 원료.','유기 화합물'],
['C8H8 스타이렌','(단순화)','bub','#f8fafc','스티로폼(폴리스타이렌) 원료.','유기 화합물'],
['C7H8 톨루엔','(단순화)','bub','#f8fafc','페인트 시너 용매.','유기 화합물'],
['C6H5OH 페놀','(단순화)','bub','#fecaca','최초의 수술용 소독약.','유기 화합물'],
['C7H6O2 벤조산','(단순화)','bub','#f8fafc','음료 방부제(안식향산).','유기 화합물'],
['C2H4O2 아세트산','(검증용 중복)','bub','#fff','','유기 화합물'],
['C4H8O2 아세트산 에틸','CH3COOH + C2H5OH → C4H8O2 + H2O','bub','#fef9c3','과일 향! 매니큐어 리무버.','유기 화합물'],
['C5H10O2 아세트산 메틸','(단순화)','bub','#fef9c3','바나나 향 계열 에스터 친구.','유기 화합물'],
['C7H14O2 아세트산 아이소아밀','(단순화)','bub','#fde047','진짜 바나나 향 성분!','유기 화합물'],
['C10H16O 캠퍼(장뇌)','(천연물)','bub','#f8fafc','멘소래담 같은 연고의 시원한 향.','유기 화합물'],
['C10H20O 멘톨','(천연물)','bub','#f8fafc','박하의 시원함.','유기 화합물'],
['C8H8O3 바닐린','(천연물)','bub','#fef3c7','바닐라 향의 주성분.','유기 화합물'],
['C9H8O 신남알데하이드','(천연물)','bub','#fdba74','계피 향!','유기 화합물'],
['C17H35COOH 스테아르산','(단순화)','bub','#f8fafc','양초·비누 원료 지방산.','유기 화합물'],
['C27H46O 콜레스테롤','(생체 분자)','bub','#fef9c3','세포막 성분.','유기 화합물'],
['C20H30O 레티놀','(생체 분자)','bub','#fde047','비타민 A.','유기 화합물'],
['C6H8O6 아스코르브산','(생체 분자)','bub','#fef3c7','비타민 C.','유기 화합물'],
['C5H5N5 아데닌','(생체 분자)','bub','#f8fafc','DNA 염기 A.','유기 화합물'],
['C5H9NO4 글루탐산','(생체 분자)','bub','#f8fafc','감칠맛(MSG)의 아미노산.','유기 화합물'],
['C3H5N3O9 나이트로글리세린','(C3H8O3 + 3HNO3 → C3H5N3O9 + 3H2O)','boom','#fef9c3','다이너마이트의 폭발 성분이자 협심증 약.','유기 화합물'],
['C7H5N3O6 TNT','(톨루엔의 나이트로화, 단순화)','boom','#fde047','폭발력 기준 단위 “TNT 환산”의 그 물질.','유기 화합물'],
['C60 풀러렌','(탄소 증발, 단순화)','flash','#1c1917','축구공 모양 탄소 분자. 1996 노벨화학상.','비금속·기타'],
['Al2SiO5 남정석','(광물)','flash','#3b82f6','파란 광물. 압력에 따라 3가지 결정형!','특수·공업'],
['Al2O3·Cr 루비','(Al2O3에 Cr 미량 → 단순화: Al 2 + O 3 + Cr 1 은 불가)','flash','#dc2626','','특수·공업'],
['CaMg(CO3)2 백운석','(광물)','flash','#f8fafc','돌로마이트. 알프스 돌로미티 산맥의 이름!','특수·공업'],
['KAlSi3O8 정장석','(광물)','flash','#fecaca','화강암의 분홍색 성분.','특수·공업'],
['NaAlSi3O8 조장석','(광물)','flash','#f8fafc','사장석 계열 광물.','특수·공업'],
['Fe2SiO4 철감람석','(광물)','flash','#365314','감람석의 철 끝성분.','특수·공업'],
['ZrSiO4 지르콘','(광물)','flash','#fca5a5','지구에서 가장 오래된 광물(약 44억 년).','특수·공업'],
['Cu2CO3(OH)2 공작석','(광물)','flash','#15803d','말라카이트. 초록 줄무늬 보석.','특수·공업'],
['PbCrO4 크로뮴산 납','(단순화)','flash','#facc15','스쿨버스 노란색 안료.','특수·공업'],
['MgB2 이붕화 마그네슘','Mg + 2B → MgB2','flash','#1c1917','39K에서 초전도가 되는 단순한 화합물.','특수·공업'],
['Nb3Sn 나이오븀-주석','3Nb + Sn → Nb3Sn','flash','#64748b','MRI·핵융합로 초전도 자석 선재.','특수·공업'],
['NbTi 나이오븀-타이타늄','Nb + Ti → NbTi (합금)','flash','#94a3b8','가장 많이 쓰이는 초전도 선재.','특수·공업'],
['Ni3Al 니켈 알루미나이드','3Ni + Al → Ni3Al','flash','#a8a29e','제트엔진 터빈 초합금의 강화상.','특수·공업'],
['SmCo5 사마륨-코발트','Sm + 5Co → SmCo5','flash','#57534e','고온에서도 강한 영구자석.','특수·공업'],
['TiC 탄화 타이타늄','Ti + C → TiC','flash','#3f3f46','공구 코팅용 초경질 세라믹.','특수·공업'],
['B4C 탄화 붕소','4B + C → B4C','flash','#1c1917','방탄조끼 세라믹, 원자로 제어봉.','특수·공업'],
['ZrC 탄화 지르코늄','Zr + C → ZrC','flash','#52525b','초고온 세라믹.','특수·공업'],
['GaP 인화 갈륨','Ga + P → GaP','flash','#86efac','초록 LED 반도체.','특수·공업'],
['AlN 질화 알루미늄','(검증용)','flash','#fff','','특수·공업'],
['InGaN 질화 인듐갈륨','In + Ga + N2 → InGaN (단순화)','flash','#60a5fa','파란·초록 LED 발광층.','특수·공업'],
['CuInSe2 셀렌화 구리인듐','(단순화)','flash','#1c1917','CIGS 박막 태양전지.','특수·공업'],
['Bi2Te3 텔루륨화 비스무트','2Bi + 3Te → Bi2Te3','flash','#78716c','열을 전기로 바꾸는 열전 소자.','특수·공업'],
['PbTe 텔루륨화 납','Pb + Te → PbTe','flash','#57534e','화성 탐사선 RTG의 열전 변환 재료.','특수·공업'],
['ZnSe 셀렌화 아연','Zn + Se → ZnSe','flash','#facc15','적외선 레이저 렌즈.','특수·공업'],
['CdS 황화 카드뮴','Cd + S → CdS','flash','#facc15','“카드뮴 옐로” 물감, 조도 센서(CdS 셀)!','황화'],
['Sb2S3 삼황화 이안티모니','2Sb + 3S → Sb2S3','flash','#1c1917','휘안석. 고대 이집트 아이라이너.','황화'],
['As2S3 삼황화 이비소','2As + 3S → As2S3','flash','#facc15','웅황. 옛 노란 안료(독성).','황화'],
['SnS2 이황화 주석','Sn + 2S → SnS2','flash','#fbbf24','“모자이크 금” 안료.','황화'],
['WS2 이황화 텅스텐','W + 2S → WS2','flash','#475569','2차원 반도체·고체 윤활제.','황화'],
['NiS 황화 니켈','Ni + S → NiS','flash','#1c1917','강화유리가 저절로 깨지는 원인 물질.','황화'],
['CoS 황화 코발트','Co + S → CoS','flash','#1c1917','석유 탈황 촉매.','황화'],
['Bi2S3 삼황화 이비스무트','2Bi + 3S → Bi2S3','flash','#292524','휘창연석.','황화'],
['Li2S 황화 리튬','2Li + S → Li2S','flash','#f8fafc','차세대 리튬-황 배터리의 핵심.','황화'],
['K2S 황화 칼륨','2K + S → K2S','boom','#fef3c7','흑색 화약이 타고 남는 성분.','황화']]
.forEach(([p,e,f,c,msg,ct])=>{if(!msg)return;const n=parseF(p.split(' ')[0]);if(!n){console.warn('파싱 실패',p);return}
 const sig=recStr(n);if(R.some(x=>x.a=='mix'&&recStr(NEED[sub(x.p)]||parseF(x.p.split(' ')[0])||{})==sig)){console.warn('중복 생략',p);return}
 if(Object.keys(n).length>4||Object.values(n).reduce((a,b)=>a+b,0)>90){console.warn('비커 초과',p);return}
 add(Object.keys(n),'mix',p,e,f,c,msg,ct)});
const seenK={};
for(const r of R){r.p=sub(r.p);
 if(r.a=='flame')r.need={[r.k]:1};
 else if(NEED[r.p])r.need=NEED[r.p];
 else{const n=parseF(r.p.split(' ')[0]);if(r.a=='water'&&n){delete n.H;delete n.O}r.need=n}
 if(!r.need)console.warn('레시피 없음',r.p);
 const base=r.a+':'+r.k;r.id=seenK[base]?base+'#'+recStr(r.need):base;seenK[base]=1}
// ---------- UI ----------
const $=id=>document.getElementById(id);let B=[],found=new Set((()=>{try{return JSON.parse(localStorage.getItem('elab2')||'[]')}catch(e){return[]}})()),safe=100,tab='전체';
const pt=$('pt');
for(const s of SYM){const e=E[s],[r,c]=pos(e.z),d=document.createElement('div');d.className='el c-'+e.c;d.style.gridRow=r;d.style.gridColumn=c;
 d.innerHTML=`<i>${e.z}</i><b>${s}</b><small>${e.n}</small>`;d.onclick=ev=>{const n=ev&&ev.shiftKey?5:1;for(let i=0;i<n;i++)put(s)};d.onmouseenter=()=>showInfo(s);pt.appendChild(d)}
const gap=document.createElement('div');gap.style.gridRow=8;gap.style.height='8px';pt.appendChild(gap);
$('legend').innerHTML=Object.entries(CAT).map(([k,v])=>`<span class="c-${k}">${v}</span>`).join('')+' <small>· 점선 테두리/정보창 ☢ = 방사성</small>';
function showInfo(s){const e=E[s],n=R.filter(r=>r.k.split(',').includes(s)).length;
 $('info').innerHTML=`<b style="font-size:18px">${s} · ${e.n}</b><br>원자 번호 ${e.z} · ${CAT[e.c]} · 상온 ${STATE[e.z]||(e.z>=104?'(미확인)':'고체')}${RADIO(e.z)?' · ☢ 방사성':''}${e.z>=93?' · 인공 원소':''}<br>${DESC[s]||''}<br>관련 실험: <b>${n}</b>개 ${n?'':'(이 원소로는 반응 실험이 준비되지 않았어요)'}`}
function put(s){showInfo(s);if(!B.includes(s)&&new Set(B).size>=4)return log('비커에는 원소 종류를 최대 4가지까지 넣을 수 있어요!');if(B.length>=90)return log("비커가 가득 찼어요! (원자 최대 90개)");B.push(s);draw()}
function tally(){const t={};B.forEach(s=>t[s]=(t[s]||0)+1);return t}
function undoB(){B.pop();draw()}
function draw(){const t=tally();$('contents').innerHTML=B.length?Object.keys(t).map(s=>`${s}<sub style="font-size:13px">×${t[s]}</sub>`).join(' + ')+`<div style="font-size:12px;font-weight:normal;opacity:.7">원자 ${B.length}개</div>`:'비어 있음';$('liquid').style.background='#38bdf855';$('liquid').style.height='30%'}
function clearB(){B=[];draw();log('비커를 비웠어요.')}
function log(h){$('log').innerHTML=h}
function fx(t,col){const f=$('fx'),bk=$('beaker');
 if(t=='boom'){bk.classList.add('shake');setTimeout(()=>bk.classList.remove('shake'),800)}
 if(t!='bub'){f.style.background=col+'cc';setTimeout(()=>f.style.background='',300)}
 for(let i=0;i<18;i++){const b=document.createElement('div');b.className='bubble';b.style.left=Math.random()*200+'px';b.style.animationDelay=Math.random()*.6+'s';f.appendChild(b);setTimeout(()=>b.remove(),2000)}}
function act(a){if(!B.length)return log('먼저 원소를 넣어주세요.');
 const z=Math.max(...B.map(s=>E[s].z));
 const k=[...new Set(B)].sort().join(','),T=tally(),same=n=>{const a=Object.keys(n);return a.length==Object.keys(T).length&&a.every(s=>T[s]==n[s])};
 if(a=='flame'){if(new Set(B).size>1)return log('불꽃 반응은 원소 1종으로만 정확히 볼 수 있어요.');const f=FL[B[0]];
  if(!f)return log(`${E[B[0]].n}은(는) 뚜렷한 불꽃색이 없어요.`);
  $('fx').style.background=`radial-gradient(circle at 50% 80%,${f[0]},transparent 70%)`;setTimeout(()=>$('fx').style.background='',1500);
  const r=R.find(x=>x.a=='flame'&&x.k==B[0]),nw=discover(r);log(`🔥 <b>${E[B[0]].n}</b>의 불꽃색: <b style="color:${f[0]}">${f[1]}</b>${nw?'<br>🎉 새 발견!':''}`);return}
 const r=R.find(x=>x.a==a&&same(x.need));
 if(!r){const near=R.filter(x=>x.a==a&&x.k==k);if(!near.length&&z>=99)return log('☢ 이 원소는 수명이 너무 짧아 알려진 화합물이 거의 없어요. (아인슈타이늄 산화물 등 극히 일부만 보고됨)');if(near.length)return log(`🤔 원소 종류는 맞았는데 <b>개수</b>가 달라요! 이 원소들로 만들 수 있는 화합물이 <b>${near.length}가지</b> 있어요. 화학식을 떠올리며 개수를 조절해 보세요. (예: H₂O → H 2개 + O 1개)`);if(B.some(s=>E[s].c=='noble'))return log('비활성 기체는 (거의) 반응하지 않아요. 단, 제논은 예외가 있다는데…?');
  if(B.some(s=>['Au','Pt'].includes(s))&&a=='mix')return log('금·백금 같은 귀금속은 산소와 잘 반응하지 않아요. 그래서 오래도록 빛나죠!');
  return log(a=='water'?'물에 넣었지만 눈에 띄는 반응이 없어요.':'반응이 일어나지 않았어요(또는 아직 준비되지 않은 조합). 다른 조합을 시도해 보세요!')}
 fx(r.fx,r.col);$('liquid').style.background=r.col+'99';$('liquid').style.height='55%';
 const isNew=discover(r);
 log(`${isNew?'🎉 <b>새 발견!</b> ':''}<b>${r.p}</b> <small>[${r.cat}]</small><br><code>${r.eq}</code><br>${r.msg}${r.cat=='핵·방사성'?'<br>☢ <small>실제로는 핫셀·차폐 시설과 허가가 필요한 물질이에요.</small>':''}`)}
function discover(r){const id=r.id,isNew=!found.has(id);if(isNew&&r)setTimeout(()=>toast(r),0);found.add(id);try{localStorage.setItem('elab2',JSON.stringify([...found]))}catch(e){}update();return isNew}
function hint(){const left=R.filter(r=>!found.has(r.id));if(!left.length)return log('🏆 모든 반응을 발견했어요!');
 const r=left[Math.floor(Math.random()*left.length)],s=r.k.split(',');log(`💡 힌트: <b>${E[s[0]].n}</b>을(를) 이용한 <b>${r.cat}</b> 실험이 아직 남아 있어요. (${r.a=='water'?'물에 넣기':r.a=='flame'?'불꽃 반응':s.length+'종 혼합'} · 원자 총 ${Object.values(r.need).reduce((a,b)=>a+b,0)}개)`)}
const cats=['전체',...new Set(R.map(r=>r.cat))];
$('tabs').innerHTML=cats.map(c=>`<button data-c="${c}">${c}</button>`).join('');
$('tabs').onclick=e=>{if(e.target.dataset.c){tab=e.target.dataset.c;update()}};
function update(){const n=R.filter(r=>found.has(r.id)).length;$('score').textContent=n;$('total').textContent=R.length;$('prog').style.width=n/R.length*100+'%';
 const t=[[0,'견습 연구원'],[10,'초보 화학자'],[30,'숙련 화학자'],[60,'수석 연구원'],[100,'노벨상 후보'],[R.length,'🏆 원소의 지배자']];$('title').textContent=t.filter(x=>n>=x[0]).pop()[1];
 [...$('tabs').children].forEach(b=>b.classList.toggle('on',b.dataset.c==tab));
 $('disc').innerHTML=R.filter(r=>tab=='전체'||r.cat==tab).map(r=>{const ok=found.has(r.id);
  return `<div class="disc ${ok?'':'no'}">${ok?'✅ <b>'+r.p+'</b> <small style="color:#93c5fd">['+recStr(r.need)+']</small>'+(r.eq?'<br><small>'+r.eq+'</small>':''):'❓ ??? <small>['+r.cat+']</small>'}</div>`}).join('')}
update();
let sessFound=0,expCount=0;
function hurt(n,why){streak=0;safe=Math.max(0,safe-n);$('safe').textContent=safe;$('safe').classList.toggle('low',safe<=30);
 if(safe<=0){$('overWhy').textContent='마지막 사고: '+why;
  const tot=R.filter(r=>found.has(r.id)).length;
  $('overStat').innerHTML=`<div class="stat">이번 판 실험<b>${expCount}</b></div><div class="stat">이번 판 새 발견<b>${sessFound}</b></div><div class="stat">전체 도감<b>${tot}/${R.length}</b></div><div class="stat">칭호<b style="font-size:16px">${$('title').textContent}</b></div>`;
  setTimeout(()=>$('over').classList.remove('hide'),900)}}
function startGame(){safe=100;sessFound=0;expCount=0;$('safe').textContent=safe;$('safe').classList.remove('low');B=[];draw();
 log('새 실험을 시작합니다! 🧪 원소를 골라 넣어 보세요.');$('menu').classList.add('hide');$('over').classList.add('hide')}
function toMenu(){const n=R.filter(r=>found.has(r.id)).length;
 $('menuRec').innerHTML=n?`<p>📖 현재 도감: <b>${n}/${R.length}</b> · 칭호 <b>${$('title').textContent}</b></p>`:'';
 $('over').classList.add('hide');$('menu').classList.remove('hide')}
function resetAll(){if(!confirm('도감 기록을 모두 지울까요?'))return;found.clear();try{localStorage.removeItem('elab2')}catch(e){}update();toMenu()}
const _act=act;act=function(a){if(safe<=0)return;if(B.length)expCount++;const before=found.size;_act(a);if(found.size>before)sessFound++};
(()=>{const bg=$('bgel');const s=['H','O','Na','Cl','Fe','Au','C','He','Cu','U','Mg','K'];
 s.forEach((x,i)=>{const d=document.createElement('div');d.className='floatel';d.textContent=x;d.style.left=(5+i*8)+'%';d.style.top=(10+(i*37)%80)+'%';d.style.animationDelay=i*.4+'s';bg.appendChild(d)})})();

let streak=0,quizCool=0;
function heal(n){if(safe<=0)return;const o=safe;safe=Math.min(100,safe+n);$('safe').textContent=safe;$('safe').classList.toggle('low',safe<=30);
 if(safe>o){$('safe').classList.add('up');setTimeout(()=>$('safe').classList.remove('up'),800)}}
function streakUp(){streak++;if(streak%5==0){heal(5);$('log').innerHTML+=`<br>🛡️ 무사고 연속 ${streak}회! 안전점수 +5`}}
const QZ=[['나트륨 같은 알칼리 금속은 어디에 보관해야 할까?',['석유(등유) 속','물 속','공기 중','냉장고 안 유리컵'],0],
['산을 묽힐 때 올바른 방법은?',['물에 산을 조금씩 넣는다','산에 물을 한꺼번에 붓는다','둘을 동시에 붓는다','흔들며 가열한다'],0],
['시약의 냄새를 맡는 올바른 방법은?',['손으로 바람을 일으켜 맡는다','코를 대고 깊게 맡는다','입으로 맛본다','가열하며 맡는다'],0],
['눈에 화학 약품이 튀었을 때 가장 먼저 할 일은?',['흐르는 물로 15분 이상 씻는다','눈을 비빈다','안약을 넣는다','그냥 참는다'],0],
['실험할 때 반드시 착용해야 하는 것은?',['보안경과 실험복','슬리퍼','반바지','콘택트렌즈만'],0],
['알코올 램프의 불은 어떻게 끄나?',['뚜껑을 덮어 끈다','입으로 분다','물을 붓는다','그대로 둔다'],0],
['시험관을 가열할 때 입구는 어디로 향해야 할까?',['사람이 없는 쪽','내 얼굴 쪽','친구 쪽','천장 정면 수직'],0],
['깨진 유리 기구는 어떻게 처리할까?',['선생님께 알리고 전용 수거함에 버린다','손으로 주워 일반 쓰레기통에','바닥에 그대로 둔다','물로 씻어 흘려보낸다'],0],
['유독 기체(예: 염소)가 발생하는 실험은 어디서 해야 할까?',['흄 후드(배기 장치) 안','밀폐된 교실','복도','책상 아래'],0],
['실험 후 남은 시약은 어떻게 할까?',['지정된 폐액통에 버린다','원래 시약병에 다시 붓는다','싱크대에 버린다','집에 가져간다'],0],
['기름(유류) 화재에 물을 부으면?',['불이 더 크게 번질 수 있다','바로 꺼진다','아무 일도 없다','얼음이 된다'],0],
['방사성 물질을 다룰 때 중요한 원칙이 아닌 것은?',['오래 가까이 머무르기','차폐하기','거리 두기','노출 시간 줄이기'],0]];
function openQuiz(){if(safe<=0)return;if(quizCool>0)return log(`🥽 안전 퀴즈는 실험을 ${quizCool}회 더 하면 다시 풀 수 있어요.`);
 const q=QZ[Math.floor(Math.random()*QZ.length)],ord=q[1].map((t,i)=>[t,i]).sort(()=>Math.random()-.5);
 $('qq').textContent=q[0];$('qr').textContent='';$('qclose').style.display='none';
 $('qo').innerHTML=ord.map(([t,i])=>`<button class="opt" data-i="${i}">${t}</button>`).join('');
 [...$('qo').children].forEach(b=>b.onclick=()=>{[...$('qo').children].forEach(x=>{x.disabled=true;if(x.dataset.i==q[2])x.classList.add('ok')});
  if(b.dataset.i==q[2]){heal(10);$('qr').innerHTML='⭕ 정답! 안전점수 <b>+10</b>'}else{b.classList.add('bad');$('qr').innerHTML='❌ 오답! 안전 수칙을 다시 확인해요. (감점 없음)'}
  quizCool=3;updQ();$('qclose').style.display='inline-block'});
 $('quiz').classList.remove('hide')}
function updQ(){$('qbtn').textContent=quizCool>0?`🥽 안전 퀴즈 (${quizCool})`:'🥽 안전 퀴즈 ✨'}
const _act2=act;act=function(a){if(safe>0&&B.length&&quizCool>0){quizCool--;updQ()}_act2(a)};
const _start=startGame;startGame=function(){streak=0;quizCool=0;updQ();_start()};

// ================= 배틀 미니게임 =================
const TY={'산화':'🔥','할로젠화':'🌿','물 반응':'💧','황화':'🟡','특수·공업':'⚙️','불꽃 반응':'🎆','비금속·기타':'🧪','유기 화합물':'🧬','염·생활 화학':'🧂','핵·방사성':'☢️'};
const BEATS={'산화':'할로젠화','할로젠화':'물 반응','물 반응':'산화','황화':'특수·공업','특수·공업':'황화','유기 화합물':'염·생활 화학','염·생활 화학':'유기 화합물','핵·방사성':'특수·공업','비금속·기타':'핵·방사성'};
let bp=0,bw=0,bl=0;try{const s=JSON.parse(localStorage.getItem('elabBP')||'{}');bp=s.bp||0;bw=s.w||0;bl=s.l||0}catch(e){}
function saveBP(){if($('shopBP'))$('shopBP').textContent=bp;try{localStorage.setItem('elabBP',JSON.stringify({bp,w:bw,l:bl}))}catch(e){}$('bp').textContent=bp;$('bpTop').textContent=bp;$('brec').textContent=`${bw}승 ${bl}패`}
function hsh(s){let x=0;for(const c of s)x=(x*31+c.charCodeAt(0))%997;return x}
function mkUnit(r){const n=r.k.split(',').length,T=Object.values(r.need).reduce((a,b)=>a+b,0),h=hsh(r.p)%10,fx=r.fx||'flash';
 let hp=55+n*12+Math.min(T,16)*2+h,atk=12+h%5,def=5+h%4;
 if(r.cat=='핵·방사성'){atk+=5;hp+=10}if(fx=='boom'){atk+=8;hp-=10}else if(fx=='bub'){def+=5;hp+=15}else{atk+=3;def+=2}
 const nm=r.p.replace(/\s.*$/,'');return{nm,full:r.p,ty:r.cat,fx,hp,max:hp,atk,def,cd:0,guard:false}}
let sel=[],me=[],en=[],busy=false;
function openBattle(){running=false;const own=R.filter(r=>found.has(r.id));sel=sel.filter(i=>found.has(R[i].id));
 $('pool').innerHTML=own.length?own.map(r=>{const i=R.indexOf(r),u=mkUnit(r);return`<div class="cc ${sel.includes(i)?'sel':''}" data-i="${i}"><b>${TY[r.cat]} ${r.p}</b><br>❤️${u.hp} ⚔️${u.atk} 🛡️${u.def}<br><span class="tp">${r.cat}</span> ${u.fx=='boom'?'💥':u.fx=='bub'?'🫧':'✨'}</div>`}).join(''):'<p>아직 발견한 화합물이 없어요! 먼저 실험실에서 도감을 채워 오세요 🧪</p>';
 [...$('pool').children].forEach(c=>c.onclick=()=>{const i=+c.dataset.i;if(sel.includes(i))sel=sel.filter(x=>x!=i);else if(sel.length<5)sel.push(i);else return;c.classList.toggle('sel');$('selN').textContent=sel.length});
 $('selN').textContent=sel.length;$('bSetup').style.display='';$('bFight').style.display='none';saveBP();
 $('menu').classList.add('hide');$('battle').classList.remove('hide')}
function closeBattle(){running=false;$('battle').classList.add('hide');if(safe<=0||!started)toMenu()}
let started=false;const _sg=startGame;startGame=function(){started=true;_sg()};
function startBattle(){if(!sel.length)return alertB('팀에 화합물을 최소 1개 넣어주세요!');
 me=sel.map(i=>mkUnit(R[i]));const pool=R.filter(r=>r.a!='flame'||true),n=Math.max(1,Math.min(5,me.length+(Math.random()<.3?1:0)));
 en=[];while(en.length<n){const r=pool[Math.floor(Math.random()*pool.length)],u=mkUnit(r);if(!en.some(e=>e.full==u.full))en.push(u)}
 $('bSetup').style.display='none';$('bFight').style.display='';$('bEnd').style.display='none';$('bAct').style.display='';$('blog').innerHTML='';
 blog(`⚔️ 배틀 시작! 내 팀 ${me.length}개 vs 상대 팀 ${en.length}개`);render()}
function alertB(t){$('selN').parentElement.innerHTML=`<b style="color:#f87171">${t}</b> (<span id="selN">${sel.length}</span>/5)`}
const alive=t=>t.filter(u=>u.hp>0);
const SK={'산화':'화염 폭발','할로젠화':'독침','물 반응':'회복 파동','황화':'가시 돌기','특수·공업':'강철 보호막','불꽃 반응':'폭죽','비금속·기타':'돌진','유기 화합물':'성장','염·생활 화학':'결정 감속장','핵·방사성':'방사선 오라'};
let balls=[],parts=[],pops=[],shots=[],bT=0,spd=1,shake=0,raf=0,running=false,cheerCd=0;
const AW=880,AH=500,TL=45,DMUL=1.8;
function mkBall(u,side,i,n){const r=Math.max(20,Math.min(42,14+u.max/7))*(u.fx=='bub'?1.12:1),a=Math.random()*Math.PI*2,v=(u.fx=='boom'?4.6:u.fx=='bub'?3:3.8);
 return Object.assign(u,{side,r,r0:r,x:side?AW-90-Math.random()*60:90+Math.random()*60,y:(AH/(n+1))*(i+1),vx:Math.cos(a)*v*(side?-1:1)*(Math.cos(a)>0?1:-1),vy:Math.sin(a)*v,v0:v,
  cd:2.5+Math.random()*3,spike:0,shield:0,dash:0,slow:0,boost:0,hitT:{},flash:0,dead:false,col:R.find(x=>x.p==u.full)?.col||'#94a3b8'})}
function startBattle(){if(!sel.length)return alertB('팀에 화합물을 최소 1개 넣어주세요!');
 me=sel.map(i=>mkUnit(R[i]));const n=Math.max(1,Math.min(5,me.length+(Math.random()<.3?1:0)));
 en=[];while(en.length<n){const r=R[Math.floor(Math.random()*R.length)],u=mkUnit(r);if(!en.some(e=>e.full==u.full))en.push(u)}
 me.forEach((u,i)=>mkBall(u,0,i,me.length));en.forEach((u,i)=>mkBall(u,1,i,en.length));balls=[...me,...en];parts=[];pops=[];shots=[];bT=0;shake=0;cheerCd=0;running=true;
 $('bSetup').style.display='none';$('bFight').style.display='';$('bEnd').style.display='none';$('bAct').style.display='';$('blog').innerHTML='';
 blog(`🎱 배틀 시작! 내 팀 ${me.length}개 vs 상대 팀 ${en.length}개`);let last=0;if(typeof cancelAnimationFrame=="function")cancelAnimationFrame(raf);
 const loop=t=>{if(!running)return;const dt=last?Math.min(.05,(t-last)/1000):.016;last=t;for(let k=0;k<spd;k++)step(dt);draw2();raf=requestAnimationFrame(loop)};
 if(typeof requestAnimationFrame=='function')raf=requestAnimationFrame(loop)}
function setSpd(){spd=spd>=3?1:spd+1;$('spdB').textContent='⏩ 속도 ×'+spd}
function cheer(){if(!running||cheerCd>0)return;cheerCd=10;alive(me).forEach(b=>{b.boost=2;burst(b.x,b.y,'#60a5fa',14)});popT(AW/4,40,'📣 힘내!','#60a5fa',26);blog('📣 응원! 내 팀이 2초간 가속해요.')}
function giveUp(){if(!running)return;me.forEach(b=>b.hp=0);blog('🏳 항복했어요…');finish()}
function burst(x,y,c,n,sp=4){for(let i=0;i<n;i++){const a=Math.random()*6.28,v=Math.random()*sp+1;parts.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:.5+Math.random()*.4,c})}}
function popT(x,y,t,c,s){pops.push({x,y,t,c,s,l:1})}
function hurt(t,d,src,big){if(t.dead)return;d*=DMUL;if(t.shield>0)d=Math.round(d*.5);d=Math.max(1,Math.round(d));t.hp=Math.max(0,t.hp-d);t.flash=.15;
 popT(t.x,t.y-t.r,'-'+d+(big?'!!':''),big?'#facc15':'#f87171',big?24:17);burst(t.x,t.y,t.col,6);if(big)shake=Math.max(shake,6);
 if(t.hp<=0)ko(t,src)}
function ko(t,src){t.dead=true;shake=10;burst(t.x,t.y,t.col,40,7);burst(t.x,t.y,'#fff',15,5);popT(t.x,t.y,'💀 KO','#fff',30);
 blog(`💀 ${t.side?'👾':'🙂'} ${t.nm} 쓰러짐!${src?' ('+src.nm+')':''}`);
 if(t.fx=='boom'){blog(`💥 ${t.nm}의 최후의 폭발!`);burst(t.x,t.y,'#f97316',40,9);balls.forEach(b=>{if(!b.dead&&b.side!=t.side&&Math.hypot(b.x-t.x,b.y-t.y)<120)hurt(b,t.atk*.8,t)})}}
function mult(x,y){return BEATS[x.ty]==y.ty?1.5:BEATS[y.ty]==x.ty?.75:1}
function skill(b){const foes=balls.filter(o=>!o.dead&&o.side!=b.side),pals=balls.filter(o=>!o.dead&&o.side==b.side);if(!foes.length)return;
 const near=foes.reduce((m,o)=>Math.hypot(o.x-b.x,o.y-b.y)<Math.hypot(m.x-b.x,m.y-b.y)?o:m),t=b.ty;popT(b.x,b.y-b.r-14,TY[t]+' '+(SK[t]||'스킬'),'#e9d5ff',15);
 if(t=='산화'){burst(b.x,b.y,'#f97316',35,8);shake=6;foes.forEach(o=>{if(Math.hypot(o.x-b.x,o.y-b.y)<b.r+110)hurt(o,b.atk*.9*mult(b,o),b)})}
 else if(t=='할로젠화'){const a=Math.atan2(near.y-b.y,near.x-b.x);shots.push({x:b.x,y:b.y,vx:Math.cos(a)*9,vy:Math.sin(a)*9,o:b,c:'#84cc16',e:'🟢',l:2})}
 else if(t=='불꽃 반응'){for(let i=0;i<3;i++){const a=Math.atan2(near.y-b.y,near.x-b.x)+(i-1)*.35;shots.push({x:b.x,y:b.y,vx:Math.cos(a)*8,vy:Math.sin(a)*8,o:b,c:b.col,e:'✨',l:2})}}
 else if(t=='물 반응'){burst(b.x,b.y,'#38bdf8',25,5);pals.forEach(o=>{if(Math.hypot(o.x-b.x,o.y-b.y)<160){const hl=Math.round(o.max*.12);o.hp=Math.min(o.max,o.hp+hl);popT(o.x,o.y,'+'+hl,'#4ade80',17)}})}
 else if(t=='핵·방사성'){burst(b.x,b.y,'#a3e635',40,6);b.aura=3;foes.forEach(o=>{if(Math.hypot(o.x-b.x,o.y-b.y)<200)hurt(o,b.atk*.45,b)})}
 else if(t=='황화')b.spike=3;
 else if(t=='특수·공업')b.shield=3.5;
 else if(t=='유기 화합물'){b.r=Math.min(b.r0*1.35,b.r*1.15);const hl=Math.round(b.max*.08);b.hp=Math.min(b.max,b.hp+hl);popT(b.x,b.y,'+'+hl,'#4ade80',16)}
 else if(t=='염·생활 화학'){burst(b.x,b.y,'#e0f2fe',25,5);foes.forEach(o=>{if(Math.hypot(o.x-b.x,o.y-b.y)<170)o.slow=3})}
 else{const a=Math.atan2(near.y-b.y,near.x-b.x);b.dash=1.5;b.vx=Math.cos(a)*b.v0*2.2;b.vy=Math.sin(a)*b.v0*2.2}}
function step(dt){if(!running)return;bT+=dt;cheerCd=Math.max(0,cheerCd-dt);const L=balls.filter(b=>!b.dead),k=dt*60;
 for(const b of L){for(const f of['spike','shield','dash','slow','boost','flash','aura'])b[f]=Math.max(0,(b[f]||0)-dt);
  b.cd-=dt;if(b.cd<=0){b.cd=4.5+Math.random()*1.5;skill(b)}
  let tv=b.v0*(b.dash>0?2.2:1)*(b.boost>0?1.8:1)*(b.slow>0?.5:1);const cv=Math.hypot(b.vx,b.vy)||1;b.vx+= (b.vx/cv*tv-b.vx)*.05;b.vy+=(b.vy/cv*tv-b.vy)*.05;
  b.x+=b.vx*k;b.y+=b.vy*k;
  if(b.x<b.r){b.x=b.r;b.vx=Math.abs(b.vx)}if(b.x>AW-b.r){b.x=AW-b.r;b.vx=-Math.abs(b.vx)}
  if(b.y<b.r){b.y=b.r;b.vy=Math.abs(b.vy)}if(b.y>AH-b.r){b.y=AH-b.r;b.vy=-Math.abs(b.vy)}
  if(Math.random()<.3)parts.push({x:b.x,y:b.y,vx:0,vy:0,l:.25,c:b.col+'88',tr:b.r*.5})}
 for(let i=0;i<L.length;i++)for(let j=i+1;j<L.length;j++){const a=L[i],b=L[j];if(a.dead||b.dead)continue;const dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||.01,ov=a.r+b.r-d;if(ov<=0)continue;
  const nx=dx/d,ny=dy/d,ma=a.r*a.r,mb=b.r*b.r;a.x-=nx*ov*mb/(ma+mb);a.y-=ny*ov*mb/(ma+mb);b.x+=nx*ov*ma/(ma+mb);b.y+=ny*ov*ma/(ma+mb);
  const rv=(b.vx-a.vx)*nx+(b.vy-a.vy)*ny;if(rv<0){const im=2*rv/(ma+mb);a.vx+=im*mb*nx;a.vy+=im*mb*ny;b.vx-=im*ma*nx;b.vy-=im*ma*ny}
  if(a.side!=b.side){const key=Math.min(balls.indexOf(a),balls.indexOf(b))+'-'+Math.max(balls.indexOf(a),balls.indexOf(b));if((a.hitT[key]||0)>bT)continue;a.hitT[key]=bT+.35;
   const sp=Math.min(2,Math.abs(rv)/4+.6);
   for(const[x,y]of[[a,b],[b,a]]){const m=mult(x,y)*(x.spike>0?2:1)*(x.dash>0?1.5:1);hurt(y,Math.max(2,(x.atk*m-y.def*.5)*sp*.55*(.85+Math.random()*.3)),x,m>=1.5)}
   burst(a.x+nx*a.r,a.y+ny*a.r,'#fff',8,5)}}
 for(const s of shots){s.x+=s.vx*k;s.y+=s.vy*k;s.l-=dt;for(const o of balls)if(!o.dead&&o.side!=s.o.side&&Math.hypot(o.x-s.x,o.y-s.y)<o.r+6){hurt(o,s.o.atk*.6*mult(s.o,o),s.o,mult(s.o,o)>1);s.l=0;break}
  if(s.x<0||s.x>AW||s.y<0||s.y>AH)s.l=0}
 shots=shots.filter(s=>s.l>0);
 for(const p of parts){p.x+=p.vx*k;p.y+=p.vy*k;p.vx*=.94;p.vy*=.94;p.l-=dt}parts=parts.filter(p=>p.l>0);if(parts.length>600)parts.splice(0,parts.length-600);
 for(const p of pops){p.y-=.6*k;p.l-=dt}pops=pops.filter(p=>p.l>0);shake=Math.max(0,shake-dt*30);
 if(!alive(me).length||!alive(en).length||bT>=TL)finish()}
function finish(){if(!running)return;running=false;
 if(bT>=TL&&alive(me).length&&alive(en).length){const pm=me.reduce((s,u)=>s+u.hp/u.max,0)/me.length,pe=en.reduce((s,u)=>s+u.hp/u.max,0)/en.length;
  blog(`⏰ 시간 종료! HP 비율 — 내 팀 ${Math.round(pm*100)}% vs 상대 ${Math.round(pe*100)}%`);(pm>=pe?en:me).forEach(u=>u.hp=0)}
 draw2();end()}
function draw2(){const c=$('bc');if(!c||!c.getContext)return;const g=c.getContext('2d');if(!g)return;g.save();g.clearRect(0,0,AW,AH);
 if(shake)g.translate((Math.random()-.5)*shake,(Math.random()-.5)*shake);
 g.strokeStyle=TH.gr;g.lineWidth=1;for(let x=0;x<AW;x+=40){g.beginPath();g.moveTo(x,0);g.lineTo(x,AH);g.stroke()}for(let y=0;y<AH;y+=40){g.beginPath();g.moveTo(0,y);g.lineTo(AW,y);g.stroke()}
 g.strokeStyle=TH.ln+'66';g.setLineDash([8,8]);g.beginPath();g.moveTo(AW/2,0);g.lineTo(AW/2,AH);g.stroke();g.setLineDash([]);
 for(const p of parts){g.globalAlpha=Math.max(0,p.l*2);g.fillStyle=p.c;g.beginPath();g.arc(p.x,p.y,p.tr||3,0,6.28);g.fill()}g.globalAlpha=1;
 for(const s of shots){g.font='20px sans-serif';g.textAlign='center';g.textBaseline='middle';g.shadowColor=s.c;g.shadowBlur=15;g.fillText(s.e,s.x,s.y)}g.shadowBlur=0;
 for(const b of balls){if(b.dead)continue;const tc=b.side?'#ef4444':'#3b82f6';
  if(b.shield>0){g.strokeStyle='#38bdf8';g.lineWidth=4;g.globalAlpha=.6+.3*Math.sin(bT*20);g.beginPath();g.arc(b.x,b.y,b.r+7,0,6.28);g.stroke();g.globalAlpha=1}
  if(b.aura>0){g.fillStyle='#a3e63522';g.beginPath();g.arc(b.x,b.y,200,0,6.28);g.fill();g.strokeStyle='#a3e63588';g.lineWidth=2;g.stroke()}
  if(b.slow>0){g.fillStyle='#e0f2fe33';g.beginPath();g.arc(b.x,b.y,b.r+4,0,6.28);g.fill()}
  if(b.spike>0){g.fillStyle='#facc15';for(let i=0;i<10;i++){const a=i/10*6.28+bT*4;g.beginPath();g.moveTo(b.x+Math.cos(a)*(b.r+12),b.y+Math.sin(a)*(b.r+12));g.lineTo(b.x+Math.cos(a+.2)*b.r,b.y+Math.sin(a+.2)*b.r);g.lineTo(b.x+Math.cos(a-.2)*b.r,b.y+Math.sin(a-.2)*b.r);g.fill()}}
  const gr=g.createRadialGradient(b.x-b.r*.35,b.y-b.r*.35,b.r*.1,b.x,b.y,b.r);gr.addColorStop(0,'#ffffff');gr.addColorStop(.35,b.col);gr.addColorStop(1,'#0f172a');
  g.fillStyle=b.flash>0?'#ffffff':gr;g.beginPath();g.arc(b.x,b.y,b.r,0,6.28);g.fill();g.lineWidth=b.dash>0||b.boost>0?5:3;g.strokeStyle=tc;g.stroke();
  g.fillStyle='#fff';g.font=`bold ${Math.max(10,Math.min(15,b.r*2.2/Math.max(3,b.nm.length)))}px sans-serif`;g.textAlign='center';g.textBaseline='middle';g.lineWidth=3;g.strokeStyle='#000';g.strokeText(b.nm,b.x,b.y);g.fillText(b.nm,b.x,b.y);
  g.font='13px sans-serif';g.fillText(TY[b.ty],b.x,b.y+b.r*.55);
  const bw2=b.r*2,f=b.hp/b.max;g.fillStyle='#000a';g.fillRect(b.x-b.r,b.y-b.r-10,bw2,5);g.fillStyle=f<.3?'#ef4444':b.side?'#f87171':'#4ade80';g.fillRect(b.x-b.r,b.y-b.r-10,bw2*f,5);
  const cf=1-Math.max(0,b.cd)/6;g.strokeStyle='#e9d5ff';g.lineWidth=2;g.beginPath();g.arc(b.x,b.y,b.r+2,-1.57,-1.57+6.28*cf);g.stroke()}
 for(const p of pops){g.globalAlpha=Math.min(1,p.l*1.5);g.font=`900 ${p.s}px sans-serif`;g.textAlign='center';g.lineWidth=4;g.strokeStyle='#000';g.strokeText(p.t,p.x,p.y);g.fillStyle=p.c;g.fillText(p.t,p.x,p.y)}
 g.globalAlpha=1;g.restore();
 $('hMe').textContent=`🙂 내 팀 ${alive(me).length}/${me.length}`;$('hEn').textContent=`👾 상대 ${alive(en).length}/${en.length}`;$('hTime').textContent=`⏱ ${Math.max(0,Math.ceil(TL-bT))}초`;
 $('cheerB').textContent=cheerCd>0?`📣 응원 (${Math.ceil(cheerCd)})`:'📣 응원 (가속)'}
function blog(t){$('blog').innerHTML+=t+'<br>';$('blog').scrollTop=1e9}
function end(){const w=!alive(en).length,l=!alive(me).length;if(!w&&!l)return false;$('bAct').style.display='none';$('bEnd').style.display='';
 if(w){const g=20+alive(me).length*10+en.length*5;bp+=g;bw++;blog(`<b style="color:#4ade80;font-size:16px">🏆 승리! 💎 +${g} BP 획득!</b>`)}
 else{bp+=3;bl++;blog(`<b style="color:#f87171;font-size:16px">😵 패배… 참가상 💎 +3 BP</b>`)}saveBP();return true}
saveBP();
toMenu();

// ================= 테마 상점 =================
const THEMES=[
 {id:'basic',n:'🧪 기본 실험실',p:0,d:'처음 테마',bg:'#0f172a',pn:'#1e293b',hd:'#1e293b',ac:'#2563eb',ar:'#0b1120',gr:'#1e293b',ln:'#334155'},
 {id:'forest',n:'🌿 숲속 연구소',p:80,d:'초록빛 자연 실험실',bg:'#052e16',pn:'#14532d',hd:'#166534',ac:'#16a34a',ar:'#022c22',gr:'#14532d',ln:'#4ade80'},
 {id:'ocean',n:'🌊 심해 기지',p:120,d:'깊은 바다 속 연구소',bg:'#082f49',pn:'#0c4a6e',hd:'#075985',ac:'#0284c7',ar:'#03213a',gr:'#0c4a6e',ln:'#38bdf8'},
 {id:'candy',n:'🍭 사탕 연구소',p:150,d:'달콤한 파스텔 테마',bg:'#500724',pn:'#831843',hd:'#9d174d',ac:'#ec4899',ar:'#3b0420',gr:'#831843',ln:'#f9a8d4'},
 {id:'neon',n:'🌃 네온 사이버',p:200,d:'형광 사이버펑크',bg:'#0a0014',pn:'#1a0033',hd:'#2e0057',ac:'#d946ef',ar:'#05000d',gr:'#3b0764',ln:'#22d3ee'},
 {id:'space',n:'🚀 우주 정거장',p:250,d:'무중력 실험실',bg:'#000000',pn:'#111827',hd:'#1f2937',ac:'#6366f1',ar:'#000005',gr:'#1e1b4b',ln:'#a5b4fc'},
 {id:'lava',n:'🌋 화산 실험실',p:300,d:'용암이 끓는 실험실',bg:'#1c0a00',pn:'#431407',hd:'#7c2d12',ac:'#ea580c',ar:'#140500',gr:'#431407',ln:'#fb923c'},
 {id:'nuke',n:'☢️ 핵 벙커',p:400,d:'방사능 경고등이 깜빡이는 지하 벙커',bg:'#0c0f00',pn:'#1a2e05',hd:'#365314',ac:'#65a30d',ar:'#070a00',gr:'#1a2e05',ln:'#bef264'},
 {id:'gold',n:'👑 황금 실험실',p:800,d:'최고의 화학자만을 위한 테마',bg:'#1c1400',pn:'#3f2d00',hd:'#713f12',ac:'#ca8a04',ar:'#120c00',gr:'#422006',ln:'#fde047'}];
let shopS={own:['basic'],cur:'basic'};try{const s=JSON.parse(localStorage.getItem('elabShop')||'null');if(s&&s.own)shopS=s}catch(e){}
function saveShop(){try{localStorage.setItem('elabShop',JSON.stringify(shopS))}catch(e){}}
let TH=THEMES[0];
function applyTheme(){TH=THEMES.find(t=>t.id==shopS.cur)||THEMES[0];let st=$('thStyle');if(!st){st=document.createElement('style');st.id='thStyle';document.head&&document.head.appendChild(st)}
 st.textContent=`body{background:${TH.bg}!important}.panel{background:${TH.pn}!important}header{background:${TH.hd}!important}button.on,.big{background:${TH.ac}}#log,#blog,.disc{background:${TH.ar}!important}`;
 const c=$('bc');if(c&&c.style){c.style.background=TH.ar;c.style.borderColor=TH.ln}}
function openShop(){renderShop();$('shop').classList.remove('hide')}
function closeShop(){$('shop').classList.add('hide')}
function renderShop(){$('shopBP').textContent=bp;
 $('shopList').innerHTML=THEMES.map(t=>{const own=shopS.own.includes(t.id),cur=shopS.cur==t.id;
  return `<div class="cc ${cur?'sel':''}"><b>${t.n}</b><div class="sw" style="background:${t.bg}"><i style="left:10px;background:${t.pn}"></i><i style="left:34px;background:${t.ac}"></i><i style="left:58px;background:${t.ln}"></i></div><small>${t.d}</small><br>
  <button data-t="${t.id}" style="margin-top:6px;width:100%;background:${cur?'#16a34a':own?'#2563eb':bp>=t.p?'#d97706':'#334155'}">${cur?'✅ 적용 중':own?'🎨 적용하기':'💎 '+t.p+' BP 구매'}</button></div>`}).join('');
 [...$('shopList').querySelectorAll?$('shopList').querySelectorAll('button'):[]].forEach(b=>b.onclick=()=>buyTheme(b.dataset.t))}
function buyTheme(id){const t=THEMES.find(x=>x.id==id);if(!t)return;
 if(!shopS.own.includes(id)){if(bp<t.p){$('shopMsg').innerHTML=`<b style="color:#f87171">💎 BP가 ${t.p-bp} 부족해요! 배틀에서 이겨 모아 오세요.</b>`;return}
  bp-=t.p;shopS.own.push(id);saveBP();$('shopMsg').innerHTML=`🎉 <b>${t.n}</b> 구매 완료!`}
 shopS.cur=id;saveShop();applyTheme();renderShop()}
heal=()=>{};streakUp=()=>{};
applyTheme();

// ===== 도감 알림 =====
function toast(r){let box=$('toasts');if(!box||!box.appendChild)return;const n=R.filter(x=>found.has(x.id)).length,
 t=document.createElement('div');t.className='toast';
 t.innerHTML=`📖 <b>도감 등록!</b> <small>(${n}/${R.length})</small><br><b class="big">${r.p}</b><br><small>[${r.cat}] ${r.need?recStr(r.need):''}</small>`+([10,30,60,100,150,200,250,300,R.length].includes(n)?`<br>🏅 <b>칭호 획득: ${$('title').textContent}</b>`:'');
 box.appendChild(t);setTimeout(()=>t.remove&&t.remove(),3800)}
</script></body></html>
"""

components.html(GAME_HTML, height=1500, scrolling=True)
