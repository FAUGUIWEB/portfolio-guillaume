from pathlib import Path
import re

css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

replacements = {
    'animation:newDropHorizontalBreathe 6.4s cubic-bezier(.37,.04,.18,.98) infinite;':
    'animation:newDropHorizontalBreathe 4.6s cubic-bezier(.37,.04,.18,.98) infinite;',
    '.wave-title span:nth-child(1){--shift:-.060em;animation-delay:0s}':
    '.wave-title span:nth-child(1){--shift:-.115em;animation-delay:0s}',
    '.wave-title span:nth-child(2){--shift:-.045em;animation-delay:.18s}':
    '.wave-title span:nth-child(2){--shift:-.090em;animation-delay:.13s}',
    '.wave-title span:nth-child(3){--shift:-.025em;animation-delay:.36s}':
    '.wave-title span:nth-child(3){--shift:-.055em;animation-delay:.26s}',
    '.wave-title span:nth-child(5){--shift:.025em;animation-delay:.54s}':
    '.wave-title span:nth-child(5){--shift:.055em;animation-delay:.39s}',
    '.wave-title span:nth-child(6){--shift:.040em;animation-delay:.72s}':
    '.wave-title span:nth-child(6){--shift:.085em;animation-delay:.52s}',
    '.wave-title span:nth-child(7){--shift:.052em;animation-delay:.90s}':
    '.wave-title span:nth-child(7){--shift:.110em;animation-delay:.65s}',
    '.wave-title span:nth-child(8){--shift:.065em;animation-delay:1.08s}':
    '.wave-title span:nth-child(8){--shift:.135em;animation-delay:.78s}',
}

for old, new in replacements.items():
    if old not in css:
        raise SystemExit(f'Missing expected rule: {old}')
    css = css.replace(old, new, 1)

old_keyframes = '''@keyframes newDropHorizontalBreathe{\n  0%,18%,100%{transform:translateX(0) scaleX(1)}\n  38%{transform:translateX(var(--shift,0)) scaleX(1.22)}\n  58%,82%{transform:translateX(0) scaleX(1)}\n}'''
new_keyframes = '''@keyframes newDropHorizontalBreathe{\n  0%,10%,100%{transform:translateX(0) scaleX(1)}\n  30%{transform:translateX(var(--shift,0)) scaleX(1.22)}\n  52%{transform:translateX(0) scaleX(1)}\n}'''
if old_keyframes not in css:
    raise SystemExit('Missing expected New Drop keyframes')
css = css.replace(old_keyframes, new_keyframes, 1)
css_path.write_text(css, encoding='utf-8')

index_path = Path('index.html')
html = index_path.read_text(encoding='utf-8')
html = re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-15', html)
index_path.write_text(html, encoding='utf-8')
