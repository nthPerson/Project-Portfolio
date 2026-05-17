# Portfolio Site Rework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completely rebuild Robert Ashe's GitHub Pages portfolio as a hand-crafted static site — a scannable landing page plus five project case-study pages — with a distinctive "Parchment" editorial visual identity.

**Architecture:** Hand-built static site: semantic HTML5, one CSS file driven by CSS custom properties, minimal vanilla JS. No framework, no build step. GitHub Pages serves `main` directly. A landing page (`index.html`) links to five detail pages under `projects/`.

**Tech Stack:** HTML5, CSS3 (custom properties, flexbox, grid), vanilla JavaScript, Google Fonts (Newsreader / Inter / JetBrains Mono). Python 3 + Pillow for build-time image optimization. `python3 -m http.server` for local preview.

**Reference spec:** `docs/superpowers/specs/2026-05-16-portfolio-rework-design.md`. Read it before starting — it defines the palette, layouts, content plan, and per-project asset placement.

---

## File Structure

```
index.html                     Landing page
projects/lark.html              LARK case study (the canonical detail-page template)
projects/bim2rdt.html           BIM2RDT case study + EDL extension section
projects/famail.html            FAMAIL case study
projects/caltrans-oda.html      Caltrans ODA case study
projects/car-sounds.html        Car Sounds (DS-CNN/TinyML) case study
css/styles.css                  Single stylesheet — tokens, base, layout, components, responsive
js/main.js                      Mobile nav toggle, scroll-reveal
assets/img/                     Optimized images (headshot, screenshots, figures, diagrams)
assets/docs/                    Downloadable PDFs (CV, EDL proposal + slides, Car Sounds report)
assets/favicon.svg              Site favicon
scripts/optimize_assets.py      One-off build script for image optimization
project_content/                Source-of-truth raw assets (unchanged; not linked from the site)
```

Legacy files removed in Task 1: `bootstrap.min.sandstone.css`, `programming/`, `industrial/`, `outreach/`.

Existing `assets/` Go1 photos are kept and reused on the BIM2RDT page: `assets/go1_full_assembly_2.jpg`, `assets/go1_side_view_2.jpg`, `assets/go1_inference_hardware_3_fixed.jpg`.

---

## Conventions

- **Verification without a test framework.** This is a static site; "tests" are concrete checks. Each task ends with: start a local server (`python3 -m http.server 8000` from the repo root, run in background), open the page in a browser, and confirm the named elements render and behave correctly. HTML is validated with `npx html-validate` (Node 18 is available).
- **Commit after every task** with the message shown in the task's final step.
- **Exact asset names.** All optimized assets use the names defined in Task 2. Use those names verbatim everywhere.
- **Palette tokens** (from spec §4.1) — never hardcode these hex values outside `:root`:
  `--paper:#EDE8DD` `--ink:#2A3B4D` `--accent:#5E7E99` `--accent-dark:#4A6985`
  `--pale:#B9C4CC` `--muted:#6E6A5F` `--card:#F4F0E8` `--sidebar-bg:#E4DECF`
  `--border:#C9C2B2` `--circle-bg:#DCD5C6`

---

## Task 1: Scaffold structure and remove legacy files

**Files:**
- Create: `css/styles.css` (empty), `js/main.js` (empty), `assets/img/.gitkeep`, `assets/docs/.gitkeep`, `scripts/.gitkeep`
- Delete: `bootstrap.min.sandstone.css`, `programming/`, `industrial/`, `outreach/`
- Modify: `index.html` (replaced wholesale in Task 7 — leave as-is for now)

- [ ] **Step 1: Create the new directory structure**

```bash
cd /home/robert/Project-Portfolio
mkdir -p css js assets/img assets/docs scripts projects
touch css/styles.css js/main.js assets/img/.gitkeep assets/docs/.gitkeep scripts/.gitkeep
```

- [ ] **Step 2: Remove legacy files**

```bash
git rm -r bootstrap.min.sandstone.css programming industrial outreach
```

Expected: git stages the deletion of one CSS file and three directories (`go1.html`, `machine_learning.html`, `mobile_payment.html`, `3d_printing.html`).

- [ ] **Step 3: Verify the tree**

Run: `ls -R css js assets scripts projects`
Expected: the new directories exist; `assets/` still contains the old image files (Go1 photos etc. — kept intentionally).

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "Scaffold new site structure, remove Bootstrap and legacy subpages

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Optimize and place image and document assets

Source assets live in `project_content/`. This task copies optimized copies into `assets/img/` and `assets/docs/` under stable names used by every later task.

**Files:**
- Create: `scripts/optimize_assets.py`
- Create: all files under `assets/img/` and `assets/docs/` (via the script + manual copies)

**Asset name mapping** (source → destination):

| Source | Destination |
|---|---|
| `pics_of_robert/RobertAshe_headshot_cropped_to_bust.jpg` | `assets/img/headshot.jpg` |
| `pics_of_robert/RobertAshe_headshot.jpg` | `assets/img/headshot-full.jpg` |
| `pics_of_robert/Graduation_with_Mom_Larry_Steven.jpg` | `assets/img/graduation.jpg` |
| `lark/screenshot_homepage_desktop.png` | `assets/img/lark-homepage.png` |
| `lark/screenshot_documents_desktop.png` | `assets/img/lark-documents.png` |
| `lark/screenshot_analysis_desktop.png` | `assets/img/lark-analysis-desktop.png` |
| `lark/screenshot_analysis_mobile.png` | `assets/img/lark-analysis-mobile.png` |
| `lark/screenshot_sidekick_desktop.png` | `assets/img/lark-sidekick-desktop.png` |
| `lark/screenshot_sidekick_mobile.png` | `assets/img/lark-sidekick-mobile.png` |
| `BIM2RDT/BIM2RDT_figure_1.png` | `assets/img/bim2rdt-figure1.png` |
| `BIM2RDT/BIM2RDT_digital_twin_vs_simulated_real_world.png` | `assets/img/bim2rdt-digital-twin.png` |
| `BIM2RDT/BIM2RDT_SG-ICP.png` | `assets/img/bim2rdt-sg-icp.png` |
| `BIM2RDT/BIM2RDT_HAV_monitoring.png` | `assets/img/bim2rdt-hav.png` |
| `edl_digital_twins/Figure_1.png` | `assets/img/edl-figure1.png` |
| `edl_digital_twins/decision_map_uncertainty_discrepancy_plane.png` | `assets/img/edl-decision-map.png` |
| `famail/screenshot_trajectory_modification_dashboard.png` | `assets/img/famail-trajectory.png` |
| `famail/screenshot_causal_fairness_term_dashboard.png` | `assets/img/famail-causal-fairness.png` |
| `famail/screenshot_objective_function_dashboard_light.png` | `assets/img/famail-objective-function.png` |
| `famail/screenshot_causal_fairness_temporal_patterns_line_graphs.png` | `assets/img/famail-temporal-patterns.png` |
| `caltrans_oda/caltrans_active_permit_arcGIS_screenshot.png` | `assets/img/caltrans-arcgis.png` |
| `car_sounds/car_sounds_deployed_hardware_under_hood_and_in_cabin.png` | `assets/img/car-sounds-hardware.png` |
| `car_sounds/car_sounds_log_mel-spectrograms.png` | `assets/img/car-sounds-melspec.png` |
| `car_sounds/car_sounds_classification_accuracy_bar_chart_all_models.png` | `assets/img/car-sounds-accuracy-bar.png` |
| `car_sounds/car_sounds_accuracy_vs_model_size_scatterplot.png` | `assets/img/car-sounds-accuracy-vs-size.png` |
| `car_sounds/car_sounds_data_augmentation_ablation_bar_chart.png` | `assets/img/car-sounds-augmentation.png` |
| `car_sounds/car_sounds_quantization_impact_bar_chart.png` | `assets/img/car-sounds-quantization.png` |
| `car_sounds/car_sounds_classification_cycle_latency_breakdown_bar_and_pie_chart.png` | `assets/img/car-sounds-latency.png` |
| `car_sounds/car_sounds_hardware_resource_utilization_stacked_bar_chart.png` | `assets/img/car-sounds-resource-util.png` |
| `current_cv/Robert_Ashe_resume_Spring_2026.pdf` | `assets/docs/Robert_Ashe_resume_Spring_2026.pdf` |
| `edl_digital_twins/CON_E_652__Final_Project_Proposal.pdf` | `assets/docs/edl-proposal.pdf` |
| `edl_digital_twins/CONE652_FinalProject_Presentation_RobertAshe_v2.pdf` | `assets/docs/edl-slides.pdf` |
| `car_sounds/Car_Sounds_Final_Report.pdf` | `assets/docs/car-sounds-report.pdf` |

- [ ] **Step 1: Install Pillow**

Run: `python3 -m pip install --user Pillow`
Expected: Pillow installs successfully (or reports already satisfied).

- [ ] **Step 2: Write the image optimization script**

Create `scripts/optimize_assets.py`:

```python
"""Optimize and copy portfolio images from project_content/ into assets/img/.

Resizes images so their largest dimension is at most MAX_DIM px and
re-encodes them compressed. JPEGs stay JPEG; PNGs stay PNG.
"""
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
MAX_DIM = 1800  # px — generous for retina, far below multi-thousand-px sources

# (source relative to project_content/, destination relative to assets/img/)
IMAGES = [
    ("pics_of_robert/RobertAshe_headshot_cropped_to_bust.jpg", "headshot.jpg"),
    ("pics_of_robert/RobertAshe_headshot.jpg", "headshot-full.jpg"),
    ("pics_of_robert/Graduation_with_Mom_Larry_Steven.jpg", "graduation.jpg"),
    ("lark/screenshot_homepage_desktop.png", "lark-homepage.png"),
    ("lark/screenshot_documents_desktop.png", "lark-documents.png"),
    ("lark/screenshot_analysis_desktop.png", "lark-analysis-desktop.png"),
    ("lark/screenshot_analysis_mobile.png", "lark-analysis-mobile.png"),
    ("lark/screenshot_sidekick_desktop.png", "lark-sidekick-desktop.png"),
    ("lark/screenshot_sidekick_mobile.png", "lark-sidekick-mobile.png"),
    ("BIM2RDT/BIM2RDT_figure_1.png", "bim2rdt-figure1.png"),
    ("BIM2RDT/BIM2RDT_digital_twin_vs_simulated_real_world.png", "bim2rdt-digital-twin.png"),
    ("BIM2RDT/BIM2RDT_SG-ICP.png", "bim2rdt-sg-icp.png"),
    ("BIM2RDT/BIM2RDT_HAV_monitoring.png", "bim2rdt-hav.png"),
    ("edl_digital_twins/Figure_1.png", "edl-figure1.png"),
    ("edl_digital_twins/decision_map_uncertainty_discrepancy_plane.png", "edl-decision-map.png"),
    ("famail/screenshot_trajectory_modification_dashboard.png", "famail-trajectory.png"),
    ("famail/screenshot_causal_fairness_term_dashboard.png", "famail-causal-fairness.png"),
    ("famail/screenshot_objective_function_dashboard_light.png", "famail-objective-function.png"),
    ("famail/screenshot_causal_fairness_temporal_patterns_line_graphs.png", "famail-temporal-patterns.png"),
    ("caltrans_oda/caltrans_active_permit_arcGIS_screenshot.png", "caltrans-arcgis.png"),
    ("car_sounds/car_sounds_deployed_hardware_under_hood_and_in_cabin.png", "car-sounds-hardware.png"),
    ("car_sounds/car_sounds_log_mel-spectrograms.png", "car-sounds-melspec.png"),
    ("car_sounds/car_sounds_classification_accuracy_bar_chart_all_models.png", "car-sounds-accuracy-bar.png"),
    ("car_sounds/car_sounds_accuracy_vs_model_size_scatterplot.png", "car-sounds-accuracy-vs-size.png"),
    ("car_sounds/car_sounds_data_augmentation_ablation_bar_chart.png", "car-sounds-augmentation.png"),
    ("car_sounds/car_sounds_quantization_impact_bar_chart.png", "car-sounds-quantization.png"),
    ("car_sounds/car_sounds_classification_cycle_latency_breakdown_bar_and_pie_chart.png", "car-sounds-latency.png"),
    ("car_sounds/car_sounds_hardware_resource_utilization_stacked_bar_chart.png", "car-sounds-resource-util.png"),
]

DOCS = [
    ("current_cv/Robert_Ashe_resume_Spring_2026.pdf", "Robert_Ashe_resume_Spring_2026.pdf"),
    ("edl_digital_twins/CON_E_652__Final_Project_Proposal.pdf", "edl-proposal.pdf"),
    ("edl_digital_twins/CONE652_FinalProject_Presentation_RobertAshe_v2.pdf", "edl-slides.pdf"),
    ("car_sounds/Car_Sounds_Final_Report.pdf", "car-sounds-report.pdf"),
]


def optimize_image(src: Path, dst: Path) -> None:
    img = Image.open(src)
    if max(img.size) > MAX_DIM:
        img.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)
    if dst.suffix.lower() in (".jpg", ".jpeg"):
        img = img.convert("RGB")
        img.save(dst, "JPEG", quality=82, optimize=True, progressive=True)
    else:
        img.save(dst, "PNG", optimize=True)
    print(f"  {src.name}  ->  {dst.name}  ({dst.stat().st_size // 1024} KB)")


def main() -> None:
    src_root = ROOT / "project_content"
    img_dst = ROOT / "assets" / "img"
    doc_dst = ROOT / "assets" / "docs"
    img_dst.mkdir(parents=True, exist_ok=True)
    doc_dst.mkdir(parents=True, exist_ok=True)

    print("Images:")
    for src_rel, dst_name in IMAGES:
        optimize_image(src_root / src_rel, img_dst / dst_name)

    print("Documents:")
    for src_rel, dst_name in DOCS:
        shutil.copy2(src_root / src_rel, doc_dst / dst_name)
        print(f"  {src_rel}  ->  {dst_name}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Run the script**

Run: `python3 scripts/optimize_assets.py`
Expected: every image and document prints a `source -> dest` line with no errors. The headshot drops well under 1 MB.

- [ ] **Step 4: Verify outputs**

Run: `ls -la assets/img assets/docs && du -sh assets/img`
Expected: 28 images in `assets/img/`, 4 PDFs in `assets/docs/`, total `assets/img` size is a few MB (not tens of MB).

- [ ] **Step 5: Commit**

```bash
git add scripts/optimize_assets.py assets/img assets/docs
git commit -m "Optimize and place project image and document assets

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: CSS — design tokens and base styles

**Files:**
- Modify: `css/styles.css` (write the first section)

- [ ] **Step 1: Write tokens, reset, and base typography**

Write this as the start of `css/styles.css`:

```css
/* ===== Robert Ashe — Portfolio styles ===== */
/* Fonts loaded via <link> in each page's <head>. */

:root {
  /* Palette — "Parchment" */
  --paper: #EDE8DD;
  --ink: #2A3B4D;
  --accent: #5E7E99;
  --accent-dark: #4A6985;
  --pale: #B9C4CC;
  --muted: #6E6A5F;
  --card: #F4F0E8;
  --sidebar-bg: #E4DECF;
  --border: #C9C2B2;
  --circle-bg: #DCD5C6;

  /* Typography */
  --font-serif: 'Newsreader', Georgia, 'Times New Roman', serif;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, Arial, sans-serif;
  --font-mono: 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace;

  /* Layout */
  --maxw: 1080px;
  --pad: clamp(1.1rem, 4vw, 2.5rem);
  --radius: 10px;
}

*, *::before, *::after { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-sans);
  font-size: 17px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  font-family: var(--font-serif);
  font-weight: 700;
  line-height: 1.15;
  margin: 0 0 0.5em;
}
h1 { font-size: clamp(2.4rem, 6vw, 3.6rem); }
h2 { font-size: clamp(1.8rem, 4vw, 2.5rem); }
h3 { font-size: 1.4rem; }

p { margin: 0 0 1rem; }

a { color: var(--accent-dark); text-decoration-thickness: 1px; text-underline-offset: 2px; }
a:hover { color: var(--ink); }

img { max-width: 100%; height: auto; display: block; }

/* Monospace technical label */
.label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

/* Layout helpers */
.wrap { max-width: var(--maxw); margin: 0 auto; padding: 0 var(--pad); }
.section { padding: clamp(3rem, 8vw, 5.5rem) 0; }
.section + .section { border-top: 1px solid var(--border); }

.section-head { margin-bottom: 2.5rem; }
.section-head .label { display: block; margin-bottom: 0.4rem; }

/* Visible focus for keyboard users */
a:focus-visible, button:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

/* Scroll-reveal — JS adds .is-visible */
.reveal { opacity: 0; transform: translateY(16px); transition: opacity .6s ease, transform .6s ease; }
.reveal.is-visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
  html { scroll-behavior: auto; }
}
```

- [ ] **Step 2: Verify the file parses**

Run: `npx html-validate --version` then visually scan `css/styles.css` for unbalanced braces.
Expected: the version prints (confirms Node tooling works); braces balanced.

- [ ] **Step 3: Commit**

```bash
git add css/styles.css
git commit -m "Add CSS design tokens and base styles

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: CSS — layout primitives and components

**Files:**
- Modify: `css/styles.css` (append)

- [ ] **Step 1: Append navigation, hero, and button styles**

Append to `css/styles.css`:

```css
/* ===== Site navigation ===== */
.site-nav {
  position: sticky; top: 0; z-index: 50;
  background: rgba(237, 232, 221, 0.92);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
}
.site-nav .wrap {
  display: flex; align-items: center; justify-content: space-between;
  height: 62px;
}
.site-nav .brand {
  font-family: var(--font-serif); font-weight: 700; font-size: 1.15rem;
  color: var(--ink); text-decoration: none;
}
.nav-links { display: flex; gap: 1.4rem; align-items: center; list-style: none; margin: 0; padding: 0; }
.nav-links a {
  font-family: var(--font-mono); font-size: 0.74rem; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--ink); text-decoration: none;
}
.nav-links a:hover { color: var(--accent-dark); }
.nav-toggle {
  display: none; background: none; border: 1px solid var(--border);
  border-radius: 6px; padding: 0.4rem 0.6rem; cursor: pointer;
  font-family: var(--font-mono); color: var(--ink);
}

/* ===== Buttons ===== */
.btn {
  display: inline-block; font-family: var(--font-sans); font-size: 0.95rem;
  font-weight: 600; padding: 0.7rem 1.4rem; border-radius: 6px;
  text-decoration: none; cursor: pointer; transition: background .2s, color .2s;
}
.btn-solid { background: var(--ink); color: var(--paper); border: 1px solid var(--ink); }
.btn-solid:hover { background: var(--accent-dark); border-color: var(--accent-dark); color: #fff; }
.btn-outline { background: transparent; color: var(--ink); border: 1px solid var(--ink); }
.btn-outline:hover { background: var(--ink); color: var(--paper); }

/* ===== Hero (centered) ===== */
.hero { text-align: center; padding: clamp(3rem, 9vw, 6rem) 0 clamp(2.5rem, 6vw, 4rem); }
.hero-photo {
  width: 150px; height: 150px; border-radius: 50%; object-fit: cover;
  margin: 0 auto 1.6rem; background: var(--circle-bg);
  border: 3px solid var(--accent);
}
.hero h1 { margin-bottom: 0.3rem; }
.hero .role { display: block; margin-bottom: 1rem; }
.hero .intro {
  font-family: var(--font-serif); font-size: clamp(1.05rem, 2.2vw, 1.3rem);
  color: var(--muted); max-width: 38ch; margin: 0 auto 1.6rem;
}
.hero-actions { display: flex; gap: 0.8rem; justify-content: center; flex-wrap: wrap; margin-bottom: 1.4rem; }
.hero-links { display: flex; gap: 1.2rem; justify-content: center; flex-wrap: wrap; }
.hero-links a {
  font-family: var(--font-mono); font-size: 0.78rem; letter-spacing: 0.05em;
  color: var(--accent-dark); text-decoration: none;
}
.hero-links a:hover { color: var(--ink); text-decoration: underline; }
.hero .location { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--muted); margin-top: 1.2rem; }

/* ===== About ===== */
.about-grid { display: grid; grid-template-columns: 1.4fr 1fr; gap: 2.5rem; align-items: center; }
.about-photo { border-radius: var(--radius); border: 1px solid var(--border); }
.about-text p:last-child { margin-bottom: 0; }

/* ===== Featured Work — alternating rows ===== */
.feature-row {
  display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem;
  align-items: center; margin-bottom: 3.5rem;
}
.feature-row:last-child { margin-bottom: 0; }
.feature-row:nth-child(even) .feature-visual { order: 2; }
.feature-visual {
  border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border);
  background: var(--card); aspect-ratio: 3 / 2;
}
.feature-visual img { width: 100%; height: 100%; object-fit: cover; }
.feature-row .label { display: block; margin-bottom: 0.5rem; }
.feature-row h3 { font-size: 1.6rem; margin-bottom: 0.5rem; }
.feature-row p { color: var(--muted); margin-bottom: 0.8rem; }
.feature-link {
  font-family: var(--font-mono); font-size: 0.78rem; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--accent-dark); text-decoration: none; font-weight: 600;
}
.feature-link:hover { color: var(--ink); }

/* On-brand fallback title card (used when an image is missing) */
.titlecard {
  width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;
  background: var(--accent); color: var(--paper);
  font-family: var(--font-mono); font-size: 1rem; letter-spacing: 0.12em;
  text-transform: uppercase; text-align: center; padding: 1rem;
}

/* ===== Publications ===== */
.pub-list { list-style: none; margin: 0; padding: 0; }
.pub-list li { padding: 1.2rem 0; border-top: 1px solid var(--border); }
.pub-list li:last-child { border-bottom: 1px solid var(--border); }
.pub-list .pub-title { font-family: var(--font-serif); font-size: 1.2rem; font-weight: 700; }
.pub-list .pub-meta { color: var(--muted); font-size: 0.95rem; }

/* ===== Experience timeline ===== */
.timeline { list-style: none; margin: 0; padding: 0; }
.timeline li {
  display: grid; grid-template-columns: 200px 1fr; gap: 1.5rem;
  padding: 1.3rem 0; border-top: 1px solid var(--border);
}
.timeline li:last-child { border-bottom: 1px solid var(--border); }
.timeline .when { font-family: var(--font-mono); font-size: 0.78rem; color: var(--accent); padding-top: 0.2rem; }
.timeline .role-title { font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; }
.timeline .org { color: var(--muted); font-size: 0.95rem; margin-bottom: 0.3rem; }

/* ===== More Projects ===== */
.more-projects { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem 2rem; list-style: none; margin: 0; padding: 0; }
.more-projects a {
  display: flex; justify-content: space-between; gap: 1rem;
  padding: 0.8rem 0; border-bottom: 1px solid var(--border);
  text-decoration: none; color: var(--ink);
}
.more-projects a:hover { color: var(--accent-dark); }
.more-projects .mp-name { font-family: var(--font-serif); font-weight: 700; }
.more-projects .mp-tag { font-family: var(--font-mono); font-size: 0.7rem; color: var(--accent); align-self: center; }

/* ===== Contact + footer ===== */
.contact-links { display: flex; gap: 1.6rem; flex-wrap: wrap; font-family: var(--font-mono); font-size: 0.85rem; }
.site-footer {
  background: var(--ink); color: var(--paper); text-align: center;
  padding: 1.6rem 0; font-family: var(--font-mono); font-size: 0.76rem; letter-spacing: 0.08em;
}
.site-footer a { color: var(--pale); }
```

- [ ] **Step 2: Append detail-page (case study) styles**

Append to `css/styles.css`:

```css
/* ===== Detail (case study) pages ===== */
.crumb {
  font-family: var(--font-mono); font-size: 0.74rem; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--accent-dark); text-decoration: none;
  display: inline-block; margin: 1.6rem 0;
}
.crumb:hover { color: var(--ink); }

.detail-header { margin-bottom: 2rem; }
.detail-header .label { display: block; margin-bottom: 0.5rem; }
.detail-header h1 { font-size: clamp(2rem, 5vw, 3rem); }
.detail-header .tagline { font-family: var(--font-serif); font-size: 1.2rem; color: var(--muted); }

.detail-layout { display: grid; grid-template-columns: 240px 1fr; gap: 3rem; align-items: start; }

.detail-sidebar {
  position: sticky; top: 86px;
  background: var(--sidebar-bg); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 1.4rem;
}
.detail-sidebar dl { margin: 0; }
.detail-sidebar dt {
  font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--accent); margin-top: 1rem;
}
.detail-sidebar dt:first-child { margin-top: 0; }
.detail-sidebar dd { margin: 0.15rem 0 0; font-size: 0.92rem; }
.detail-sidebar dd a { display: block; }

.detail-main > section { margin-bottom: 2.6rem; }
.detail-main h2 { font-size: 1.7rem; }
.detail-main .label { display: block; margin-bottom: 0.4rem; }

.detail-hero {
  border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border);
  margin-bottom: 2.4rem;
}

figure { margin: 1.4rem 0; }
figure img { border-radius: 8px; border: 1px solid var(--border); }
figcaption { font-size: 0.85rem; color: var(--muted); margin-top: 0.5rem; font-style: italic; }

.gallery { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.2rem; }
.gallery figure { margin: 0; }

/* Generated diagram container */
.diagram {
  background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 1.6rem; margin: 1.4rem 0;
}

/* Highlight callouts */
.highlights { list-style: none; margin: 0; padding: 0; }
.highlights li {
  padding: 0.8rem 0 0.8rem 1.6rem; position: relative; border-top: 1px solid var(--border);
}
.highlights li::before { content: "▸"; position: absolute; left: 0; color: var(--accent); }

/* Download links */
.downloads { display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem; }

/* Prev/next nav */
.prevnext {
  display: flex; justify-content: space-between; gap: 1rem;
  border-top: 1px solid var(--border); margin-top: 2rem; padding-top: 1.4rem;
  font-family: var(--font-mono); font-size: 0.78rem;
}
.prevnext a { text-decoration: none; color: var(--accent-dark); }
.prevnext a:hover { color: var(--ink); }
```

- [ ] **Step 3: Verify**

Visually scan `css/styles.css` for balanced braces. The file should now contain tokens, base, components, and detail-page styles.

- [ ] **Step 4: Commit**

```bash
git add css/styles.css
git commit -m "Add CSS layout primitives, components, and case-study styles

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: CSS — responsive rules

**Files:**
- Modify: `css/styles.css` (append)

- [ ] **Step 1: Append responsive media queries**

Append to `css/styles.css`:

```css
/* ===== Responsive ===== */
@media (max-width: 860px) {
  body { font-size: 16px; }

  /* Mobile nav: links collapse behind the toggle */
  .nav-toggle { display: block; }
  .nav-links {
    display: none; position: absolute; top: 62px; left: 0; right: 0;
    flex-direction: column; gap: 0; background: var(--paper);
    border-bottom: 1px solid var(--border); padding: 0.5rem 0;
  }
  .nav-links.open { display: flex; }
  .nav-links a { padding: 0.8rem var(--pad); width: 100%; }

  /* Single-column stacks */
  .about-grid { grid-template-columns: 1fr; gap: 1.6rem; }
  .feature-row { grid-template-columns: 1fr; gap: 1.2rem; margin-bottom: 2.6rem; }
  .feature-row:nth-child(even) .feature-visual { order: 0; }
  .more-projects { grid-template-columns: 1fr; }
  .timeline li { grid-template-columns: 1fr; gap: 0.3rem; }
  .timeline .when { padding-top: 0; }

  /* Detail page collapses to one column; sidebar un-sticks */
  .detail-layout { grid-template-columns: 1fr; gap: 1.8rem; }
  .detail-sidebar { position: static; }

  .gallery { grid-template-columns: 1fr; }
}

@media (max-width: 480px) {
  .hero-photo { width: 120px; height: 120px; }
  .hero-actions { flex-direction: column; align-items: stretch; }
  .btn { text-align: center; }
}
```

- [ ] **Step 2: Commit**

```bash
git add css/styles.css
git commit -m "Add responsive CSS rules

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: JavaScript — mobile nav and scroll-reveal

**Files:**
- Modify: `js/main.js`

- [ ] **Step 1: Write `js/main.js`**

```javascript
// Portfolio interactivity — mobile nav toggle + scroll reveal.
(function () {
  "use strict";

  // Mobile navigation toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close the menu after following an in-page link
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Scroll reveal — adds .is-visible to .reveal elements as they enter view
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    // No IntersectionObserver — show everything
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }
})();
```

- [ ] **Step 2: Verify syntax**

Run: `node --check js/main.js`
Expected: no output (valid syntax).

- [ ] **Step 3: Commit**

```bash
git add js/main.js
git commit -m "Add mobile nav toggle and scroll-reveal JS

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Shared HTML building blocks

These blocks are reused verbatim across pages. Tasks below reference them by name.

**BLOCK A — `<head>` (landing page).** Paths are root-relative for `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Robert Ashe — Applied AI Engineer, Researcher, Co-Founder</title>
  <meta name="description" content="Robert Ashe — applied AI engineer and researcher building agentic systems and ML models that bridge software and the physical world. Co-author of BIM2RDT; co-founder of LARK.">
  <meta property="og:title" content="Robert Ashe — Applied AI Engineer, Researcher, Co-Founder">
  <meta property="og:description" content="Agentic AI, ML, and robotics — building systems where software meets the physical world.">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://nthperson.github.io/Project-Portfolio/assets/img/headshot.jpg">
  <meta name="twitter:card" content="summary">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,700;1,6..72,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
```

**BLOCK B — site navigation (landing page).** Detail pages use the same markup but with `../` prefixes and the brand linking to `../index.html`; anchor links point to `../index.html#...`.

```html
<nav class="site-nav">
  <div class="wrap">
    <a class="brand" href="#top">Robert Ashe</a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">MENU</button>
    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#featured-work">Work</a></li>
      <li><a href="#publications">Publications</a></li>
      <li><a href="#experience">Experience</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </div>
</nav>
```

**BLOCK C — footer.** Detail pages use the same markup.

```html
<footer class="site-footer">
  <div class="wrap">
    © 2026 Robert Ashe ·
    <a href="https://github.com/nthPerson/Project-Portfolio" target="_blank" rel="noopener">View this site on GitHub</a>
  </div>
</footer>
<script src="js/main.js"></script>
```

(Detail pages load the script with `../js/main.js`.)

---

## Task 7: Landing page — skeleton, hero, and About

**Files:**
- Create: `index.html` (overwrites the old file), `assets/favicon.svg`

- [ ] **Step 1: Create the favicon**

Create `assets/favicon.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#2A3B4D"/>
  <text x="32" y="44" font-family="Georgia, serif" font-size="34" font-weight="700"
        fill="#EDE8DD" text-anchor="middle">RA</text>
</svg>
```

- [ ] **Step 2: Create `index.html` with head, nav, hero, and About**

Use BLOCK A, then `<body id="top">`, then BLOCK B, then `<main>` containing the hero and About sections below. (Featured Work, Publications, Experience, More Projects, Contact, and the footer are added in Tasks 8–9.)

```html
<body id="top">
  <!-- BLOCK B: site navigation -->

  <main>
    <header class="hero wrap">
      <img class="hero-photo" src="assets/img/headshot.jpg"
           alt="Robert Ashe, head and shoulders portrait">
      <h1>Robert Ashe</h1>
      <span class="label role">Applied AI Engineer · Researcher · Co-Founder</span>
      <p class="intro">Building agentic systems and ML models that bridge software and the physical world.</p>
      <div class="hero-actions">
        <a class="btn btn-solid" href="#featured-work">View Work</a>
        <a class="btn btn-outline" href="assets/docs/Robert_Ashe_resume_Spring_2026.pdf" target="_blank" rel="noopener">Download CV</a>
      </div>
      <div class="hero-links">
        <a href="mailto:robertashe2.0@gmail.com">Email</a>
        <a href="https://www.linkedin.com/in/robert-ashe-a55b211a7/" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://github.com/nthPerson" target="_blank" rel="noopener">GitHub</a>
        <a href="https://arxiv.org/abs/2509.20705" target="_blank" rel="noopener">arXiv</a>
      </div>
      <div class="location">San Diego, CA</div>
    </header>

    <section class="section" id="about">
      <div class="wrap">
        <div class="section-head"><span class="label">About</span></div>
        <div class="about-grid reveal">
          <div class="about-text">
            <p>I'm an applied AI engineer and researcher who builds systems where software meets the physical world — agentic AI pipelines, machine-learning models, and the robotics and edge hardware they run on. I co-authored <strong>BIM2RDT</strong>, an agentic AI safety-first framework that turns building information models into robot-ready site digital twins, and I co-founded <strong>LARK Analysis Services</strong>, where I architected a multi-agent document-ingestion platform for the merchant card processing industry.</p>
            <p>I'm pursuing an M.S. in Big Data Analytics at San Diego State University (expected Spring 2027), after completing my B.S. in Computer Science there with a 4.0 major GPA, summa cum laude. I work as a research assistant in two SDSU labs — the Data-informed Construction Engineering (DiCE) Lab and the FAMAIL fairness-aware imitation-learning project. The throughline across all of it is the same: I like taking hard, ambiguous problems and turning them into systems that work.</p>
          </div>
          <img class="about-photo" src="assets/img/graduation.jpg"
               alt="Robert Ashe at his B.S. Computer Science graduation with family">
        </div>
      </div>
    </section>

    <!-- Task 8: Featured Work -->
    <!-- Task 9: Publications, Experience, More Projects, Contact -->
  </main>

  <!-- BLOCK C: footer -->
</body>
</html>
```

- [ ] **Step 3: Preview locally**

Run (background): `python3 -m http.server 8000`
Open `http://localhost:8000/` in a browser.
Expected: sticky nav, centered hero with circular headshot, intro, two buttons, social links; the About section shows two paragraphs beside the graduation photo. Fonts render as Newsreader (headings) / Inter (body).

- [ ] **Step 4: Validate HTML**

Run: `npx html-validate index.html`
Expected: no errors. (The file is incomplete but must still be well-formed; if html-validate complains about the unclosed structure, ignore only errors about the missing later sections — there should be none if the snippet is well-formed.)

- [ ] **Step 5: Commit**

```bash
git add index.html assets/favicon.svg
git commit -m "Build landing page hero and About section

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 8: Landing page — Featured Work section

**Files:**
- Modify: `index.html` (replace the `<!-- Task 8: Featured Work -->` comment)

Five alternating rows, order: LARK, BIM2RDT, FAMAIL, Caltrans ODA, Car Sounds. The CSS auto-alternates the visual side via `:nth-child(even)`.

- [ ] **Step 1: Insert the Featured Work section**

Replace `<!-- Task 8: Featured Work -->` in `index.html` with:

```html
<section class="section" id="featured-work">
  <div class="wrap">
    <div class="section-head"><span class="label">Featured Work</span>
      <h2>Selected projects</h2>
    </div>

    <article class="feature-row reveal">
      <div class="feature-visual">
        <img src="assets/img/lark-homepage.png" alt="LARK platform dashboard interface">
      </div>
      <div class="feature-text">
        <span class="label">01 · Multi-Agent · RAG · Co-Founder</span>
        <h3>LARK Analysis Services</h3>
        <p>An AI-native platform for merchant card processing professionals — a multi-agent document-ingestion pipeline and RAG-grounded analysis engine I architected as co-founder and lead AI engineer.</p>
        <a class="feature-link" href="projects/lark.html">Read the case study →</a>
      </div>
    </article>

    <article class="feature-row reveal">
      <div class="feature-visual">
        <img src="assets/img/bim2rdt-digital-twin.png" alt="BIM2RDT digital twin compared with a simulated real-world scene">
      </div>
      <div class="feature-text">
        <span class="label">02 · Robotics · BIM · Publication</span>
        <h3>BIM2RDT — Agentic Digital Twins</h3>
        <p>An arXiv-published agentic AI framework fusing building information models with live LiDAR/IMU data into robot-ready site digital twins — plus my active extension closing the loop with uncertainty-aware, evidential-deep-learning IFC updates.</p>
        <a class="feature-link" href="projects/bim2rdt.html">Read the case study →</a>
      </div>
    </article>

    <article class="feature-row reveal">
      <div class="feature-visual">
        <img src="assets/img/famail-trajectory.png" alt="FAMAIL trajectory modification dashboard with heatmaps">
      </div>
      <div class="feature-text">
        <span class="label">03 · PyTorch · Fairness · Research</span>
        <h3>FAMAIL — Fairness-Aware Imitation Learning</h3>
        <p>A spatial-temporal data augmentation framework for taxi GPS trajectories that reduces bias amplification in multi-agent imitation-learning policies trained on human behavior.</p>
        <a class="feature-link" href="projects/famail.html">Read the case study →</a>
      </div>
    </article>

    <article class="feature-row reveal">
      <div class="feature-visual">
        <img src="assets/img/caltrans-arcgis.png" alt="Caltrans Active Permitted Displays ArcGIS map viewer">
      </div>
      <div class="feature-text">
        <span class="label">04 · Crash-Data Analysis · Lead Developer</span>
        <h3>Caltrans ODA — Traffic Safety Study</h3>
        <p>Lead developer on a Caltrans-funded study of how outdoor advertising displays affect driver distraction — geospatial crash-data pipelines, propensity-score matching, and a driving-simulator experiment design.</p>
        <a class="feature-link" href="projects/caltrans-oda.html">Read the case study →</a>
      </div>
    </article>

    <article class="feature-row reveal">
      <div class="feature-visual">
        <img src="assets/img/car-sounds-hardware.png" alt="Car Sounds classifier hardware installed under-hood and in-cabin">
      </div>
      <div class="feature-text">
        <span class="label">05 · Edge AI · TinyML · Hardware</span>
        <h3>Car Sounds — On-Device Fault Diagnosis</h3>
        <p>A depthwise-separable CNN that classifies automotive faults from engine audio, post-training-quantized and deployed to an Arduino Nano 33 BLE Sense — AI/ML, data engineering, and hardware in one project.</p>
        <a class="feature-link" href="projects/car-sounds.html">Read the case study →</a>
      </div>
    </article>
  </div>
</section>
```

- [ ] **Step 2: Preview**

Reload `http://localhost:8000/`.
Expected: five project rows; rows 2 and 4 have the image on the right, rows 1/3/5 on the left. Each "Read the case study →" link is present (links will 404 until Tasks 10–14 — that is expected now).

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Add Featured Work section to landing page

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 9: Landing page — Publications, Experience, More Projects, Contact

**Files:**
- Modify: `index.html` (replace the `<!-- Task 9: ... -->` comment; add BLOCK C footer)

- [ ] **Step 1: Insert the remaining sections and footer**

Replace `<!-- Task 9: Publications, Experience, More Projects, Contact -->` with the four sections below, then append BLOCK C (footer) before `</body>`.

```html
<section class="section" id="publications">
  <div class="wrap">
    <div class="section-head"><span class="label">Publications</span>
      <h2>Peer-reviewed &amp; preprint work</h2>
    </div>
    <ul class="pub-list reveal">
      <li>
        <div class="pub-title">Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework</div>
        <div class="pub-meta">Akhavian, R., Amani, M., Mootz, J., Ashe, R., Beheshti, B. — arXiv:2509.20705 (2025).
          <a href="https://arxiv.org/abs/2509.20705" target="_blank" rel="noopener">arxiv.org/abs/2509.20705</a></div>
      </li>
      <li>
        <div class="pub-title">Accessible Control Framework for Unitree Robots</div>
        <div class="pub-meta">Co-authored. Accepted, ASCE International Conference on Computing in Civil Engineering (i3ce) 2025.</div>
      </li>
    </ul>
  </div>
</section>

<section class="section" id="experience">
  <div class="wrap">
    <div class="section-head"><span class="label">Experience</span>
      <h2>Roles &amp; research</h2>
    </div>
    <ul class="timeline reveal">
      <li>
        <div class="when">2024 — Present</div>
        <div>
          <div class="role-title">Research Assistant — SDSU DiCE Lab</div>
          <div class="org">Data-informed Construction Engineering Lab · PI: Dr. Reza Akhavian</div>
          <p>Co-authored BIM2RDT; lead developer on a Caltrans-funded traffic-safety study; co-authored the i3ce 2025 Unitree control-framework paper.</p>
        </div>
      </li>
      <li>
        <div class="when">Aug 2025 — Present</div>
        <div>
          <div class="role-title">Research Assistant — FAMAIL Project</div>
          <div class="org">Fairness-Aware Multi-Agent Imitation Learning · PI: Dr. Xin Zhang</div>
          <p>Developing a spatial-temporal data augmentation framework that reduces bias amplification in imitation-learning policies.</p>
        </div>
      </li>
      <li>
        <div class="when">Jan 2026 — Present</div>
        <div>
          <div class="role-title">Co-Founder &amp; Lead AI Engineer — LARK Analysis Services</div>
          <div class="org">AI-native platform for merchant card processing professionals</div>
          <p>Architected the multi-agent document-ingestion pipeline, RAG systems, the "Sidekick" agent, and multi-tenant admin features.</p>
        </div>
      </li>
      <li>
        <div class="when">2025 — Present</div>
        <div>
          <div class="role-title">Instructional Student Assistant — SDSU CS 420</div>
          <div class="org">Advanced Programming Languages</div>
          <p>Built and maintained an auto-grading system for Python, C, C++, and Scala submissions; held office hours on language design.</p>
        </div>
      </li>
      <li>
        <div class="when">2021 — Present</div>
        <div>
          <div class="role-title">Founder — Robert Ashe Designs</div>
          <div class="org">3D printing &amp; CAD</div>
          <p>Designed and manufactured 300+ custom parts for a mobile payment system used by Go Rentals across 220 nationwide locations.</p>
        </div>
      </li>
      <li>
        <div class="when">2024</div>
        <div>
          <div class="role-title">3D Printing Outreach Presenter — Miramar Ranch Elementary</div>
          <div class="org">STEM outreach</div>
          <p>Developed and led a hands-on 3D printing program presented to over 200 students.</p>
        </div>
      </li>
    </ul>
  </div>
</section>

<section class="section" id="more-projects">
  <div class="wrap">
    <div class="section-head"><span class="label">More Projects</span>
      <h2>Additional work on GitHub</h2>
    </div>
    <ul class="more-projects reveal">
      <li><a href="https://github.com/nthPerson/FEURCast" target="_blank" rel="noopener"><span class="mp-name">FEURcast</span><span class="mp-tag">SPY FORECASTING</span></a></li>
      <li><a href="https://github.com/nthPerson/From_Beats_to_Hits" target="_blank" rel="noopener"><span class="mp-name">From Beats to Hits</span><span class="mp-tag">MODEL SELECTION</span></a></li>
      <li><a href="https://github.com/nthPerson/Apple_Watch_Activity_Recognition" target="_blank" rel="noopener"><span class="mp-name">Apple Watch HAR</span><span class="mp-tag">ACTIVITY RECOGNITION</span></a></li>
      <li><a href="https://github.com/nthPerson/Machine_Learning" target="_blank" rel="noopener"><span class="mp-name">ML Implementations</span><span class="mp-tag">NUMPY · PYTORCH</span></a></li>
      <li><a href="https://github.com/nthPerson/UnitreeGO1-HRI-BIM" target="_blank" rel="noopener"><span class="mp-name">Unitree Go1 Framework</span><span class="mp-tag">ROBOTICS · i3ce</span></a></li>
      <li><a href="https://github.com/nthPerson/MIS686_Streaming_Service_Movie_-_TV_Data_Dashboard" target="_blank" rel="noopener"><span class="mp-name">Streaming Data Dashboard</span><span class="mp-tag">DATABASE</span></a></li>
    </ul>
  </div>
</section>

<section class="section" id="contact">
  <div class="wrap">
    <div class="section-head"><span class="label">Contact</span>
      <h2>Get in touch</h2>
    </div>
    <p class="reveal">Open to applied AI / ML engineering roles, research positions, and collaboration. The fastest way to reach me is email.</p>
    <div class="contact-links reveal">
      <a href="mailto:robertashe2.0@gmail.com">robertashe2.0@gmail.com</a>
      <a href="https://www.linkedin.com/in/robert-ashe-a55b211a7/" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://github.com/nthPerson" target="_blank" rel="noopener">GitHub · nthPerson</a>
      <a href="https://arxiv.org/abs/2509.20705" target="_blank" rel="noopener">arXiv · BIM2RDT</a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Preview and validate**

Reload `http://localhost:8000/`. Confirm all sections render with dividers between them.
Run: `npx html-validate index.html`
Expected: no errors. The landing page is now structurally complete.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Complete landing page: publications, experience, more projects, contact

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Detail page template

All five case-study pages share this structure. Task 10 builds LARK as the canonical reference; Tasks 11–14 reuse this exact skeleton with page-specific content.

**DETAIL TEMPLATE** — `<head>` uses BLOCK A with `../` on the `css`/`favicon` paths and a page-specific `<title>`/`<meta description>`. Body skeleton:

```html
<body id="top">
  <!-- BLOCK B navigation, with ../ prefixes:
       brand -> ../index.html ; links -> ../index.html#about etc. -->
  <main class="wrap">
    <a class="crumb" href="../index.html#featured-work">← Back to Work</a>

    <header class="detail-header">
      <span class="label"><!-- eyebrow metadata --></span>
      <h1><!-- project name --></h1>
      <p class="tagline"><!-- one-line tagline --></p>
    </header>

    <div class="detail-hero">
      <img src="../assets/img/<!-- hero image -->" alt="<!-- ... -->">
    </div>

    <div class="detail-layout">
      <aside class="detail-sidebar">
        <dl>
          <dt>Role</dt><dd><!-- ... --></dd>
          <dt>Timeline</dt><dd><!-- ... --></dd>
          <dt>Stack</dt><dd><!-- ... --></dd>
          <dt>Status</dt><dd><!-- ... --></dd>
          <dt>Links</dt><dd><!-- ... --></dd>
        </dl>
      </aside>

      <div class="detail-main">
        <section><span class="label">The Problem</span><h2>...</h2> ... </section>
        <section><span class="label">What I Built</span><h2>...</h2> ... </section>
        <section><span class="label">Architecture</span><h2>...</h2> ... </section>
        <section><span class="label">Highlights</span><h2>...</h2> ... </section>
        <section><span class="label">Tech Stack</span><h2>...</h2> ... </section>
        <section><span class="label">Gallery</span><h2>...</h2> ... </section>
      </div>
    </div>

    <nav class="prevnext">
      <a href="<!-- prev -->">← <!-- prev name --></a>
      <a href="<!-- next -->"><!-- next name --> →</a>
    </nav>
  </main>
  <!-- BLOCK C footer, with ../js/main.js -->
</body>
```

Prev/next ordering wraps: LARK ↔ BIM2RDT ↔ FAMAIL ↔ Caltrans ODA ↔ Car Sounds ↔ (back to LARK).

---

## Task 10: LARK detail page (canonical template)

**Files:**
- Create: `projects/lark.html`

Reference spec §6.1 (LARK) and §7 (LARK proprietary-safe strategy). **No repo link, no code, no prompts.**

- [ ] **Step 1: Create `projects/lark.html`**

Build the full page from the DETAIL TEMPLATE. `<title>`: "LARK Analysis Services — Robert Ashe". `<meta description>`: "LARK — an AI-native, multi-agent document-ingestion and RAG platform for merchant card processing, architected by Robert Ashe."

- Eyebrow: `Multi-Agent · RAG · Co-Founder · 2026`
- Tagline: "An AI-native platform for merchant card processing professionals."
- Hero image: `lark-homepage.png`, alt "LARK platform dashboard".
- Sidebar: Role "Co-Founder & Lead AI Engineer"; Timeline "Jan 2026 – Present"; Stack "Python · Multi-agent LLMs · RAG · REST APIs · Multi-tenant SaaS"; Status "Shipping — in active development"; Links "Private repository — demo available on request" (plain text, no link).

Section content (write as `<p>` paragraphs and lists inside each `<section>`):

- **The Problem** — "Merchant card processing statements arrive in dozens of incompatible formats, one per processor. Sales professionals reconcile them by hand to find interchange optimizations, downgrades, and the true effective rate a merchant pays. It is slow, error-prone work that does not scale."
- **What I Built** — "As co-founder and lead AI engineer I architected and built all of LARK's AI/ML systems and core backend. The platform normalizes statements from disparate processors into a single schema, then runs downstream analysis for interchange optimization, downgrade detection, and effective-rate calculation." Mention the "Sidekick" agent (proposal prep, portfolio analytics, statement Q&A), branded sales-proposal PDF generation, the portfolio analytics module, and multi-tenant admin (ISO/agent management, RBAC, user provisioning), plus the in-progress Echelon Payments integration.
- **Architecture** — describe the multi-agent ingestion pipeline + RAG grounding. Include the generated diagram (Step 2). One paragraph: "A multi-agent extraction pipeline parses each statement; a retrieval-augmented layer grounds agent reasoning in authoritative interchange rules and processor knowledge, so analysis cites real sources rather than hallucinating." Place a desktop screenshot figure: `lark-documents.png`, caption "Document ingestion and analysis workspace."
- **Highlights** — `<ul class="highlights">`: "Multi-agent pipeline normalizes statements across all major processors into one schema." · "RAG over interchange rules grounds agent reasoning in authoritative sources." · "Sidekick agent ships proposal prep, portfolio analytics, and document Q&A." · "Multi-tenant admin with role-based access control and user provisioning."
- **Tech Stack** — paragraph: "Python · multi-agent LLM orchestration · retrieval-augmented generation · REST APIs · multi-tenant SaaS architecture · branded PDF generation."
- **Gallery** — `<div class="gallery">` with figures: `lark-analysis-desktop.png` ("Analysis view — desktop") and `lark-sidekick-desktop.png` ("Sidekick AI agent — desktop"); then `lark-analysis-mobile.png` ("Analysis — mobile") and `lark-sidekick-mobile.png` ("Sidekick — mobile"). Add a sentence: "LARK is fully responsive — the same workflows on desktop and mobile."

Prev/next: prev `car-sounds.html` ("Car Sounds"), next `bim2rdt.html` ("BIM2RDT").

- [ ] **Step 2: Add the generated architecture diagram**

Inside the Architecture `<section>`, before the screenshot figure, add this diagram (pure HTML/CSS, on-brand — no image file):

```html
<div class="diagram" role="img" aria-label="LARK architecture: statements flow through a multi-agent ingestion pipeline and a RAG layer into normalized analysis.">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:0.6rem;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.74rem;text-transform:uppercase;letter-spacing:0.06em">
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Raw statements<br>(any processor)</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Multi-agent<br>extraction</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">RAG grounding<br>(interchange rules)</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Normalized<br>analysis</span>
  </div>
</div>
```

- [ ] **Step 3: Preview and validate**

Open `http://localhost:8000/projects/lark.html`.
Expected: back-link, header, hero image, sticky sidebar beside the narrative, all six sections, the architecture diagram, the gallery grid, prev/next nav. Confirm the sidebar Links field is the plain "Private repository" text with **no hyperlink**.
Run: `npx html-validate projects/lark.html` — expect no errors.

- [ ] **Step 4: Commit**

```bash
git add projects/lark.html
git commit -m "Build LARK case-study page (canonical detail template)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 11: BIM2RDT detail page (with EDL extension section)

**Files:**
- Create: `projects/bim2rdt.html`

Reference spec §6.1 (BIM2RDT). This page has an **extra `Current Research` section** for the EDL extension, placed after `Highlights`.

- [ ] **Step 1: Create `projects/bim2rdt.html` from the DETAIL TEMPLATE**

`<title>`: "BIM2RDT — Agentic Digital Twins — Robert Ashe". `<meta description>`: "BIM2RDT — an agentic AI safety-first framework turning building information models into robot-ready site digital twins, co-authored by Robert Ashe."

- Eyebrow: `Robotics · BIM · Publication · 2025`
- Tagline: "An agentic AI safety-first framework for robot-ready site digital twins."
- Hero image: `bim2rdt-digital-twin.png`, alt "BIM2RDT digital twin beside a simulated real-world construction scene".
- Sidebar: Role "Co-author — SDSU DiCE Lab"; Timeline "2024 – Present"; Stack "Agentic AI · BIM/IFC · LiDAR/IMU fusion · Semantic-Gravity ICP"; Status "Published — arXiv:2509.20705"; Links — two links: arXiv abstract `https://arxiv.org/abs/2509.20705` and paper PDF `https://arxiv.org/pdf/2509.20705`.

Sections:
- **The Problem** — "Building information models are created once, then drift out of date the moment construction begins. Robots operating on a site need a current, semantically rich model to navigate, inspect, and monitor safety — but keeping a BIM synchronized with the physical world is an unsolved problem."
- **What I Built** — "BIM2RDT is an agentic AI framework that fuses a static BIM with live LiDAR and IMU sensor data to produce safety-aware, robot-ready site digital twins. I co-authored the framework and contributed to its agentic pipeline, which grounds LLM-driven robot task planning in up-to-date geometric and semantic site context." Mention autonomous inspection, navigation, and safety monitoring.
- **Architecture** — describe the pipeline; embed figure `bim2rdt-figure1.png`, caption "BIM2RDT system overview (Figure 1, arXiv:2509.20705)." Add a paragraph on Semantic-Gravity ICP with figure `bim2rdt-sg-icp.png`, caption "Semantic-Gravity ICP registration — before and after alignment."
- **Highlights** — `<ul class="highlights">`: "Fuses BIM with live LiDAR/IMU data into robot-ready site digital twins." · "Semantic-Gravity ICP uses LLM-derived gravity priors to constrain scan-to-BIM registration." · "Writes IoT sensor events into the IFC model via IfcTask and IfcEvent entities." · "Supports autonomous inspection, navigation, and construction-safety monitoring." Include figure `bim2rdt-hav.png`, caption "Worker hand-arm-vibration (HAV) safety monitoring."
- **Current Research** (extra section — `<span class="label">Current Research</span><h2>Uncertainty-Aware Scan-to-BIM via Evidential Deep Learning</h2>`) — "BIM2RDT demonstrates perception and event injection but explicitly leaves the geometric update closure — deciding when a detected discrepancy should actually edit the BIM — as future work. My CONE 652 research proposal closes exactly that gap. It inserts a calibrated uncertainty layer between point-cloud semantic segmentation and IFC editing: a segmentation network with an evidential deep learning head produces per-point uncertainty in a single forward pass, and a decision policy maps uncertainty and scan-vs-BIM discrepancy onto an action set — autonomous update, human review, mark-missing, or ignore — committing autonomous edits only when perception and geometry agree." Embed figure `edl-figure1.png`, caption "Proposed uncertainty-aware Scan-to-BIM pipeline." Embed figure `edl-decision-map.png`, caption "Decision policy over the (uncertainty, discrepancy) plane." Add a `<div class="downloads">` with two buttons: `<a class="btn btn-outline" href="../assets/docs/edl-proposal.pdf" target="_blank" rel="noopener">Download the proposal (PDF)</a>` and `<a class="btn btn-outline" href="../assets/docs/edl-slides.pdf" target="_blank" rel="noopener">Presentation slides (PDF)</a>`.
- **Tech Stack** — "Agentic AI / multi-agent LLMs · BIM and IFC (IfcOpenShell) · LiDAR and IMU sensor fusion · point-cloud semantic segmentation · evidential deep learning · PyTorch."
- **Gallery** — `<div class="gallery">` with the related DiCE Lab robotics photos, each captioned as related work: `../assets/go1_full_assembly_2.jpg` ("Unitree Go1 sensor platform — related DiCE Lab robotics work"), `../assets/go1_side_view_2.jpg` ("Go1 quadruped — related DiCE Lab robotics work"). Add a sentence noting these are from the related i3ce Unitree control-framework project.

Prev/next: prev `lark.html` ("LARK"), next `famail.html` ("FAMAIL").

- [ ] **Step 2: Preview and validate**

Open `http://localhost:8000/projects/bim2rdt.html`. Confirm seven narrative sections (the extra Current Research section present), all figures load, both PDF download buttons work, both arXiv links present in the sidebar.
Run: `npx html-validate projects/bim2rdt.html` — expect no errors.

- [ ] **Step 3: Commit**

```bash
git add projects/bim2rdt.html
git commit -m "Build BIM2RDT case-study page with EDL extension section

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 12: FAMAIL detail page

**Files:**
- Create: `projects/famail.html`

Reference spec §6.1 (FAMAIL).

- [ ] **Step 1: Create `projects/famail.html` from the DETAIL TEMPLATE**

`<title>`: "FAMAIL — Fairness-Aware Imitation Learning — Robert Ashe". `<meta description>`: "FAMAIL — a spatial-temporal data augmentation framework reducing bias amplification in multi-agent imitation learning, by Robert Ashe."

- Eyebrow: `PyTorch · Fairness · Research · 2025–`
- Tagline: "Reducing bias amplification in multi-agent imitation learning."
- Hero image: `famail-trajectory.png`, alt "FAMAIL trajectory modification dashboard with two heatmaps".
- Sidebar: Role "Research Assistant — SDSU"; Timeline "Aug 2025 – Present"; Stack "PyTorch · Imitation learning · Fairness/bias mitigation · Spatial-temporal data · HPC"; Status "Ongoing research"; Links — two: GitHub repo `https://github.com/nthPerson/FAMAIL` and project site `https://nthperson.github.io/FAMAIL/`.

Sections:
- **The Problem** — "Imitation-learning models trained on human-generated trajectories inherit human bias — and can amplify it. In urban mobility, behavioral cloning from taxi GPS data can entrench inequitable service patterns if left unchecked."
- **What I Built** — "I'm developing a spatial-temporal data augmentation framework for taxi GPS trajectories that mitigates the propagation and amplification of human bias. I design PyTorch augmentation operators that perturb spatial-temporal features while preserving task-relevant structure, yielding fairer multi-agent imitation-learning policies."
- **Architecture** — describe the augmentation pipeline; include the generated diagram (Step 2). Embed figure `famail-objective-function.png`, caption "Objective-function analysis dashboard."
- **Highlights** — `<ul class="highlights">`: "PyTorch augmentation operators perturb spatial-temporal features while preserving task structure." · "Cut augmentation runtime from 16 days (CPU) to 39 minutes by partitioning workloads across CPU and GPU." · "Contributes to a broader research agenda on responsible AI in urban systems." Include figure `famail-causal-fairness.png`, caption "Causal-fairness term dashboard."
- **Tech Stack** — "PyTorch · imitation learning / behavioral cloning · fairness and bias mitigation · spatial-temporal data processing · high-performance computing (CPU/GPU workload partitioning)."
- **Gallery** — `<div class="gallery">` figures: `famail-temporal-patterns.png` ("Causal-fairness temporal patterns") and `famail-trajectory.png` ("Trajectory modification dashboard"). Add a sentence linking to the dedicated FAMAIL project site for more.

Prev/next: prev `bim2rdt.html` ("BIM2RDT"), next `caltrans-oda.html` ("Caltrans ODA").

- [ ] **Step 2: Add the generated methodology diagram**

Inside the Architecture `<section>`, add:

```html
<div class="diagram" role="img" aria-label="FAMAIL augmentation pipeline: human taxi trajectories pass through spatial-temporal augmentation operators into a fairer imitation-learning policy.">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:0.6rem;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.74rem;text-transform:uppercase;letter-spacing:0.06em">
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Human taxi<br>trajectories</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Spatial-temporal<br>augmentation</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Multi-agent<br>imitation learning</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Fairer<br>policy</span>
  </div>
</div>
```

- [ ] **Step 3: Preview and validate**

Open `http://localhost:8000/projects/famail.html`. Confirm sections, diagram, figures, and both sidebar links.
Run: `npx html-validate projects/famail.html` — expect no errors.

- [ ] **Step 4: Commit**

```bash
git add projects/famail.html
git commit -m "Build FAMAIL case-study page

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 13: Caltrans ODA detail page

**Files:**
- Create: `projects/caltrans-oda.html`

Reference spec §6.1 (Caltrans ODA). Materials are largely confidential — this page leans on generated diagrams.

- [ ] **Step 1: Create `projects/caltrans-oda.html` from the DETAIL TEMPLATE**

`<title>`: "Caltrans ODA — Traffic Safety Study — Robert Ashe". `<meta description>`: "Caltrans ODA — a study of how outdoor advertising displays affect driver distraction and traffic safety; lead developer Robert Ashe."

- Eyebrow: `Crash-Data Analysis · Lead Developer · 2024–`
- Tagline: "How outdoor advertising displays affect driver distraction and traffic safety."
- Hero image: `caltrans-arcgis.png`, alt "Caltrans Active Permitted Displays ArcGIS map viewer".
- Sidebar: Role "Lead Developer — SDSU DiCE Lab"; Timeline "2024 – Present"; Stack "SWITRS/geospatial analysis · Multivariate regression · Propensity-score matching · Pupil Core eye tracking · EMOTIV EPOC X EEG · DriveSafety RS-250"; Status "Ongoing research"; Links — Caltrans Active Permitted Displays Map Viewer `https://caltrans.maps.arcgis.com/apps/webappviewer/index.html?id=f0bb9147535d49a4bd24099475883c15`.

Sections:
- **The Problem** — "Outdoor advertising displays — static billboards and digital signs — line California highways. Whether, and how much, they distract drivers and affect collision rates is a question with real public-safety stakes and no easy answer: traffic volume, road geometry, weather, and time of day all confound the signal."
- **What I Built** — "I'm lead developer on a Caltrans-funded research contract (65A1302) studying the impact of outdoor advertising displays on traffic safety. I built crash-data analysis pipelines over SWITRS records, TSN, and Traffic Collision Reports, using geospatial joins to associate collisions with display locations along California highway segments."
- **Architecture** — "The analysis pipeline ingests heterogeneous crash datasets, joins them geospatially to permitted-display locations, and applies statistical methods that isolate the display effect from confounders." Include the generated crash-data pipeline diagram (Step 2). Note the provided ArcGIS screenshot (hero) is the public Caltrans Active Permitted Displays Map Viewer used to locate displays.
- **Highlights** — `<ul class="highlights">`: "Built crash-data pipelines over SWITRS, TSN, and Traffic Collision Report datasets." · "Geospatial joins associate collisions with outdoor-display locations along highway segments." · "Applied multivariate regression and propensity-score matching to isolate the display effect from traffic volume, road geometry, weather, and time of day." · "Contributed to a driving-simulator experiment design on the DriveSafety RS-250, scripting scenarios in HyperDrive TCL." · "Helped define analysis plans for eye-tracking (Pupil Core) and EEG (EMOTIV EPOC X) data."
- **Architecture (study design)** — add the generated study-design diagram (Step 2) under a paragraph: "Beyond the observational crash-data study, the project includes a controlled driving-simulator experiment combining eye-tracking and EEG to measure driver distraction directly."
- **Tech Stack** — "SWITRS / geospatial crash-data analysis · multivariate regression · propensity-score matching · Pupil Core eye tracker · EMOTIV EPOC X 14 EEG · DriveSafety RS-250 simulator · HyperDrive TCL scripting · Python (NumPy/Pandas)."
- **Gallery** — single figure: `caltrans-arcgis.png` wrapped in a link to the live viewer, caption "Caltrans Active Permitted Displays Map Viewer (public ArcGIS app). Most project materials are confidential."

Note: this page has no separate "Gallery grid" beyond the one figure; that is intentional given confidentiality.

Prev/next: prev `famail.html` ("FAMAIL"), next `car-sounds.html` ("Car Sounds").

- [ ] **Step 2: Add the two generated diagrams**

Crash-data pipeline diagram (in the first Architecture section):

```html
<div class="diagram" role="img" aria-label="Caltrans crash-data pipeline: SWITRS, TSN, and Traffic Collision Report data are joined geospatially to display locations, then analyzed with regression and propensity-score matching.">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:0.6rem;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.74rem;text-transform:uppercase;letter-spacing:0.06em">
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">SWITRS · TSN · TCR<br>crash data</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Geospatial join<br>to displays</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Regression +<br>propensity matching</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Isolated<br>display effect</span>
  </div>
</div>
```

Study-design diagram (in the study-design Architecture paragraph):

```html
<div class="diagram" role="img" aria-label="Driving-simulator study design: DriveSafety RS-250 scenarios are measured with eye tracking and EEG to quantify driver distraction.">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:0.6rem;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.74rem;text-transform:uppercase;letter-spacing:0.06em">
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">DriveSafety RS-250<br>scenarios (TCL)</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Pupil Core<br>eye tracking</span>
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">EMOTIV EPOC X<br>EEG</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Distraction<br>metrics</span>
  </div>
</div>
```

- [ ] **Step 3: Preview and validate**

Open `http://localhost:8000/projects/caltrans-oda.html`. Confirm both diagrams render, the hero ArcGIS screenshot links to the live viewer.
Run: `npx html-validate projects/caltrans-oda.html` — expect no errors.

- [ ] **Step 4: Commit**

```bash
git add projects/caltrans-oda.html
git commit -m "Build Caltrans ODA case-study page

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 14: Car Sounds detail page

**Files:**
- Create: `projects/car-sounds.html`

Reference spec §6.1 (Car Sounds). This page is figure-rich — feature all eight result figures and the downloadable report.

- [ ] **Step 1: Create `projects/car-sounds.html` from the DETAIL TEMPLATE**

`<title>`: "Car Sounds — On-Device Fault Diagnosis — Robert Ashe". `<meta description>`: "Car Sounds — a depthwise-separable CNN for automotive fault diagnosis, quantized and deployed to an Arduino Nano 33 BLE Sense, by Robert Ashe."

- Eyebrow: `Edge AI · TinyML · Hardware · 2026`
- Tagline: "On-device automotive fault diagnosis from engine audio."
- Hero image: `car-sounds-hardware.png`, alt "Car Sounds classifier hardware installed under-hood and in-cabin".
- Sidebar: Role "Graduate ML / TinyML coursework"; Timeline "2026"; Stack "PyTorch/TensorFlow · Depthwise-separable CNN · Mel-spectrograms · Post-training quantization · Arduino Nano 33 BLE Sense Rev2"; Status "Complete"; Links — GitHub repo `https://github.com/nthPerson/Car_Sounds_Classification`.

Sections:
- **The Problem** — "Automotive faults often announce themselves in sound long before a dashboard light. Diagnosing them on-device — with no cloud, no connectivity, and a microcontroller's memory budget — means a model that is both accurate and tiny."
- **What I Built** — "I designed a depthwise-separable convolutional neural network (DS-CNN) that classifies automotive faults from engine and vehicle audio using mel-spectrogram features. I applied post-training quantization and deployed the model to an Arduino Nano 33 BLE Sense Rev2, demonstrating sub-second inference on edge hardware." Embed figure `car-sounds-melspec.png`, caption "Log-mel-spectrogram inputs across vehicle sound classes."
- **Architecture** — add the generated DS-CNN pipeline diagram (Step 2). Paragraph: "Audio is captured on-device, transformed into log-mel-spectrograms, classified by the DS-CNN, and the model is post-training-quantized to fit the microcontroller."
- **Highlights** — `<ul class="highlights">`: "Depthwise-separable CNN classifies faults from mel-spectrogram audio features." · "Post-training quantization shrinks the model to fit a microcontroller with minimal accuracy loss." · "Deployed to an Arduino Nano 33 BLE Sense Rev2 with sub-second on-device inference." · "Profiled accuracy, latency, and memory trade-offs across model variants." Embed figure `car-sounds-accuracy-bar.png`, caption "Classification accuracy across all models, including baselines."
- **Results** (use `<span class="label">Results</span><h2>Results</h2>`) — a results showcase. Intro sentence, then a `<div class="gallery">` with figures: `car-sounds-accuracy-vs-size.png` ("Accuracy vs. model size"), `car-sounds-augmentation.png` ("Data-augmentation ablation"), `car-sounds-quantization.png` ("Quantization impact"), `car-sounds-latency.png` ("Inference-cycle latency breakdown"). Then a full-width figure `car-sounds-resource-util.png`, caption "On-device resource utilization of the deployed M6 DS-CNN model."
- **Tech Stack** — "PyTorch / TensorFlow · depthwise-separable CNN · mel-spectrogram feature extraction · post-training quantization (PTQ) · Arduino Nano 33 BLE Sense Rev2 · edge-AI deployment."
- **Gallery** — replace the generic Gallery section with a download: `<span class="label">Full Report</span><h2>Read the full report</h2>`, a sentence, and `<div class="downloads"><a class="btn btn-outline" href="../assets/docs/car-sounds-report.pdf" target="_blank" rel="noopener">Download the final report (PDF)</a></div>`.

Prev/next: prev `caltrans-oda.html` ("Caltrans ODA"), next `lark.html` ("LARK").

- [ ] **Step 2: Add the generated DS-CNN pipeline diagram**

Inside the Architecture `<section>`:

```html
<div class="diagram" role="img" aria-label="Car Sounds pipeline: engine audio becomes a mel-spectrogram, is classified by a depthwise-separable CNN, quantized, and runs on an Arduino.">
  <div style="display:flex;align-items:center;justify-content:space-between;gap:0.6rem;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.74rem;text-transform:uppercase;letter-spacing:0.06em">
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Engine<br>audio</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">Log-mel<br>spectrogram</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--ink);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">DS-CNN +<br>quantization</span>
    <span style="color:var(--accent)">→</span>
    <span style="background:var(--accent);color:var(--paper);padding:0.7rem 0.9rem;border-radius:6px">On-device<br>inference (Arduino)</span>
  </div>
</div>
```

- [ ] **Step 3: Preview and validate**

Open `http://localhost:8000/projects/car-sounds.html`. Confirm all 8 figures load, the diagram renders, the report download works.
Run: `npx html-validate projects/car-sounds.html` — expect no errors.

- [ ] **Step 4: Commit**

```bash
git add projects/car-sounds.html
git commit -m "Build Car Sounds case-study page

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 15: Cross-page QA — links, responsive, accessibility

**Files:**
- Modify: any page needing fixes found during QA

- [ ] **Step 1: Link check**

With the local server running, click through every page: landing nav anchors, all five "Read the case study" links, every prev/next link (confirm the cycle wraps LARK→BIM2RDT→FAMAIL→Caltrans→Car Sounds→LARK), every "Back to Work" crumb, all external links, and all four PDF downloads.
Expected: no 404s; every link resolves. Fix any broken `href`.

- [ ] **Step 2: Responsive check**

In the browser dev tools, view the landing page and one detail page at 375px, 768px, and 1280px widths.
Expected at 375px: the nav collapses behind the MENU button and the toggle opens/closes it; feature rows stack to one column; the detail page is single-column with a non-sticky sidebar; galleries are one column. Fix any overflow or broken layout.

- [ ] **Step 3: Accessibility check**

Confirm: every `<img>` has a meaningful `alt`; every page has exactly one `<h1>`; heading levels do not skip; the mobile toggle has `aria-expanded` that flips on click; text/background contrast is acceptable (body text is `--ink` on `--paper`, never `--accent`).
Run: `npx html-validate index.html projects/*.html`
Expected: no errors across all six pages.

- [ ] **Step 4: Commit any fixes**

```bash
git add -A
git commit -m "Fix issues found in cross-page QA (links, responsive, accessibility)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

(If QA found no issues, skip the commit.)

---

## Task 16: Final verification and deploy

**Files:**
- Modify: none (verification + merge)

- [ ] **Step 1: Full-site smoke test**

Restart the local server fresh. Load all six pages. Confirm: fonts load (Newsreader/Inter/JetBrains Mono — no fallback flash of Times/Arial only), the hero headshot and About graduation photo display, all project images load, scroll-reveal animations fire, the favicon appears in the browser tab.

- [ ] **Step 2: Confirm legacy content is gone**

Run: `ls` and confirm `bootstrap.min.sandstone.css`, `programming/`, `industrial/`, `outreach/` no longer exist. Confirm `index.html` no longer references Bootstrap.
Run: `grep -ri "bootstrap" index.html projects/ css/ || echo "clean"`
Expected: `clean`.

- [ ] **Step 3: Verify the LARK proprietary-safe rule**

Run: `grep -ri "github.com/nthPerson/LARK\|lark.*repo" projects/lark.html || echo "no LARK repo link — correct"`
Expected: `no LARK repo link — correct`. Manually confirm `projects/lark.html` contains no code snippets and the sidebar Links field is plain text.

- [ ] **Step 4: Merge to `main` and deploy**

```bash
git checkout main
git merge --no-ff portfolio-rework -m "Merge portfolio site rework"
git push origin main
```

GitHub Pages serves `main` automatically.

- [ ] **Step 5: Verify the live site**

After ~1–2 minutes, open `https://nthperson.github.io/Project-Portfolio/` and spot-check the landing page and one detail page live.
Expected: the reworked site is live and matches local preview.

---

## Self-Review Notes

**Spec coverage check (against `2026-05-16-portfolio-rework-design.md`):**
- §3 architecture (landing + 5 detail pages, static, no build) → Tasks 1, 7–14.
- §4 visual system (Parchment palette, fonts, layout primitives) → Tasks 3–5.
- §5 landing sections (hero, about, featured work, publications, experience, more projects, contact, footer) → Tasks 7–9.
- §6 detail template (two-column sticky sidebar, six sections, prev/next) → Tasks 10–14.
- §6.1 per-project content & assets → Tasks 10–14 (each cites its assets).
- §7 LARK proprietary-safe strategy → Task 10 + Task 16 Step 3 verification.
- §8 legacy content disposition → Task 1 (removals), Task 9 (Go1/3D-printing into experience), Task 16 Step 2.
- §9 file structure, image optimization → Tasks 1, 2.
- §10 accessibility, SEO/meta, responsive → BLOCK A meta, Task 5, Task 15.
- §11 asset inventory, generated diagrams, fallbacks → Task 2, generated diagrams in Tasks 10–14, `.titlecard` fallback in Task 4.
- §13 open items (fonts, generated diagrams) → resolved in plan (fonts in BLOCK A; diagrams specified inline).

All spec requirements map to tasks. No placeholders remain; all class names and asset filenames are consistent across tasks.
