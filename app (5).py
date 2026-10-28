"""원소 실험실 시뮬레이터 v2 - Streamlit 앱
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
<title>원소 실험실 시뮬레이터 v3</title>
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
</style></head><body>
<div class="ov" id="menu"><div id="bgel"></div><div class="card">
<div class="logo">🧪</div><h1>원소 실험실</h1><p>118개 원소로 숨겨진 화학 반응을 찾아 도감을 완성하세요!<br>단, 위험한 실험을 너무 많이 하면 실험실이 폐쇄됩니다…</p>
<div id="menuRec"></div>
<button class="big" onclick="startGame()">▶ 게임 시작</button><button class="big" style="background:#9333ea" onclick="openBattle()">⚔️ 원소 배틀</button><button class="big" style="background:#475569" onclick="resetAll()">🗑 기록 초기화</button>
<div class="how"><b>🎮 게임 방법</b><br>
① 원소를 <b>화학식 개수만큼</b> 클릭해 넣어요 (예: H₂O = H 2번 + O 1번)<br>
② ⚗️ 혼합 · 💧 물 · 🔥 불꽃 버튼으로 실험해요<br>
③ 새로운 반응을 발견하면 도감에 등록돼요<br>
⚠️ 폭발 반응 <b>-5점</b>, 방사성 원소 사용 <b>-10점</b><br>💚 안전한 새 발견 <b>+2점</b>, 무사고 연속 5회 실험 <b>+5점</b>, 🥽 안전 퀴즈 정답 <b>+10점</b> (실험 3회마다 1번, 최대 100점)<br>
💀 <b>안전점수가 0이 되면 게임 오버!</b> (도감 기록은 유지돼요)</div>
<small style="color:#64748b">※ 교육용으로 단순화한 시뮬레이션입니다. 위험 반응은 절대 따라 하지 마세요.</small></div></div>
<div class="ov hide" id="quiz" style="background:#020617dd"><div class="card"><div class="logo" style="font-size:48px">🥽</div><h2 style="font-size:20px">실험실 안전 퀴즈</h2><p id="qq" style="font-size:17px"></p><div id="qo"></div><p id="qr"></p><button id="qclose" class="big" style="display:none" onclick="$('quiz').classList.add('hide')">계속 실험하기</button></div></div>
<div class="ov hide" id="battle"><div class="card">
<h1 style="font-size:32px;margin:4px">⚔️ 원소 배틀</h1><p>💎 배틀 포인트: <b id="bp">0</b> · 전적 <span id="brec"></span></p>
<div id="bSetup"><p>도감에서 발견한 화합물 중 <b>최대 5개</b>를 골라 팀을 만드세요! (<span id="selN">0</span>/5)</p>
<div class="bcards" id="pool"></div>
<div class="how" style="font-size:13px"><b>📘 배틀 규칙</b><br>
· 능력치는 반응 특성에서 나와요: 💥폭발 반응 = 공격형, ✨섬광 반응 = 균형형, 🫧거품 반응 = 방어형 (구성 원소가 많을수록 HP↑)<br>
· 타입 상성(공격 ×1.5): 🔥산화 → 🌿할로젠화 → 💧물 반응 → 🔥산화 / 🟡황화 ↔ ⚙️특수·공업 / 🧬유기 ↔ 🧂염·생활 / 🎆불꽃·🧪비금속은 무상성<br>
· 필살기: 공격력 ×2, 2턴 쿨타임 · 🛡️방어: 다음 피해 절반 + HP 10% 회복<br>
· 승리 시 💎 BP = 20 + 남은 화합물 수×10 + 상대 팀 수×5 (패배 시 참가상 3 BP)</div>
<button class="big" onclick="startBattle()">⚔️ 배틀 시작</button><button class="big" style="background:#475569" onclick="closeBattle()">↩ 돌아가기</button></div>
<div id="bFight" style="display:none">
<div class="arena" id="arena" style="position:relative"><div class="fighter" id="fMe"></div><div style="font-size:30px">VS</div><div class="fighter" id="fEn"></div></div>
<div class="btns" id="bAct"><button onclick="turn('atk')">👊 공격</button><button id="bSkill" onclick="turn('skill')">💥 필살기</button><button onclick="turn('def')">🛡️ 방어</button><button onclick="swapNext()">🔄 교체</button></div>
<div id="blog" style="margin-top:8px"></div>
<div id="bEnd" style="display:none"><button class="big" onclick="openBattle()">🔁 다시 배틀</button><button class="big" style="background:#475569" onclick="closeBattle()">↩ 돌아가기</button></div>
</div></div></div>
<div class="ov hide" id="over"><div class="card"><div class="logo">💥</div><h1>GAME OVER</h1>
<p>안전점수가 0이 되어 실험실이 폐쇄되었습니다!<br><span id="overWhy"></span></p>
<div id="overStat"></div>
<button class="big" onclick="startGame()">🔄 다시 도전</button><button class="big" style="background:#475569" onclick="toMenu()">🏠 메인 화면</button></div></div>
<header><h1><button onclick="toMenu()" style="padding:4px 8px">🏠</button> 🧪 원소 실험실 시뮬레이터 v2</h1><div>발견 <b id="score">0</b>/<span id="total"></span> · 안전점수 <b id="safe">100</b> · 칭호 <b id="title">견습 연구원</b> · 💎 BP <b id="bpTop">0</b></div></header>
<div class="panel"><h2>① 주기율표 — 화학식의 원자 개수만큼 클릭! (H₂O = H 2번 + O 1번 · 최대 4종/24개)</h2><div id="pt"></div>
<div class="legend" id="legend"></div></div>
<div class="row">
 <div class="panel"><h2>원소 정보</h2><div id="info">원소에 마우스를 올리면 정보가 보여요.</div></div>
 <div class="panel" id="bench"><h2>② 실험대</h2>
  <div id="beaker"><div id="contents">비어 있음</div><div id="liquid"></div><div id="fx"></div></div>
  <div class="btns"><button onclick="act('mix')">⚗️ 혼합/가열·점화</button><button onclick="act('water')">💧 물에 넣기</button><button onclick="act('flame')">🔥 불꽃 반응</button><button onclick="hint()">💡 힌트</button><button onclick="openBattle()" style="background:#7e22ce">⚔️ 배틀</button><button id="qbtn" onclick="openQuiz()">🥽 안전 퀴즈</button><button onclick="undoB()">↩ 하나 빼기</button><button onclick="clearB()">🧹 비우기</button></div>
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
 d.innerHTML=`<i>${e.z}</i><b>${s}</b><small>${e.n}</small>`;d.onclick=()=>put(s);d.onmouseenter=()=>showInfo(s);pt.appendChild(d)}
const gap=document.createElement('div');gap.style.gridRow=8;gap.style.height='8px';pt.appendChild(gap);
$('legend').innerHTML=Object.entries(CAT).map(([k,v])=>`<span class="c-${k}">${v}</span>`).join('')+' <small>· 점선 테두리/정보창 ☢ = 방사성</small>';
function showInfo(s){const e=E[s],n=R.filter(r=>r.k.split(',').includes(s)).length;
 $('info').innerHTML=`<b style="font-size:18px">${s} · ${e.n}</b><br>원자 번호 ${e.z} · ${CAT[e.c]} · 상온 ${STATE[e.z]||(e.z>=104?'(미확인)':'고체')}${RADIO(e.z)?' · ☢ 방사성':''}${e.z>=93?' · 인공 원소':''}<br>${DESC[s]||''}<br>관련 실험: <b>${n}</b>개 ${n?'':'(이 원소로는 반응 실험이 준비되지 않았어요)'}`}
function put(s){showInfo(s);if(!B.includes(s)&&new Set(B).size>=4)return log('비커에는 원소 종류를 최대 4가지까지 넣을 수 있어요!');if(B.length>=24)return log('비커가 가득 찼어요! (원자 최대 24개)');B.push(s);draw()}
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
 if(z>=99)return log('☢ 이 원소는 몇 초~몇 분 만에 붕괴하는 초중원소예요. 입자가속기에서 원자 몇 개만 만들어져 화학 실험이 거의 불가능해요!');
 if(B.some(s=>RADIO(E[s].z))){log('☢ 방사성 원소는 이 실험실에서 다룰 수 없어요! 차폐 시설이 필요합니다. (안전점수 -10)');return hurt(10,'방사성 원소 '+B.filter(s=>RADIO(E[s].z)).map(s=>E[s].n).join(', ')+' 취급')}
 const k=[...new Set(B)].sort().join(','),T=tally(),same=n=>{const a=Object.keys(n);return a.length==Object.keys(T).length&&a.every(s=>T[s]==n[s])};
 if(a=='flame'){if(new Set(B).size>1)return log('불꽃 반응은 원소 1종으로만 정확히 볼 수 있어요.');const f=FL[B[0]];
  if(!f)return log(`${E[B[0]].n}은(는) 뚜렷한 불꽃색이 없어요.`);
  $('fx').style.background=`radial-gradient(circle at 50% 80%,${f[0]},transparent 70%)`;setTimeout(()=>$('fx').style.background='',1500);
  const r=R.find(x=>x.a=='flame'&&x.k==B[0]),nw=discover(r);log(`🔥 <b>${E[B[0]].n}</b>의 불꽃색: <b style="color:${f[0]}">${f[1]}</b>${nw?'<br>💚 새 발견 — 안전점수 +2':''}`);if(nw)heal(2);streakUp();return}
 const r=R.find(x=>x.a==a&&same(x.need));
 if(!r){const near=R.filter(x=>x.a==a&&x.k==k);if(near.length)return log(`🤔 원소 종류는 맞았는데 <b>개수</b>가 달라요! 이 원소들로 만들 수 있는 화합물이 <b>${near.length}가지</b> 있어요. 화학식을 떠올리며 개수를 조절해 보세요. (예: H₂O → H 2개 + O 1개)`);if(B.some(s=>E[s].c=='noble'))return log('비활성 기체는 (거의) 반응하지 않아요. 단, 제논은 예외가 있다는데…?');
  if(B.some(s=>['Au','Pt'].includes(s))&&a=='mix')return log('금·백금 같은 귀금속은 산소와 잘 반응하지 않아요. 그래서 오래도록 빛나죠!');
  return log(a=='water'?'물에 넣었지만 눈에 띄는 반응이 없어요.':'반응이 일어나지 않았어요(또는 아직 준비되지 않은 조합). 다른 조합을 시도해 보세요!')}
 fx(r.fx,r.col);$('liquid').style.background=r.col+'99';$('liquid').style.height='55%';
 const isNew=discover(r);
 log(`${isNew?'🎉 <b>새 발견!</b> ':''}<b>${r.p}</b> <small>[${r.cat}]</small><br><code>${r.eq}</code><br>${r.msg}${r.fx=='boom'?'<br>⚠️ 위험 반응 — 안전점수 -5':''}${isNew&&r.fx!='boom'?'<br>💚 안전한 새 발견 — 안전점수 +2':''}`);if(r.fx=='boom')hurt(5,r.p+' 폭발');else{if(isNew)heal(2);streakUp()}}
function discover(r){const id=r.id,isNew=!found.has(id);found.add(id);try{localStorage.setItem('elab2',JSON.stringify([...found]))}catch(e){}update();return isNew}
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
 log('새 실험을 시작합니다! 안전점수 100점. 조심해서 실험하세요 🥽');$('menu').classList.add('hide');$('over').classList.add('hide')}
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
const TY={'산화':'🔥','할로젠화':'🌿','물 반응':'💧','황화':'🟡','특수·공업':'⚙️','불꽃 반응':'🎆','비금속·기타':'🧪','유기 화합물':'🧬','염·생활 화학':'🧂'};
const BEATS={'산화':'할로젠화','할로젠화':'물 반응','물 반응':'산화','황화':'특수·공업','특수·공업':'황화','유기 화합물':'염·생활 화학','염·생활 화학':'유기 화합물'};
let bp=0,bw=0,bl=0;try{const s=JSON.parse(localStorage.getItem('elabBP')||'{}');bp=s.bp||0;bw=s.w||0;bl=s.l||0}catch(e){}
function saveBP(){try{localStorage.setItem('elabBP',JSON.stringify({bp,w:bw,l:bl}))}catch(e){}$('bp').textContent=bp;$('bpTop').textContent=bp;$('brec').textContent=`${bw}승 ${bl}패`}
function hsh(s){let x=0;for(const c of s)x=(x*31+c.charCodeAt(0))%997;return x}
function mkUnit(r){const n=r.k.split(',').length,T=Object.values(r.need).reduce((a,b)=>a+b,0),h=hsh(r.p)%10,fx=r.fx||'flash';
 let hp=55+n*12+Math.min(T,16)*2+h,atk=12+h%5,def=5+h%4;
 if(fx=='boom'){atk+=8;hp-=10}else if(fx=='bub'){def+=5;hp+=15}else{atk+=3;def+=2}
 const nm=r.p.replace(/\s.*$/,'');return{nm,full:r.p,ty:r.cat,fx,hp,max:hp,atk,def,cd:0,guard:false}}
let sel=[],me=[],en=[],busy=false;
function openBattle(){const own=R.filter(r=>found.has(r.id));sel=sel.filter(i=>found.has(R[i].id));
 $('pool').innerHTML=own.length?own.map(r=>{const i=R.indexOf(r),u=mkUnit(r);return`<div class="cc ${sel.includes(i)?'sel':''}" data-i="${i}"><b>${TY[r.cat]} ${r.p}</b><br>❤️${u.hp} ⚔️${u.atk} 🛡️${u.def}<br><span class="tp">${r.cat}</span> ${u.fx=='boom'?'💥':u.fx=='bub'?'🫧':'✨'}</div>`}).join(''):'<p>아직 발견한 화합물이 없어요! 먼저 실험실에서 도감을 채워 오세요 🧪</p>';
 [...$('pool').children].forEach(c=>c.onclick=()=>{const i=+c.dataset.i;if(sel.includes(i))sel=sel.filter(x=>x!=i);else if(sel.length<5)sel.push(i);else return;c.classList.toggle('sel');$('selN').textContent=sel.length});
 $('selN').textContent=sel.length;$('bSetup').style.display='';$('bFight').style.display='none';saveBP();
 $('menu').classList.add('hide');$('battle').classList.remove('hide')}
function closeBattle(){$('battle').classList.add('hide');if(safe<=0||!started)toMenu()}
let started=false;const _sg=startGame;startGame=function(){started=true;_sg()};
function startBattle(){if(!sel.length)return alertB('팀에 화합물을 최소 1개 넣어주세요!');
 me=sel.map(i=>mkUnit(R[i]));const pool=R.filter(r=>r.a!='flame'||true),n=Math.max(1,Math.min(5,me.length+Math.floor(Math.random()*2)));
 en=[];while(en.length<n){const r=pool[Math.floor(Math.random()*pool.length)],u=mkUnit(r);if(!en.some(e=>e.full==u.full))en.push(u)}
 $('bSetup').style.display='none';$('bFight').style.display='';$('bEnd').style.display='none';$('bAct').style.display='';$('blog').innerHTML='';
 blog(`⚔️ 배틀 시작! 내 팀 ${me.length}개 vs 상대 팀 ${en.length}개`);render()}
function alertB(t){$('selN').parentElement.innerHTML=`<b style="color:#f87171">${t}</b> (<span id="selN">${sel.length}</span>/5)`}
const alive=t=>t.filter(u=>u.hp>0);
function fighter(u,t){return`<div class="nm">${TY[u.ty]} ${u.nm}</div><span class="tp">${u.ty}</span><div class="hp"><div style="width:${u.hp/u.max*100}%;background:${u.hp/u.max<.3?'#ef4444':'#22c55e'}"></div></div>❤️ ${u.hp}/${u.max} ⚔️${u.atk} 🛡️${u.def}${u.guard?' 🛡️방어중':''}<div class="team">${t.map(x=>x.hp>0?'🟢':'⚫').join('')}</div>`}
function render(){const a=alive(me)[0],b=alive(en)[0];if(a)$('fMe').innerHTML='<small>내 화합물</small>'+fighter(a,me);if(b)$('fEn').innerHTML='<small>상대 화합물</small>'+fighter(b,en);
 if(a)$('bSkill').textContent=a.cd>0?`💥 필살기 (${a.cd})`:'💥 필살기';}
function blog(t){$('blog').innerHTML+=t+'<br>';$('blog').scrollTop=1e9}
function dmg(x,y,mul){let m=mul;if(BEATS[x.ty]==y.ty)m*=1.5;else if(BEATS[y.ty]==x.ty)m*=.75;
 let d=Math.max(3,Math.round((x.atk*m-y.def)*(0.85+Math.random()*.3)));if(y.guard){d=Math.round(d/2);y.guard=false}y.hp=Math.max(0,y.hp-d);
 return[d,m>mul?' (효과 굉장함!)':m<mul?' (효과 별로…)':'']}
function spawn(cls,txt,ms,css){const ar=$('arena'),d=document.createElement('div');d.className=cls;d.textContent=txt;if(css)Object.assign(d.style,css);ar.appendChild(d);setTimeout(()=>d.remove(),ms)}
function flashCls(el,c,ms){el.classList.add(c);setTimeout(()=>el.classList.remove(c),ms)}
function act1(x,y,k,who){const mine=who=='🙂',self=$(mine?'fMe':'fEn'),tgt=$(mine?'fEn':'fMe'),side=mine?'atL':'atR',oside=mine?'atR':'atL';
 if(k=='def'){x.guard=true;const hl=Math.round(x.max*.1);x.hp=Math.min(x.max,x.hp+hl);flashCls(self,'guardfx',700);spawn('pop '+side,'🛡️ +'+hl,900,{color:'#38bdf8',fontSize:'24px'});return blog(`${who} ${x.nm}: 🛡️ 방어 태세! HP +${hl}`)}
 const sk=k=='skill';if(sk)x.cd=3;const guarded=y.guard,[d,eff]=dmg(x,y,sk?2:1);
 spawn('proj '+(mine?'toR':'toL')+(sk?' big':''),sk?TY[x.ty]+'💥':TY[x.ty],450);
 setTimeout(()=>{flashCls(tgt,'hit',450);
  spawn('pop '+oside,(guarded?'🛡️':'')+'-'+d+(eff.includes('굉장')?'!!':''),900,{color:eff.includes('굉장')?'#facc15':eff.includes('별로')?'#94a3b8':'#f87171',fontSize:(sk?40:28)+'px'});
  if(sk){spawn('boomfx '+oside,'💥',650);flashCls($('arena'),'flashA',300)}
  if(y.hp<=0){flashCls(tgt,'ko',600);spawn('pop '+oside,'💀 KO',1000,{color:'#fff',fontSize:'34px',top:'55%'})}},380);
 blog(`${who} ${x.nm}의 ${sk?'💥 필살기':'👊 공격'}! → ${y.nm}에게 ${d} 피해${eff}`);if(y.hp<=0)blog(`💀 ${y.nm} 쓰러짐!`)}
function turn(k){if(busy)return;const a=alive(me)[0],b=alive(en)[0];if(!a||!b)return;if(k=='skill'&&a.cd>0)return blog(`⏳ 필살기 쿨타임 ${a.cd}턴 남음`);
 act1(a,b,k,'🙂');a.cd=Math.max(0,a.cd-(k=='skill'?0:1));busy=true;setTimeout(()=>{render();if(end()){busy=false;return}
 setTimeout(()=>{const e=alive(en)[0],t=alive(me)[0];const r=Math.random(),ek=e.cd==0&&r<.3?'skill':r>.85&&e.hp<e.max*.5?'def':'atk';
  act1(e,t,ek,'👾');if(ek!='skill')e.cd=Math.max(0,e.cd-1);setTimeout(()=>{busy=false;render();end()},420)},500)},420)}
function swapNext(){if(busy)return;const al=alive(me);if(al.length<2)return blog('교체할 화합물이 없어요!');
 const i=me.indexOf(al[0]);me.push(me.splice(i,1)[0]);blog(`🔄 ${al[0].nm} 후퇴! ${alive(me)[0].nm} 등장! (상대가 공격해요)`);render();busy=true;
 setTimeout(()=>{act1(alive(en)[0],alive(me)[0],'atk','👾');setTimeout(()=>{busy=false;render();end()},420)},600)}
function end(){const w=!alive(en).length,l=!alive(me).length;if(!w&&!l)return false;$('bAct').style.display='none';$('bEnd').style.display='';
 if(w){const g=20+alive(me).length*10+en.length*5;bp+=g;bw++;blog(`<b style="color:#4ade80;font-size:16px">🏆 승리! 💎 +${g} BP 획득!</b>`)}
 else{bp+=3;bl++;blog(`<b style="color:#f87171;font-size:16px">😵 패배… 참가상 💎 +3 BP</b>`)}saveBP();return true}
saveBP();
toMenu();
</script></body></html>
"""

components.html(GAME_HTML, height=1400, scrolling=True)
