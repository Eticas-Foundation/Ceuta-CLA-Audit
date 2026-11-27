# Community-Led Audit: Hate Speech on TikTok and X during the 2026 Ceuta Migration Crisis

**Eticas Foundation** | Community-led audit
**Partner:** Institut de les Desigualtats (Barcelona)
**Data collection and analysis:** Signal4 Analyses
**Status:** In progress. This case is one of three in a community-led audit of hate speech on social media (Southport 2024, "gender ideology", Ceuta 2026); the full audit is due in December 2026.

---

## Overview

On 30 and 31 July 2026, tens of thousands of people, most of them young Moroccans, crossed from Morocco into Ceuta. This repository holds the published results of the case study *Ceuta on TikTok*, which measured how hate speech about the event spread on TikTok and X from 1 July to 30 September 2026, and whether the platforms' product features and moderation measures slowed it.

The study collected 43,984 TikTok videos that name Ceuta (13,976 accounts, 3.76 billion plays), 406,573 comments and 140,170 replies, and 9,118 posts on X. A language model (Claude Haiku 5.5) coded 9,472 videos in full, every caption and comment, and every X post, under one definition of hate speech. No person hand-coded the data: every code is the model's first pass. The method, findings and limitations are in the report.

---

## Repository Structure

```
.
├── report/
│   ├── ceuta-case-study.md      # The case study (Signal4 Analyses for Eticas Foundation)
│   ├── report_numbers.json      # Every number the report's text prints
│   └── figures/                 # The report's figures
│
├── chart_data/                  # The aggregate tables behind the report's charts
│
├── codebook.md                  # What each code means, and the exact prompts given to the model
│
├── draft/
│   └── ceuta-case-study-draft.md  # DRAFT of the Eticas Foundation / Institut de les Desigualtats case study
│
├── index.html, report/, draft/, data/, codebook/, assets/   # the website (GitHub Pages)
├── _site_src/                   # the site's source: `python3 _site_src/build.py` rebuilds the HTML (needs pandoc)
│
└── README.md
```

---

## Aggregate data (`chart_data/`)

| File | What it holds |
|---|---|
| `ct_comments_region.csv` | Where the commenters were: top-level comments under videos posted from Spain and from Morocco, by the commenter's region |
| `ct_coverage.csv` | How much of what search could return the two search routes found, by plays: an order-of-magnitude estimate |
| `ct_daily.csv` | Videos and plays per day, with the coded videos and the clearly hateful ones among them |
| `ct_hate_weekly.csv` | Clearly hateful share of videos and of plays, by week (corpus estimates) |
| `ct_incidents.csv` | The events the clearly hateful videos showed, with videos and plays |
| `ct_methods_flow_counts.csv` | The counts the Method section prints |
| `ct_methods_qa.csv` | The method in steps: each step's question, answer and count |
| `ct_partner_accounts.csv` | The community partner's key accounts: their Ceuta videos, codes and Ceuta-vs-other-posts ratio |
| `ct_reach_share.csv` | Share of videos and of plays by group (news outlets, top creators, small creators, Spain, Morocco, ...) |
| `ct_size_bands.csv` | Plays beyond the follower count, by creator size |
| `ct_size_model.csv` | Plays against the creator's followers, one row per video (no IDs) |
| `ct_size_model_fit.csv` | The fitted line of plays on followers (log scale) |
| `ct_tag_mechanism.csv` | What was measured for an unlinked tag (#menas) and the ordinary form of the same word (#mena) |
| `ct_tagpages.csv` | The one-page tag test of 18 October 2026, as scored for the report |
| `ct_themes.csv` | What the clearly hateful videos said: each theme's share of videos and of plays |
| `ct_topics.csv` | What the Ceuta videos were about: each main topic's share of videos and plays, and the clearly hateful share in it |

"Hateful" in headline counts means the model's `yes` (clearly hateful); `borderline` is reported separately. Plays are not people: TikTok counts replays.

---

## What is not here, and why

The row-level files (one row per video, post, comment, creator or request) are **not published**. They are personal data, not anonymous data: each video or post ID leads back to an account, captions and transcripts are their authors' words, and commenters are private people, some of them minors. TikTok's and X's terms also restrict redistributing their content. Signal4 Analyses shared these files with Eticas Foundation for this study only.

The report, its figures and the aggregate tables in `chart_data/` reproduce every chart and number in the report. Researchers who need row-level data for a specific question can contact Eticas Foundation.

---

## About the draft

`draft/ceuta-case-study-draft.md` is a **work-in-progress draft** of the case study written by Eticas Foundation and the Institut de les Desigualtats, published ahead of the 29 November 2026 Spanish elections. It is not the final text. Its figures are not included, and one passage naming individual accounts has been removed because those codes have not yet been reviewed by a person.

---

## Team

**Eticas Foundation**
**Community Partner:** Institut de les Desigualtats
**Data collection, coding and analysis:** Signal4 Analyses

---

## License

The report, its figures and the tables in `chart_data/` are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution: *Signal4 Analyses for Eticas Foundation*.

The codes are a language model's first pass. Do not attribute hate to a named or identifiable account on the strength of these codes alone.
