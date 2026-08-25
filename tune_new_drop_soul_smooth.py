from pathlib import Path
import re

css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

start = css.index('.wave-title{')
end = css.index('.new-drop-carousel{', start)

new = r'''.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 10px rgba(255,43,43,.72),0 0 24px rgba(255,43,43,.46),0 0 48px rgba(255,43,43,.18);filter:drop-shadow(0 0 8px rgba(255,43,43,.26));overflow:visible;}
.wave-title span{position:relative;display:inline-block;transform-origin:center center;will-change:transform,filter,opacity;animation:newDropSoulStretch 4.8s cubic-bezier(.16,.72,.18,1) infinite;}
.wave-title span::after{content:attr(data-letter);position:absolute;inset:0;color:var(--red);-webkit-text-fill-color:var(--red);pointer-events:none;opacity:0;transform-origin:var(--origin,center) center;filter:blur(0);text-shadow:0 0 18px rgba(255,43,43,.82),0 0 42px rgba(255,43,43,.48);animation:newDropSoulTrail 4.8s cubic-bezier(.14,.72,.16,1) infinite;}
.wave-title span:nth-child(1){--shift:-.20em;--pull:-.42em;--origin:right;animation-delay:0s}.wave-title span:nth-child(2){--shift:-.16em;--pull:-.35em;--origin:right;animation-delay:.10s}.wave-title span:nth-child(3){--shift:-.10em;--pull:-.27em;--origin:right;animation-delay:.20s}.wave-title span:nth-child(4){animation:none;transform:none}.wave-title span:nth-child(4)::after{display:none}.wave-title span:nth-child(5){--shift:.10em;--pull:.27em;--origin:left;animation-delay:.30s}.wave-title span:nth-child(6){--shift:.16em;--pull:.35em;--origin:left;animation-delay:.40s}.wave-title span:nth-child(7){--shift:.20em;--pull:.41em;--origin:left;animation-delay:.50s}.wave-title span:nth-child(8){--shift:.24em;--pull:.48em;--origin:left;animation-delay:.60s}
.wave-title span:nth-child(1)::after{animation-delay:0s}.wave-title span:nth-child(2)::after{animation-delay:.10s}.wave-title span:nth-child(3)::after{animation-delay:.20s}.wave-title span:nth-child(5)::after{animation-delay:.30s}.wave-title span:nth-child(6)::after{animation-delay:.40s}.wave-title span:nth-child(7)::after{animation-delay:.50s}.wave-title span:nth-child(8)::after{animation-delay:.60s}
.wave-title::before,.wave-title::after,.wave-title span::before{content:none!important;display:none!important;}
@keyframes newDropSoulStretch{0%,4%,100%{transform:translateX(0) scaleX(1);filter:blur(0);opacity:1}16%{transform:translateX(calc(var(--shift,0)*.20)) scaleX(1.07);filter:blur(0);opacity:1}30%{transform:translateX(calc(var(--shift,0)*.62)) scaleX(1.22);filter:blur(.08px);opacity:1}44%{transform:translateX(var(--shift,0)) scaleX(1.44);filter:blur(.22px);opacity:.985}57%{transform:translateX(calc(var(--shift,0)*.90)) scaleX(1.34);filter:blur(.10px);opacity:.995}70%{transform:translateX(calc(var(--shift,0)*.42)) scaleX(1.14);filter:blur(0);opacity:1}82%{transform:translateX(calc(var(--shift,0)*-.10)) scaleX(.985);filter:blur(0);opacity:1}91%{transform:translateX(calc(var(--shift,0)*.04)) scaleX(1.015);filter:blur(0);opacity:1}96%,100%{transform:translateX(0) scaleX(1);filter:blur(0);opacity:1}}
@keyframes newDropSoulTrail{0%,7%,97%,100%{opacity:0;transform:translateX(0) scaleX(1);filter:blur(0)}16%{opacity:.10;transform:translateX(calc(var(--pull,0)*.16)) scaleX(1.14);filter:blur(.8px)}29%{opacity:.26;transform:translateX(calc(var(--pull,0)*.48)) scaleX(1.48);filter:blur(1.8px)}43%{opacity:.52;transform:translateX(var(--pull,0)) scaleX(2.05);filter:blur(4.2px)}55%{opacity:.40;transform:translateX(calc(var(--pull,0)*1.14)) scaleX(2.38);filter:blur(6.8px)}68%{opacity:.22;transform:translateX(calc(var(--pull,0)*.86)) scaleX(1.92);filter:blur(5.4px)}80%{opacity:.10;transform:translateX(calc(var(--pull,0)*.36)) scaleX(1.42);filter:blur(3px)}91%{opacity:.025;transform:translateX(calc(var(--pull,0)*.08)) scaleX(1.08);filter:blur(1px)}96%,100%{opacity:0;transform:translateX(0) scaleX(1);filter:blur(0)}}
'''

css = css[:start] + new + css[end:]
css_path.write_text(css, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
html = re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-17', html, count=1)
index_path.write_text(html, encoding='utf-8')
