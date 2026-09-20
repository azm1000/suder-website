#!/usr/bin/env python3
"""Generate the Suder, LLC static site into ../public.  Run: python3 src/build.py"""
import os, re, html, shutil, datetime
from pathlib import Path
import sys
sys.path.insert(0, os.path.dirname(__file__))
from site_content import *
import landing_content as LC

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
V = "20260920d"  # cache-bust for css/js

def esc(s): return html.escape(s, quote=True)

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 8h11M9 3l5 5-5 5"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg>'

def btn(href, text, kind="primary"):
    return f'<a class="btn btn-{kind}" href="{href}">{esc(text)}{ARROW}</a>'

def link(href, text):
    return f'<a class="link" href="{href}">{esc(text)}{ARROW}</a>'

# ------------------------------------------------------------------ chrome
def header(dark_hero=True):
    solid = "" if dark_hero else ' data-solid="1"'
    menu = "".join(f'<a href="/practice/{s}/">{esc(n)}<span>{esc(PRACTICE_BLURBS[s].split(".")[0])}.</span></a>' for s, n in PRACTICES)
    mob = "".join(f'<a class="sub" href="/practice/{s}/">{esc(n)}</a>' for s, n in PRACTICES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="header"{solid}>
  <div class="header-inner">
    <a class="brand" href="/" aria-label="Suder, LLC home">
      <img class="logo-white" src="/assets/img/logo-white.png" alt="Suder, LLC" width="1403" height="382">
      <img class="logo-dark" src="/assets/img/logo-dark.png" alt="Suder, LLC" width="1403" height="382">
    </a>
    <nav class="nav" aria-label="Primary">
      <div class="has-menu"><a href="/practice/land-use-zoning/">Practice areas {CHEV}</a><div class="menu">{menu}</div></div>
      <a href="/results/">Results</a>
      <a href="/team/">Team</a>
      <a href="/jurisdictions/">Jurisdictions</a>
      <a href="/contact/" class="btn btn-primary">Get in touch{ARROW}</a>
    </nav>
    <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-nav" aria-label="Mobile navigation">
  <button class="close" aria-label="Close menu">&times;</button>
  <a href="/">Home</a>
  <a href="/practice/land-use-zoning/">Practice areas</a>
  {mob}
  <a href="/results/">Results</a>
  <a href="/opinions/">Published opinions</a>
  <a href="/team/">Team</a>
  <a href="/jurisdictions/">Jurisdictions</a>
  <a href="/zoning-letters/">Zoning letters &amp; opinions</a>
  <a href="/contact/">Contact</a>
</div>'''

def footer():
    pr = "".join(f'<a href="/practice/{s}/">{esc(n)}</a>' for s, n in PRACTICES)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <img src="/assets/img/logo-white.png" alt="Suder, LLC" width="1403" height="382">
        <div class="tag">{esc(FIRM["tagline"])}.</div>
        <div>{esc(FIRM["address1"])}<br>{esc(FIRM["address2"])}<br><span class="muted">{esc(FIRM["address_note"])}</span></div>
        <div style="margin-top:12px"><a href="tel:{FIRM["phone_tel"]}">{esc(FIRM["phone"])}</a><a href="mailto:{FIRM["email"]}">{esc(FIRM["email"])}</a></div>
      </div>
      <div><h4>Practice areas</h4>{pr}</div>
      <div><h4>Firm</h4><a href="/results/">Results</a><a href="/opinions/">Published opinions</a><a href="/jurisdictions/">Jurisdictions</a><a href="/zoning-letters/">Zoning letters &amp; opinions</a><a href="/team/">Team</a><a href="/careers/">Careers</a><a href="/contact/">Contact</a></div>
      <div><h4>Recognition</h4><a href="/team/sean-suder/">Best Lawyers "Lawyer of the Year" 2026</a><a href="/team/sean-suder/">Chambers USA Band 1, every year since 2019</a><a href="/">Chambers Spotlight Firm 2025–2026</a><a href="{FIRM["zoneco"]}" rel="noopener" target="_blank">Sister firm: ZoneCo ↗</a></div>
    </div>
    <div class="bottom">
      <div>&copy; <span data-year>2026</span> Suder, LLC. All rights reserved. Attorney advertising.</div>
      <div><a href="/terms/">Terms of use</a><a href="{FIRM["linkedin"]}" rel="noopener" target="_blank">LinkedIn</a></div>
    </div>
  </div>
</footer>'''

def page(title, desc, body, path, dark_hero=True, canonical=None):
    canon = FIRM["domain"] + (canonical or path)
    full_title = title if title.startswith("Suder") else f"{title} | Suder, LLC"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:image" content="{FIRM["domain"]}/assets/img/hero-skylines.jpg">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,300;1,9..144,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v={V}">
</head>
<body>
{header(dark_hero)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/js/site.js?v={V}" defer></script>
</body>
</html>'''

def write(path, content):
    p = PUB / path.lstrip("/")
    if path.endswith("/"): p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return path

# ------------------------------------------------------------------ pieces
def hero(h1, lede, actions, img=None, tag=None, short=False, eyebrow=None, caption=None):
    media = f'<div class="hero-media"><img src="/assets/img/{img}" alt="{esc(caption or "")}" fetchpriority="high"></div><div class="hero-shade"></div>' if img else '<div class="hero-pattern"></div>'
    eb = f'<div class="eyebrow reveal in">{esc(eyebrow)}</div>' if eyebrow else ""
    tg = f'<div class="hero-tag reveal" data-delay="3">{esc(tag)}</div>' if tag else ""
    return f'''<section class="hero{" hero-short" if short else ""}">
  {media}
  <div class="hero-inner">
    {eb}
    <h1 class="reveal">{h1}</h1>
    <p class="lede reveal" data-delay="1">{esc(lede)}</p>
    <div class="hero-actions reveal" data-delay="2">{actions}</div>
  </div>
  {tg}
  <div class="hero-scroll">Scroll</div>
  {f'<div class="hero-caption">{esc(caption)}</div>' if caption else ''}
</section>'''

def stats_band():
    items = ""
    for big, txt in CREDENTIALS:
        m = re.match(r"^(\d+)(\+?)$", big)
        b = f'<b data-count="{m.group(1)}" data-suffix="{m.group(2)}">{m.group(1)}{m.group(2)}</b>' if m else f"<b>{esc(big)}</b>"
        items += f'<div class="stat reveal">{b}<span>{esc(txt)}</span></div>'
    return f'<section class="stats"><div class="wrap">{items}</div></section>'

def practice_cards(exclude=None):
    out = ""
    i = 0
    for s, n in PRACTICES:
        if s == exclude: continue
        i += 1
        dark = ' card-dark' if s == "land-use-zoning" else ""
        out += f'<a class="card{dark} reveal" data-delay="{i%3}" href="/practice/{s}/"><div class="num">0{i}</div><h3>{esc(n)}</h3><p>{esc(PRACTICE_BLURBS[s])}</p><span class="link">Explore{ARROW}</span></a>'
    return out

def result_row(r):
    tags = " ".join(r["practices"])
    th = f'<div class="thumb"><img src="/assets/img/{r["img"]}" alt="" loading="lazy" width="900" height="675"></div>' if r.get("img") else '<div class="thumb thumb-empty"><span>{}</span></div>'.format(esc(r["kicker"].split()[0]))
    return f'''<a class="row reveal" id="{r["slug"]}" data-tags="{tags}" href="/results/#{r["slug"]}">
  {th}
  <div><div class="kicker">{esc(r["kicker"])}</div><h3>{esc(r["title"])}</h3><div class="meta">{esc(r["meta"])}</div></div>
  <p>{esc(r["summary"])}</p>
  <div class="arrow">{ARROW}</div>
</a>'''

def result_rows(results):
    return '<div class="rows">' + "".join(result_row(r) for r in results) + '</div>'

def awards_grid():
    out = ""
    for a in AWARDS:
        img = f'<img src="/assets/img/{a["img"]}" alt="{esc(a["alt"])}" loading="lazy">' if a["img"] else '<div class="ph">Chambers<br>Spotlight</div>'
        out += f'<div class="award reveal">{img}<div><b>{esc(a["title"])}</b><span>{esc(a["sub"])}</span></div></div>'
    return f'<div class="awards">{out}</div>'

def people_grid():
    out = ""
    for i, t in enumerate(TEAM):
        out += f'<a class="person reveal" data-delay="{i%4}" href="/team/{t["slug"]}/"><div class="ph"><img src="/assets/img/{t["img"]}-portrait.jpg" alt="{esc(t["name"])}" loading="lazy" width="900" height="1125"></div><b>{esc(t["name"])}</b><span>{esc(t["role"])}</span></a>'
    return f'<div class="people">{out}</div>'

def marquee():
    return '<div class="marquee" aria-hidden="true"><div class="marquee-track">' + "".join(f"<span>{esc(j)}</span>" for j in JURISDICTIONS) + '</div></div>'

def cta(h="Let's talk about your property.", sub="Tell us what you are trying to build, buy, keep, or defend. We will tell you plainly how we can help."):
    return f'''<section class="cta"><div class="wrap">
  <div><h2 class="reveal">{esc(h)}</h2><p class="lede reveal" data-delay="1">{esc(sub)}</p><div class="reveal" data-delay="2" style="margin-top:26px">{btn("/contact/", "Get in touch")}</div></div>
  <div class="contact-lines reveal" data-delay="2">{esc(FIRM["address1"])}<br>{esc(FIRM["address2"])}<br><span class="muted">{esc(FIRM["address_note"])}</span><br><a href="tel:{FIRM["phone_tel"]}">{esc(FIRM["phone"])}</a><br><a href="mailto:{FIRM["email"]}">{esc(FIRM["email"])}</a></div>
</div></section>'''

def by_slug(): return {r["slug"]: r for r in RESULTS}

# ------------------------------------------------------------------ pages
def build_home():
    featured = [r for r in RESULTS if r.get("featured")]
    body = hero(
        'Counsel for the <em>Built Environment.</em>',
        "Ohio's land use and zoning counsel, with a commercial real estate practice built by former big-firm partners. At Suder, zoning is not just another practice area. It is the practice area.",
        btn("/contact/", "Get in touch") + btn("/practice/land-use-zoning/", "Explore our work", "outline"),
        img="hero-skylines.jpg", tag="Cincinnati · Columbus · Cleveland and 60+ jurisdictions across Ohio and Northern Kentucky",
        eyebrow="Land use · Real estate · Litigation")
    body += stats_band()
    body += f'''<section><div class="wrap split">
  <div class="sticky"><div class="eyebrow reveal">Why Suder</div><h2 class="reveal">Lawyers who have sat on every side of the table.</h2></div>
  <div>
    <p class="lede reveal">Our founder spent nearly four years as the City of Cincinnati's Chief Counsel for Land Use and Planning, wrote its land development code, and now rewrites zoning codes for cities across the country. Our transactional lawyers were partners at global and national firms. Our eminent domain counsel is a certified planner who has represented more than 100 property owners.</p>
    <p class="reveal" data-delay="1">That mix of government, big-firm, and planning experience is why Chambers USA has ranked Sean Suder in Band 1 for Ohio zoning and land use every year since 2019, why Best Lawyers named him Cincinnati's Land Use and Zoning "Lawyer of the Year" for 2026, and why Am Law firms call Suder when their clients' matters land in Ohio.</p>
    <div class="reveal" data-delay="2" style="display:flex;gap:28px;flex-wrap:wrap;margin-top:8px">{link("/team/", "Meet the team")}{link("/results/", "See our results")}</div>
  </div>
</div></section>'''
    body += f'''<section class="dark"><div class="wrap">
  <div class="eyebrow reveal">Practice areas</div>
  <h2 class="reveal" style="max-width:18ch">Everything real property, and nothing else.</h2>
  <div class="grid grid-3" style="margin-top:40px">{practice_cards()}</div>
</div></section>'''
    body += f'''<section><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:34px"><div><div class="eyebrow reveal">Results</div><h2 class="reveal">Work we are proud of.</h2></div><div class="reveal" data-delay="1">{link("/results/", "All results and case studies")}</div></div>
  {result_rows(featured)}
</div></section>'''
    body += f'''<section class="section-tight" style="background:var(--paper-2)"><div class="wrap">
  <div class="eyebrow reveal">Recognition</div>
  <h2 class="reveal" style="max-width:16ch">Peer reviewed. Consistently.</h2>
  <div style="margin-top:34px">{awards_grid()}</div>
</div></section>'''
    body += f'''<section class="dark-ink"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:34px"><div><div class="eyebrow reveal">The team</div><h2 class="reveal">Lawyers and planners, under one roof.</h2></div><div class="reveal" data-delay="1"><span class="link" style="border-color:var(--brass-2)"><a href="/team/">Attorneys &amp; professionals</a>{ARROW}</span></div></div>
  {people_grid()}
</div></section>'''
    body += f'''<section class="section-tight" style="padding-bottom:0"><div class="wrap" style="text-align:center;margin-bottom:26px"><div class="eyebrow reveal" style="justify-content:center">Where we work</div><h3 class="reveal">Zoning matters in more than 60 jurisdictions across Ohio and Northern Kentucky</h3><div class="reveal" data-delay="1">{link("/jurisdictions/", "See the list")}</div></div>{marquee()}</section>'''
    body += cta()
    write("/", page("Suder, LLC | Counsel for the Built Environment | Ohio Land Use, Zoning & Real Estate Law", "Suder, LLC is a Cincinnati commercial real estate and land use law firm: zoning, real property litigation and appeals, transactions, eminent domain, historic preservation, real estate taxation, and local counsel across Ohio and Northern Kentucky.", body, "/"))

def build_practices():
    lc = {LANDING_TO_SLUG[p["name"]]: p for p in LC.PAGES}
    rs = by_slug()
    for slug, name in PRACTICES:
        p = lc[slug]
        img, cap = PRACTICE_HERO[slug]
        results = [r for r in RESULTS if slug in r["practices"]]
        bullets = "".join(f'<li class="reveal" data-delay="{i%4}">{esc(b)}</li>' for i, b in enumerate(p["bullets"]))
        cred = f'''<div class="credbar"><div class="wrap">
  <div class="item"><b>Band 1</b><span>Chambers USA, Ohio Zoning/Land Use, every year since 2019</span></div>
  <div class="item"><b>2026</b><span>Best Lawyers "Lawyer of the Year," Land Use and Zoning Law, Cincinnati</span></div>
  <div class="item"><b>60+</b><span>jurisdictions across Ohio and Northern Kentucky</span></div>
  <div class="item"><b>5</b><span>states of licensure: OH, KY, TX, NY, and D.C.</span></div>
</div></div>'''
        results_html = ""
        if results:
            results_html = f'''<section class="dark"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:34px"><div><div class="eyebrow reveal">Results</div><h2 class="reveal">Representative matters.</h2></div><div class="reveal" data-delay="1"><span class="link" style="border-color:var(--brass-2)"><a href="/results/#{slug}">All results</a>{ARROW}</span></div></div>
  {result_rows(results)}
</div></section>'''
        others = f'''<section><div class="wrap"><div class="eyebrow reveal">Related practice areas</div><h2 class="reveal" style="max-width:16ch">Everything real property.</h2><div class="grid grid-3" style="margin-top:40px">{practice_cards(exclude=slug)}</div></div></section>'''
        body = hero(esc(p["heading"]), p["subheading"], btn("/contact/", p["button"]) + btn("/results/#" + slug, "See results", "outline"),
                    img=img, tag=p["image_text"], short=True, eyebrow=LC.LICENSED, caption=cap)
        body += cred
        body += f'''<section><div class="wrap split">
  <div class="sticky"><div class="eyebrow reveal">Why Suder</div><h2 class="reveal">{esc(name)}</h2></div>
  <div><p class="lede reveal">{esc(p["description"])}</p>
  <h3 class="reveal" style="margin-top:44px;font-size:14px;letter-spacing:.16em;text-transform:uppercase;font-family:var(--body);font-weight:600;color:var(--stone)">How we help</h3>
  <ul class="bullets">{bullets}</ul></div>
</div></section>'''
        body += results_html + others + cta(f"Talk to us about {name.lower() if slug!='local-counsel' else 'local counsel'}.")
        desc = p["subheading"]
        write(f"/practice/{slug}/", page(name, desc, body, f"/practice/{slug}/"))

def build_results():
    chips = '<div class="chips"><button class="chip active" data-filter="all">All</button>' + "".join(f'<button class="chip" data-filter="{s}">{esc(n)}</button>' for s, n in PRACTICES) + '</div>'
    body = f'''<section class="page-head"><div class="wrap"><div class="eyebrow">Results</div><h1>We are proud of what we do, and how we do it.</h1><p class="lede">Representative matters and published decisions from across the firm. Filter by practice area.</p></div></section>
<section style="padding-top:0"><div class="wrap">{chips}{result_rows(RESULTS)}
<p class="muted" style="margin-top:30px;font-size:14px">Prior results do not guarantee a similar outcome. Client names are used only where the matter is a matter of public record.</p></div></section>''' + cta()
    write("/results/", page("Results & Case Studies", "Representative land use, zoning, litigation, and real estate transaction results from Suder, LLC.", body, "/results/", dark_hero=False))

def build_opinions():
    rs = by_slug()
    items = ""
    for topic, case, cite, url, slug in OPINIONS:
        more = f' · <a href="/results/#{slug}" style="border-bottom:1px solid var(--brass)">Case study</a>' if slug else ""
        items += f'<div class="opinion reveal"><div><div class="topic">{esc(topic)}</div><b>{esc(case)}</b><span>{esc(cite)}{more}</span></div><a class="btn btn-outline" href="{url}" target="_blank" rel="noopener">Read the opinion{ARROW}</a></div>'
    body = f'''<section class="page-head"><div class="wrap"><div class="eyebrow">Published opinions</div><h1>Real property, tried and published.</h1><p class="lede">We have successfully represented clients on real property matters in Ohio's trial and appellate courts. Example published opinions:</p></div></section>
<section style="padding-top:0"><div class="wrap-narrow" style="max-width:960px">{items}</div></section>''' + cta("Facing a real property dispute?", "We resolve disputes efficiently when we can and try them when we must.")
    write("/opinions/", page("Published Opinions", "Published Ohio appellate decisions won by Suder, LLC on taxpayer standing, nonconforming uses, use variances, mandamus, spot zoning, and foreclosure.", body, "/opinions/", dark_hero=False))

def build_jurisdictions():
    lis = "".join(f"<li>{esc(j)}</li>" for j in JURISDICTIONS)
    body = f'''<section class="page-head"><div class="wrap"><div class="eyebrow">Jurisdictions</div><h1>{len(JURISDICTIONS)}+ jurisdictions. One firm.</h1><p class="lede">We have represented clients on zoning matters in more than 60 jurisdictions in Ohio and Northern Kentucky, from Cincinnati's neighborhoods to Cleveland, Columbus, Toledo, and Akron.</p></div></section>
{marquee()}
<section><div class="wrap"><ul class="list-cols">{lis}</ul></div></section>''' + cta("Your project is in a jurisdiction we know.", "Boards, staff, codes, and neighbors: we have probably been in that hearing room before.")
    write("/jurisdictions/", page("Jurisdictions", "Suder, LLC has handled zoning matters in more than 60 jurisdictions across Ohio and Northern Kentucky.", body, "/jurisdictions/", dark_hero=False))

def build_zoning_letters():
    body = f'''<section class="page-head"><div class="wrap"><div class="eyebrow">Zoning letters &amp; opinions</div><h1>Zoning verification letters and zoning opinions.</h1><p class="lede">Now offered in Ohio, Kentucky, and Washington, D.C.</p></div></section>
<section style="padding-top:0"><div class="wrap split">
  <div class="sticky"><h2 style="font-size:30px">Fast, lender-ready answers on what a property can be used for.</h2></div>
  <div class="prose">
    <p class="lede">Having trouble getting a zoning verification or opinion letter from the municipality? Need one for your financing? Don't want to pay the high cost of a title insurance zoning endorsement?</p>
    <p>Suder provides zoning verification letters and formal zoning opinions for owners, buyers, and lenders, prepared by lawyers who read and write zoning codes for a living. We confirm the zoning classification, permitted uses, conformity of existing improvements, and open violations, and we can address the specific questions your lender or title company is asking.</p>
    <p>We can provide immediate assistance. <a href="/contact/" style="border-bottom:1px solid var(--brass)">Contact us</a> with the property address and your closing timeline.</p>
    <ul>
      <li>Zoning verification letters for acquisitions, refinancings, and CMBS and agency loans</li>
      <li>Formal zoning opinion letters as an alternative to ALTA zoning endorsements</li>
      <li>Nonconforming use and rebuild analyses</li>
      <li>Entitlement due diligence for portfolios across multiple jurisdictions</li>
    </ul>
  </div>
</div></section>''' + cta("Need a zoning letter for a closing?", "Send us the address and the deadline.")
    write("/zoning-letters/", page("Zoning Letters & Opinions", "Zoning verification letters and zoning opinion letters in Ohio, Kentucky, and Washington, D.C., from Suder, LLC.", body, "/zoning-letters/", dark_hero=False))

def build_team():
    body = f'''<section class="page-head"><div class="wrap"><div class="eyebrow">Attorneys &amp; professionals</div><h1>Lawyers and planners, under one roof.</h1><p class="lede">Every member of the team has spent a career on the built environment: in city hall, at large law firms, in planning departments, and on development sites.</p></div></section>
<section style="padding-top:0"><div class="wrap">{people_grid()}</div></section>''' + cta("Work with us.", "Reach any of us directly, or use the form and we will route it to the right person.")
    write("/team/", page("Team", "The attorneys and professionals of Suder, LLC: Sean Suder, J.P. Burleigh, Teresa Bamberger, Josh Bernstein, and Todd Kinskey.", body, "/team/", dark_hero=False))
    for t in TEAM:
        paras = "".join(f'<p class="reveal">{esc(x)}</p>' for x in t["bio"])
        facts = "".join(f'<h3>{esc(h)}</h3><ul>' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>" for h, items in t["sections"])
        mail = t["email"]
        body = f'''<section class="bio-hero"><div class="wrap">
  <div class="ph reveal"><img src="/assets/img/{t["img"]}-portrait.jpg" alt="{esc(t["name"])}" width="900" height="1125" fetchpriority="high"></div>
  <div><span class="role reveal">{esc(t["role"])}</span><h1 class="reveal">{esc(t["name"])}<span style="display:block;font-size:.45em;color:var(--stone);margin-top:6px">{esc(t["suffix"])}</span></h1>
  <p class="lede reveal" data-delay="1">{esc(t["intro"])}</p>
  <div class="contact reveal" data-delay="2"><a href="mailto:{mail}" style="border-bottom:1px solid var(--brass)">{mail}</a><br>{esc(t["phones"])}</div></div>
</div></section>
<section class="bio-body" style="padding-top:20px"><div class="wrap"><div>{paras}<p class="reveal" style="font-family:var(--display);font-style:italic;font-size:20px">{esc(t["first"])} is proud to be Counsel for the Built Environment.</p></div><aside class="facts reveal">{facts}</aside></div></section>''' + cta(f"Reach {t['first']} directly.", "Or use the contact form and we will route your matter to the right person.")
        write(f"/team/{t['slug']}/", page(f"{t['name']}, {t['suffix']}", t["intro"], body, f"/team/{t['slug']}/", dark_hero=False))

def build_contact():
    body = f'''<section class="page-head"><div class="wrap"><div class="eyebrow">Contact</div><h1>Tell us about your property.</h1><p class="lede">Send a note and we will respond promptly. Please do not include confidential information until we have confirmed there is no conflict of interest.</p></div></section>
<section style="padding-top:0"><div class="wrap split">
  <div class="sticky">
    <h3>Suder, LLC</h3>
    <p>{esc(FIRM["address1"])}<br>{esc(FIRM["address2"])}<br><span class="muted">{esc(FIRM["address_note"])}</span></p>
    <p><a href="tel:{FIRM["phone_tel"]}" style="border-bottom:1px solid var(--brass)">{esc(FIRM["phone"])}</a><br><a href="mailto:{FIRM["email"]}" style="border-bottom:1px solid var(--brass)">{esc(FIRM["email"])}</a></p>
    <p><a href="https://maps.google.com/?q=1502+Vine+Street,+Cincinnati,+OH+45202" target="_blank" rel="noopener" class="link">Directions{ARROW}</a></p>
    <p class="muted" style="font-size:14px">Zoning verification letters and opinions: <a href="/zoning-letters/" style="border-bottom:1px solid var(--brass)">learn more</a>.</p>
  </div>
  <div>
    <form class="form" name="contact" method="POST" action="/thanks/" data-netlify="true" data-ok="form-ok" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="contact">
      <p class="hp"><label>Don't fill this out: <input name="bot-field"></label></p>
      <div class="two"><div><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div><div><label for="company">Company</label><input id="company" name="company" autocomplete="organization"></div></div>
      <div class="two"><div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div><div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div></div>
      <div><label for="matter">What can we help with?</label><select id="matter" name="matter"><option>Land use &amp; zoning</option><option>Real property litigation &amp; appeals</option><option>Real estate transaction</option><option>Eminent domain / takings</option><option>Historic preservation</option><option>Real estate taxation</option><option>Local counsel / co-counsel</option><option>Zoning verification letter or opinion</option><option>Other</option></select></div>
      <div><label for="message">Message</label><textarea id="message" name="message" required placeholder="Property address, jurisdiction, and a short description of the situation. No confidential details yet, please."></textarea></div>
      <div class="note">Submitting this form does not create an attorney-client relationship. See our <a href="/terms/" style="text-decoration:underline">terms of use</a>.</div>
      <div><button class="btn btn-primary" type="submit">Send message{ARROW}</button></div>
    </form>
    <div class="form-ok" id="form-ok"><b>Thank you.</b> Your message is on its way. We will be in touch shortly.</div>
  </div>
</div></section>'''
    write("/contact/", page("Contact", "Contact Suder, LLC, Counsel for the Built Environment, at 1502 Vine Street, Cincinnati, Ohio. 513.694.7500.", body, "/contact/", dark_hero=False))
    write("/thanks/", page("Thank you", "Your message has been received.", '<section class="page-head"><div class="wrap-narrow"><div class="eyebrow">Message received</div><h1>Thank you.</h1><p class="lede">We will be in touch shortly.</p><p>' + btn("/", "Back to home", "outline") + '</p></div></section>', "/thanks/", dark_hero=False))

def build_misc():
    write("/careers/", page("Careers", "Career opportunities at Suder, LLC.", f'''<section class="page-head"><div class="wrap-narrow"><div class="eyebrow">Careers</div><h1>Build a career on the built environment.</h1><p class="lede">No open positions at this time.</p><p>Suder, LLC is an equal opportunity employer, and we welcome attorneys and planners of all backgrounds. If you think you belong here, tell us why at <a href="mailto:{FIRM["email"]}" style="border-bottom:1px solid var(--brass)">{FIRM["email"]}</a>.</p></div></section>''', "/careers/", dark_hero=False))
    terms = (ROOT / "src" / "terms.txt").read_text(encoding="utf-8")
    th = ""
    for block in terms.strip().split("\n\n"):
        if block.startswith("## "): th += f"<h2>{esc(block[3:])}</h2>"
        else: th += f"<p>{esc(block)}</p>"
    credits = "".join(f'<li>{esc(t_)} by {esc(a)} (<a href="{lu}" rel="noopener" target="_blank" style="text-decoration:underline">{esc(l)}</a>), <a href="{pg}" rel="noopener" target="_blank" style="text-decoration:underline">via Wikimedia Commons</a></li>' for f, t_, a, l, lu, pg in PHOTO_CREDITS)
    th += f'<h2 id="photo-credits">Photo credits</h2><p>Photographs of Cincinnati, Cleveland, and Austin landmarks are used under Creative Commons licenses and are credited here with thanks:</p><ul style="font-size:14px">{credits}</ul>'
    write("/terms/", page("Terms of Use", "Terms of use for the Suder, LLC website.", f'<section class="page-head"><div class="wrap-narrow"><div class="eyebrow">Terms of use</div><h1>Terms of use.</h1></div></section><section style="padding-top:0"><div class="wrap-narrow prose">{th}</div></section>', "/terms/", dark_hero=False))
    write("/404.html", page("Page not found", "Page not found.", f'<section class="page-head"><div class="wrap-narrow"><div class="eyebrow">404</div><h1>That page moved, or never existed.</h1><p class="lede">Try the practice areas, results, or team pages, or head home.</p><p>{btn("/", "Back to home")}</p></div></section>', "/404.html", dark_hero=False))

def build_infra():
    # redirects, netlify.toml, robots, sitemap, favicon
    lines = [f"{a}  {b}  301" for a, b in REDIRECTS]
    (PUB / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "netlify.toml").write_text('''[build]
  publish = "public"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
''', encoding="utf-8")
    (PUB / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {FIRM['domain']}/sitemap.xml\n", encoding="utf-8")
    urls = ["/", "/results/", "/opinions/", "/jurisdictions/", "/zoning-letters/", "/team/", "/contact/", "/careers/", "/terms/"] + [f"/practice/{s}/" for s, _ in PRACTICES] + [f"/team/{t['slug']}/" for t in TEAM]
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{FIRM['domain']}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    (PUB / "sitemap.xml").write_text(sm, encoding="utf-8")
    (PUB / "assets/img/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#15243b"/><text x="32" y="45" text-anchor="middle" font-family="Georgia,serif" font-size="40" fill="#f5f2ec">S</text><rect x="14" y="50" width="36" height="3" fill="#b9924a"/></svg>', encoding="utf-8")

if __name__ == "__main__":
    for d in ["practice", "team", "results", "opinions", "jurisdictions", "zoning-letters", "contact", "thanks", "careers", "terms"]:
        shutil.rmtree(PUB / d, ignore_errors=True)
    build_home(); build_practices(); build_results(); build_opinions(); build_jurisdictions(); build_zoning_letters(); build_team(); build_contact(); build_misc(); build_infra()
    n = sum(1 for _ in PUB.rglob("*.html"))
    print("built", n, "pages")
