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
<title>원소 실험실 시뮬레이터 v2 – 118 원소</title>
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
</style></head><body>
<div class="ov" id="menu"><div id="bgel"></div><div class="card">
<div class="logo">🧪</div><h1>원소 실험실</h1><p>118개 원소로 숨겨진 화학 반응을 찾아 도감을 완성하세요!<br>단, 위험한 실험을 너무 많이 하면 실험실이 폐쇄됩니다…</p>
<div id="menuRec"></div>
<button class="big" onclick="startGame()">▶ 게임 시작</button><button class="big" style="background:#475569" onclick="resetAll()">🗑 기록 초기화</button>
<div class="how"><b>🎮 게임 방법</b><br>
① 주기율표에서 원소를 클릭해 비커에 넣어요 (최대 3종)<br>
② ⚗️ 혼합 · 💧 물 · 🔥 불꽃 버튼으로 실험해요<br>
③ 새로운 반응을 발견하면 도감에 등록돼요<br>
⚠️ 폭발 반응 <b>-5점</b>, 방사성 원소 사용 <b>-10점</b><br>
💀 <b>안전점수가 0이 되면 게임 오버!</b> (도감 기록은 유지돼요)</div>
<small style="color:#64748b">※ 교육용으로 단순화한 시뮬레이션입니다. 위험 반응은 절대 따라 하지 마세요.</small></div></div>
<div class="ov hide" id="over"><div class="card"><div class="logo">💥</div><h1>GAME OVER</h1>
<p>안전점수가 0이 되어 실험실이 폐쇄되었습니다!<br><span id="overWhy"></span></p>
<div id="overStat"></div>
<button class="big" onclick="startGame()">🔄 다시 도전</button><button class="big" style="background:#475569" onclick="toMenu()">🏠 메인 화면</button></div></div>
<header><h1><button onclick="toMenu()" style="padding:4px 8px">🏠</button> 🧪 원소 실험실 시뮬레이터 v2</h1><div>발견 <b id="score">0</b>/<span id="total"></span> · 안전점수 <b id="safe">100</b> · 칭호 <b id="title">견습 연구원</b></div></header>
<div class="panel"><h2>① 주기율표 — 클릭해서 비커에 넣기 (최대 3종)</h2><div id="pt"></div>
<div class="legend" id="legend"></div></div>
<div class="row">
 <div class="panel"><h2>원소 정보</h2><div id="info">원소에 마우스를 올리면 정보가 보여요.</div></div>
 <div class="panel" id="bench"><h2>② 실험대</h2>
  <div id="beaker"><div id="contents">비어 있음</div><div id="liquid"></div><div id="fx"></div></div>
  <div class="btns"><button onclick="act('mix')">⚗️ 혼합/가열·점화</button><button onclick="act('water')">💧 물에 넣기</button><button onclick="act('flame')">🔥 불꽃 반응</button><button onclick="hint()">💡 힌트</button><button onclick="clearB()">🧹 비우기</button></div>
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
const sub=s=>s.replace(/(\d+)/g,m=>[...m].map(d=>'₀₁₂₃₄₅₆₇₈₉'[d]).join(''));
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
// ---------- UI ----------
const $=id=>document.getElementById(id);let B=[],found=new Set((()=>{try{return JSON.parse(localStorage.getItem('elab2')||'[]')}catch(e){return[]}})()),safe=100,tab='전체';
const pt=$('pt');
for(const s of SYM){const e=E[s],[r,c]=pos(e.z),d=document.createElement('div');d.className='el c-'+e.c;d.style.gridRow=r;d.style.gridColumn=c;
 d.innerHTML=`<i>${e.z}</i><b>${s}</b><small>${e.n}</small>`;d.onclick=()=>put(s);d.onmouseenter=()=>showInfo(s);pt.appendChild(d)}
const gap=document.createElement('div');gap.style.gridRow=8;gap.style.height='8px';pt.appendChild(gap);
$('legend').innerHTML=Object.entries(CAT).map(([k,v])=>`<span class="c-${k}">${v}</span>`).join('')+' <small>· 점선 테두리/정보창 ☢ = 방사성</small>';
function showInfo(s){const e=E[s],n=R.filter(r=>r.k.split(',').includes(s)).length;
 $('info').innerHTML=`<b style="font-size:18px">${s} · ${e.n}</b><br>원자 번호 ${e.z} · ${CAT[e.c]} · 상온 ${STATE[e.z]||(e.z>=104?'(미확인)':'고체')}${RADIO(e.z)?' · ☢ 방사성':''}${e.z>=93?' · 인공 원소':''}<br>${DESC[s]||''}<br>관련 실험: <b>${n}</b>개 ${n?'':'(이 원소로는 반응 실험이 준비되지 않았어요)'}`}
function put(s){showInfo(s);if(B.includes(s))return log(`${E[s].n}은(는) 이미 들어 있어요.`);if(B.length>=3)return log('비커에는 최대 3종까지!');B.push(s);draw()}
function draw(){$('contents').textContent=B.length?B.join(' + '):'비어 있음';$('liquid').style.background='#38bdf855';$('liquid').style.height='30%'}
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
 const k=[...B].sort().join(',');
 if(a=='flame'){if(B.length>1)return log('불꽃 반응은 원소 1종으로만 정확히 볼 수 있어요.');const f=FL[B[0]];
  if(!f)return log(`${E[B[0]].n}은(는) 뚜렷한 불꽃색이 없어요.`);
  $('fx').style.background=`radial-gradient(circle at 50% 80%,${f[0]},transparent 70%)`;setTimeout(()=>$('fx').style.background='',1500);
  const r=R.find(x=>x.a=='flame'&&x.k==B[0]);discover(r);return log(`🔥 <b>${E[B[0]].n}</b>의 불꽃색: <b style="color:${f[0]}">${f[1]}</b>`)}
 const r=R.find(x=>x.k==k&&x.a==a);
 if(!r){if(B.some(s=>E[s].c=='noble'))return log('비활성 기체는 (거의) 반응하지 않아요. 단, 제논은 예외가 있다는데…?');
  if(B.some(s=>['Au','Pt'].includes(s))&&a=='mix')return log('금·백금 같은 귀금속은 산소와 잘 반응하지 않아요. 그래서 오래도록 빛나죠!');
  return log(a=='water'?'물에 넣었지만 눈에 띄는 반응이 없어요.':'반응이 일어나지 않았어요(또는 아직 준비되지 않은 조합). 다른 조합을 시도해 보세요!')}
 fx(r.fx,r.col);$('liquid').style.background=r.col+'99';$('liquid').style.height='55%';
 const isNew=discover(r);
 log(`${isNew?'🎉 <b>새 발견!</b> ':''}<b>${r.p}</b> <small>[${r.cat}]</small><br><code>${r.eq}</code><br>${r.msg}${r.fx=='boom'?'<br>⚠️ 위험 반응 — 안전점수 -5':''}`);if(r.fx=='boom')hurt(5,r.p+' 폭발')}
function discover(r){const id=r.a+':'+r.k,isNew=!found.has(id);found.add(id);try{localStorage.setItem('elab2',JSON.stringify([...found]))}catch(e){}update();return isNew}
function hint(){const left=R.filter(r=>!found.has(r.a+':'+r.k));if(!left.length)return log('🏆 모든 반응을 발견했어요!');
 const r=left[Math.floor(Math.random()*left.length)],s=r.k.split(',');log(`💡 힌트: <b>${E[s[0]].n}</b>을(를) 이용한 <b>${r.cat}</b> 실험이 아직 남아 있어요. (${r.a=='water'?'물에 넣기':r.a=='flame'?'불꽃 반응':s.length+'종 혼합'})`)}
const cats=['전체',...new Set(R.map(r=>r.cat))];
$('tabs').innerHTML=cats.map(c=>`<button data-c="${c}">${c}</button>`).join('');
$('tabs').onclick=e=>{if(e.target.dataset.c){tab=e.target.dataset.c;update()}};
function update(){const n=R.filter(r=>found.has(r.a+':'+r.k)).length;$('score').textContent=n;$('total').textContent=R.length;$('prog').style.width=n/R.length*100+'%';
 const t=[[0,'견습 연구원'],[10,'초보 화학자'],[30,'숙련 화학자'],[60,'수석 연구원'],[100,'노벨상 후보'],[R.length,'🏆 원소의 지배자']];$('title').textContent=t.filter(x=>n>=x[0]).pop()[1];
 [...$('tabs').children].forEach(b=>b.classList.toggle('on',b.dataset.c==tab));
 $('disc').innerHTML=R.filter(r=>tab=='전체'||r.cat==tab).map(r=>{const ok=found.has(r.a+':'+r.k);
  return `<div class="disc ${ok?'':'no'}">${ok?'✅ <b>'+r.p+'</b>'+(r.eq?'<br><small>'+r.eq+'</small>':''):'❓ ??? <small>['+r.cat+']</small>'}</div>`}).join('')}
update();
let sessFound=0,expCount=0;
function hurt(n,why){safe=Math.max(0,safe-n);$('safe').textContent=safe;$('safe').classList.toggle('low',safe<=30);
 if(safe<=0){$('overWhy').textContent='마지막 사고: '+why;
  const tot=R.filter(r=>found.has(r.a+':'+r.k)).length;
  $('overStat').innerHTML=`<div class="stat">이번 판 실험<b>${expCount}</b></div><div class="stat">이번 판 새 발견<b>${sessFound}</b></div><div class="stat">전체 도감<b>${tot}/${R.length}</b></div><div class="stat">칭호<b style="font-size:16px">${$('title').textContent}</b></div>`;
  setTimeout(()=>$('over').classList.remove('hide'),900)}}
function startGame(){safe=100;sessFound=0;expCount=0;$('safe').textContent=safe;$('safe').classList.remove('low');B=[];draw();
 log('새 실험을 시작합니다! 안전점수 100점. 조심해서 실험하세요 🥽');$('menu').classList.add('hide');$('over').classList.add('hide')}
function toMenu(){const n=R.filter(r=>found.has(r.a+':'+r.k)).length;
 $('menuRec').innerHTML=n?`<p>📖 현재 도감: <b>${n}/${R.length}</b> · 칭호 <b>${$('title').textContent}</b></p>`:'';
 $('over').classList.add('hide');$('menu').classList.remove('hide')}
function resetAll(){if(!confirm('도감 기록을 모두 지울까요?'))return;found.clear();try{localStorage.removeItem('elab2')}catch(e){}update();toMenu()}
const _act=act;act=function(a){if(safe<=0)return;if(B.length)expCount++;const before=found.size;_act(a);if(found.size>before)sessFound++};
(()=>{const bg=$('bgel');const s=['H','O','Na','Cl','Fe','Au','C','He','Cu','U','Mg','K'];
 s.forEach((x,i)=>{const d=document.createElement('div');d.className='floatel';d.textContent=x;d.style.left=(5+i*8)+'%';d.style.top=(10+(i*37)%80)+'%';d.style.animationDelay=i*.4+'s';bg.appendChild(d)})})();
toMenu();
</script></body></html>
"""

components.html(GAME_HTML, height=1400, scrolling=True)
