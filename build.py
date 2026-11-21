#!/usr/bin/env python3
"""Builds the static pages: shared head, nav and footer + each page body from pages/*.html.
Run:  python3 build.py   (writes index.html, services.html, hire.html, contact.html)"""
from pathlib import Path
import time
VER = str(int(time.time()))

ROOT = Path(__file__).parent
PAGES = {
    "index":    ("Sydney Laser Cleaning | Laser Cleaning Hire & Services in Sydney",
                 "Laser cleaning machine hire and on-site laser cleaning across Sydney. Rust, paint, graffiti and fire damage removed without chemicals or sandblasting. Call 0432 722 498."),
    "services": ("Laser Cleaning Services | Rust, Paint, Graffiti & Fire Damage | Sydney Laser Cleaning",
                 "Rust removal, paint stripping, graffiti removal and fire damage restoration by laser in Sydney. No chemicals, no blasting media, no damage to the surface."),
    "hire":     ("Laser Cleaning Machine Hire Sydney | Sydney Laser Cleaning",
                 "Hire a laser cleaning machine by the day, week or month in Sydney. Hire 6 days get 1 free, 30 days 30% off. Call 0432 722 498."),
    "gallery":  ("Gallery | Laser Cleaning Jobs in Sydney | Sydney Laser Cleaning",
                 "Photos and videos of real laser cleaning jobs in Sydney: rust off steel rails and beams, pitted rust out of car panels, brake drums, engine parts and concrete."),
    "contact":  ("Contact & Free Quote | Sydney Laser Cleaning",
                 "Get a free laser cleaning quote. Text a photo to 0432 722 498 or email sydneylasercleaning@gmail.com."),
}
SITE_URL = "https://smpr2026.github.io/sydney-laser-cleaning/"  # change when the own domain goes live
NAV = [("index", "Home"), ("services", "Services"), ("hire", "Machine hire"), ("gallery", "Gallery"), ("contact", "Contact")]

def head(title, desc):
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060b1a">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sydney Laser Cleaning">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}img/share.jpg?v=3">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sydney Laser Cleaning: laser line clearing rust off a steel beam">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE_URL}img/share.jpg?v=3">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Montserrat:wght@700;800&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">
<link rel="stylesheet" href="style.css?v={VER}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Sydney Laser Cleaning","telephone":"+61432722498","email":"sydneylasercleaning@gmail.com","areaServed":"Sydney NSW","description":"Laser cleaning machine hire and on-site laser cleaning services."}}</script>
</head>
<body>
<div id="top-sentinel" style="position:absolute;top:0;height:80px;width:1px"></div>
"""

def nav(active):
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{k}.html"{cur if k == active else ""}>{n}</a></li>' for k, n in NAV)
    mlinks = "".join(f'<a href="{k}.html">{n}</a>' for k, n in NAV)
    return f"""<header class="nav">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Sydney Laser Cleaning home"><img src="img/logo-mark.svg?v=2" alt=""><span class="wm"><b>SYDNEY<sup>&reg;</sup></b><small>LASER CLEANING</small></span></a>
    <ul class="links">{links}</ul>
    <a class="btn btn-p" href="contact.html">Get a free quote</a>
    <button class="burger" type="button" aria-label="Menu" aria-expanded="false"><i class="ph ph-list"></i></button>
  </div>
  <nav class="mmenu" aria-label="Mobile"><div>{mlinks}<a class="btn btn-p" href="contact.html">Get a free quote</a></div></nav>
</header>
"""

FOOT = """<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="brand" href="index.html"><img src="img/logo-mark.svg?v=2" alt=""><span class="wm"><b>SYDNEY<sup>&reg;</sup></b><small>LASER CLEANING</small></span></a>
        <p class="about">Laser cleaning machine hire and on-site laser cleaning across Sydney. Rust, paint, graffiti and soot off, surface left intact.</p>
      </div>
      <div><h4>Pages</h4><ul><li><a href="index.html">Home</a></li><li><a href="services.html">Services</a></li><li><a href="hire.html">Machine hire</a></li><li><a href="gallery.html">Gallery</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Get in touch</h4><ul><li><a href="tel:0432722498">0432 722 498</a></li><li><a href="mailto:sydneylasercleaning@gmail.com">sydneylasercleaning@gmail.com</a></li><li>Sydney, NSW</li></ul></div>
    </div>
    <div class="fbot"><span>&copy; <span data-year></span> Sydney Laser Cleaning</span><span>Laser cleaning hire &amp; services</span></div>
  </div>
</footer>
<a class="fab" href="sms:0432722498" aria-label="Text us a photo of the job"><i class="ph-fill ph-chat-circle-text"></i>Text us a photo</a>
<script src="site.js?v=__VER__"></script>
</body>
</html>
"""

for key, (title, desc) in PAGES.items():
    body = (ROOT / "pages" / f"{key}.html").read_text().replace("__BVER__", VER)
    (ROOT / f"{key}.html").write_text(head(title, desc) + nav(key) + "<main>\n" + body + "\n</main>\n" + FOOT.replace("__VER__", VER))
    print("built", key + ".html")
