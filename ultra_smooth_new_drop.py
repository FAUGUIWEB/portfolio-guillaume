from pathlib import Path
import re
p=Path('styles.css'); s=p.read_text(encoding='utf-8')
start=s.index('.wave-title{'); end=s.index('.new-drop-carousel{',start)
new=r'''.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 10px rgba(255,43,43,.68),0 0 26px rgba(255,43,43,.38);overflow:visible;contain:layout style;}
.wave-title span{position:relative;display:inline-block;transform-origin:center;will-change:transform;transform:translate3d(0,0,0);backface-visibility:hidden;animation:newDropSoul 4.15s cubic-bezier(.25,.72,.2,1) infinite;}
.wave-title span::after{content:attr(data-letter);position:absolute;inset:0;pointer-events:none;color:var(--red);-webkit-text-fill-color:var(--red);opacity:0;transform-origin:var(--origin,center);transform:translate3d(0,0,0);will-change:transform,opacity;backface-visibility:hidden;text-shadow:0 0 12px rgba(255,43,43,.42);animation:newDropGhost 4.15s cubic-bezier(.25,.72,.2,1) infinite;}
.wave-title span:nth-child(1){--x:-.22em;--gx:-.48em;--origin:right;animation-delay:0s}.wave-title span:nth-child(2){--x:-.17em;--gx:-.39em;--origin:right;animation-delay:.09s}.wave-title span:nth-child(3){--x:-.11em;--gx:-.30em;--origin:right;animation-delay:.18s}.wave-title span:nth-child(4){animation:none}.wave-title span:nth-child(4)::after{display:none}.wave-title span:nth-child(5){--x:.11em;--gx:.30em;--origin:left;animation-delay:.27s}.wave-title span:nth-child(6){--x:.17em;--gx:.39em;--origin:left;animation-delay:.36s}.wave-title span:nth-child(7){--x:.21em;--gx:.46em;--origin:left;animation-delay:.45s}.wave-title span:nth-child(8){--x:.25em;--gx:.54em;--origin:left;animation-delay:.54s}
.wave-title span:nth-child(1)::after{animation-delay:0s}.wave-title span:nth-child(2)::after{animation-delay:.09s}.wave-title span:nth-child(3)::after{animation-delay:.18s}.wave-title span:nth-child(5)::after{animation-delay:.27s}.wave-title span:nth-child(6)::after{animation-delay:.36s}.wave-title span:nth-child(7)::after{animation-delay:.45s}.wave-title span:nth-child(8)::after{animation-delay:.54s}
.wave-title::before,.wave-title::after,.wave-title span::before{content:none!important;display:none!important}
@keyframes newDropSoul{0%,8%{transform:translate3d(0,0,0) scaleX(1)}42%{transform:translate3d(var(--x,0),0,0) scaleX(1.43)}70%{transform:translate3d(calc(var(--x,0)*.12),0,0) scaleX(1.03)}82%,100%{transform:translate3d(0,0,0) scaleX(1)}}
@keyframes newDropGhost{0%,14%{opacity:0;transform:translate3d(0,0,0) scaleX(1)}38%{opacity:.38;transform:translate3d(var(--gx,0),0,0) scaleX(2.32)}58%{opacity:.20;transform:translate3d(calc(var(--gx,0)*1.08),0,0) scaleX(2.62)}78%,100%{opacity:0;transform:translate3d(0,0,0) scaleX(1)}}
'''
s=s[:start]+new+s[end:]; p.write_text(s,encoding='utf-8')
h=Path('index.html'); x=h.read_text(encoding='utf-8'); x=re.sub(r'styles\.css\?v=[^"\']+','styles.css?v=20260825-19',x,count=1); h.write_text(x,encoding='utf-8')
