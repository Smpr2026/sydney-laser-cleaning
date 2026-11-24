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
SITE_URL = "https://sydneylasercleaning.com.au/"
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
<script async src="https://www.googletagmanager.com/gtag/js?id=G-X6KDXRPL9P"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('js',new Date());gtag('config','G-X6KDXRPL9P');
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href');
if(h.indexOf('tel:')===0)gtag('event','call_click',{{link_url:h}});
else if(h.indexOf('sms:')===0)gtag('event','sms_click',{{link_url:h}});
else if(h.indexOf('mailto:')===0)gtag('event','email_click',{{link_url:h}});
else if(/contact[.]html/.test(h)&&a.classList.contains('btn'))gtag('event','quote_button_click');}});
document.addEventListener('submit',function(e){{gtag('event','generate_lead',{{form_id:e.target.id||'form'}});}});
</script>
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


# ---- Video watch pages (one per job video, so Google can index them) ----
import json, html as _h
from datetime import date
VIDEOS = [
  # slug, title, description, duration_seconds
  ("rim-timelapse", "Car rim laser stripped back to bare steel (time-lapse)", "Time-lapse of a car rim going from old cream paint to bare steel with laser cleaning in Sydney. No sandblasting, no chemicals, no damage to the metal underneath.", 16),
  ("pulse-pitting", "200W pulse laser lifting pitted rust out of a car panel", "A 200W pulse laser cleaning pitted rust out of a sanded car panel. The laser reaches into the pits that sanding leaves behind, so the panel is ready to prime.", 16),
  ("angle-rust", "Rusty steel angle laser cleaned down one face", "Laser rust removal on a steel angle in Sydney. One face is cleaned back to bright metal in a single pass so you can see the before and after side by side.", 16),
  ("stone-step", "Stone step cleaned with a 200W pulse laser", "Grime and staining lifted off a stone step with a 200W pulse laser. Laser cleaning works on stone and concrete without water blasting or harsh chemicals.", 19),
  ("cw-ceiling", "1500W laser clearing fire soot off a concrete ceiling", "Fire damage restoration in Sydney: a 1500W continuous laser clearing heavy fire soot off a concrete ceiling, with no water, chemicals or mess.", 18),
  ("soot-ceiling", "Laser removing soot damage from a balcony", "Soot damage on a balcony that other cleaning methods could not shift. The laser lifted it off and left the surface intact.", 11),
  ("job-9950", "Laser line clearing rust off a steel beam", "Industrial laser rust removal on a steel beam, filmed on site in Sydney. The laser line strips rust back to bare steel ready for coating.", 14),
  ("job-9962", "Long steel rail half cleaned with a laser", "A long steel rail half laser cleaned, showing the rusty and cleaned sections side by side. On-site laser rust removal across Sydney.", 13),
  ("job1", "Rusty steel rail cleaned in one pass", "Laser cleaning a rusty steel rail back to bare metal in one pass. No sandblasting media to clean up and no damage to the steel.", 17),
  ("job-0153", "Yellow paint laser stripped off a steel rail", "Laser paint removal: yellow paint stripped off a steel rail in Sydney without grinding, chemicals or blasting.", 14),
  ("job-0149", "Laser cleaning under a steel rail on site", "Laser cleaning the underside of a steel rail on site in Sydney, getting into tight spots a grinder or blaster can't reach.", 14),
]
UPLOAD = "2026-11-23T00:00:00+11:00"
BASE = "https://sydneylasercleaning.com.au/"

def video_ld(slug, title, desc, dur):
    return {"@context":"https://schema.org","@type":"VideoObject","name":title,"description":desc,
            "thumbnailUrl":[BASE+f"video/{slug}-poster.jpg"],"uploadDate":UPLOAD,
            "duration":f"PT{dur}S","contentUrl":BASE+f"video/{slug}.mp4","embedUrl":BASE+f"video-{slug}.html",
            "publisher":{"@type":"Organization","name":"Sydney Laser Cleaning","logo":{"@type":"ImageObject","url":BASE+"img/share.jpg"}}}

for i,(slug,title,desc,dur) in enumerate(VIDEOS):
    others = "".join(f'<li><a href="video-{s}.html">{_h.escape(t)}</a></li>' for s,t,_,_ in VIDEOS if s!=slug)
    body = f"""<section class="sec" style="padding-top:140px">
  <div class="wrap" style="max-width:960px">
    <span class="kicker">Job video</span>
    <h1 class="disp" style="font-size:clamp(30px,4.5vw,52px)">{_h.escape(title)}</h1>
    <video controls playsinline preload="metadata" poster="video/{slug}-poster.jpg" style="width:100%;border-radius:18px;margin-top:24px;background:#000">
      <source src="video/{slug}.mp4" type="video/mp4">
    </video>
    <p style="color:#c9d6ea;font-size:18px;margin-top:20px;max-width:64ch">{_h.escape(desc)}</p>
    <p style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-p" href="contact.html">Get a free quote</a><a class="btn btn-o" href="gallery.html">See the full gallery</a></p>
    <h2 class="disp" style="font-size:24px;margin-top:56px">More laser cleaning videos</h2>
    <ul style="margin-top:14px;line-height:2;color:#c9d6ea">{others}</ul>
  </div>
</section>
<script type="application/ld+json">{json.dumps(video_ld(slug,title,desc,dur))}</script>"""
    (ROOT / f"video-{slug}.html").write_text(head(f"{title} | Sydney Laser Cleaning", desc) + nav("gallery") + "<main>\n" + body + "\n</main>\n" + FOOT.replace("__VER__", VER))
    print("built", f"video-{slug}.html")

# video list on the gallery page + sitemap with video entries
glist = "".join(f'<li><a href="video-{s}.html">{_h.escape(t)}</a></li>' for s,t,_,_ in VIDEOS)
g = (ROOT/"gallery.html").read_text()
g = g.replace("\n</main>\n", f'\n<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="disp" style="font-size:28px">All job videos</h2><ul style="margin-top:14px;line-height:2;color:#c9d6ea">{glist}</ul></div></section>\n</main>\n',1)
(ROOT/"gallery.html").write_text(g)

today = date.today().isoformat()
urls = "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{today}</lastmod></url>\n" for p in ["","services.html","hire.html","gallery.html","contact.html"])
for slug,title,desc,dur in VIDEOS:
    urls += f"""  <url><loc>{BASE}video-{slug}.html</loc><lastmod>{today}</lastmod>
    <video:video><video:thumbnail_loc>{BASE}video/{slug}-poster.jpg</video:thumbnail_loc><video:title>{_h.escape(title)}</video:title><video:description>{_h.escape(desc)}</video:description><video:content_loc>{BASE}video/{slug}.mp4</video:content_loc><video:duration>{dur}</video:duration></video:video></url>
"""
(ROOT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n{urls}</urlset>\n')
print("built sitemap.xml")
