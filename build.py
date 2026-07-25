# -*- coding: utf-8 -*-
"""
Builds the MLF 1.0 site into dist/.

    python build.py

English at the root, Traditional Chinese under /zh/. Both trees come from the
same block list per page in src/content.py; the build fails if a page is
missing from either language.
"""

from __future__ import annotations

import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import content as C  # noqa: E402

DIST = ROOT / "dist"

FONTS_BASE = (
    "https://fonts.googleapis.com/css2"
    "?family=Archivo:wdth,wght@75..125,400;75..125,600;75..125,700"
    "&family=Zilla+Slab:ital,wght@0,400;0,500;0,700;1,400"
    "&family=Azeret+Mono:wght@400;500;600"
)
FONTS_ZH = "&family=Noto+Sans+TC:wght@500;700&family=Noto+Serif+TC:wght@400;500"


def url_path(lang, slug):
    base = "/" if lang == "en" else "/zh/"
    return base if not slug else f"{base}{slug}/"


def out_file(lang, slug):
    rel = url_path(lang, slug).strip("/")
    return DIST / rel / "index.html" if rel else DIST / "index.html"


# --------------------------------------------------------------------------
# blocks
# --------------------------------------------------------------------------

def r_h2(text, anchor):
    return f'<h2 class="h2" id="{anchor}">{text}</h2>'


def r_p(text):
    return f'<p class="p">{text}</p>'


def r_quote(text):
    return f'<blockquote class="quote">{text}</blockquote>'


def r_bullets(items, extra=""):
    cls = "list" + (f" {extra}" if extra else "")
    return f'<ul class="{cls}">{"".join(f"<li>{i}</li>" for i in items)}</ul>'


def r_reg(headers, rows, zero_cls, zero_row):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = ["<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows]
    if zero_row:
        cells = "".join(f"<td>{c}</td>" for c in zero_row)
        pad = len(headers) - len(zero_row)
        if pad > 0:
            cells += "<td></td>" * pad
        body.append(f'<tr class="reg-{zero_cls}">{cells}</tr>')
    return (
        '<div class="reg-wrap"><table class="reg">'
        f'<thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'
    )


STAMP_MARK = {
    "en": {
        "verified": "verified", "structural": "structural",
        "content": "content", "semantic": "semantic", "presentation": "presentation",
    },
    "zh": {
        "verified": "已驗證", "structural": "結構",
        "content": "內容", "semantic": "語意", "presentation": "呈現",
    },
}


def r_stamp(lang, state, text):
    return (
        f'<div class="stamp" data-state="{state}">'
        f'<span class="stamp-mark">{STAMP_MARK[lang][state]}</span>'
        f'<p class="stamp-text">{text}</p></div>'
    )


def r_defs(rows):
    out = "".join(
        f'<div class="defs-row"><dt class="defs-term">{t}</dt>'
        f'<dd class="defs-desc">{d}</dd></div>' for t, d in rows
    )
    return f'<dl class="defs">{out}</dl>'


def r_code(tag, text):
    return (
        f'<div class="code"><div class="code-tag">{tag}</div>'
        f"<pre><code>{html.escape(text)}</code></pre></div>"
    )


def r_isnt_list(pairs):
    items = "".join(
        '<li><div class="isnt">'
        f'<span class="isnt-a">{a}</span>'
        '<span class="isnt-op" aria-hidden="true">&#8800;</span>'
        f'<span class="isnt-b">{b}</span></div></li>'
        for a, b in pairs
    )
    return f'<ul class="isnt-list">{items}</ul>'


def r_fplist(lang):
    t = C.FP_TEXT[lang]
    rows = "".join(
        f'<li class="fprow" style="--tone: var(--fp-{k})">'
        f'<span class="fpname">{t["labels"][k]}</span>'
        f'<p class="fpdef">{t["defs"][k]}</p></li>'
        for k in C.FP_KEYS
    )
    return f'<ul class="fplist">{rows}</ul>'


def r_layers(lang):
    tag = {"en": "stable format", "zh": "穩定格式"}[lang]
    rows = "".join(
        '<li data-stable="{s}"><span class="layers-l">{l}</span>'
        '<span class="layers-w">{w}</span>'
        '<span class="layers-tag">{t}</span></li>'.format(
            s="true" if l in C.LAYERS_STABLE else "false",
            l=l, w=w, t=tag if l in C.LAYERS_STABLE else "",
        )
        for l, w in C.LAYERS[lang]
    )
    return (
        f'<ul class="layers">{rows}</ul>'
        f'<p class="layers-note">{C.LAYERS_NOTE[lang]}</p>'
    )


def render_blocks(blocks, lang):
    out = []
    for b in blocks:
        k = b[0]
        if k == "h2":
            out.append(r_h2(b[1], b[2]))
        elif k == "p":
            out.append(r_p(b[1]))
        elif k == "quote":
            out.append(r_quote(b[1]))
        elif k == "bullets":
            out.append(r_bullets(b[1]))
        elif k == "refuse_list":
            out.append(r_bullets(b[1], "list-refuse"))
        elif k == "reg":
            out.append(r_reg(b[1], b[2], b[3], b[4]))
        elif k == "stamp":
            out.append(r_stamp(lang, b[1], b[2]))
        elif k == "defs":
            out.append(r_defs(b[1]))
        elif k == "code":
            out.append(r_code(b[1], b[2]))
        elif k == "isnt_list":
            out.append(r_isnt_list(b[1]))
        elif k == "fplist":
            out.append(r_fplist(lang))
        elif k == "layers":
            out.append(r_layers(lang))
        else:
            raise ValueError(f"unknown block: {k}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# hero
# --------------------------------------------------------------------------

def render_anatomy(lang):
    t = C.FP_TEXT[lang]
    members = C.ANATOMY[lang]
    first = members[0]

    rows = []
    for n, m in enumerate(members):
        chips = "".join(f'<span class="chip" data-fp="{k}"></span>' for k in m["fp"])
        rows.append(
            f'<li><button class="tree-row" type="button" data-row '
            f'aria-selected="{"true" if n == 0 else "false"}">'
            f'<span class="tree-path">{html.escape(m["path"])}</span>'
            f'<span class="chips">{chips}</span></button></li>'
        )

    labels = json.dumps(t["labels"], ensure_ascii=False)

    return f"""<section class="anatomy" data-anatomy data-labels='{labels}' aria-label="{t['select']}">
  <ul class="tree">{''.join(rows)}</ul>
  <div class="anatomy-panel" aria-live="polite">
    <p class="panel-path" data-panel-path>{html.escape(first['path'])}</p>
    <p class="panel-what" data-panel-what>{html.escape(first['what'])}</p>
    <div class="panel-feeds">
      <span class="panel-label">{t['feeds']}</span>
      <ul class="feeds" data-feeds hidden></ul>
      <p class="feeds-none" data-feeds-none>{t['feeds_none']}</p>
    </div>
  </div>
</section>
<p class="anatomy-caption">{t['caption']}</p>"""


def anatomy_data(lang):
    return (
        '<script type="application/json" id="anatomy-data">'
        + json.dumps(C.ANATOMY[lang], ensure_ascii=False)
        + "</script>"
    )


# --------------------------------------------------------------------------
# shell
# --------------------------------------------------------------------------

THEME_BOOT = (
    "<script>(function(){try{var t=localStorage.getItem('mlf-theme');"
    "if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t);}}"
    "catch(e){}})();</script>"
)

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" fill="#14161a"/>
<rect x="5" y="6" width="9" height="9" fill="#5cc6d6"/>
<rect x="18" y="6" width="9" height="9" fill="#ee8f61"/>
<rect x="5" y="18" width="9" height="9" fill="#ab93e8"/>
<rect x="18" y="18" width="9" height="9" fill="#dcc463"/>
</svg>
"""


def render_page(lang, slug):
    page = C.PAGES[lang][slug]
    chrome = C.CHROME[lang]
    other = "zh" if lang == "en" else "en"

    here = C.SITE["origin"] + url_path(lang, slug)
    there = url_path(other, slug)

    nav = "".join(
        '<a class="plate-link" href="{h}"{c}>{l}</a>'.format(
            h=url_path(lang, s), l=label,
            c=' aria-current="page"' if s == slug else "",
        )
        for s, label in chrome["nav"]
    )

    items = [(b[2], b[1]) for b in page["blocks"] if b[0] == "h2"]
    index = ""
    if items:
        links = "".join(
            f'<a class="index-link" data-index-link href="#{a}">{l}</a>' for a, l in items
        )
        index = (
            f'<nav class="index" aria-label="{chrome["on_this_page"]}">'
            f'<span class="index-label">{chrome["on_this_page"]}</span>{links}</nav>'
        )

    hero = data = ""
    if page.get("hero") == "anatomy":
        hero = render_anatomy(lang)
        data = anatomy_data(lang)

    fonts = FONTS_BASE + (FONTS_ZH if lang == "zh" else "") + "&display=swap"

    jsonld = {
        "@context": "https://schema.org",
        "@type": "SoftwareSourceCode",
        "name": "MLF — AI Matrix Ledger Format",
        "version": C.SITE["compiler"],
        "codeRepository": C.SITE["repo"],
        "programmingLanguage": "Python",
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "url": here,
        "description": page["description"],
        "inLanguage": chrome["lang"],
        "author": {"@type": "Organization", "name": "EveMissLab", "url": C.SITE["lab"]},
    }

    return f"""<!doctype html>
<html lang="{chrome['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page['meta_title'])}</title>
<meta name="description" content="{html.escape(page['description'])}">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{C.SITE['origin'] + url_path('en', slug)}">
<link rel="alternate" hreflang="zh-Hant" href="{C.SITE['origin'] + url_path('zh', slug)}">
<link rel="alternate" hreflang="x-default" href="{C.SITE['origin'] + url_path('en', slug)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MLF">
<meta property="og:title" content="{html.escape(page['meta_title'])}">
<meta property="og:description" content="{html.escape(page['description'])}">
<meta property="og:url" content="{here}">
<meta property="og:locale" content="{'zh_TW' if lang == 'zh' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if lang == 'zh' else 'zh_TW'}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#14161a" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f2f1ee" media="(prefers-color-scheme: light)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="/assets/styles.css">
{THEME_BOOT}
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{chrome['skip']}</a>

<header class="plate">
  <div class="plate-in">
    <a class="plate-mark" href="{url_path(lang, '')}">MLF
      <span class="plate-ver">{C.SITE['spec']} &middot; {C.SITE['cli']} {C.SITE['compiler']}</span></a>
    <nav class="plate-nav" aria-label="MLF">{nav}</nav>
    <div class="plate-tools">
      <a class="plate-btn" href="{there}" hreflang="{'zh-Hant' if other == 'zh' else 'en'}" title="{chrome['lang_switch_title']}">{chrome['lang_switch']}</a>
      <button class="plate-btn" type="button" data-theme-toggle aria-label="{chrome['theme']}">&#9681;</button>
    </div>
  </div>
</header>

<main id="main">
  <div class="shell">
    <div class="mast">
      <p class="mast-eyebrow">{html.escape(page['title'])}</p>
      <h1 class="mast-display">{page['display']}</h1>
      <p class="mast-stand">{page['standfirst']}</p>
    </div>
    {hero}
  </div>

  <div class="shell body">
    {index}
    <div class="flow">
{render_blocks(page['blocks'], lang)}
    </div>
  </div>
</main>

<footer class="foot">
  <div class="shell foot-grid">
    <p class="foot-note">{chrome['footer_note']}</p>
    <div class="foot-meta">
      <span class="foot-line">MLF {C.SITE['spec']} &middot; {C.SITE['cli']} {C.SITE['compiler']} &middot; {chrome['footer_release']} {C.SITE['release_date']}</span>
      <span class="foot-line">{C.SITE['licence']}</span>
      <span class="foot-line"><a href="{C.SITE['repo']}" rel="noopener">{chrome['repo_link']}</a></span>
      <span class="foot-line"><a href="{C.SITE['lab']}" rel="noopener">{chrome['footer_lab']}</a></span>
    </div>
  </div>
</footer>

{data}
<script src="/assets/app.js" defer></script>
</body>
</html>
"""


def render_404():
    chrome = C.CHROME["en"]
    fonts = FONTS_BASE + "&display=swap"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Not found — MLF</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="/assets/styles.css">
{THEME_BOOT}
</head>
<body>
<header class="plate"><div class="plate-in">
  <a class="plate-mark" href="/">MLF <span class="plate-ver">{C.SITE['spec']}</span></a>
</div></header>
<main class="shell gone">
  <p class="mast-eyebrow">404</p>
  <h1 class="mast-display">No record at this path.</h1>
  <p class="mast-stand">The manifest does not select anything here.
    Start from the <a href="/">overview</a>, or read the
    <a href="/limits/">limits</a>.</p>
</main>
<footer class="foot"><div class="shell foot-grid">
  <p class="foot-note">{chrome['footer_note']}</p>
</div></footer>
</body>
</html>
"""


def render_sitemap():
    urls = []
    for lang in ("en", "zh"):
        for slug in C.SLUGS:
            loc = C.SITE["origin"] + url_path(lang, slug)
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{h}" '
                f'href="{C.SITE["origin"] + url_path(l, slug)}"/>'
                for h, l in (("en", "en"), ("zh-Hant", "zh"), ("x-default", "en"))
            )
            urls.append(
                f"<url><loc>{loc}</loc><lastmod>{C.SITE['release_date']}</lastmod>{alts}</url>"
            )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(urls) + "</urlset>\n"
    )


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    n = 0
    for lang in ("en", "zh"):
        for slug in C.SLUGS:
            if slug not in C.PAGES[lang]:
                raise SystemExit(f"missing page: {lang}/{slug or 'index'}")
            target = out_file(lang, slug)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_page(lang, slug), encoding="utf-8")
            n += 1

    assets = DIST / "assets"
    assets.mkdir()
    for name in ("styles.css", "app.js"):
        shutil.copyfile(ROOT / "src" / "assets" / name, assets / name)

    (DIST / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (DIST / "404.html").write_text(render_404(), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(render_sitemap(), encoding="utf-8")
    (DIST / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {C.SITE['origin']}/sitemap.xml\n",
        encoding="utf-8",
    )

    print(f"built {n} pages into {DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
