from pathlib import Path
import re

css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

# Replace only the current New Drop breathing rules; keep the rest of the global stylesheet untouched.
css = re.sub(
    r'\.wave-title\{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var\(--red\);-webkit-text-fill-color:var\(--red\);text-shadow:[^}]+\}\s*\.wave-title span\{[^}]+\}\s*\.wave-title span:nth-child\(1\)\{[^\n]+\}\s*\.wave-title::before,\.wave-title::after,\.wave-title span::before,\.wave-title span::after\{[^}]+\}\s*@keyframes newDropBreathe\{[^}]+\}[^@]*',
    '',
    css,
    count=1,
    flags=re.S,
)

# Safer targeted cleanup in case the minified block differs slightly.
css = re.sub(r'\.wave-title span:nth-child\([1-8]\)\{animation-delay:[^}]*\}', '', css)
css = re.sub(r'\.wave-title span:nth-child\(4\)\{animation:none\}', '', css)
css = re.sub(r'@keyframes newDropBreathe\{.*?\}\}', '', css, flags=re.S)

new_rules = r'''
/* NEW DROP — clean horizontal breathing animation */
.wave-title{
  position:relative;
  display:flex;
  align-items:flex-end;
  width:fit-content;
  color:var(--red);
  -webkit-text-fill-color:var(--red);
  text-shadow:0 0 10px rgba(255,43,43,.72),0 0 24px rgba(255,43,43,.46),0 0 48px rgba(255,43,43,.18);
  filter:drop-shadow(0 0 8px rgba(255,43,43,.26));
}
.wave-title span{
  display:inline-block;
  transform-origin:center center;
  will-change:transform;
  animation:newDropHorizontalBreathe 6.4s cubic-bezier(.37,.04,.18,.98) infinite;
}
.wave-title span:nth-child(1){--shift:-.060em;animation-delay:0s}
.wave-title span:nth-child(2){--shift:-.045em;animation-delay:.18s}
.wave-title span:nth-child(3){--shift:-.025em;animation-delay:.36s}
.wave-title span:nth-child(4){animation:none;transform:none}
.wave-title span:nth-child(5){--shift:.025em;animation-delay:.54s}
.wave-title span:nth-child(6){--shift:.040em;animation-delay:.72s}
.wave-title span:nth-child(7){--shift:.052em;animation-delay:.90s}
.wave-title span:nth-child(8){--shift:.065em;animation-delay:1.08s}
.wave-title::before,.wave-title::after,.wave-title span::before,.wave-title span::after{content:none!important;display:none!important;}
@keyframes newDropHorizontalBreathe{
  0%,18%,100%{transform:translateX(0) scaleX(1)}
  38%{transform:translateX(var(--shift,0)) scaleX(1.22)}
  58%,82%{transform:translateX(0) scaleX(1)}
}
'''

anchor = css.find('.new-drop-carousel{')
if anchor == -1:
    raise SystemExit('Could not locate New Drop carousel anchor')
css = css[:anchor] + new_rules + css[anchor:]
css_path.write_text(css, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
html = re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-14', html)
index_path.write_text(html, encoding='utf-8')
