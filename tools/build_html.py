#!/usr/bin/env python3
"""Build navigable HTML pages from the roadmap markdown.

Usage (from the repo root):  python3 tools/build_html.py

Reads  ROADMAP.md and tracks/*.md,  writes  html/index.html  and one page per track.
Each track page has a "Next ride" panel (the next two unwatched videos), a snake diagram of the
blocks in dependency order, and the ordered video lists. Progress is kept in the browser.
Re-run this script after any change to the markdown.
"""
import html
import pathlib
import re
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "html"

TRACKS = [
    ("A", "A-ai-math", "AI math", "Math"),
    ("B", "B-ai-ml-concepts", "AI and ML concepts", "AI and ML"),
    ("C", "C-genai-stack", "The GenAI stack and enterprise architecture", "GenAI stack"),
    ("D", "D-tech-stack-bike", "Enterprise tech stack foundations (bike path)", "Tech stack, bike", "bike"),
    ("E", "E-tech-stack-desk", "Enterprise tech stack hands-on (desk path)", "Tech stack, desk", "desk"),
    ("F", "F-ut-courses", "UT Austin MSAI course tracker", "UT courses"),
    ("G", "G-genai-end-to-end", "End-to-end GenAI: from data to a governed production system", "End-to-end GenAI"),
    ("H", "H-genai-build-projects", "Build GenAI projects, one layer at a time", "Build projects", "desk"),
]

# Short labels for the block diagram where the heading is too long for a box.
SHORT_NAMES = {
    "C": {0: "Big picture", 1: "LLMs for architects", 2: "Prompting and structured outputs",
          3: "Embeddings, vector search and RAG", 4: "Agents and tools",
          5: "Evaluation and observability", 6: "Safety, security and governance",
          7: "Customization and serving", 8: "AWS GenAI", 9: "Enterprise architecture at scale"},
    "D": {0: "Stack map", 1: "Distributed systems", 2: "The data layer", 3: "APIs and messaging",
          4: "Cloud-native platform", 5: "Security and identity", 6: "Reliability and observability",
          7: "Data and ML platform", 8: "Architecture judgment"},
    "F": {1: "Machine Learning", 2: "Deep Learning", 3: "Reinforcement Learning", 4: "Planning and search",
          5: "Ethics in AI", 6: "Natural Language Processing", 7: "Advances in Deep Learning",
          8: "Deep Generative Models", 9: "Case Studies in ML", 10: "Optimization",
          11: "Online learning", 12: "Logical reasoning", 13: "AI in Healthcare", 14: "AI in Astrophysics", 15: "Agentic software engineering"},
    "G": {0: "The build map", 1: "Language-model basics", 2: "Pretraining", 3: "Post-training",
          4: "Adaptation", 5: "Inference and serving", 6: "Grounding and RAG", 7: "Agents and tools",
          8: "Multimodal and diffusion", 9: "Evaluation", 10: "Safety and governance",
          11: "LLMOps and platform", 12: "Capstone designs"},
    "H": {0: "The map", 1: "First LLM call", 2: "Terminal chatbot", 3: "Prompts and structured output",
          4: "Chat web UI", 5: "Your own API", 6: "Local models", 7: "Embeddings and search", 8: "RAG",
          9: "Containers", 10: "Database", 11: "Tool calling", 12: "Agents and MCP", 13: "Auth and gateway",
          14: "AWS foundations", 15: "Deploy to AWS", 16: "Internet edge", 17: "Amazon Bedrock",
          18: "Queues and caching", 19: "Tracing and evals", 20: "Guardrails", 21: "IaC and CI/CD", 22: "Capstone"},
    "E": {0: "Drawing systems", 1: "Data layer lab", 2: "APIs and messaging lab", 3: "Cloud-native lab",
          4: "Security and observability lab", 5: "Data and ML platform lab",
          6: "System-design walkthroughs", 7: "GenAI-era designs"},
}

# Where the rows from "Gap-fill pass 1" (Track C) are placed.
GAP_GROUPS = [
    (r"Prompting and structured", 2),
    (r"Tool and function", 2),
    (r"Prompt injection", 6),
    (r"Vector database", 3),
    (r"Token-cost", 7),
]

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print("WARNING:", msg, file=sys.stderr)


# ----------------------------------------------------------------------------- markdown helpers

_ITEM = re.compile(r"^([-*]|\d+\.)\s+\S")


def fix_lists(text):
    """Python-Markdown needs a blank line before a list. Our sources often put a
    list right under a bold label line, which would otherwise render as one
    run-on paragraph."""
    out, prev, in_code = [], "", False
    for ln in text.split("\n"):
        if ln.strip().startswith("```"):
            in_code = not in_code
        if (not in_code and _ITEM.match(ln) and prev.strip()
                and not _ITEM.match(prev) and not prev.startswith((" ", "|", "<"))):
            out.append("")
        out.append(ln)
        prev = ln
    return "\n".join(out)


def md(text):
    return markdown.markdown(fix_lists(text), extensions=["extra", "sane_lists"])


def md_inline(text):
    h = md(text).strip()
    m = re.fullmatch(r"<p>(.*)</p>", h, re.S)
    return m.group(1) if m else h


def external_links(h):
    return re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', h)


DETAILS = re.compile(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>", re.S)


def render_text(text):
    """Markdown to HTML, with <details> bodies rendered as markdown too."""
    stash = []

    def rep(m):
        stash.append((m.group(1).strip(), m.group(2).strip()))
        return "\n\nDETAILSTOKEN%dEND\n\n" % (len(stash) - 1)

    h = md(DETAILS.sub(rep, text))
    for i, (summary, body) in enumerate(stash):
        h = h.replace("<p>DETAILSTOKEN%dEND</p>" % i,
                      '<details class="answers"><summary>%s</summary>%s</details>' % (html.escape(summary), md(body)))
    return external_links(h)


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line)]


def split_segments(body):
    """Split markdown into ('text', str) and ('table', header, rows) pieces."""
    segs, buf, tab = [], [], []

    def flush_text():
        if buf and "".join(buf).strip():
            segs.append(("text", "\n".join(buf)))
        buf.clear()

    def flush_table():
        if not tab:
            return
        header = split_row(tab[0])
        rows = [split_row(l) for l in tab[1:] if not all(re.fullmatch(r":?-{2,}:?", c) for c in split_row(l) if c)]
        rows = [r for r in rows if any(r)]
        segs.append(("table", header, rows))
        tab.clear()

    for line in body.split("\n"):
        if line.lstrip().startswith("|"):
            if buf:
                flush_text()
            tab.append(line)
        else:
            if tab:
                flush_table()
            buf.append(line)
    flush_table()
    flush_text()
    return segs


def split_sections(lines, level):
    """Split a list of lines on headings of the given level ('## ' -> level 2)."""
    prefix = "#" * level + " "
    head, sections, cur = [], [], None
    for line in lines:
        if line.startswith(prefix):
            cur = [line[len(prefix):].strip(), []]
            sections.append(cur)
        elif cur is None:
            head.append(line)
        else:
            cur[1].append(line)
    return head, [(t, "\n".join(b).strip("\n")) for t, b in sections]


# ----------------------------------------------------------------------------- video rows

def youtube_id(url):
    m = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", url) or re.search(r"youtu\.be/([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None


def row_to_video(header, cells, in_block):
    if len(cells) != len(header):
        warn("row has %d cells, header has %d: %s" % (len(cells), len(header), cells[:3]))
        cells = (cells + [""] * len(header))[:len(header)]
    d = {h.strip().lower(): c for h, c in zip(header, cells)}
    um = re.search(r"https?://[^\s)|]+", d.get("link", ""))
    url = um.group(0) if um else ""
    vid = youtube_id(url)
    if not vid:
        warn("no video id in row %s" % d.get("#"))
    rid = d.get("#", "").strip()
    mode = d.get("mode", "").upper()
    return {
        "id": rid,
        "vid": vid or "",
        "url": url,
        "title": d.get("title", ""),
        "channel": d.get("channel", ""),
        "length": d.get("length", "").strip(),
        "published": d.get("published", "").strip(),
        "layer": d.get("layer", "").strip(),
        "level": d.get("level", "").strip(),
        "mode": "DESK" if "DESK" in mode else "BIKE",
        "why": d.get("what you will get", ""),
        "status": d.get("status", "").strip(),
        "main": bool(in_block and re.fullmatch(r"\d+(\.\d+)?", rid)),
        "added": False,
        "note": "",
    }


def video_li(v):
    meta = []
    if v["channel"]:
        meta.append('<span class="ch">%s</span>' % html.escape(v["channel"]))
    length = v["length"]
    if length and not length.lower().startswith("length ?"):
        meta.append('<span>%s</span>' % html.escape(length))
    if v["published"] and "?" not in v["published"]:
        meta.append('<span>Published %s</span>' % html.escape(v["published"]))
    if v["level"]:
        meta.append('<span>%s level</span>' % html.escape(v["level"]))
    if v["layer"]:
        meta.append('<span>Layer: %s</span>' % html.escape(v["layer"]))
    meta.append('<span class="pill %s">%s</span>' % ("desk" if v["mode"] == "DESK" else "bike",
                                                       "Desk" if v["mode"] == "DESK" else "Bike"))
    if v["added"]:
        meta.append('<span class="tag added">Added later</span>')
    if "unverified" in v["status"].lower():
        meta.append('<span class="tag warn">Not confirmed to exist</span>')
    meta.append('<span class="watched">Watched</span>')
    note = '<p class="vnote">Where it fits: %s</p>' % md_inline(v["note"]) if v["note"] else ""
    return (
        '<li class="video" data-vid="%(vid)s" data-main="%(main)d" data-desk="%(desk)d" id="v-%(vid)s">'
        '<label class="check"><input type="checkbox" aria-label="Mark as watched: %(title_attr)s"></label>'
        '<div class="vbody">'
        '<div class="vtitle"><span class="vnum">%(id)s</span> <a href="%(url)s" target="_blank" rel="noopener noreferrer">%(title)s</a></div>'
        '<div class="vmeta">%(meta)s</div>'
        '<p class="vwhy">%(why)s</p>%(note)s'
        '</div></li>'
    ) % {
        "vid": v["vid"], "main": 1 if v["main"] and not v.get("optional") else 0,
        "desk": 1 if v["mode"] == "DESK" else 0,
        "title_attr": html.escape(v["title"], quote=True), "id": html.escape(v["id"]),
        "url": html.escape(v["url"], quote=True), "title": html.escape(v["title"]),
        "meta": "".join(meta), "why": md_inline(v["why"]), "note": note,
    }


def render_table(header, rows):
    th = "".join("<th>%s</th>" % md_inline(h) for h in header)
    trs = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % md_inline(c) for c in r) for r in rows)
    return external_links('<div class="scroll"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, trs))


def render_layers(rows):
    items = "".join(
        '<li><span class="ln">%s</span><div><strong>%s</strong><span>%s</span></div></li>'
        % (html.escape(r[0]), html.escape(r[1]), md_inline(r[2])) for r in rows)
    return '<ol class="layers">%s</ol>' % items


# ----------------------------------------------------------------------------- sections

def clean_text(t):
    t = re.sub(r"(?im)^\s*Optional desk list[^\n]*\n?", "", t)
    return t


def render_generic(body, collect=None):
    """Sections without videos (or with video tables that go to the optional list)."""
    out, opt = [], []
    for seg in split_segments(body):
        if seg[0] == "text":
            t = clean_text(seg[1])
            if t.strip():
                out.append(render_text(t))
        else:
            header, rows = seg[1], seg[2]
            names = [h.lower() for h in header]
            if "link" in names:
                for r in rows:
                    v = row_to_video(header, r, in_block=False)
                    v["optional"] = True
                    opt.append(v)
            elif len(header) == 3 and names[1] == "layer":
                out.append(render_layers(rows))
            else:
                out.append(render_table(header, rows))
    return "".join(out), opt


def optional_details(videos, label):
    if not videos:
        return ""
    lis = "".join(video_li(v) for v in videos)
    return ('<details class="optional"><summary>%s (%d)</summary><ul class="videos">%s</ul></details>'
            % (html.escape(label), len(videos), lis))


def render_block(num, title, body, added):
    main, opt, pieces, placed = [], [], [], False
    for seg in split_segments(body):
        if seg[0] == "text":
            t = clean_text(seg[1])
            if t.strip():
                pieces.append(("html", render_text(t)))
            continue
        header, rows = seg[1], seg[2]
        if "link" not in [h.lower() for h in header]:
            pieces.append(("html", render_table(header, rows)))
            continue
        if not placed:
            pieces.append(("videos", None))
            placed = True
        for r in rows:
            v = row_to_video(header, r, in_block=True)
            (main if v["main"] else opt).append(v)
    for v in added:
        v["optional"] = v["level"].lower() == "scholar"
        v["main"] = not v["optional"]
        if v["optional"]:
            opt.append(v)
        elif v["id"] == "G1" and CUR_TRACK[0] == "C":
            main.insert(0, v)
        else:
            am = re.search(r"Belongs after #(\d+(?:\.\d+)?)", v["note"])
            pos = None
            if am:   # place it right after the numbered video its note names
                idx = [i for i, m_ in enumerate(main) if m_["id"] == am.group(1)]
                if idx:
                    pos = idx[0] + 1
                    while pos < len(main) and main[pos]["added"] and re.search(
                            r"Belongs after #%s(?![\d.])" % re.escape(am.group(1)), main[pos]["note"]):
                        pos += 1
            if pos is None:
                main.append(v)
            else:
                main.insert(pos, v)
    seen_notes = set()   # a group's "where it fits" note is shown once, on its first row
    for v in main + opt:
        if v["added"] and v["note"]:
            if v["note"] in seen_notes:
                v["note"] = ""
            else:
                seen_notes.add(v["note"])
    counted = main
    bike = [v for v in main if v["mode"] != "DESK"]
    out = []
    for kind, payload in pieces:
        if kind == "html":
            out.append(payload)
        else:
            out.append('<ul class="videos">%s</ul>' % "".join(video_li(v) for v in main))
            out.append(optional_details(opt, "Optional videos for this block"))
    short = SHORT_NAMES.get(CUR_TRACK[0], {}).get(num) or re.sub(r"\s*\(.*$", "", title).strip()
    heading = "Block %d: %s" % (num, title)
    section = ('<section class="block" id="b%d" data-block="%d" data-short="%s"><h2>%s</h2>%s</section>'
               % (num, num, html.escape(short, quote=True), html.escape(heading), "".join(out)))
    return section, {"num": num, "short": short, "total": len(counted), "optional": len(opt),
                     "bike": len(bike), "desk": len(counted) - len(bike),
                     "vids": [v["vid"] for v in main + opt]}


CUR_TRACK = ["A"]


def chain_html(blocks, cols=4):
    items = []
    n = len(blocks)
    for i, b in enumerate(blocks):
        row, pos = divmod(i, cols)
        col = pos if row % 2 == 0 else cols - 1 - pos
        last_in_row = pos == cols - 1
        if i == n - 1:
            arrow = ""
        elif last_in_row:
            arrow = "down"
        else:
            arrow = "right" if row % 2 == 0 else "left"
        items.append(
            '<li class="%s" style="--c:%d;--r:%d"><a href="#b%d" id="chain-%d">'
            '<span class="cn">Block %d</span><span class="cname">%s</span>'
            '<span class="ccount"><span class="cdone">0</span> of %d watched</span>'
            '<span class="bar"><i></i></span></a></li>'
            % (("to-" + arrow) if arrow else "", col + 1, row + 1, b["num"], b["num"], b["num"],
               html.escape(b["short"]), b["total"]))
    return ('<ol class="chain" aria-label="Blocks in the order to watch them; each block builds on the one before">%s</ol>'
            % "".join(items))


# ----------------------------------------------------------------------------- page chrome

CSS = r"""
:root{
  --bg:#F2F5F8; --panel:#FFFFFF; --ink:#12202D; --muted:#4F6071; --line:#CBD6E0;
  --accent:#0A5FC4; --accent-ink:#FFFFFF; --done:#1C7A4B; --warn:#8F5200; --tint:#E6EFF9;
  --body:"Atkinson Hyperlegible","Segoe UI",system-ui,-apple-system,sans-serif;
  --head:"Bricolage Grotesque","Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0E1621; --panel:#152131; --ink:#E9EFF5; --muted:#A3B5C6; --line:#28394C;
    --accent:#6BB8FF; --accent-ink:#06121E; --done:#6FD09A; --warn:#F0B45A; --tint:#16293D;
  }
}
:root[data-theme="dark"]{
  --bg:#0E1621; --panel:#152131; --ink:#E9EFF5; --muted:#A3B5C6; --line:#28394C;
  --accent:#6BB8FF; --accent-ink:#06121E; --done:#6FD09A; --warn:#F0B45A; --tint:#16293D;
}
*{box-sizing:border-box}
html{font-size:19px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);line-height:1.55;overflow-wrap:anywhere}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-999px}
.skip:focus{left:12px;top:12px;background:var(--accent);color:var(--accent-ink);padding:8px 14px;border-radius:6px;z-index:10}
a{color:var(--accent);text-underline-offset:3px}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px;border-radius:4px}
.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
.topbar{display:flex;align-items:center;gap:6px 18px;flex-wrap:wrap;min-height:56px;padding-top:6px;padding-bottom:6px}
.brand{font-family:var(--head);font-weight:800;font-size:1.05rem;color:var(--ink);text-decoration:none;margin-right:auto}
.top nav{display:flex;flex-wrap:wrap;gap:2px 6px}
.top nav a{display:inline-flex;align-items:center;min-height:44px;padding:0 12px;color:var(--ink);text-decoration:none;border-radius:8px;font-weight:700;font-size:.92rem}
.top nav a[aria-current="page"]{background:var(--tint);color:var(--accent);box-shadow:inset 0 -3px 0 var(--accent)}
.top nav a:hover{background:var(--tint)}
#theme{min-height:44px;padding:0 14px;border:2px solid var(--line);background:transparent;color:var(--ink);border-radius:8px;font:inherit;font-size:.9rem;cursor:pointer}
h1,h2,h3{font-family:var(--head);line-height:1.12;letter-spacing:-.01em;margin:0}
h1{font-size:clamp(2.1rem,5.2vw,3.3rem);font-weight:800;margin:36px 0 10px}
h2{font-size:clamp(1.55rem,3.4vw,2.05rem);font-weight:800;margin:0 0 14px}
h3{font-size:1.3rem;font-weight:700;margin:26px 0 8px}
p{margin:0 0 14px;max-width:72ch}
ul,ol{max-width:72ch}
.lede{font-size:1.12rem;color:var(--muted);max-width:60ch;margin-bottom:20px}
.overall{font-weight:700;margin:0 0 6px}
section{margin:44px 0}
section,.video{scroll-margin-top:76px}
.block{padding-top:6px}
#upnext-wrap{margin:24px 0 8px}
#upnext{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))}
.ride{background:var(--panel);border:3px solid var(--accent);border-radius:12px;padding:22px 22px 20px}
.ride .where{margin:0 0 6px;color:var(--muted);font-size:.9rem}
.ride h3{margin:0 0 8px;font-size:clamp(1.35rem,2.6vw,1.65rem)}
.ride h3 a{color:var(--ink);text-decoration:none}
.ride h3 a:hover{text-decoration:underline}
.ride .vwhy{margin:10px 0 16px}
.actions{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 20px;border-radius:8px;border:2px solid var(--accent);background:transparent;color:var(--accent);font:inherit;font-weight:700;text-decoration:none;cursor:pointer}
.btn.primary{background:var(--accent);color:var(--accent-ink)}
.empty{background:var(--panel);border:2px dashed var(--line);border-radius:12px;padding:20px}
.chain{list-style:none;margin:20px 0 0;padding:0;max-width:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:56px;row-gap:34px}
.chain li{grid-column:var(--c);grid-row:var(--r);position:relative}
.chain a{display:flex;flex-direction:column;gap:2px;height:100%;padding:14px 16px 16px;background:var(--panel);border:2px solid var(--line);border-radius:8px;color:var(--ink);text-decoration:none}
.chain a:hover{border-color:var(--accent)}
.cn{font-size:.85rem;color:var(--muted)}
.cname{font-family:var(--head);font-weight:700;font-size:1.08rem;line-height:1.2}
.ccount{font-size:.88rem;color:var(--muted);margin-top:4px}
.chain .bar{display:block;height:7px;border-radius:4px;background:var(--line);margin-top:10px;overflow:hidden}
.chain .bar i{display:block;height:100%;width:0;background:var(--done)}
.chain li::after{position:absolute;font-size:1.7rem;font-weight:700;color:var(--muted);line-height:1}
.chain li.to-right::after{content:"\2192";right:-44px;top:calc(50% - 14px)}
.chain li.to-left::after{content:"\2190";left:-44px;top:calc(50% - 14px)}
.chain li.to-down::after{content:"\2193";left:calc(50% - 8px);bottom:-30px}
.layers{list-style:none;margin:16px 0;padding:0;max-width:640px}
.layers li{display:grid;grid-template-columns:44px 1fr;gap:12px;padding:14px 0;border-top:1px solid var(--line);position:relative}
.layers li:not(:last-child)::after{content:"\2193";position:absolute;left:12px;bottom:-14px;background:var(--bg);color:var(--muted);font-weight:700;line-height:1;z-index:1}
.layers .ln{font-family:var(--head);font-weight:800;font-size:1.3rem;color:var(--accent)}
.layers strong{display:block;font-family:var(--head);font-size:1.1rem}
.layers span:not(.ln){color:var(--muted)}
.videos{list-style:none;padding:0;margin:8px 0 18px;max-width:none}
.video{display:grid;grid-template-columns:48px minmax(0,1fr);gap:10px;padding:18px 0;border-top:1px solid var(--line)}
.video:last-child{border-bottom:1px solid var(--line)}
.check{display:flex;align-items:flex-start;justify-content:center;padding-top:3px;cursor:pointer}
.check input{width:30px;height:30px;accent-color:var(--done);cursor:pointer;margin:0}
.vtitle{font-size:1.12rem;font-weight:700;line-height:1.3}
.vtitle a{color:var(--accent)}
.vnum{display:inline-block;min-width:2.4em;color:var(--muted);font-weight:400;font-size:.9rem}
.vmeta{display:flex;flex-wrap:wrap;gap:4px 18px;margin-top:4px;color:var(--muted);font-size:.88rem;align-items:center}
.pill{padding:0 11px;border:1.5px solid currentColor;border-radius:999px;font-weight:700;line-height:1.5}
.pill.desk{border-style:dashed}
.tag{padding:0 8px;border-radius:4px;font-weight:700}
.tag.added{background:var(--tint);color:var(--accent)}
.tag.warn{border:1.5px solid var(--warn);color:var(--warn)}
.watched{display:none;color:var(--done);font-weight:700}
.vwhy{margin:8px 0 0;max-width:68ch}
.vnote{margin:6px 0 0;color:var(--muted);font-size:.92rem}
.video.done .vtitle a{color:var(--muted)}
.video.done .watched{display:inline}
.video.done .vwhy{color:var(--muted)}
details{margin:14px 0}
summary{cursor:pointer;min-height:44px;display:flex;align-items:center;font-weight:700;color:var(--accent)}
.answers,.optional,.fold{background:var(--panel);border:2px solid var(--line);border-radius:8px;padding:0 18px}
.answers[open],.optional[open],.fold[open]{padding-bottom:10px}
.answers p,.answers li{max-width:68ch}
.optional .videos{margin-top:0}
.optional .video:first-child{border-top:0}
.scroll{overflow-x:auto;margin:14px 0}
table{border-collapse:collapse;min-width:100%;font-size:.92rem}
th,td{border-top:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}
th{font-family:var(--head);font-size:.95rem;border-top:0;border-bottom:2px solid var(--ink)}
.tracks{list-style:none;padding:0;margin:20px 0 0;max-width:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:16px}
.tracks a{display:block;height:100%;padding:18px 20px;background:var(--panel);border:2px solid var(--line);border-radius:8px;color:var(--ink);text-decoration:none}
.tracks a:hover{border-color:var(--accent)}
.tracks strong{display:block;font-family:var(--head);font-size:1.25rem;margin-bottom:4px}
.tracks span{color:var(--muted);font-size:.92rem}
code{font-size:.9em;background:var(--tint);padding:1px 5px;border-radius:4px}
hr{border:0;border-top:1px solid var(--line);margin:28px 0}
footer{margin:56px 0 40px;color:var(--muted);font-size:.9rem}
footer p{max-width:72ch}
@media (max-width:900px){
  .chain{grid-template-columns:1fr;row-gap:34px}
  .chain li{grid-column:1;grid-row:auto}
  .chain li.to-right::after,.chain li.to-left::after,.chain li.to-down::after{content:"\2193";left:calc(50% - 8px);right:auto;top:auto;bottom:-30px}
}
@media (max-width:560px){
  html{font-size:18px}
  .wrap{padding:0 16px}
  .top{position:static}
  .brand{order:1}
  #theme{order:2}
  .top nav{order:3;width:100%}
  .video{grid-template-columns:40px minmax(0,1fr)}
  .ride{padding:18px 16px}
}
@media (prefers-reduced-motion:no-preference){
  .chain .bar i{transition:width .3s ease}
}
"""

JS = r"""
(function () {
  var KEY = 'msai-watched', THEME = 'msai-theme';
  var watched = {};
  try { (JSON.parse(window.localStorage.getItem(KEY) || '[]') || []).forEach(function (i) { watched[i] = 1; }); } catch (e) {}
  function save() { try { window.localStorage.setItem(KEY, JSON.stringify(Object.keys(watched))); } catch (e) {} }

  try {
    var t = window.localStorage.getItem(THEME);
    if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
  } catch (e) {}
  var themeBtn = document.getElementById('theme');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var cur = document.documentElement.getAttribute('data-theme');
    if (!cur) cur = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
    var next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { window.localStorage.setItem(THEME, next); } catch (e) {}
  });

  var items = Array.prototype.slice.call(document.querySelectorAll('li.video'));
  if (!items.length) return;
  var upnext = document.getElementById('upnext');
  var overall = document.getElementById('overall');

  function isDone(li) { return !!watched[li.getAttribute('data-vid')]; }
  function setDone(li, on) {
    var id = li.getAttribute('data-vid');
    if (on) watched[id] = 1; else delete watched[id];
    save(); refresh();
  }
  items.forEach(function (li) {
    var cb = li.querySelector('input');
    cb.addEventListener('change', function () { setDone(li, cb.checked); });
  });

  function isMain(li) { return li.getAttribute('data-main') === '1'; }
  var wrapEl = document.getElementById('upnext-wrap');
  var deskTrack = !!wrapEl && wrapEl.getAttribute('data-mode') === 'desk';
  function isQueue(li) { return isMain(li) && (deskTrack || li.getAttribute('data-desk') === '0'); }

  function makeCard(li) {
    var sec = li.closest('section');
    var a = li.querySelector('.vtitle a');
    var card = document.createElement('article');
    card.className = 'ride';
    var where = document.createElement('p');
    where.className = 'where';
    where.textContent = (sec ? 'Block ' + sec.getAttribute('data-block') + ': ' + sec.getAttribute('data-short') : '') +
      ', video ' + li.querySelector('.vnum').textContent;
    var h3 = document.createElement('h3');
    var link = document.createElement('a');
    link.href = a.href; link.target = '_blank'; link.rel = 'noopener noreferrer';
    link.textContent = a.textContent;
    h3.appendChild(link);
    var meta = li.querySelector('.vmeta').cloneNode(true);
    var w = meta.querySelector('.watched'); if (w) w.remove();
    var why = document.createElement('p');
    why.className = 'vwhy';
    why.textContent = li.querySelector('.vwhy').textContent;
    var actions = document.createElement('div');
    actions.className = 'actions';
    var open = document.createElement('a');
    open.className = 'btn primary'; open.href = a.href; open.target = '_blank'; open.rel = 'noopener noreferrer';
    open.textContent = 'Open the video';
    var mark = document.createElement('button');
    mark.type = 'button'; mark.className = 'btn'; mark.textContent = 'Mark as watched';
    mark.addEventListener('click', function () { setDone(li, true); });
    var jump = document.createElement('a');
    jump.className = 'btn'; jump.href = '#' + li.id; jump.textContent = 'Show in the list';
    actions.appendChild(open); actions.appendChild(mark); actions.appendChild(jump);
    [where, h3, meta, why, actions].forEach(function (n) { card.appendChild(n); });
    return card;
  }

  function refresh() {
    items.forEach(function (li) {
      var on = isDone(li);
      li.classList.toggle('done', on);
      li.querySelector('input').checked = on;
    });
    var totalAll = 0, doneAll = 0;
    Array.prototype.forEach.call(document.querySelectorAll('[data-block]'), function (sec) {
      var n = sec.getAttribute('data-block');
      var rows = Array.prototype.filter.call(sec.querySelectorAll('li.video'), isMain);
      var done = rows.filter(isDone).length;
      totalAll += rows.length; doneAll += done;
      var chain = document.getElementById('chain-' + n);
      if (chain) {
        chain.querySelector('.cdone').textContent = done;
        chain.querySelector('.bar i').style.width = (rows.length ? Math.round(100 * done / rows.length) : 0) + '%';
      }
    });
    if (overall) overall.textContent = doneAll + ' of ' + totalAll + ' main-path videos watched in this track.';
    if (upnext) {
      upnext.textContent = '';
      var next = items.filter(function (li) { return isQueue(li) && !isDone(li); }).slice(0, 2);
      if (!next.length) {
        var e = document.createElement('div');
        e.className = 'empty';
        var deskLeft = items.filter(function (li) { return isMain(li) && !isDone(li); }).length;
        e.textContent = deskLeft
          ? 'Every bike video in this track is watched. ' + deskLeft + ' desk video' + (deskLeft === 1 ? ' is' : 's are') + ' left in the lists; save them for a desk session.'
          : 'Every main-path video in this track is marked as watched. Open the optional lists inside each block, or go on to the next track.';
        upnext.appendChild(e);
      } else {
        next.forEach(function (li) { upnext.appendChild(makeCard(li)); });
      }
    }
  }

  var reset = document.getElementById('reset');
  if (reset) {
    var armed = null;
    reset.addEventListener('click', function () {
      if (!armed) {
        reset.textContent = 'Press again to clear all watched marks';
        armed = setTimeout(function () { armed = null; reset.textContent = 'Clear watched marks'; }, 4000);
        return;
      }
      clearTimeout(armed); armed = null;
      watched = {}; save(); refresh(); reset.textContent = 'Clear watched marks';
    });
  }
  refresh();
})();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body>
<a class="skip" href="#main">Skip to the content</a>
<header class="top"><div class="wrap topbar">
<a class="brand" href="index.html">MSAI video plan</a>
<nav aria-label="Pages">__NAV__</nav>
<button id="theme" type="button" aria-label="Switch between light and dark colours">Light / dark</button>
</div></header>
<main id="main" class="wrap">
__BODY__
</main>
<footer class="wrap">__FOOTER__</footer>
<script>__JS__</script>
</body>
</html>
"""


def nav_html(current):
    items = [("index.html", "Roadmap", "index")] + [
        ("%s.html" % slug, "%s: %s" % (key, short), key) for key, slug, _, short, *_m in TRACKS]
    return "".join('<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if k == current else "", html.escape(label))
                   for href, label, k in items)


def page(title, desc, current, body, footer_extra=""):
    footer = (
        "<p>Every video was confirmed to exist with YouTube's embed lookup (title and channel copied as returned). "
        "None was watched by the person who compiled this list; each length was read from the video's YouTube page. "
        "Watched marks are kept in this browser; browsers that give each saved file its own storage will not carry them from one page to another.</p>"
        "%s"
        '<p><button id="reset" class="btn" type="button">Clear watched marks</button></p>' % footer_extra)
    return (PAGE.replace("__TITLE__", html.escape(title)).replace("__DESC__", html.escape(desc, quote=True))
            .replace("__CSS__", CSS).replace("__JS__", JS).replace("__NAV__", nav_html(current))
            .replace("__BODY__", body).replace("__FOOTER__", footer))


# ----------------------------------------------------------------------------- track pages

def build_track(key, slug, long_title, short, mode="bike"):
    CUR_TRACK[0] = key
    src = ROOT / "tracks" / (slug + ".md")
    lines = src.read_text(encoding="utf-8").split("\n")
    head, sections = split_sections(lines, 2)
    title_line = next((l for l in head if l.startswith("# ")), "# " + long_title)
    page_title = re.sub(r"^#\s*", "", title_line).strip()
    intro_md = "\n".join(l for l in head if not l.startswith("# ")).strip()

    # Gap-fill rows (Track C): placed into their blocks.
    gap_added, gap_notes, gap_intro = {}, [], ""
    for t, b in sections:
        if t.startswith("Gap-fill pass"):
            _, subs = split_sections(b.split("\n"), 3)
            pre, _s = split_sections(b.split("\n"), 3)
            gap_intro = "\n".join(pre).strip()
            for st, sb in subs:
                segs = split_segments(sb)
                tables = [s for s in segs if s[0] == "table" and "link" in [h.lower() for h in s[1]]]
                if not tables:
                    gap_notes.append((st, sb))
                    continue
                blk = next((n for pat, n in GAP_GROUPS if re.search(pat, st, re.I)), None)
                if blk is None:
                    mb = re.search(r"\(Block (\d+)", st)   # headings like "Sets (Block 7 gap)"
                    blk = int(mb.group(1)) if mb else None
                if blk is None:
                    warn("gap-fill group without block: " + st)
                    continue
                belongs = " ".join(l.strip() for l in sb.split("\n") if l.strip().startswith("Belongs after"))
                for s in tables:
                    for r in s[2]:
                        v = row_to_video(s[1], r, in_block=True)
                        v["added"] = True
                        v["note"] = belongs
                        gap_added.setdefault(blk, []).append(v)

    parts, blocks, extras, notes_html = [], [], [], []
    all_vids = []
    for t, b in sections:
        m = re.match(r"Block (\d+):\s*(.*)$", t)
        if m:
            num = int(m.group(1))
            sec_html, info = render_block(num, m.group(2).strip(), b, gap_added.get(num, []))
            parts.append(sec_html)
            blocks.append(info)
            all_vids += info["vids"]
        elif t.startswith("Gap-fill pass"):
            continue
        elif t in ("Gaps", "Not checked"):
            body_html, _ = render_generic(b)
            notes_html.append((t, body_html))
        elif t.startswith("Optional extras"):
            body_html, opt = render_generic(b)
            extras.append('<section><h2>%s</h2>%s%s</section>' % (html.escape(t), body_html, optional_details(opt, "Optional videos")))
            all_vids += [v["vid"] for v in opt]
        else:
            body_html, opt = render_generic(b)
            parts.append('<section><h2>%s</h2>%s%s</section>' % (html.escape(t), body_html, optional_details(opt, t)))
    # order: stack map etc. appear where they sat in the file
    total_main = sum(bk["total"] for bk in blocks)
    total_bike = sum(bk["bike"] for bk in blocks)
    total_desk = sum(bk["desk"] for bk in blocks)
    if not blocks:
        warn("no blocks in " + slug)

    notes = []
    for t, body_html in notes_html:
        if t == "Gaps":
            notes.append('<section><h2>Gaps: topics with no good video found</h2>%s</section>' % body_html)
    if gap_intro or gap_notes:
        inner = render_text(gap_intro) if gap_intro else ""
        for st, sb in gap_notes:
            inner += "<h3>%s</h3>%s" % (html.escape(st), render_text(sb))
        notes.append('<details class="fold"><summary>Added in the later gap-fill pass: how it was checked and what is still missing</summary>%s</details>' % inner)
    for t, body_html in notes_html:
        if t == "Not checked":
            notes.append('<details class="fold"><summary>Not checked: read before relying on the lists</summary>%s</details>' % body_html)

    # Stack map / intro-type sections come before Block 0 in file order, so parts already holds them in order.
    first_block = next((i for i, p in enumerate(parts) if p.startswith('<section class="block"')), 0)
    before, after = parts[:first_block], parts[first_block:]

    if mode == "desk":
        lede = ("%d main-path videos in %d blocks, in the order to watch them. These are for a desk session: "
                "you will pause, type, draw or run things. The next-session panel offers the next two unwatched videos." % (total_main, len(blocks)))
    else:
        lede = ("%d main-path videos in %d blocks, in the order to watch them: %d to watch on the bike%s. The next-ride panel only offers bike videos."
                % (total_main, len(blocks), total_bike,
                   (" and %d that need paper or pausing (marked Desk)" % total_desk) if total_desk else ""))
    hero = (
        '<h1>%s</h1>'
        '<p class="lede">%s</p>'
        '<p class="overall" id="overall" aria-live="polite"></p>'
        '<div id="upnext-wrap" data-mode="%s"><h2>%s</h2><div id="upnext" aria-live="polite"></div></div>'
        '<section><h2>Order of the blocks</h2>'
        '<p>Each block needs the one before it. Follow the arrows; the bar fills as you mark videos as watched.</p>%s</section>'
        % (html.escape(page_title), lede, mode, "Next session" if mode == "desk" else "Next ride", chain_html(blocks)))
    about = ('<details class="fold" open><summary>About this track and how to read it</summary>%s</details>' % render_text(intro_md)) if intro_md else ""
    body = hero + about + "".join(before) + "".join(after) + "".join(extras) + "".join(notes)
    out = page("%s - MSAI video plan" % page_title, "Ordered video list: %s." % long_title, key, body)
    (OUT / (slug + ".html")).write_text(out, encoding="utf-8")
    statuses = {}
    for p in [] : pass
    return {"key": key, "slug": slug, "title": page_title, "main": total_main, "blocks": len(blocks),
            "vids": sorted(set(all_vids)), "long": long_title}


def build_index(infos):
    md_text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    md_text = re.sub(r"\]\(tracks/([^)]+)\.md\)", r"](\1.html)", md_text)
    lines = md_text.split("\n")
    head, sections = split_sections(lines, 2)
    title = next((l[2:].strip() for l in head if l.startswith("# ")), "Roadmap")
    intro = "\n".join(l for l in head if not l.startswith("# ")).strip()
    cards = "".join(
        '<li><a href="%s.html"><strong>%s: %s</strong><span>%d main-path videos in %d blocks</span></a></li>'
        % (i["slug"], i["key"], html.escape(i["long"]), i["main"], i["blocks"]) for i in infos)
    body = ('<h1>%s</h1>%s<h2>Pick a track</h2><ul class="tracks">%s</ul>'
            % (html.escape(title), render_text(intro), cards))
    for t, b in sections:
        body += "<section><h2>%s</h2>%s</section>" % (html.escape(t), render_text(b))
    out = page(title, "Plan for watching the AI math, AI/ML and GenAI stack videos.", "index", body)
    (OUT / "index.html").write_text(out, encoding="utf-8")


def main():
    OUT.mkdir(exist_ok=True)
    infos = [build_track(*t) for t in TRACKS if (ROOT / "tracks" / (t[1] + ".md")).exists()]
    build_index(infos)
    for i in infos:
        print("%s: %d main-path videos, %d blocks, %d distinct video ids" % (i["key"], i["main"], i["blocks"], len(i["vids"])))
    print("warnings:", len(WARNINGS))


if __name__ == "__main__":
    main()
