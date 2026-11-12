"""Build the Atrium Intelligence website.

    python build.py            # writes the finished site into ./dist
    python build.py --serve    # builds, then serves it at http://localhost:8000

The site is plain HTML/CSS generated from Python (content.py + Jinja2 templates),
so it can be hosted free on GitHub Pages, Netlify or Cloudflare Pages.
"""

from __future__ import annotations

import shutil
import sys
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
DOMAIN = "www.atriumintelligence.net"


def atrium_plan_svg(rooms: list[str]) -> str:
    """Draw the hero floor plan: six rooms that all open onto a central atrium."""
    o0, o1 = 40, 560     # outer walls
    i0, i1 = 200, 400    # atrium walls
    door = 34            # doorway width
    mid = 300

    def gap_h(y, centers):   # horizontal inner wall with doorway gaps
        xs = [i0] + [v for c in centers for v in (c - door / 2, c + door / 2)] + [i1]
        return " ".join(f"M{xs[k]:.0f} {y} H{xs[k + 1]:.0f}" for k in range(0, len(xs), 2))

    def gap_v(x, centers):
        ys = [i0] + [v for c in centers for v in (c - door / 2, c + door / 2)] + [i1]
        return " ".join(f"M{x} {ys[k]:.0f} V{ys[k + 1]:.0f}" for k in range(0, len(ys), 2))

    outer = f"M{o0} {o0} H{o1} V{o1} H{o0} Z"
    partitions = (f"M{o0} {o0} L{i0} {i0} M{o1} {o0} L{i1} {i0} M{o1} {o1} L{i1} {i1} M{o0} {o1} L{i0} {i1} "
                  f"M{mid} {o0} V{i0} M{mid} {i1} V{o1}")
    inner = " ".join([gap_h(i0, [250, 350]), gap_v(i1, [mid]), gap_h(i1, [250, 350]), gap_v(i0, [mid])])

    labels = [(215, 118), (385, 118), (482, 300), (385, 486), (215, 486), (118, 300)]
    names = (rooms + [""] * 6)[:6]
    # top-left, top-right, right, bottom-right, bottom-left, left
    order = [names[0], names[1], names[2], names[3], names[4], names[5]]

    def label(x, y, text):
        words = text.split(" ")
        if len(text) > 12 and len(words) > 1:
            half = (len(words) + 1) // 2
            lines = [" ".join(words[:half]), " ".join(words[half:])]
        else:
            lines = [text]
        dy0 = -(len(lines) - 1) * 11
        spans = "".join(f'<tspan x="{x}" dy="{dy0 if n == 0 else 22}">{ln}</tspan>' for n, ln in enumerate(lines))
        return f'<text class="room" x="{x}" y="{y}">{spans}</text>'

    arrows = []
    for (cx, cy, dx, dy) in [(250, 182, 0, 1), (350, 182, 0, 1), (418, 300, -1, 0),
                             (350, 418, 0, -1), (250, 418, 0, -1), (182, 300, 1, 0)]:
        x2, y2 = cx + dx * 26, cy + dy * 26
        arrows.append(f'<path class="flow" d="M{cx} {cy} L{x2} {y2}"/>')

    return f"""<svg class="plan" viewBox="0 0 600 600" role="img"
  aria-label="Floor plan: six rooms ({', '.join(rooms)}) all open onto a central atrium labelled One dashboard.">
  <defs>
    <pattern id="rays" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="14" height="14" class="sky"/>
      <line x1="0" y1="0" x2="0" y2="14" class="ray"/>
    </pattern>
  </defs>
  <rect class="atrium" x="{i0}" y="{i0}" width="{i1 - i0}" height="{i1 - i0}" fill="url(#rays)"/>
  <text class="atrium-label" x="{mid}" y="{mid - 6}">One</text>
  <text class="atrium-label" x="{mid}" y="{mid + 22}">dashboard</text>
  <path class="wall wall-outer" pathLength="1" d="{outer}"/>
  <path class="wall" pathLength="1" d="{partitions}"/>
  <path class="wall wall-inner" pathLength="1" d="{inner}"/>
  {''.join(arrows)}
  {''.join(label(x, y, t) for (x, y), t in zip(labels, order))}
</svg>"""


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST / "static")

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
    ctx = {k: getattr(content, k) for k in dir(content) if k.isupper()}
    ctx["plan_svg"] = atrium_plan_svg(content.PLAN_ROOMS)
    ctx["year"] = date.today().year

    pages = {"index.html": "Home", "demo.html": "Live demo", "contact.html": "Contact"}
    for page, title in pages.items():
        html = env.get_template(page).render(page=page, title=title, **ctx)
        (DIST / page).write_text(html, encoding="utf-8")

    (DIST / "CNAME").write_text(DOMAIN + "\n")     # custom domain for GitHub Pages
    (DIST / ".nojekyll").write_text("")
    urls = "".join(f"<url><loc>https://{DOMAIN}/{p if p != 'index.html' else ''}</loc></url>" for p in pages)
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
    print(f"Built {len(pages)} pages into {DIST}")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
        print("Serving at http://localhost:8000  (Ctrl+C to stop)")
        http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()
