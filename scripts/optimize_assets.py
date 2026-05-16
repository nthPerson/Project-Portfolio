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
