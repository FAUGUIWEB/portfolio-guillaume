from pathlib import Path
import re

css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

# Remove every appended New Drop experiment block.
first_marker = css.find('/* NEW DROP')
if first_marker != -1:
    css = css[:first_marker].rstrip() + '\n'

# Replace the original New Drop title effect region in the main stylesheet.
start = css.find('.new-drop-title,.section-title{')
end = css.find('.new-drop-carousel{', start)
if start == -1 or end == -1:
    raise SystemExit('Could not locate New Drop CSS region')

clean_region = '''.new-drop-title,.section-title{font-size:clamp(80px,13vw,190px);line-height:.8;letter-spacing:-.01em;margin-bottom:55px;}
.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;perspective:1000px;transform-style:preserve-3d;color:var(--red);-webkit-text-fill-color:currentColor;}
.wave-title span{display:inline-block;transform-origin:center center;transform-style:preserve-3d;backface-visibility:visible;-webkit-backface-visibility:visible;will-change:transform,color,text-shadow;animation:newDropFlipFresh 6.4s cubic-bezier(.55,.02,.18,.98) infinite;}
.wave-title span:nth-child(1){animation-delay:0s}.wave-title span:nth-child(2){animation-delay:.09s}.wave-title span:nth-child(3){animation-delay:.18s}.wave-title span:nth-child(4){animation-delay:.27s}.wave-title span:nth-child(5){animation-delay:.36s}.wave-title span:nth-child(6){animation-delay:.45s}.wave-title span:nth-child(7){animation-delay:.54s}.wave-title span:nth-child(8){animation-delay:.63s}
@keyframes newDropFlipFresh{0%,26%{transform:rotateY(0deg);color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 14px rgba(255,43,43,.60),0 0 34px rgba(255,43,43,.28)}36%{transform:rotateY(-88deg);color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 4px rgba(255,43,43,.14)}36.01%{transform:rotateY(88deg);color:#fff;-webkit-text-fill-color:#fff;text-shadow:none}46%,62%{transform:rotateY(0deg);color:#fff;-webkit-text-fill-color:#fff;text-shadow:none}72%{transform:rotateY(-88deg);color:#fff;-webkit-text-fill-color:#fff;text-shadow:none}72.01%{transform:rotateY(88deg);color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 4px rgba(255,43,43,.14)}82%,100%{transform:rotateY(0deg);color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 14px rgba(255,43,43,.60),0 0 34px rgba(255,43,43,.28)}}
.wave-title::before,.wave-title::after,.wave-title span::before,.wave-title span::after{content:none!important;display:none!important;}
'''

css = css[:start] + clean_region + css[end:]
css_path.write_text(css, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
html = re.sub(r'styles\.css\?v=[^\"\']+', 'styles.css?v=20260825-11', html)
index_path.write_text(html, encoding='utf-8')

# Remove obsolete temporary New Drop workflows if they still exist.
for old in [
    Path('.github/workflows/clean-new-drop-css.yml'),
    Path('.github/workflows/fix-new-drop-readable.yml'),
    Path('.github/workflows/fix-new-drop-single-text.yml'),
    Path('.github/workflows/rebuild-new-drop.yml'),
    Path('rebuild_new_drop.py'),
]:
    if old.exists():
        old.unlink()
