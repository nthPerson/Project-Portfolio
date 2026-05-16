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

1. **Hero** — circular headshot (`RobertAshe_headshot_cropped_to_bust.jpg`);
   "Robert Ashe"; `APPLIED AI ENGINEER · RESEARCHER · CO-FOUNDER`; one-line
   intro ("Building agentic systems and ML models that bridge software and the
   physical world."); View Work + Download CV buttons; email/LinkedIn/GitHub/
   arXiv links; "San Diego, CA".
2. **About** — rewritten present-day narrative replacing the old "dreamed of
   being a scientist" essay. Two short paragraphs: the software-meets-physical-
   world throughline; current M.S. Big Data Analytics (expected Spring 2027)
   and B.S. Computer Science (4.0 major GPA, summa cum laude). Retains a spark
   of the original voice, modernized and sharper. Includes the B.S. graduation
   photo (`Graduation_with_Mom_Larry_Steven.jpg`) as a warm, personal image.
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

### 6.1 Featured project content & assets

Each entry lists narrative focus, sidebar facts, the provided images/documents
to use, and any diagrams to generate. Source files are staged in
`project_content/`; the build optimizes them (resize, compress) and copies
them into `assets/img/` and `assets/docs/`. File paths below are relative to
`project_content/`.

**LARK** — Co-Founder & Lead AI Engineer, Jan 2026–Present.
- Sidebar: Stack Python · multi-agent LLMs · RAG · REST APIs · multi-tenant
  SaaS; Status shipping / active development; Links "Private repository —
  demo available on request."
- Narrative: multi-agent statement-ingestion pipeline, RAG over interchange
  rules, the "Sidekick" agent, branded proposal-PDF generation, portfolio
  analytics, multi-tenant admin/RBAC, Echelon Payments integration.
- Provided images (clean, publishable): `lark/screenshot_homepage_desktop.png`
  (hero), `screenshot_documents_desktop.png`, `screenshot_analysis_desktop.png`
  + `screenshot_analysis_mobile.png`, `screenshot_sidekick_desktop.png` +
  `screenshot_sidekick_mobile.png`. Desktop shots anchor sections; each
  desktop/mobile pair shown together demonstrates responsive design.
- To generate during build: a conceptual multi-agent ingestion + RAG
  architecture diagram (system-level, no proprietary detail).

**BIM2RDT** — DiCE Lab, co-author; paper 2025. Go1 photo reuse approved.
- Sidebar: Stack agentic AI · BIM/IFC · LiDAR/IMU sensor fusion ·
  Semantic-Gravity ICP; Status published; Links — arXiv abstract
  (`arxiv.org/abs/2509.20705`) and paper PDF (`arxiv.org/pdf/2509.20705`).
- Provided images: `BIM2RDT/BIM2RDT_figure_1.png` (feature prominently — the
  paper's main system figure), `BIM2RDT_digital_twin_vs_simulated_real_world.png`
  (hero candidate), `BIM2RDT_SG-ICP.png` (SG-ICP before/after — the paper's
  headline contribution), `BIM2RDT_HAV_monitoring.png` (worker hand-arm-
  vibration monitoring chart). Existing `assets/` Go1 quadruped photos may
  supplement the hero/gallery, captioned as related DiCE Lab robotics work.
- **Current Research block** — "Uncertainty-Aware Scan-to-BIM via Evidential
  Deep Learning" (CONE 652, May 2026, sole-authored). Explains the gap it
  closes (a calibrated decision layer for autonomous IFC updates) that BIM2RDT
  left as future work. Feature `edl_digital_twins/Figure_1.png` prominently;
  include `decision_map_uncertainty_discrepancy_plane.png`. Downloadable from
  this section: `CON_E_652__Final_Project_Proposal.pdf` (proposal) and
  `CONE652_FinalProject_Presentation_RobertAshe_v2.pdf` (presentation slides).

**FAMAIL** — RA, PI Dr. Xin Zhang, Aug 2025–Present.
- Sidebar: Stack PyTorch · imitation learning · fairness/bias mitigation ·
  spatial-temporal augmentation · HPC; Status ongoing research; Links public
  `FAMAIL` GitHub repo + dedicated project site
  `https://nthperson.github.io/FAMAIL/`.
- Highlight: cut augmentation runtime from 16 days (CPU) to 39 minutes via
  CPU/GPU workload partitioning.
- Provided images: `famail/screenshot_trajectory_modification_dashboard.png`
  (dark-mode, two heatmaps — hero candidate),
  `screenshot_causal_fairness_term_dashboard.png`,
  `screenshot_objective_function_dashboard_light.png`,
  `screenshot_causal_fairness_temporal_patterns_line_graphs.png`.
- To generate during build: a spatial-temporal augmentation pipeline /
  methodology diagram.

**Caltrans ODA** — DiCE Lab, lead developer, Caltrans contract 65A1302.
Project materials are largely confidential — this page leans most heavily on
generated visuals.
- Sidebar: Stack SWITRS/geospatial crash-data analysis · multivariate
  regression · propensity-score matching · Pupil Core eye tracking · EMOTIV
  EPOC X EEG · DriveSafety RS-250 · HyperDrive/TCL; Status ongoing research;
  Links — Caltrans Active Permitted Displays Map Viewer
  (`caltrans.maps.arcgis.com/apps/webappviewer/index.html?id=f0bb9147535d49a4bd24099475883c15`).
- Provided images: `caltrans_oda/caltrans_active_permit_arcGIS_screenshot.png`
  (the public ArcGIS map viewer; links to the live viewer above).
- To generate during build (carry the page in place of confidential imagery):
  a crash-data analysis pipeline diagram (SWITRS/TSN/TCR → geospatial join →
  multivariate regression + propensity-score matching) and a study-design
  methodology diagram (driving simulator + eye-tracking + EEG).

**Car Sounds (DS-CNN / TinyML)** — Graduate ML/TinyML coursework. A flagship
project — it showcases AI/ML, data, and hardware skills together. The page
should feature most/all provided figures and offer the report for download.
- Sidebar: Stack PyTorch/TensorFlow · depthwise-separable CNN · mel-spectrograms
  · post-training quantization · Arduino Nano 33 BLE Sense Rev2; Status complete
  (M.S. coursework); Links public `Car_Sounds_Classification` GitHub repo.
- Provided images: `car_sounds/car_sounds_deployed_hardware_under_hood_and_in_cabin.png`
  (hero — the physical deployment), `car_sounds_log_mel-spectrograms.png`,
  `car_sounds_classification_accuracy_bar_chart_all_models.png`,
  `car_sounds_accuracy_vs_model_size_scatterplot.png`,
  `car_sounds_data_augmentation_ablation_bar_chart.png`,
  `car_sounds_quantization_impact_bar_chart.png`,
  `car_sounds_classification_cycle_latency_breakdown_bar_and_pie_chart.png`,
  `car_sounds_hardware_resource_utilization_stacked_bar_chart.png`. Used across
  the Architecture / Highlights / Gallery sections as a results showcase.
- Downloadable: `Car_Sounds_Final_Report.pdf`.
- To generate during build: a DS-CNN pipeline diagram (audio capture →
  mel-spectrogram → DS-CNN → post-training quantization → on-device inference).

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
  docs/                 Downloadable PDFs (CV, EDL proposal + slides,
                        Car Sounds report)
  favicon
project_content/        Source-of-truth staging area for Robert's raw assets
                        (not linked from the deployed site)
docs/superpowers/specs/ This design doc
```

- Build-time image optimization is required: resize images to sensible display
  dimensions and compress them. The 8.8 MB source headshot in particular must
  be reduced; large PNG screenshots/figures should be optimized for web.

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

## 11. Asset Inventory & Handling

All source materials are staged in `project_content/` (not part of the
deployed site's linked pages). During the build, images are optimized (resized
and compressed) and copied into `assets/img/`; PDFs into `assets/docs/`.

### 11.1 Provided assets

**People / general**
- Hero headshot — `pics_of_robert/RobertAshe_headshot_cropped_to_bust.jpg`
  (head-and-shoulders crop; preferred for the hero).
- Full headshot — `pics_of_robert/RobertAshe_headshot.jpg` (alternate /
  backup).
- About-section photo — `pics_of_robert/Graduation_with_Mom_Larry_Steven.jpg`
  (B.S. graduation; warm and personal).
- CV download — `current_cv/Robert_Ashe_resume_Spring_2026.pdf`.

**Per project** — placement detailed in §6.1:
- LARK — 6 UI screenshots (3 desktop, 1 documents, analysis + sidekick
  desktop/mobile pairs).
- BIM2RDT — 4 paper figures + EDL extension: 2 figures and 2 PDFs.
- FAMAIL — 4 dashboard screenshots + external project site link.
- Caltrans ODA — 1 ArcGIS map-viewer screenshot.
- Car Sounds — 8 result figures + 1 report PDF.

### 11.2 To generate during the build (no source files needed)

On-brand diagrams in the Parchment palette, built as HTML/CSS/SVG:
- LARK — multi-agent ingestion + RAG architecture diagram.
- FAMAIL — spatial-temporal augmentation pipeline / methodology diagram.
- Caltrans ODA — crash-data analysis pipeline + study-design methodology
  diagrams (this page depends on them most).
- Car Sounds — DS-CNN pipeline diagram.
- BIM2RDT — optional simplified pipeline diagram (the provided Figure 1 may
  suffice on its own).

### 11.3 External links (all provided)

- BIM2RDT paper — arXiv abstract `https://arxiv.org/abs/2509.20705`; paper PDF
  `https://arxiv.org/pdf/2509.20705`.
- Caltrans Active Permitted Displays Map Viewer —
  `https://caltrans.maps.arcgis.com/apps/webappviewer/index.html?id=f0bb9147535d49a4bd24099475883c15`
  (the provided ArcGIS screenshot links here).
- FAMAIL project site — `https://nthperson.github.io/FAMAIL/`.

### 11.4 Default / backup image handling

- Each project hero has a fallback: if its image is missing or fails to load,
  render an on-brand "title card" — a solid `--ink` or `--accent` block with
  the project name in monospace (as in the approved layout mockups).
- All images carry descriptive `alt` text.
- Provided figures that are charts/plots get short captions so they read
  clearly outside their original paper context.

## 12. Out of Scope

- No backend, CMS, or build pipeline.
- No blog/writing section (can be added later).
- No analytics integration (can be added later).
- No custom domain (stays on `github.io`) unless requested.

## 13. Open Items to Confirm During Implementation

- Final font selection (Newsreader / Inter / JetBrains Mono proposed).
- Generated-diagram content for LARK, FAMAIL, Caltrans ODA, and Car Sounds —
  drafted during the build, reviewed by Robert before launch.
- EDL proposal PDF and presentation slides are hosted on-site for download
  (confirmed).
