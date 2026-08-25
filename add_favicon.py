from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
link = '<link rel="icon" href="logo.svg" type="image/svg+xml">'
if link not in s:
    s = s.replace('</title>', '</title>' + link, 1)
p.write_text(s, encoding='utf-8')
