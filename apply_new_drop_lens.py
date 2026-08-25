from pathlib import Path
import re

css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

start = css.find('.new-drop-title,.section-title{')
end = css.find('.new-drop-carousel{', start)
if start < 0 or end < 0:
    raise SystemExit('New Drop CSS region not found')

region = r'''.new-drop-title,.section-title{font-size:clamp(80px,13vw,190px);line-height:.8;letter-spacing:-.01em;margin-bottom:55px;}
.new-drop-title-wrap{position:relative;width:fit-content;max-width:100%;margin-bottom:55px;isolation:isolate;}
.new-drop-title-wrap .new-drop-title{margin-bottom:0;}
.wave-title{position:relative;display:flex;align-items:flex-end;width:fit-content;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 12px rgba(255,43,43,.58),0 0 30px rgba(255,43,43,.25);filter:drop-shadow(0 0 8px rgba(255,43,43,.22));}
.wave-title span{display:inline-block;transform:none!important;animation:none!important;}
.wave-title::before,.wave-title::after,.wave-title span::before,.wave-title span::after{content:none!important;display:none!important;}
.new-drop-magnified{position:absolute;inset:0;z-index:2;margin:0!important;pointer-events:none;color:var(--red);-webkit-text-fill-color:var(--red);text-shadow:0 0 16px rgba(255,43,43,.68),0 0 40px rgba(255,43,43,.32);transform:scale(1.18);transform-origin:center center;clip-path:ellipse(13% 78% at -10% 50%);animation:newDropLensMask 8.4s cubic-bezier(.45,.02,.18,.98) infinite;}
.new-drop-lens{position:absolute;z-index:4;top:50%;left:-12%;width:24%;min-width:150px;max-width:265px;aspect-ratio:1.35/1;transform:translateY(-50%) rotate(-8deg);pointer-events:none;overflow:hidden;border:1px solid rgba(255,255,255,.24);border-radius:47% 53% 44% 56% / 55% 45% 57% 43%;background:radial-gradient(circle at 31% 23%,rgba(255,255,255,.27),transparent 18%),radial-gradient(circle at 72% 69%,rgba(255,43,43,.22),transparent 36%),linear-gradient(125deg,rgba(255,255,255,.09),rgba(255,43,43,.08) 47%,rgba(255,255,255,.02));backdrop-filter:blur(2px) saturate(150%);-webkit-backdrop-filter:blur(2px) saturate(150%);box-shadow:inset 14px 10px 30px rgba(255,255,255,.09),inset -18px -12px 36px rgba(255,43,43,.12),0 18px 34px rgba(0,0,0,.30),0 0 30px rgba(255,43,43,.11);animation:newDropLensTravel 8.4s cubic-bezier(.45,.02,.18,.98) infinite,newDropLensMorph 5.4s ease-in-out infinite alternate;}
.new-drop-lens::before{content:"";position:absolute;inset:7% 9% 12% 7%;border-radius:55% 45% 52% 48% / 43% 58% 42% 57%;background:linear-gradient(110deg,rgba(255,255,255,.30),transparent 22%,rgba(255,43,43,.14) 47%,transparent 70%,rgba(120,90,255,.05) 84%,rgba(255,255,255,.12));mix-blend-mode:screen;filter:blur(.4px);opacity:.82;animation:newDropOilFlow 4.8s ease-in-out infinite alternate;}
.new-drop-lens::after{content:"";position:absolute;right:18%;top:15%;width:47%;height:24%;border-radius:999px;background:linear-gradient(90deg,rgba(255,255,255,.42),rgba(255,43,43,.18),rgba(120,90,255,.07),transparent);filter:blur(2px);transform:rotate(-18deg);opacity:.75;box-shadow:0 0 14px rgba(255,255,255,.08);animation:newDropHighlight 3.6s ease-in-out infinite alternate;}
.new-drop-lens-core{position:absolute;inset:19% 16% 15% 20%;border-radius:50% 44% 56% 48% / 46% 56% 44% 54%;background:radial-gradient(circle at 55% 48%,rgba(255,43,43,.15),transparent 52%),radial-gradient(circle at 36% 38%,rgba(255,255,255,.08),transparent 58%);box-shadow:inset 0 0 28px rgba(255,255,255,.06),inset 0 0 34px rgba(255,43,43,.09);animation:newDropCoreFloat 4.4s ease-in-out infinite alternate;}
@keyframes newDropLensTravel{0%,8%{left:-12%;transform:translateY(-50%) rotate(-8deg) scale(.94)}42%{left:35%;transform:translateY(-53%) rotate(4deg) scale(1.04)}74%{left:79%;transform:translateY(-48%) rotate(-2deg) scale(.99)}88%,100%{left:104%;transform:translateY(-50%) rotate(7deg) scale(.92)}}
@keyframes newDropLensMask{0%,8%{clip-path:ellipse(13% 78% at -10% 50%)}42%{clip-path:ellipse(14% 80% at 43% 48%)}74%{clip-path:ellipse(13% 76% at 86% 52%)}88%,100%{clip-path:ellipse(12% 72% at 112% 50%)}}
@keyframes newDropLensMorph{0%{border-radius:47% 53% 44% 56% / 55% 45% 57% 43%}35%{border-radius:57% 43% 53% 47% / 44% 58% 42% 56%}70%{border-radius:42% 58% 49% 51% / 60% 40% 55% 45%}100%{border-radius:54% 46% 58% 42% / 47% 55% 45% 53%}}
@keyframes newDropOilFlow{0%{transform:translate3d(-4%,-2%,0) rotate(-8deg) scale(.96);opacity:.58}50%{transform:translate3d(5%,4%,0) rotate(5deg) scale(1.05);opacity:.92}100%{transform:translate3d(-2%,6%,0) rotate(-2deg) scale(1);opacity:.72}}
@keyframes newDropHighlight{0%{transform:translate3d(-8%,3%,0) rotate(-18deg);opacity:.5}100%{transform:translate3d(12%,-5%,0) rotate(-12deg);opacity:.92}}
@keyframes newDropCoreFloat{0%{transform:translate3d(-5%,2%,0) scale(.96)}100%{transform:translate3d(6%,-4%,0) scale(1.06)}}
@media (max-width:800px){.new-drop-title-wrap{margin-bottom:45px}.new-drop-title-wrap .new-drop-title{margin-bottom:0}.new-drop-lens{width:28%;min-width:105px;max-width:150px}.new-drop-magnified{transform:scale(1.16)}}
'''

css = css[:start] + region + css[end:]
css_path.write_text(css, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
pattern = r'<h2 class="new-drop-title wave-title" aria-label="New Drop" >.*?</h2>'
replacement = '<div class="new-drop-title-wrap"><h2 class="new-drop-title wave-title" aria-label="New Drop" ><span>N</span><span>E</span><span>W</span><span>&nbsp;</span><span>D</span><span>R</span><span>O</span><span>P</span></h2><h2 class="new-drop-title wave-title new-drop-magnified" aria-hidden="true"><span>N</span><span>E</span><span>W</span><span>&nbsp;</span><span>D</span><span>R</span><span>O</span><span>P</span></h2><div class="new-drop-lens" aria-hidden="true"><span class="new-drop-lens-core"></span></div></div>'
html, n = re.subn(pattern, replacement, html, count=1, flags=re.S)
if n != 1:
    raise SystemExit('New Drop title markup not found')
html = re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-12', html)
index_path.write_text(html, encoding='utf-8')

for old in [
    Path('.github/workflows/rebuild-new-drop-css.yml'),
    Path('.github/workflows/new-drop-liquid-lens.yml'),
    Path('.github/workflows/refine-new-drop-timing.yml'),
    Path('.github/workflows/clean-new-drop-animation.yml'),
]:
    if old.exists():
        old.unlink()
