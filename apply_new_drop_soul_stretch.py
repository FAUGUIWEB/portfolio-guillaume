from pathlib import Path
import re

css_path=Path('styles.css')
css=css_path.read_text(encoding='utf-8')
start=css.index('.wave-title{')
end=css.index('.new-drop-carousel{', start)
new='''.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 10px rgba(255,43,43,.72),0 0 24px rgba(255,43,43,.46),0 0 48px rgba(255,43,43,.18);filter:drop-shadow(0 0 8px rgba(255,43,43,.26));overflow:visible;}
.wave-title span{position:relative;display:inline-block;transform-origin:center center;will-change:transform,filter,opacity;animation:newDropSoulStretch 4.25s cubic-bezier(.22,.72,.18,1) infinite;}
.wave-title span::after{content:attr(data-letter);position:absolute;inset:0;color:var(--red);-webkit-text-fill-color:var(--red);pointer-events:none;opacity:0;transform-origin:var(--origin,center) center;filter:blur(0);text-shadow:0 0 14px rgba(255,43,43,.8),0 0 34px rgba(255,43,43,.45);animation:newDropSoulTrail 4.25s cubic-bezier(.16,.76,.18,1) infinite;}
.wave-title span:nth-child(1){--shift:-.16em;--pull:-.30em;--origin:right;animation-delay:0s}.wave-title span:nth-child(2){--shift:-.12em;--pull:-.25em;--origin:right;animation-delay:.12s}.wave-title span:nth-child(3){--shift:-.075em;--pull:-.20em;--origin:right;animation-delay:.24s}.wave-title span:nth-child(4){animation:none;transform:none}.wave-title span:nth-child(4)::after{display:none}.wave-title span:nth-child(5){--shift:.075em;--pull:.20em;--origin:left;animation-delay:.36s}.wave-title span:nth-child(6){--shift:.12em;--pull:.25em;--origin:left;animation-delay:.48s}.wave-title span:nth-child(7){--shift:.15em;--pull:.29em;--origin:left;animation-delay:.60s}.wave-title span:nth-child(8){--shift:.18em;--pull:.34em;--origin:left;animation-delay:.72s}
.wave-title span:nth-child(1)::after{animation-delay:0s}.wave-title span:nth-child(2)::after{animation-delay:.12s}.wave-title span:nth-child(3)::after{animation-delay:.24s}.wave-title span:nth-child(5)::after{animation-delay:.36s}.wave-title span:nth-child(6)::after{animation-delay:.48s}.wave-title span:nth-child(7)::after{animation-delay:.60s}.wave-title span:nth-child(8)::after{animation-delay:.72s}
.wave-title::before,.wave-title::after,.wave-title span::before{content:none!important;display:none!important;}
@keyframes newDropSoulStretch{0%,8%,100%{transform:translateX(0) scaleX(1);filter:blur(0);opacity:1}24%{transform:translateX(calc(var(--shift,0)*.45)) scaleX(1.10);filter:blur(0);opacity:1}37%{transform:translateX(var(--shift,0)) scaleX(1.34);filter:blur(.15px);opacity:.98}48%{transform:translateX(calc(var(--shift,0)*.88)) scaleX(1.24);filter:blur(0);opacity:1}62%{transform:translateX(calc(var(--shift,0)*-.12)) scaleX(.985);filter:blur(0);opacity:1}72%,100%{transform:translateX(0) scaleX(1);filter:blur(0);opacity:1}}
@keyframes newDropSoulTrail{0%,13%,70%,100%{opacity:0;transform:translateX(0) scaleX(1);filter:blur(0)}24%{opacity:.20;transform:translateX(calc(var(--pull,0)*.28)) scaleX(1.18);filter:blur(.8px)}37%{opacity:.46;transform:translateX(var(--pull,0)) scaleX(1.72);filter:blur(2.2px)}46%{opacity:.25;transform:translateX(calc(var(--pull,0)*1.12)) scaleX(1.92);filter:blur(4px)}58%{opacity:.10;transform:translateX(calc(var(--pull,0)*.35)) scaleX(1.30);filter:blur(2px)}69%{opacity:0;transform:translateX(0) scaleX(1);filter:blur(0)}}
'''
css=css[:start]+new+css[end:]
css_path.write_text(css,encoding='utf-8')

html_path=Path('index.html')
html=html_path.read_text(encoding='utf-8')
old='<h2 class="new-drop-title wave-title" aria-label="New Drop"><span>N</span><span>E</span><span>W</span><span>&nbsp;</span><span>D</span><span>R</span><span>O</span><span>P</span></h2>'
newh='<h2 class="new-drop-title wave-title" aria-label="New Drop"><span data-letter="N">N</span><span data-letter="E">E</span><span data-letter="W">W</span><span>&nbsp;</span><span data-letter="D">D</span><span data-letter="R">R</span><span data-letter="O">O</span><span data-letter="P">P</span></h2>'
if old not in html: raise SystemExit('New Drop markup not found')
html=html.replace(old,newh,1)
html=re.sub(r'styles\.css\?v=[^"\']+','styles.css?v=20260825-16',html,1)
html_path.write_text(html,encoding='utf-8')
