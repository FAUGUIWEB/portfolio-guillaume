from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# The finishing pass accidentally wrote JavaScript single quotes as literal \'
# inside double-quoted HTML event attributes. Browsers parse those handlers as
# invalid JavaScript, so openVideo() never runs. In HTML attributes the quotes
# do not need backslashes, so remove them globally from inline JS strings.
s = s.replace("\\'", "'")

p.write_text(s, encoding='utf-8')
