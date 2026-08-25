from pathlib import Path
import re

p=Path('styles.css')
s=p.read_text(encoding='utf-8')
start=s.index('.wave-title{')
end=s.index('.new-drop-carousel{', start)
new=r'''.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 10px rgba(255,43,43,.72),0 0 24px rgba(255,43,43,.46),0 0 48px rgba(255,43,43,.18);overflow:visible;transform:translateZ(0);}
.wave-title span{position:relative;display:inline-block;transform-origin:center center;will-change:transform;backface-visibility:hidden;-webkit-backface-visibility:hidden;animation:newDropSoulStretch 4.35s cubic-bezier(.22,.68,.18,1) infinite;}
.wave-title span::after{content:attr(data-letter);position:absolute;inset:0;color:var(--red);-webkit-text-fill-color:var(--red);pointer-events:none;opacity:0;transform-origin:var(--origin,center) center;filter:blur(2.8px);text-shadow:0 0 18px rgba(255,43,43,.72),0 0 36px rgba(255,43,43,.34);will-change:transform,opacity;backface-visibility:hidden;-webkit-backface-visibility:hidden;animation:newDropSoulTrail 4.35s cubic-bezier(.18,.70,.16,1) infinite;}
.wave-title span:nth-child(1){--shift:-.22em;--pull:-.42em;--origin:right;animation-delay:0s}.wave-title span:nth-child(2){--shift:-.17em;--pull:-.35em;--origin:right;animation-delay:.10s}.wave-title span:nth-child(3){--shift:-.11em;--pull:-.28em;--origin:right;animation-delay:.20s}.wave-title span:nth-child(4){animation:none;transform:none}.wave-title span:nth-child(4)::after{display:none}.wave-title span:nth-child(5){--shift:.11em;--pull:.28em;--origin:left;animation-delay:.30s}.wave-title span:nth-child(6){--shift:.17em;--pull:.35em;--origin:left;animation-delay:.40s}.wave-title span:nth-child(7){--shift:.21em;--pull:.41em;--origin:left;animation-delay:.50s}.wave-title span:nth-child(8){--shift:.25em;--pull:.48em;--origin:left;animation-delay:.60s}
.wave-title span:nth-child(1)::after{animation-delay:0s}.wave-title span:nth-child(2)::after{animation-delay:.10s}.wave-title span:nth-child(3)::after{animation-delay:.20s}.wave-title span:nth-child(5)::after{animation-delay:.30s}.wave-title span:nth-child(6)::after{animation-delay:.40s}.wave-title span:nth-child(7)::after{animation-delay:.50s}.wave-title span:nth-child(8)::after{animation-delay:.60s}
.wave-title::before,.wave-title::after,.wave-title span::before{content:none!important;display:none!important;}
@keyframes newDropSoulStretch{0%,6%{transform:translate3d(0,0,0) scaleX(1)}28%{transform:translate3d(calc(var(--shift,0)*.48),0,0) scaleX(1.16)}43%{transform:translate3d(var(--shift,0),0,0) scaleX(1.44)}58%{transform:translate3d(calc(var(--shift,0)*.76),0,0) scaleX(1.28)}76%{transform:translate3d(calc(var(--shift,0)*-.08),0,0) scaleX(.99)}88%,100%{transform:translate3d(0,0,0) scaleX(1)}}
@keyframes newDropSoulTrail{0%,12%{opacity:0;transform:translate3d(0,0,0) scaleX(1)}30%{opacity:.22;transform:translate3d(calc(var(--pull,0)*.38),0,0) scaleX(1.42)}44%{opacity:.48;transform:translate3d(var(--pull,0),0,0) scaleX(2.05)}56%{opacity:.30;transform:translate3d(calc(var(--pull,0)*1.14),0,0) scaleX(2.42)}72%{opacity:.10;transform:translate3d(calc(var(--pull,0)*.46),0,0) scaleX(1.48)}84%,100%{opacity:0;transform:translate3d(0,0,0) scaleX(1)}}
'''
s=s[:start]+new+s[end:]
p.write_text(s,encoding='utf-8')

h=Path('index.html')
html=h.read_text(encoding='utf-8')
html=re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-18', html, count=1)
h.write_text(html,encoding='utf-8')
