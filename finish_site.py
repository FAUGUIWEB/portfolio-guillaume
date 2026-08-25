from pathlib import Path
import re
p=Path('index.html'); s=p.read_text(encoding='utf-8')
# SEO + sharing, without guessing production canonical domain.
s=s.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0" />', '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n    <meta name="description" content="Portfolio de Guillaume Faucompré, vidéaste et motion designer. Découvrez ses réalisations, son showreel et ses derniers projets." />\n    <meta name="robots" content="index, follow" />\n    <meta name="theme-color" content="#050505" />\n    <meta property="og:type" content="website" />\n    <meta property="og:locale" content="fr_FR" />\n    <meta property="og:title" content="Guillaume Faucompré — Vidéaste & Motion Designer" />\n    <meta property="og:description" content="Portfolio de Guillaume Faucompré — vidéaste et motion designer." />\n    <meta name="twitter:card" content="summary" />')
# Resource hints and hero image priority.
s=s.replace('<link rel="icon" href="logo.svg" type="image/svg+xml" />', '<link rel="icon" href="logo.svg" type="image/svg+xml" />\n    <link rel="preload" href="Cassette.png" as="image" fetchpriority="high" />')
s=s.replace('class="hero-cassette" src="Cassette.png" alt=""', 'class="hero-cassette" src="Cassette.png" alt="" decoding="async" fetchpriority="high"')
# Better image decoding everywhere; lazy images stay lazy.
s=re.sub(r'<img(?![^>]*\bdecoding=)([^>]*\bloading="lazy"[^>]*)>', r'<img decoding="async"\1>', s)
# Showreel preview should not download full video before needed.
s=s.replace('autoplay muted loop playsinline preload="metadata" aria-hidden="true"', 'autoplay muted loop playsinline preload="metadata" aria-hidden="true"')
# Interactive project articles: keyboard + semantics, preserve onclick.
s=re.sub(r'<article class="project" onclick="openVideo\(\'([^\']+)\'\)"', r'<article class="project" role="button" tabindex="0" aria-label="Lire la vidéo" onclick="openVideo(\'\1\')" onkeydown="if(event.key===\'Enter\'||event.key===\' \'){event.preventDefault();openVideo(\'\1\')}"', s)
# External thumbnails: preconnect to YouTube image CDN.
needle='<link rel="preconnect"\n      href="https://fonts.googleapis.com" />'
if needle in s:
    s=s.replace(needle, needle+'\n    <link rel="preconnect" href="https://i.ytimg.com" crossorigin />')
# CSS cache bump.
s=re.sub(r'styles\.css\?v=[^"\']+', 'styles.css?v=20260825-21', s, count=1)
p.write_text(s,encoding='utf-8')

# Append non-invasive accessibility/perf CSS.
c=Path('styles.css'); css=c.read_text(encoding='utf-8')
addon=r'''
/* Production finishing: accessibility + rendering */
:focus-visible{outline:2px solid var(--red);outline-offset:4px;}
.project[role="button"]{cursor:pointer;}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.wave-title span,.wave-title span::before,.wave-title span::after,.hero-cassette-float,.hero-showreel-card,.hero-showreel::before,.hero-role-line::after{animation:none!important}.hero-title-stage,.hero-cassette-layer,.hero-showreel-tilt{transition:none!important}}
@media (max-width:768px){.projects,.about,.contact-section{content-visibility:auto;contain-intrinsic-size:900px}}
'''
if '/* Production finishing: accessibility + rendering */' not in css:
    css += addon
c.write_text(css,encoding='utf-8')
