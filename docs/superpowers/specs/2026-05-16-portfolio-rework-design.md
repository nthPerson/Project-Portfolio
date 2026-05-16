# Portfolio Site Rework — Design Document

**Date:** 2026-05-16
**Author:** Robert Ashe (with Claude)
**Status:** Approved design — ready for implementation planning

---

## 1. Overview

Completely rework the existing GitHub Pages portfolio site
(`nthperson.github.io/Project-Portfolio`). The current site is a ~2-year-old,
projects-only Bootstrap (Sandstone) page built to support an M.S. application.
Since then Robert has co-authored two papers, co-founded a startup (LARK), and
joined two research labs — the current site badly undersells him.

The reworked site presents Robert across three professional faces — **applied
AI engineer**, **researcher**, and **technical co-founder** — through a
hand-crafted static site with a distinctive editorial visual identity.

## 2. Goals & Audience

Primary audiences (the site must serve all three):

1. **Industry / AI engineering recruiters** — emphasize shipped products,
   technical depth, impact.
2. **PhD / research positions** — emphasize publications, research
   contributions, academic rigor.
3. **LARK / startup credibility** — investors, partners, collaborators
   evaluating Robert as a technical co-founder.

Success criteria: the site reads as credible and current to all three
audiences, showcases both academic achievement and engineering ability, and
presents LARK compellingly without exposing proprietary code.

## 3. Architecture

- **Landing page + detail pages.** One scannable single-page landing
  (`index.html`) plus a dedicated case-study detail page for each of the 5
  featured projects.
- **Hand-built static site.** Semantic HTML5, one CSS file, minimal vanilla
  JS. No framework, no build step. Bootstrap is removed entirely.
- **Hosting unchanged.** GitHub Pages serving the `main` branch of the
  existing `Project-Portfolio` repo. No CI, no generator.

### Page inventory

```
index.html                  Landing page
projects/lark.html          LARK case study
projects/bim2rdt.html       BIM2RDT case study (+ EDL extension)
projects/famail.html        FAMAIL case study
projects/caltrans-oda.html  Caltrans ODA case study
projects/car-sounds.html    Car Sounds (DS-CNN/TinyML) case study
```

## 4. Visual Design System

Direction: **modern technical + warm** — editorial serif headings, monospace
technical labels, warm-paper background. Distinctive, not generic; deliberately
avoids the Anthropic cream/clay association.

### 4.1 Palette ("Parchment")

Derived from the blues of Robert's headshot tie plus a warm-neutral paper.

| Token            | Hex       | Use                                            |
|------------------|-----------|------------------------------------------------|
| `--paper`        | `#EDE8DD` | Page background (warm off-white)               |
| `--ink`          | `#2A3B4D` | Primary text, headings, solid buttons          |
| `--accent`       | `#5E7E99` | Steel-blue — labels, links, accents, hovers    |
| `--pale`         | `#B9C4CC` | Pale blue-grey — dividers, subtle fills        |
| `--muted`        | `#6E6A5F` | Secondary / descriptive text                   |
| `--card`         | `#F4F0E8` | Raised card surface                            |
| `--sidebar-bg`   | `#E4DECF` | Detail-page sidebar / section tint             |
| `--border`       | `#C9C2B2` | Hairline borders                               |
| `--circle-bg`    | `#DCD5C6` | Headshot circle backing                        |

Contrast rule: body text uses `--ink` on `--paper` (passes WCAG AA). `--accent`
is reserved for headings, labels, links, and large text — never small body
copy on `--paper`.

### 4.2 Typography (proposed, swappable during build)

- **Headings:** Newsreader (serif) — warm, editorial.
- **Body:** Inter (sans-serif) — clean, neutral.
- **Labels / metadata:** JetBrains Mono — uppercase, letter-spaced technical
  labels (e.g. `MULTI-AGENT · RAG · CO-FOUNDER · 2026`).

Loaded via Google Fonts. Final font selection confirmed during implementation.

### 4.3 Layout primitives

- **Hero:** centered — circular headshot above name, monospace role line,
  one-line intro, two buttons (View Work, Download CV), social links.
- **Featured Work:** alternating full-width feature rows — visual on one side,
  text on the other, alternating left/right down the page. Each row: index
  number, monospace metadata, serif title, one-line description, "Read the case
  study →" link.
- **Detail page:** two-column — a narrow sticky fact sidebar (Role, Timeline,
  Stack, Status, Links) beside a scrolling narrative. Collapses to single
  column on mobile.

## 5. Landing Page Specification

Sections, top to bottom:

1. **Hero** — headshot; "Robert Ashe"; `APPLIED AI ENGINEER · RESEARCHER ·
   CO-FOUNDER`; one-line intro ("Building agentic systems and ML models that
   bridge software and the physical world."); View Work + Download CV buttons;
   email/LinkedIn/GitHub/arXiv links; "San Diego, CA".
2. **About** — rewritten present-day narrative replacing the old "dreamed of
   being a scientist" essay. Two short paragraphs: the software-meets-physical-
   world throughline; current M.S. Big Data Analytics (expected Spring 2027)
   and B.S. Computer Science (4.0 major GPA, summa cum laude). Retains a spark
   of the original voice, modernized and sharper.
3. **Featured Work** — 5 alternating rows linking to detail pages, in order:
   LARK · BIM2RDT · FAMAIL · Caltrans ODA · Car Sounds. The **BIM2RDT row's
   description explicitly teases the Evidential Deep Learning extension** so
   visitors know the active research is there before clicking.
4. **Publications** — BIM2RDT, "Building Information Models to Robot-Ready Site
   Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework," arXiv:
   2509.20705 (2025), linked. "Accessible Control Framework for Unitree
   Robots," accepted, ASCE i3ce 2025.
5. **Experience** — timeline: DiCE Lab RA (2024–Present) · FAMAIL RA (Aug 2025–
   Present) · LARK Co-Founder & Lead AI Engineer (Jan 2026–Present) · CS 420
   Instructional Student Assistant (2025–Present) · Robert Ashe Designs (Go
   Rentals 3D printing, 2021–Present) · Miramar Ranch 3D-printing outreach
   (2024, compact).
6. **More Projects** — compact list linking GitHub repos: FEURcast, From Beats
   to Hits, Apple Watch HAR, Machine Learning implementations, Go1 / Unitree
   control framework, Streaming Service dashboard.
7. **Contact** — email (`robertashe2.0@gmail.com`), LinkedIn, GitHub
   (`nthPerson`), arXiv. **No home address or phone number.**
8. **Footer** — copyright, "View this site on GitHub" link.

Sticky top nav with anchor links to landing sections; on detail pages it links
back to the landing sections.

## 6. Detail Page Specification

All 5 detail pages share the two-column template:

- **Sticky sidebar:** Role · Timeline · Stack · Status · Links · (optional)
  one-line summary.
- **Narrative column:** eyebrow metadata + title → hero visual → `The Problem`
  → `What I Built` → `Architecture` (with diagram) → `Highlights` → `Tech
  Stack` → `Gallery`.
- **Footer:** previous / next project navigation.

### 6.1 Featured project content

- **LARK** — Co-Founder & Lead AI Engineer, Jan 2026–Present. Stack: Python,
  multi-agent LLMs, RAG, REST APIs, multi-tenant SaaS. Status: shipping / in
  active development. Links: "Private repository — demo available on request."
  Content: multi-agent statement-ingestion pipeline, RAG over interchange
  rules, the "Sidekick" agent, branded proposal-PDF generation, portfolio
  analytics, multi-tenant admin/RBAC, Echelon Payments integration.
- **BIM2RDT** — DiCE Lab, co-author; paper 2025. Stack: agentic AI, BIM/IFC,
  LiDAR/IMU sensor fusion, Semantic-Gravity ICP. Links: arXiv:2509.20705.
  Includes a **Current Research** block on the sole-authored extension,
  "Uncertainty-Aware Scan-to-BIM via Evidential Deep Learning" (CONE 652
  proposal, May 2026) — the proposal PDF is linked as a download. The block
  explains the gap it closes (calibrated decision layer for autonomous IFC
  updates), which BIM2RDT explicitly left as future work.
- **FAMAIL** — RA, PI Dr. Xin Zhang, Aug 2025–Present. Stack: PyTorch,
  imitation learning, fairness/bias mitigation, spatial-temporal augmentation,
  HPC. Links: public `FAMAIL` GitHub repo. Highlight: cut augmentation runtime
  from 16 days (CPU) to 39 minutes via CPU/GPU workload partitioning.
- **Caltrans ODA** — DiCE Lab, lead developer, Caltrans contract 65A1302.
  Stack: SWITRS/geospatial crash-data analysis, multivariate regression,
  propensity-score matching, Pupil Core eye tracking, EMOTIV EPOC X EEG,
  DriveSafety RS-250, HyperDrive/TCL. Status: ongoing research.
- **Car Sounds (DS-CNN / TinyML)** — Graduate ML/TinyML coursework. Stack:
  PyTorch/TensorFlow, depthwise-separable CNN, mel-spectrograms, post-training
  quantization, Arduino Nano 33 BLE Sense Rev2. Links: public
  `Car_Sounds_Classification` GitHub repo.

## 7. LARK Showcase Strategy (Proprietary-Safe)

LARK's code is a private repository and must stay proprietary. The case study:

- Shows **no repository link, no code snippets, no prompts, no proprietary
  algorithms.** Sidebar Links field reads "Private repository — demo available
  on request."
- Uses **clean UI screenshots provided by Robert** (already safe to publish —
  demo/fake data): Homepage, document analysis page, Sidekick (AI agent) page,
  and others as available.
- Uses **1–2 conceptual architecture diagrams** designed during implementation
  (multi-agent ingestion pipeline; RAG grounding over interchange rules) —
  system-level only, nothing proprietary.
- Narrative describes the problem, what Robert architected, the agent system,
  capabilities, and project status — impact and design thinking, not
  implementation secrets.

## 8. Disposition of Existing Content

- **Go1 Software Package** → reframed as the i3ce 2025 publication; also a
  "More Projects" GitHub link. No longer its own featured card.
- **Machine Learning Implementations** → "More Projects" list entry.
- **Mobile Payment System Mounting Solution** → folded into the Experience
  timeline as **Robert Ashe Designs** (Go Rentals, 300+ custom parts).
- **3D Printing Outreach** → compact Experience entry.
- **"Dreamed of being a scientist" essay** → rewritten as the new About
  section.
- **`bootstrap.min.sandstone.css`** and the `programming/`, `industrial/`,
  `outreach/` subpage directories → removed.
- Existing `assets/` images (Go1 photos, etc.) → reused where relevant on
  detail pages; pruned otherwise.

## 9. Tech Stack & File Structure

```
index.html
projects/
  lark.html  bim2rdt.html  famail.html  caltrans-oda.html  car-sounds.html
css/
  styles.css            Single stylesheet; CSS custom properties for tokens
js/
  main.js               Mobile nav toggle, subtle scroll-reveal
assets/
  img/                  Headshot, project visuals, diagrams, screenshots
  robert-ashe-cv.pdf    Downloadable resume
  favicon
docs/superpowers/specs/ This design doc
```

- Semantic HTML5 (`header`, `nav`, `main`, `section`, `article`, `footer`).
- CSS: design tokens as custom properties; mobile-first responsive; alternating
  rows stack and the detail two-column collapses to one column on narrow
  viewports.
- JS: vanilla, minimal — mobile nav toggle and optional scroll-reveal. Site is
  fully functional without JS.
- Fonts via Google Fonts.

## 10. Accessibility, SEO, Responsive

- WCAG AA contrast (see palette rule in §4.1); semantic landmarks; descriptive
  `alt` text on all images; visible focus states; keyboard-navigable.
- Per-page `<title>`, meta description, Open Graph / Twitter Card tags, favicon.
- Mobile-first; verified at common breakpoints.

## 11. Assets Required From Robert

- Professional headshot (provided).
- Clean LARK UI screenshots (Homepage, document analysis, Sidekick, others).
- Up-to-date CV PDF for download (current: the SDSU AI/Robotics/Construction
  resume).
- Confirmation/links for project visuals (BIM2RDT, FAMAIL, Caltrans, Car
  Sounds) — existing repo assets or new images.

## 12. Out of Scope

- No backend, CMS, or build pipeline.
- No blog/writing section (can be added later).
- No analytics integration (can be added later).
- No custom domain (stays on `github.io`) unless requested.

## 13. Open Items to Confirm During Implementation

- Final font selection (Newsreader / Inter / JetBrains Mono proposed).
- Architecture-diagram content for LARK and BIM2RDT (drafted during build,
  reviewed by Robert).
- Exact project visuals for non-LARK detail pages.
- Whether the EDL proposal PDF is hosted on-site for download (assumed yes).
