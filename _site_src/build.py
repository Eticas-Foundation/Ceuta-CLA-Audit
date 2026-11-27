#!/usr/bin/env python3
"""Builds the GitHub Pages site (HTML at the repo root) from the Markdown in the repo.

Run from the repo root:  python3 _site_src/build.py
Needs pandoc. The site is static: no Jekyll (.nojekyll at the root).
"""
import os
import re
import subprocess
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_URL = "https://github.com/Eticas-Foundation/Ceuta-CLA-Audit"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800'
         '&family=Raleway:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">')

NAV = [("", "Findings"), ("report/", "Report"), ("draft/", "Draft case study"),
       ("data/", "Data"), ("codebook/", "Codebook")]


def page(title, body, depth, active, description):
    pre = "../" * depth
    nav = "".join(
        f'<a href="{pre}{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for href, label in NAV)
    nav += f'<a href="{REPO_URL}">GitHub</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
{FONTS}
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <a class="logo" href="{pre}"><img src="{pre}assets/eticas-foundation-logo.png" alt="Eticas Foundation"></a>
    <nav class="site-nav">{nav}</nav>
  </div>
  <div class="brandbar"><span></span><span></span><span></span><span></span><span></span><span></span></div>
</header>
{body}
<footer class="site-footer">
  <div class="brandbar"><span></span><span></span><span></span><span></span><span></span><span></span></div>
  <div class="inner">
    <div>
      <h4>Eticas Foundation</h4>
      <p>Community-led audit with the Institut de les Desigualtats. Data collection, coding and analysis by Signal4 Analyses.</p>
    </div>
    <div>
      <h4>Licence</h4>
      <p>The report, its figures and the tables in <code>chart_data/</code> are released under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Attribution: <em>Signal4 Analyses for Eticas Foundation</em>.</p>
    </div>
    <div>
      <h4>About the codes</h4>
      <p>Every code is a language model's first pass; no person hand-coded the data. Do not attribute hate to a named or identifiable account on the strength of these codes alone.</p>
    </div>
  </div>
</footer>
</body>
</html>
"""


def pandoc(md_text, toc=False):
    args = ["pandoc", "-f", "markdown+pipe_tables+raw_html", "-t", "html5", "--wrap=none"]
    if toc:
        args += ["--toc", "--toc-depth=1", "--standalone",
                 "--template", os.path.join(ROOT, "_site_src", "toc_template.html")]
    return subprocess.run(args, input=md_text, capture_output=True, text=True, check=True).stdout


def split_toc(out):
    m = re.search(r"<!--TOC-->(.*?)<!--/TOC-->(.*)", out, re.S)
    return m.group(1), m.group(2)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


# ---------- Report ----------
report_md = read("report/ceuta-case-study.md")
toc, body = split_toc(pandoc(report_md, toc=True))
report_body = f"""
<section class="doc-head"><div class="inner">
  <p class="eyebrow">Report · Signal4 Analyses for Eticas Foundation</p>
  <h1>Ceuta on TikTok</h1>
  <p>Hate speech on TikTok and X about the Ceuta crossings, from 1 July to 30 September 2026. The full report, with its method, findings, limitations and sources.</p>
</div></section>
<div class="doc-layout">
  <aside class="toc"><div class="label">Contents</div>{toc}</aside>
  <article class="prose">{body}</article>
</div>
"""
write("report/index.html", page("Ceuta on TikTok — Report | Eticas Foundation", report_body, 1, "report/",
                                "The full report: hate speech on TikTok and X about the 2026 Ceuta crossings."))

# ---------- Draft ----------
draft_md = read("draft/ceuta-case-study-draft.md")
draft_md = re.sub(r"^> \*\*DRAFT.*?\n\n", "", draft_md, count=1, flags=re.S)
draft_body = f"""
<section class="doc-head"><div class="inner">
  <p class="eyebrow">Draft · Eticas Foundation and Institut de les Desigualtats</p>
  <h1>Analysing the 2026 Ceuta Migration Crisis on X and TikTok</h1>
  <p>Special edition ahead of the 29 November 2026 Spanish elections.</p>
</div></section>
<div class="doc-layout single">
  <article class="prose">
  <div class="notice"><strong>Draft — work in progress.</strong> This is a working draft of the case study by Eticas Foundation and the Institut de les Desigualtats. It will change before the full audit is released in December 2026. Its figures are not included here; the report's own figures are in the <a href="../report/">report</a>. One passage naming individual accounts has been removed because those codes have not yet been reviewed by a person.</div>
  {pandoc(re.sub(r"^# .*\n", "", draft_md, count=1, flags=re.M))}
  </article>
</div>
"""
write("draft/index.html", page("Draft case study — Ceuta | Eticas Foundation", draft_body, 1, "draft/",
                               "Work-in-progress draft of the Ceuta case study by Eticas Foundation and the Institut de les Desigualtats."))

# ---------- Codebook ----------
cb_toc, cb_body = split_toc(pandoc(read("codebook.md"), toc=True))
codebook_body = f"""
<section class="doc-head"><div class="inner">
  <p class="eyebrow">Codebook · Signal4 Analyses</p>
  <h1>How the content was coded</h1>
  <p>What each code means, how it was assigned, and the exact prompts given to the model. Some sections describe files that are not published here (see <a href="../data/">Data</a>).</p>
</div></section>
<div class="doc-layout">
  <aside class="toc"><div class="label">Contents</div>{cb_toc}</aside>
  <article class="prose">{cb_body}</article>
</div>
"""
write("codebook/index.html", page("Codebook — Ceuta | Eticas Foundation", codebook_body, 1, "codebook/",
                                  "Codes and exact model prompts used in the Ceuta case study."))

# ---------- Data ----------
DATA = [
    ("ct_daily.csv", "Videos and plays per day, with the coded videos and the clearly hateful ones among them"),
    ("ct_hate_weekly.csv", "Clearly hateful share of videos and of plays, by week (corpus estimates)"),
    ("ct_themes.csv", "What the clearly hateful videos said: each theme's share of videos and of plays"),
    ("ct_topics.csv", "What the Ceuta videos were about: each main topic's share of videos and plays, and the clearly hateful share in it"),
    ("ct_incidents.csv", "The events the clearly hateful videos showed, with videos and plays"),
    ("ct_reach_share.csv", "Share of videos and of plays by group (news outlets, top creators, small creators, Spain, Morocco, ...)"),
    ("ct_size_bands.csv", "Plays beyond the follower count, by creator size"),
    ("ct_size_model.csv", "Plays against the creator's followers, one row per video (no IDs)"),
    ("ct_size_model_fit.csv", "The fitted line of plays on followers (log scale)"),
    ("ct_comments_region.csv", "Where the commenters were: top-level comments under videos posted from Spain and from Morocco, by the commenter's region"),
    ("ct_tagpages.csv", "The one-page tag test of 18 October 2026, as scored for the report"),
    ("ct_tag_mechanism.csv", "What was measured for an unlinked tag (#menas) and the ordinary form of the same word (#mena)"),
    ("ct_partner_accounts.csv", "The community partner's key accounts: their Ceuta videos, codes and Ceuta-vs-other-posts ratio"),
    ("ct_coverage.csv", "How much of what search could return the two search routes found, by plays: an order-of-magnitude estimate"),
    ("ct_methods_flow_counts.csv", "The counts the Method section prints"),
    ("ct_methods_qa.csv", "The method in steps: each step's question, answer and count"),
]
rows = "".join(
    f'<tr><td><a class="dl" href="../chart_data/{f}" download>{f}</a></td><td>{html.escape(d)}</td>'
    f'<td class="num">{os.path.getsize(os.path.join(ROOT, "chart_data", f)) / 1024:,.1f} KB</td></tr>'
    for f, d in DATA)
data_body = f"""
<section class="doc-head"><div class="inner">
  <p class="eyebrow">Data</p>
  <h1>The aggregate data behind the report</h1>
  <p>Every chart and number in the report can be reproduced from these files. They are plain CSV (UTF-8, comma-separated).</p>
</div></section>
<div class="doc-layout single">
  <article class="prose" style="max-width:none">
  <h2>Chart data</h2>
  <div class="table-wrap"><table>
    <thead><tr><th>File</th><th>What it holds</th><th class="num">Size</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
  <p class="table-note">Also: <a href="../report/report_numbers.json" download>report_numbers.json</a>, every number the report's text prints, and the <a href="../codebook/">codebook</a>. Licence: CC BY 4.0, attribution <em>Signal4 Analyses for Eticas Foundation</em>.</p>
  <h2>Reading the numbers</h2>
  <ul>
    <li><strong>"Hateful" in headline counts means the model's <code>yes</code></strong> (clearly hateful). <code>borderline</code> is reported separately and is not counted as hate.</li>
    <li><strong>Plays are not people.</strong> TikTok counts replays. "Plays beyond the followers" is reach beyond the following, not a head count.</li>
    <li><strong>No one hand-coded a sample.</strong> Every code is the model's first pass.</li>
    <li><strong>The corpus is what TikTok surfaced</strong>, not everything posted: its hashtag pages and search favour videos that already did well.</li>
  </ul>
  <h2>What is not here, and why</h2>
  <p>The row-level files (one row per video, post, comment, creator or request) are not published. They are personal data, not anonymous data: each video or post ID leads back to an account, captions and transcripts are their authors' words, and commenters are private people, some of them minors. TikTok's and X's terms also restrict redistributing their content. Signal4 Analyses shared these files with Eticas Foundation for this study only. Researchers who need row-level data for a specific question can contact Eticas Foundation.</p>
  </article>
</div>
"""
write("data/index.html", page("Data — Ceuta | Eticas Foundation", data_body, 1, "data/",
                              "Aggregate data behind the Ceuta report: chart tables and every number the report prints."))

# ---------- Home ----------
write("index.html", page("Ceuta on TikTok and X | Eticas Foundation", read("_site_src/home.html"), 0, "",
                         "How hate speech about the 2026 Ceuta crossings spread on TikTok and X, and whether the platforms slowed it. A community-led audit by Eticas Foundation."))

open(os.path.join(ROOT, ".nojekyll"), "w").close()
print("built")
