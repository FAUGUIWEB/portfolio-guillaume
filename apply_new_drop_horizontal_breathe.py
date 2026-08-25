from pathlib import Path
import re

css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

old = r'''.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 10px rgba(255,43,43,.72),0 0 24px rgba(255,43,43,.46),0 0 48px rgba(255,43,43,.18);filter:drop-shadow(0 0 8px rgba(255,43,43,.26));}
.wave-title span{display:inline-block;transform-origin:center 68%;will-change:transform;animation:newDropBreathe 5.8s cubic-bezier(.37,.04,.18,.98) infinite;}
.wave-title span:nth-child(1){animation-delay:0s}.wave-title span:nth-child(2){animation-delay:.16s}.wave-title span:nth-child(3){animation-delay:.32s}.wave-title span:nth-child(4){animation:none}.wave-title span:nth-child(5){animation-delay:.48s}.wave-title span:nth-child(6){animation-delay:.64s}.wave-title span:nth-child(7){animation-delay:.80s}.wave-title span:nth-child(8){animation-delay:.96s}
.wave-title::before,.wave-title::after,.wave-title span::before,.wave-title span::after{content:none!important;display:none!important;}
@keyframes newDropBreathe{0%,16%,100%{transform:scaleX(1) scaleY(1) translateY(0)}34%{transform:scaleX(1.20) scaleY(1.055) translateY(-.012em)}52%,82%{transform:scaleX(1) scaleY(1) translateY(0)}}
'''

new = r'''.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 10px rgba(255,43,43,.72),0 0 24px rgba(255,43,43,.46),0 0 48px rgba(255,43,43,.18);filter:drop-shadow(0 0 8px rgba(255,43,43,.26));}
.wave-title span{display:inline-block;transform-origin:center center;will-change:transform;animation:newDropHorizontalBreathe 6.4s cubic-bezier(.37,.04,.18,.98) infinite;}
.wave-title span:nth-child(1){--shift:-.060em;animation-delay:0s}.wave-title span:nth-child(2){--shift:-.045em;animation-delay:.18s}.wave-title span:nth-child(3){--shift:-.025em;animation-delay:.36s}.wave-title span:nth-child(4){animation:none;transform:none}.wave-title span:nth-child(5){--shift:.025em;animation-delay:.54s}.wave-title span:nth-child(6){--shift:.040em;animation-delay:.72s}.wave-title span:nth-child(7){--shift:.052em;animation-delay:.90s}.wave-title span:nth-child(8){--shift:.065em;animation-delay:1.08s}
.wave-title::before,.wave-title::after,.wave-title span::before,.wave-title span::after{content:none!important;display:none!important;}
@keyframes newDropHorizontalBreathe{0%,18%,100%{transform:translateX(0) scaleX(1)}38%{transform:translateX(var(--shift,0)) scaleX(1.22)}58%,82%{transform:translateX(0) scaleX(1)}}
'''

if old in css:
    css = css.replace(old, new, 1)
else:
    # Fallback: append a single authoritative override without touching unrelated styles.
    css += '\n' + new

css_path.write_text(css, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
html = re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-14', html)
index_path.write_text(html, encoding='utf-8')
