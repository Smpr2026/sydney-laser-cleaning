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
                 "Get a free laser cleaning quote. Text a photo to 0432 722 498 or email zap@sydneylasercleaning.com.au."),
}
SITE_URL = "https://sydneylasercleaning.com.au/"
EMAIL = "zap@sydneylasercleaning.com.au"

import json as _json
AREAS = ["Sydney CBD","Inner West","Eastern Suburbs","St George","Sutherland Shire","Canterbury-Bankstown","Western Sydney","Parramatta","Hills District","North Shore","Northern Beaches","South West Sydney"]
SERVICE_PAGES = [
  ("laser-rust-removal-sydney.html","Laser rust removal"),
  ("laser-paint-removal-sydney.html","Laser paint removal"),
  ("graffiti-removal-sydney.html","Laser graffiti removal"),
  ("fire-damage-soot-removal-sydney.html","Fire damage and soot removal"),
  ("concrete-stone-cleaning-sydney.html","Concrete, brick and stone cleaning"),
  ("hire.html","Laser cleaning machine hire"),
]
BIZ_LD = _json.dumps({
  "@context":"https://schema.org","@type":"ProfessionalService","@id":SITE_URL+"#business",
  "name":"Sydney Laser Cleaning","url":SITE_URL,"telephone":"+61432722498","email":EMAIL,
  "logo":SITE_URL+"img/logo-mark.svg","image":SITE_URL+"img/share.jpg",
  "description":"Laser cleaning machine hire and on-site laser cleaning across Sydney: rust removal, paint stripping, graffiti removal and fire damage soot removal, with no chemicals or sandblasting.",
  "address":{"@type":"PostalAddress","addressLocality":"Sydney","addressRegion":"NSW","addressCountry":"AU"},
  "areaServed":[{"@type":"City","name":"Sydney"}]+[{"@type":"Place","name":a+", Sydney NSW"} for a in AREAS],
  "knowsAbout":["Laser cleaning","Laser rust removal","Laser paint removal","Graffiti removal","Fire damage restoration","Soot removal"],
  "hasOfferCatalog":{"@type":"OfferCatalog","name":"Laser cleaning services","itemListElement":[
     {"@type":"Offer","itemOffered":{"@type":"Service","name":n,"url":SITE_URL+u}} for u,n in SERVICE_PAGES]}
})

NAV = [("index", "Home"), ("services", "Services"), ("hire", "Machine hire"), ("gallery", "Gallery"), ("contact", "Contact")]

def head(title, desc, path="", image="img/share.jpg?v=3", extra_ld=""):
    url = SITE_URL + ("" if path in ("", "index.html") else path)
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
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_AU">
<meta name="robots" content="index,follow,max-image-preview:large,max-video-preview:-1">
<meta name="geo.region" content="AU-NSW">
<meta name="geo.placename" content="Sydney">
<meta property="og:image" content="{SITE_URL}{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sydney Laser Cleaning: laser line clearing rust off a steel beam">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE_URL}{image}">
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
<script type="application/ld+json">{BIZ_LD}</script>{extra_ld}
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
      <div><h4>Services</h4><ul><li><a href="laser-rust-removal-sydney.html">Laser rust removal</a></li><li><a href="laser-paint-removal-sydney.html">Laser paint removal</a></li><li><a href="graffiti-removal-sydney.html">Graffiti removal</a></li><li><a href="fire-damage-soot-removal-sydney.html">Fire damage &amp; soot</a></li><li><a href="concrete-stone-cleaning-sydney.html">Concrete &amp; stone</a></li></ul></div>
      <div><h4>Get in touch</h4><ul><li><a href="tel:0432722498">0432 722 498</a></li><li><a href="mailto:zap@sydneylasercleaning.com.au">zap@sydneylasercleaning.com.au</a></li><li>Sydney, NSW</li></ul></div>
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
    (ROOT / f"{key}.html").write_text(head(title, desc, f"{key}.html") + nav(key) + "<main>\n" + body + "\n</main>\n" + FOOT.replace("__VER__", VER))
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
    <video controls playsinline preload="metadata" poster="video/{slug}-poster.jpg" style="width:100%;max-height:75vh;object-fit:contain;border-radius:18px;margin-top:24px;background:#000">
      <source src="video/{slug}.mp4" type="video/mp4">
    </video>
    <p style="color:#c9d6ea;font-size:18px;margin-top:20px;max-width:64ch">{_h.escape(desc)}</p>
    <p style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-p" href="contact.html">Get a free quote</a><a class="btn btn-o" href="gallery.html">See the full gallery</a></p>
    <h2 class="disp" style="font-size:24px;margin-top:56px">More laser cleaning videos</h2>
    <ul style="margin-top:14px;line-height:2;color:#c9d6ea">{others}</ul>
  </div>
</section>
<script type="application/ld+json">{json.dumps(video_ld(slug,title,desc,dur))}</script>"""
    (ROOT / f"video-{slug}.html").write_text(head(f"{title} | Sydney Laser Cleaning", desc, f"video-{slug}.html", f"video/{slug}-poster.jpg") + nav("gallery") + "<main>\n" + body + "\n</main>\n" + FOOT.replace("__VER__", VER))
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

# ---- Service landing pages (one per search term people use) ----
SVC = [
 dict(file="laser-rust-removal-sydney.html", short="Rust removal", kicker="Metal",
  title="Laser Rust Removal Sydney | No Sandblasting, No Chemicals | Sydney Laser Cleaning",
  desc="Laser rust removal across Sydney for steel beams, rails, trailers, machinery, car panels and parts. Back to bare metal, ready to prime or weld. Free quote: 0432 722 498.",
  h1="Laser rust removal in Sydney", video="job-9950", image="img/real/rail-cleaning.jpg",
  intro="We take rust off steel of any size with a laser: beams, rails, trailers, machinery, wheels, tools and car panels. The beam lifts the surface oxide and leaves the steel underneath as it was, so the part is ready to prime or weld straight after. No grit, no chemicals and nothing to wash away.",
  why=["Removes rust without changing the chemical or structural makeup of the steel","Gets into pitted rust that sanding and cutting back can't reach (200W pulse laser)","No sandblasting media to sweep up and no chemical runoff","Precise: one seam, one edge or a whole beam"],
  items=["Structural steel, beams and rails","Trailers and machinery","Car panels and classic restorations","Wheels, rims, brake drums and parts","Tools and workshop equipment","Weld prep and mill scale"],
  machine="For heavy rust on thick steel we use the 1500W continuous laser, which moves fast through big jobs. For car panels, thin sheet and pitted rust we use the 200W pulse laser, which cleans with very little heat so thin metal doesn't warp.",
  faq=[("Does laser rust removal damage the metal?","No. The laser takes off the surface rust and leaves the steel underneath intact. We match the laser to the job: the 200W pulse laser for thin panels so they don't warp, the 1500W for thick steel."),
       ("Is the steel ready to paint after laser cleaning?","Yes. Once the oxide is off, the part is ready to prime or weld straight after."),
       ("Can you remove rust on site?","Yes. We bring the machine and an operator to your site anywhere in Sydney. You can also hire a machine and do it yourself."),
       ("How much does laser rust removal cost?","It depends on the size and condition of the job. Text a photo to 0432 722 498 and we'll give you a free quote.")]),
 dict(file="laser-paint-removal-sydney.html", short="Paint removal", kicker="Coatings",
  title="Laser Paint Removal Sydney | Car Panels, Rims & Machinery | Sydney Laser Cleaning",
  desc="Laser paint stripping in Sydney for car bodies, rims, classic restorations, powder coat and machinery. Back to bare metal with no blasting dust or chemical stripper. Free quote.",
  h1="Laser paint removal in Sydney", video="rim-timelapse", image="img/real/rim-after.jpg",
  intro="We strip paint and coatings back to bare metal with a laser: car panels, rims, classic restorations, powder coat and machinery. There's no blasting dust through the workshop and no chemical stripper to wash off.",
  why=["Bare metal without sandblasting dust","No chemical paint stripper or runoff","Controlled: strip one area and leave the rest","Safe on thin panels with the 200W pulse laser"],
  items=["Car bodies and panels","Rims and wheels","Classic car and bike restorations","Powder coat","Machinery and coated parts","Steel rails and structures"],
  machine="Thin car panels get the 200W pulse laser so the heat doesn't warp them. Thick paint on heavy steel and machinery gets the 1500W continuous laser.",
  faq=[("Can a laser remove paint from a car without damaging the panel?","Yes, with the right machine. We use the 200W pulse laser on car panels because it cleans with very little heat, so thin metal doesn't warp."),
       ("Can you strip powder coat?","Yes. Powder coat and other coatings can be stripped back to bare metal."),
       ("Is laser paint removal better than sandblasting?","There's no grit to clean up, no dust through the workshop and the metal underneath isn't worn down by blasting media."),
       ("How do I get a price?","Text a photo of the part to 0432 722 498 for a free quote.")]),
 dict(file="graffiti-removal-sydney.html", short="Graffiti removal", kicker="Masonry",
  title="Laser Graffiti Removal Sydney | Sandstone, Brick & Heritage | Sydney Laser Cleaning",
  desc="Laser graffiti removal in Sydney for sandstone, brick, heritage walls and roller shutters. Lifts the paint and leaves the wall, without sandblasting or harsh chemicals.",
  h1="Laser graffiti removal in Sydney", video="stone-step", image="img/graffiti.jpg",
  intro="Steam and chemicals often don't get all the graffiti off, and sandblasting wears down the surface, which is a real problem on soft stone and heritage buildings. The laser lifts the paint and leaves the wall.",
  why=["Doesn't wear down the surface like sandblasting","No harsh chemicals soaking into stone","Gets the paint out of the texture of brick and stone","Precise around seams, signage and edges"],
  items=["Sandstone","Brick walls","Heritage walls and buildings","Roller shutters","Concrete and render","Stone steps and features"],
  machine="For softer stone and detailed surfaces we use the 200W pulse laser, which works with very little heat.",
  faq=[("Can a laser remove graffiti from sandstone?","Yes. The laser lifts the paint without blasting the stone away, which matters on soft stone and heritage surfaces."),
       ("Will it leave a ghost mark?","Send us a photo first and we'll tell you straight what to expect on your surface."),
       ("Do you use chemicals?","No. Laser cleaning uses no chemicals, no grit and no water."),
       ("Do you come to us?","Yes, we bring the machine to your site anywhere in Sydney.")]),
 dict(file="fire-damage-soot-removal-sydney.html", short="Fire damage", kicker="Restoration",
  title="Fire Damage & Soot Removal Sydney | Laser Cleaning | Sydney Laser Cleaning",
  desc="Laser soot and smoke damage removal in Sydney for concrete ceilings, brick, timber and plaster. Shifts soot that pressure washing and chemicals couldn't. Free quote.",
  h1="Fire damage and soot removal in Sydney", video="cw-ceiling", image="img/real/ceiling.jpg",
  intro="We remove fire soot and smoke staining with a laser. On a concrete ceiling where pressure washing and chemicals couldn't shift the soot, our 1500W continuous laser did. On a balcony where other methods had already failed, the laser lifted it. The beam reflects off white plasterboard and painted walls while it removes the soot, so restoration doesn't have to mean repainting everything.",
  why=["Shifts soot that pressure washing and chemicals couldn't","No water through the building and no chemical runoff","Overhead work: ceilings and soffits","Can mean less repainting on light surfaces"],
  items=["Concrete ceilings and soffits","Brick and masonry","Timber","Plaster and plasterboard","Balconies and walls","Steel structures"],
  machine="Heavy soot on concrete and masonry gets the 1500W continuous laser. Softer and finer surfaces get the 200W pulse laser.",
  faq=[("Can a laser remove soot from a ceiling?","Yes. We've cleared heavy fire soot off concrete ceilings with the 1500W continuous laser where pressure washing and chemicals couldn't."),
       ("Do you need to use water?","No. Laser cleaning uses no water, chemicals or grit, so nothing washes through the building."),
       ("Do I need to repaint after?","Not always. The beam reflects off white plasterboard and painted walls while it removes the soot. Send a photo and we'll tell you what to expect."),
       ("Do you work with insurance and restoration jobs?","Send us the details and photos and we'll quote the job.")]),
 dict(file="concrete-stone-cleaning-sydney.html", short="Concrete & stone", kicker="Concrete & stone",
  title="Concrete, Brick & Stone Cleaning Sydney | Laser Cleaning | Sydney Laser Cleaning",
  desc="Laser cleaning for concrete, brick and stone in Sydney: fire soot, mould staining and grime, including ceilings and stone steps. No chemicals or water blasting.",
  h1="Concrete, brick and stone cleaning in Sydney", video="stone-step", image="img/real/ceiling.jpg",
  intro="We take fire soot, mould staining and grime off concrete, brick and stone, including overhead work like ceilings and soffits. The 200W pulse laser also brings stone steps and floors back up clean.",
  why=["No chemicals soaking into porous surfaces","No water blasting","Works overhead on ceilings and soffits","Gentle on stone with the 200W pulse laser"],
  items=["Concrete ceilings and walls","Brick","Sandstone and stone steps","Floors","Soffits","Paving and features"],
  machine="The 1500W continuous laser handles heavy soot on concrete and masonry. The 200W pulse laser is used for stone steps, floors and softer surfaces.",
  faq=[("Can you clean stone steps with a laser?","Yes. The 200W pulse laser lifts grime off stone steps and floors."),
       ("Does it remove mould staining?","Yes, mould staining and grime can be lifted off concrete, brick and stone."),
       ("Is it safe on soft stone?","We use the 200W pulse laser on softer surfaces. Send a photo and we'll tell you if your surface suits laser cleaning."),
       ("Do you service my area?","We work right across Sydney. Text a photo to 0432 722 498.")]),
]

def faq_ld(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
def crumbs_ld(name, path):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE_URL},
      {"@type":"ListItem","position":2,"name":"Services","item":SITE_URL+"services.html"},
      {"@type":"ListItem","position":3,"name":name,"item":SITE_URL+path}]}

ul = lambda xs: "".join(f"<li>{_h.escape(x)}</li>" for x in xs)
for sv in SVC:
    vt = next(t for sl,t,_,_ in VIDEOS if sl==sv["video"])
    others = "".join(f'<li><a href="{x["file"]}">{_h.escape(x["h1"])}</a></li>' for x in SVC if x is not sv)
    areas = ", ".join(AREAS)
    faqhtml = "".join(f'<details style="border:1px solid rgba(148,163,184,.25);border-radius:14px;padding:16px 20px;margin-top:12px"><summary style="cursor:pointer;font-weight:700">{_h.escape(q)}</summary><p style="color:#c9d6ea;margin-top:10px">{_h.escape(a)}</p></details>' for q,a in sv["faq"])
    service_ld = {"@context":"https://schema.org","@type":"Service","name":sv["h1"],"serviceType":sv["short"],
                  "provider":{"@id":SITE_URL+"#business"},"areaServed":{"@type":"City","name":"Sydney"},"url":SITE_URL+sv["file"],"description":sv["desc"]}
    extra = "".join(f'\n<script type="application/ld+json">{json.dumps(x)}</script>' for x in (service_ld, faq_ld(sv["faq"]), crumbs_ld(sv["short"], sv["file"])))
    body = f"""<section class="phero">
  <img src="{sv['image']}" alt="">
  <div class="wrap">
    <span class="kicker in i1">{_h.escape(sv['kicker'])}</span>
    <h1 class="disp in i2">{_h.escape(sv['h1'])}</h1>
    <p class="in i3">{_h.escape(sv['intro'])}</p>
    <p class="in i3" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px"><a class="btn btn-p" href="contact.html">Get a free quote</a><a class="btn btn-o" href="sms:0432722498">Text a photo</a></p>
  </div>
</section>
<section class="sec">
  <div class="wrap" style="max-width:1000px">
    <nav aria-label="Breadcrumb" style="color:#94a3b8;font-size:14px;margin-bottom:28px"><a href="index.html">Home</a> › <a href="services.html">Services</a> › {_h.escape(sv['short'])}</nav>
    <h2 class="disp" style="font-size:clamp(26px,3.4vw,38px)">Why use a laser</h2>
    <ul style="margin-top:16px;line-height:1.9;color:#c9d6ea;font-size:18px">{ul(sv['why'])}</ul>
    <h2 class="disp" style="font-size:clamp(26px,3.4vw,38px);margin-top:48px">What we clean</h2>
    <ul style="margin-top:16px;line-height:1.9;color:#c9d6ea;font-size:18px">{ul(sv['items'])}</ul>
    <h2 class="disp" style="font-size:clamp(26px,3.4vw,38px);margin-top:48px">Watch a real job</h2>
    <video controls playsinline preload="none" poster="video/{sv['video']}-poster.jpg" style="width:100%;max-height:70vh;object-fit:contain;border-radius:18px;margin-top:18px;background:#000" aria-label="{_h.escape(vt)}"><source src="video/{sv['video']}.mp4" type="video/mp4"></video>
    <p style="color:#94a3b8;margin-top:10px"><a href="video-{sv['video']}.html">{_h.escape(vt)}</a></p>
    <h2 class="disp" style="font-size:clamp(26px,3.4vw,38px);margin-top:48px">Which laser we use</h2>
    <p style="color:#c9d6ea;font-size:18px;margin-top:16px;max-width:70ch">{_h.escape(sv['machine'])} Not sure which one your job needs? Send us a photo and we'll tell you.</p>
    <h2 class="disp" style="font-size:clamp(26px,3.4vw,38px);margin-top:48px">On site across Sydney, or hire the machine</h2>
    <p style="color:#c9d6ea;font-size:18px;margin-top:16px;max-width:70ch">We bring the machine and an operator to your site, Sydney wide, including {areas}. Rather do it yourself? <a href="hire.html">Hire a laser cleaning machine</a> by the day, week or month.</p>
    <h2 class="disp" style="font-size:clamp(26px,3.4vw,38px);margin-top:48px">Questions</h2>
    {faqhtml}
    <div style="margin-top:48px;padding:28px;border-radius:20px;background:rgba(37,99,235,.12);border:1px solid rgba(37,99,235,.35)">
      <h2 class="disp" style="font-size:28px">Free quote</h2>
      <p style="color:#c9d6ea;margin-top:8px">Text a photo of the job to <a href="sms:0432722498">0432 722 498</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <p style="margin-top:18px"><a class="btn btn-p" href="contact.html">Get a free quote</a></p>
    </div>
    <h2 class="disp" style="font-size:24px;margin-top:48px">Other laser cleaning services</h2>
    <ul style="margin-top:14px;line-height:2;color:#c9d6ea">{others}<li><a href="hire.html">Laser cleaning machine hire</a></li></ul>
  </div>
</section>"""
    (ROOT/sv["file"]).write_text(head(sv["title"], sv["desc"], sv["file"], sv["image"], extra) + nav("services") + "<main>\n" + body + "\n</main>\n" + FOOT.replace("__VER__", VER))
    print("built", sv["file"])

# add service pages to sitemap
sm = (ROOT/"sitemap.xml").read_text()
add = "".join(f"  <url><loc>{BASE}{x['file']}</loc><lastmod>{today}</lastmod></url>\n" for x in SVC)
(ROOT/"sitemap.xml").write_text(sm.replace("</urlset>", add + "</urlset>"))

# 404 page
nf = """<section class="phero"><div class="wrap"><span class="kicker">Page not found</span><h1 class="disp">That page isn't here</h1><p>Try one of these instead.</p><ul style="margin-top:20px;line-height:2">""" + "".join(f'<li><a href="{u}">{n}</a></li>' for u,n in SERVICE_PAGES) + """<li><a href="index.html">Home</a></li><li><a href="contact.html">Get a free quote</a></li></ul></div></section>"""
(ROOT/"404.html").write_text(head("Page not found | Sydney Laser Cleaning","Page not found.","404.html").replace('content="index,follow,max-image-preview:large,max-video-preview:-1"','content="noindex"') + nav("") + "<main>\n" + nf + "\n</main>\n" + FOOT.replace("__VER__", VER))
print("built 404.html")
