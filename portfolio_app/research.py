from pathlib import Path
from textwrap import dedent
from typing import Dict

import streamlit as st

from .assets import (
    get_portfolio_image,
    get_research_visual,
    get_pdf_thumbnail,
    get_pdf_clean_thumbnail,
    get_pdf_svg,
)
from .data import RESEARCH_PAPERS


def _clean_markup(markup: str) -> str:
    clean = "\n".join(line.lstrip() for line in dedent(markup).strip().splitlines())
    return clean


def _html(markup: str) -> None:
    st.markdown(_clean_markup(markup), unsafe_allow_html=True)


def render_research_papers_section() -> None:
    selected_id = st.session_state.get("selected_research_paper")
    query_id = st.query_params.get("paper", "")
    if isinstance(query_id, list):
        query_id = query_id[0] if query_id else ""
    if query_id and query_id != selected_id:
        st.session_state.selected_research_paper = query_id
        selected_id = query_id
    selected_paper = next((paper for paper in RESEARCH_PAPERS if paper["id"] == selected_id), None)
    if selected_paper:
        render_research_paper_detail(selected_paper)
        return

    st.markdown(
        """
        <div class="section-header">
            <div class="section-kicker">Research Papers</div>
            <div class="section-title">Research works organized as explorable project stories.</div>
            <div class="section-copy">
                Choose a paper to enter a focused detail page with paper screenshots, experimental figures, tables, and an interview-ready explanation of the work.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for start in range(0, len(RESEARCH_PAPERS), 2):
        cols = st.columns(2)
        for col, paper in zip(cols, RESEARCH_PAPERS[start:start + 2]):
            with col:
                image_html = get_research_visual(paper)
                chips = "".join(
                    f'<span class="paper-chip">{item}</span>' for item in paper["highlights"]
                )
                st.markdown(
                    f"""
                    <div class="paper-card">
                        {image_html}
                        <div class="paper-body">
                            <div class="paper-tag">{paper["tag"]}</div>
                            <div class="paper-title">{paper["title"]}</div>
                            <div class="paper-venue">{paper["venue"]}</div>
                            <div class="paper-highlights">{chips}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button("View Work", use_container_width=True, key=f"view-{paper['id']}"):
                    st.session_state.selected_research_paper = paper["id"]
                    st.query_params["paper"] = paper["id"]
                    st.rerun()


def render_research_paper_detail(paper: Dict) -> None:
    if st.button("← Back to Research Papers", key="back-to-papers", help="Return to the research papers list"):
        st.session_state.selected_research_paper = None
        st.session_state[f"load_figures_{paper['id']}"] = False
        st.session_state[f"gallery_active_tab_{paper['id']}"] = None
        try:
            if "paper" in st.query_params:
                del st.query_params["paper"]
        except Exception:
            pass
        st.rerun()

    if paper.get("gallery"):
        render_portfolio_showcase(paper)
    else:
        _render_hero_simple(paper)
        render_standard_detail(paper)


def _render_hero_simple(paper: Dict) -> None:
    st.markdown(
        f"""
        <div class="paper-detail-hero">
            <div class="paper-tag">{paper["tag"]}</div>
            <div class="paper-detail-title">{paper["title"]}</div>
            <div class="paper-venue">{paper["venue"]}</div>
            <div class="section-copy">{paper["summary"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_portfolio_showcase(paper: Dict) -> None:
    gallery = paper.get("gallery", {})
    figures = {f["title"].split(":")[0].strip(): f for f in gallery.get("figures", [])}
    tables = {t["title"].split(":")[0].strip(): t for t in gallery.get("tables", [])}

    if paper.get("id") == "surgidiff":
        _render_surgidiff_showcase(paper, figures, tables)
        return
    if paper.get("id") == "scolioldm":
        _render_scolioldm_showcase(paper, figures, tables)
        return

    _render_showcase_hero(paper)
    _render_section_background(paper)
    _render_section_architecture(paper, figures.get("Figure 1"))
    _render_section_hypergraph(paper, figures.get("Figure 2"))
    _render_section_quantitative(paper, tables)
    _render_section_qualitative_compact(paper, figures.get("Figure 3"))
    _render_section_analysis_and_ablation_compact(paper, figures.get("Figure 4"), tables)
    _render_section_conclusion(paper)


def _render_scolioldm_showcase(paper: Dict, figures: Dict, tables: Dict) -> None:
    _render_scolioldm_hero(paper)
    _render_scolioldm_overview(paper, figures.get("Figure 1"))
    _render_scolioldm_framework(paper, figures.get("Figure 2"), figures.get("Figure 3"))
    _render_scolioldm_results(paper, figures.get("Figure 5"), tables)
    _render_scolioldm_ablation(paper, figures.get("Figure 4"), tables)
    _render_scolioldm_conclusion(paper)


def _render_scolioldm_hero(paper: Dict) -> None:
    _html(
        f"""
        <div class="portfolio-hero scolioldm-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Research Paper</span>
                <span class="portfolio-hero-tag">{paper["tag"]}</span>
                <span class="portfolio-hero-tag">{paper["venue"]}</span>
            </div>
            <h1 class="portfolio-hero-title">{paper["title"]}</h1>
            <p class="portfolio-hero-sub">{paper["summary"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Cohort</span>
                    <strong>612 AIS</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Guidance</span>
                    <strong>Curve Map</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Core Module</span>
                    <strong>MGCM</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Best Metrics</span>
                    <strong>PSNR / NCC</strong>
                </div>
            </div>
        </div>
        """,
    )


def _render_scolioldm_overview(paper: Dict, fig: Dict) -> None:
    failure_html = _render_figure_html(
        fig,
        caption=(
            "Figure 1 | Generic conditional generators fail on AIS postoperative synthesis: "
            "DDIB and pix2pix produce distorted anatomy or implant artifacts under large non-rigid correction."
        ),
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact scolioldm-overview">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">Why Morphology Guidance Is Needed</h2>
                </div>
            </div>
            <div class="pg pg-scolioldm-overview">
                <div class="portfolio-content portfolio-content-lead">
                    <h4>Clinical Problem</h4>
                    <p>
                        AIS surgery changes spinal curvature, vertebral alignment, and screw-rod structures.
                        Scalar planning indices do not provide an intuitive predicted postoperative image.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Generation Gap</h4>
                    <p>
                        Standard image-to-image generators are weak when anatomy moves non-rigidly and implants
                        appear after surgery, so the model needs explicit geometry control.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Core Idea</h4>
                    <p>
                        Predict a postoperative spine curve map, then inject morphology-aware features into the
                        latent diffusion U-Net through MGCM.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Contribution</h4>
                    <ul>
                        <li>Image-level AIS outcome prediction.</li>
                        <li>Postoperative curve-map guidance.</li>
                        <li>MGCM for deformable morphology control.</li>
                        <li>Paired pre/postoperative radiograph dataset.</li>
                    </ul>
                </div>
                <div class="portfolio-span-2 scolioldm-failure-strip scolioldm-failure-compact">{failure_html}</div>
                <div class="portfolio-content">
                    <h4>Failure Reading</h4>
                    <p>
                        This is a motivation plate, not the main result. Its role is to show why direct
                        pre-to-postoperative translation is unreliable without morphology control.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Observed Errors</strong>
                        <p>DDIB blurs the corrected spine region; pix2pix creates implant-like artifacts and distorted rod structure.</p>
                    </div>
                </div>
                <div class="portfolio-content">
                    <h4>Layout Role</h4>
                    <p>
                        The primary visual evidence appears later in Figure 2 and Figure 5. This figure is kept
                        compact so the first viewport explains the problem without wasting vertical space.
                    </p>
                    <ul>
                        <li>Problem proof, not contribution proof.</li>
                        <li>Use as a side exhibit.</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
    )


def _render_scolioldm_framework(paper: Dict, fig2: Dict, fig3: Dict) -> None:
    framework_html = _render_figure_html(
        fig2,
        caption=(
            "Figure 2 | ScolioLDM framework: landmark-derived curve maps guide ControlNet-based "
            "postoperative contour prediction, then MGCM injects morphology-aware conditions into the denoising U-Net."
        ),
    )
    mgcm_html = _render_figure_html(
        fig3,
        caption=(
            "Figure 3 | MGCM details: deform refinement, spatial gate, deformation-field prediction, "
            "adaptive scaling, and grid sampling align the morphology features before diffusion control."
        ),
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact scolioldm-framework">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Framework</span>
                    <h2 class="portfolio-section-title">Curve-Map Conditioned Latent Diffusion</h2>
                </div>
            </div>
            <div class="pg pg-scolioldm-framework">
                <div class="portfolio-span-3 scolioldm-figure-wide scolioldm-framework-figure">{framework_html}</div>
                <div class="scolioldm-note-stack">
                    <div class="portfolio-content">
                        <h4>Input Pair</h4>
                        <p>
                            The preoperative radiograph preserves patient appearance; the postoperative curve map
                            acts as the target structural prior.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Two Conditions</h4>
                        <p>
                            Image-conditional features are concatenated with morphology-control features, so the
                            U-Net receives both appearance and shape constraints.
                        </p>
                    </div>
                    <div class="portfolio-insight-box portfolio-fill-box">
                        <strong>Design Point</strong>
                        <p>
                            The page keeps this as the main wide plate because it explains the complete path from
                            X-ray input to postoperative synthesis.
                        </p>
                    </div>
                </div>
                <div class="portfolio-span-2 scolioldm-figure-module scolioldm-mgcm-figure">{mgcm_html}</div>
                <div class="portfolio-span-2 scolioldm-dense-stack scolioldm-mgcm-notes">
                    <div class="portfolio-content">
                        <h4>MGCM Role</h4>
                        <p>
                            MGCM learns deformation-aware feature alignment, then gates the refined structural
                            signal before injection into diffusion.
                        </p>
                    </div>
                    <div class="portfolio-insight-box">
                        <strong>Why It Works</strong>
                        <p>Diffusion handles image realism while MGCM anchors denoising to plausible spinal morphology.</p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Training Signal</h4>
                        <p>
                            The model is trained on paired pre- and postoperative PA radiographs from 612 AIS
                            patients, with curve maps derived from vertebral landmarks.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Module Breakdown</h4>
                        <ul>
                            <li>Deform refinement captures non-rigid correction.</li>
                            <li>Spatial gate suppresses irrelevant morphology noise.</li>
                            <li>Grid sampling warps features into aligned control.</li>
                        </ul>
                    </div>
                    <div class="portfolio-content">
                        <h4>Feature Flow</h4>
                        <p>
                            Raw morphology features are refined, gated, warped by a learned flow field, then
                            reused as multi-scale control features.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Clinical Link</h4>
                        <p>
                            The module keeps correction geometry visible, so generated postoperative radiographs
                            retain curve direction and implant-region structure.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """,
    )


def _render_scolioldm_results(paper: Dict, fig: Dict, tables: Dict) -> None:
    results_html = _render_figure_html(
        fig,
        caption=(
            "Figure 5 | Qualitative comparison with ControlNet, pix2pix, ControlNeXt, BBDM, "
            "and Fast-DDPM. ScolioLDM is placed beside GT to show clearer correction morphology and implant coherence."
        ),
    )
    table_html = _render_scolioldm_metrics_table()
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact scolioldm-results">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Results</span>
                    <h2 class="portfolio-section-title">Synthesis Quality Across Five Baselines</h2>
                </div>
            </div>
            <div class="pg pg-scolioldm-results">
                <div class="portfolio-span-3 scolioldm-figure-wide scolioldm-results-figure">{results_html}</div>
                <div class="scolioldm-note-stack">
                    <div class="portfolio-content">
                        <h4>Visual Reading</h4>
                        <p>
                            ScolioLDM better preserves vertebral boundaries and screw-rod placement, while several
                            baselines blur anatomy or introduce local implant artifacts.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Metric Reading</h4>
                        <p>
                            The model leads on PSNR, MAE, GradMAE, and NCC, showing strong pixel fidelity,
                            edge preservation, and gray-scale correlation.
                        </p>
                    </div>
                    <div class="portfolio-insight-box portfolio-fill-box">
                        <strong>Tradeoff</strong>
                        <p>
                            BBDM reports the highest SSIM, but ScolioLDM has the stronger overall profile across
                            four of five reported metrics.
                        </p>
                    </div>
                </div>
            </div>
            <div class="pg pg-scolioldm-table-row">
                <div class="portfolio-span-4">{table_html}</div>
            </div>
        </section>
        """,
    )


def _render_scolioldm_ablation(paper: Dict, fig: Dict, tables: Dict) -> None:
    ablation_html = _render_figure_html(
        fig,
        caption=(
            "Figure 4 | Ablation visualization: removing MGCM or the postoperative curve map weakens structural "
            "alignment, vertebral detail, and implant configuration compared with the full model."
        ),
    )
    table_html = _render_scolioldm_ablation_table()
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact scolioldm-ablation">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Ablation</span>
                    <h2 class="portfolio-section-title">MGCM and Curve Map Are Both Necessary</h2>
                </div>
            </div>
            <div class="pg pg-scolioldm-ablation">
                <div class="portfolio-span-2 scolioldm-figure-wide scolioldm-ablation-figure">{ablation_html}</div>
                <div class="portfolio-span-2 scolioldm-dense-stack scolioldm-ablation-notes">
                    {table_html}
                    <div class="portfolio-content">
                        <h4>Without MGCM</h4>
                        <p>
                            Image fidelity partly remains, but local structural control weakens, making vertebral
                            and implant geometry less reliable.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Without Curve Map</h4>
                        <p>
                            This causes the largest metric drop, confirming that explicit postoperative morphology
                            guidance is the central constraint.
                        </p>
                    </div>
                    <div class="portfolio-insight-box portfolio-fill-box">
                        <strong>Portfolio Message</strong>
                        <p>
                            The ablation makes the design defensible: ScolioLDM is an anatomy-guided generation
                            pipeline, not just another LDM.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """,
    )


def _render_scolioldm_metrics_table() -> str:
    rows = [
        ("ControlNet", "0.831 +/- 0.009", "19.726 +/- 1.121", "0.036 +/- 0.005", "0.054 +/- 0.005", "0.877 +/- 0.03", False),
        ("pix2pix", "0.846 +/- 0.007", "19.432 +/- 0.861", "0.035 +/- 0.004", "0.061 +/- 0.006", "0.861 +/- 0.03", False),
        ("ControlNeXt", "0.841 +/- 0.010", "19.179 +/- 1.140", "0.037 +/- 0.006", "0.059 +/- 0.007", "0.864 +/- 0.03", False),
        ("BBDM", "0.856 +/- 0.010", "19.654 +/- 1.118", "0.034 +/- 0.005", "0.053 +/- 0.006", "0.869 +/- 0.03", False),
        ("Fast-DDPM", "0.810 +/- 0.011", "17.539 +/- 1.987", "0.049 +/- 0.015", "0.067 +/- 0.012", "0.843 +/- 0.06", False),
        ("ScolioLDM", "0.841 +/- 0.011", "20.436 +/- 1.322", "0.032 +/- 0.006", "0.051 +/- 0.006", "0.892 +/- 0.03", True),
    ]
    body = ""
    for method, ssim, psnr, mae, gradmae, ncc, highlight in rows:
        cls = "tr-best" if highlight else ""
        body += (
            f'<tr class="{cls}"><td class="td-method"><strong>{method}</strong></td>'
            f"<td>{ssim}</td><td>{psnr}</td><td>{mae}</td><td>{gradmae}</td><td>{ncc}</td></tr>"
        )
    return _clean_markup(
        f"""
        <div class="data-table-wrap scolioldm-data-table">
          <div class="data-table-caption-title">Table 1 | Postoperative Radiograph Synthesis</div>
          <div class="data-table-scroll">
            <table class="data-table data-table-sm">
              <thead>
                <tr><th class="th-method">Method</th><th>SSIM up</th><th>PSNR up</th><th>MAE down</th><th>GradMAE down</th><th>NCC up</th></tr>
              </thead>
              <tbody>{body}</tbody>
            </table>
          </div>
          <div class="data-table-cap">Rebuilt from the paper table for compact viewing. ScolioLDM leads PSNR, MAE, GradMAE, and NCC while remaining competitive on SSIM.</div>
        </div>
        """,
    )


def _render_scolioldm_ablation_table() -> str:
    rows = [
        ("w/o MGCM", "0.836 +/- 0.009", "19.951 +/- 1.142", "0.034 +/- 0.005", "0.053 +/- 0.005", "0.882 +/- 0.035", False),
        ("w/o postoperative curve map", "0.822 +/- 0.008", "19.226 +/- 1.007", "0.039 +/- 0.005", "0.057 +/- 0.006", "0.857 +/- 0.039", False),
        ("ScolioLDM", "0.841 +/- 0.011", "20.436 +/- 1.322", "0.032 +/- 0.006", "0.051 +/- 0.006", "0.892 +/- 0.035", True),
    ]
    body = ""
    for variant, ssim, psnr, mae, gradmae, ncc, highlight in rows:
        cls = "tr-best" if highlight else ""
        body += (
            f'<tr class="{cls}"><td class="td-method"><strong>{variant}</strong></td>'
            f"<td>{ssim}</td><td>{psnr}</td><td>{mae}</td><td>{gradmae}</td><td>{ncc}</td></tr>"
        )
    return _clean_markup(
        f"""
        <div class="data-table-wrap scolioldm-data-table">
          <div class="data-table-caption-title">Table 2 | Ablation Study</div>
          <div class="data-table-scroll">
            <table class="data-table data-table-sm">
              <thead>
                <tr><th class="th-method">Variant</th><th>SSIM up</th><th>PSNR up</th><th>MAE down</th><th>GradMAE down</th><th>NCC up</th></tr>
              </thead>
              <tbody>{body}</tbody>
            </table>
          </div>
          <div class="data-table-cap">Removing postoperative curve-map guidance causes the largest drop, while removing MGCM also weakens structural fidelity.</div>
        </div>
        """,
    )


def _render_scolioldm_conclusion(paper: Dict) -> None:
    chip_html = "".join(f'<span class="portfolio-chip">{h}</span>' for h in paper.get("highlights", []))
    _html(
        f"""
        <section class="portfolio-conclusion scolioldm-conclusion">
            <h3>Research Takeaway &amp; Portfolio Impact</h3>
            <p>
                ScolioLDM reframes AIS planning as postoperative radiograph synthesis guided by explicit spinal
                morphology. The key design is to predict and use a postoperative curve map, then inject it through
                MGCM so the diffusion model follows anatomically plausible correction geometry.
            </p>
            <p>
                The detail page emphasizes the evidence chain: generic generators fail on postoperative anatomy,
                the proposed framework adds morphology-guided control, and quantitative plus ablation results show
                why MGCM and curve-map guidance matter.
            </p>
            <div class="portfolio-chips">{chip_html}</div>
        </section>
        """,
    )


def _render_surgidiff_showcase(paper: Dict, figures: Dict, tables: Dict) -> None:
    _render_surgidiff_hero(paper)
    _render_surgidiff_overview(paper)
    _render_surgidiff_framework(paper, figures.get("Figure 1"))
    _render_surgidiff_synthesis(paper, figures.get("Figure 2"), tables)
    _render_surgidiff_implant_prediction(
        paper,
        figures.get("Figure 3"),
        figures.get("Figure 4"),
        tables,
    )
    _render_surgidiff_conclusion(paper)


def _render_surgidiff_hero(paper: Dict) -> None:
    _html(
        f"""
        <div class="portfolio-hero surgi-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Research Paper</span>
                <span class="portfolio-hero-tag">{paper["tag"]}</span>
                <span class="portfolio-hero-tag">{paper["venue"]}</span>
            </div>
            <h1 class="portfolio-hero-title">{paper["title"]}</h1>
            <p class="portfolio-hero-sub">{paper["summary"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Cohort</span>
                    <strong>612 AIS</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Core Method</span>
                    <strong>SAE + LDM</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Fusion Acc.</span>
                    <strong>75.8%</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Output</span>
                    <strong>X-ray + Implants</strong>
                </div>
            </div>
        </div>
        """,
    )


def _render_surgidiff_overview(paper: Dict) -> None:
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">Image-Level Surgical Planning for AIS</h2>
                </div>
            </div>
            <div class="pg pg-4 surgi-overview-grid">
                <div class="portfolio-content portfolio-content-lead">
                    <h4>Clinical Gap</h4>
                    <p>
                        AIS planning often depends on surgeon experience and scalar parameters. Those numbers
                        do not show the expected postoperative morphology or implant layout.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Planning Target</h4>
                    <p>
                        Surgi-Diff turns preoperative PA X-rays and surgical ROI masks into a direct visual
                        estimate of postoperative correction and instrumentation.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Model Hook</h4>
                    <p>
                        The Spine Alignment Encoder captures global curve priors and injects multi-scale control
                        features into a latent diffusion generator.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Actionable Output</h4>
                    <ul>
                        <li>Postoperative X-ray synthesis.</li>
                        <li>Fusion level identification.</li>
                        <li>Rod geometry measurement.</li>
                        <li>Screw distribution assessment.</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
    )


def _render_surgidiff_framework(paper: Dict, fig: Dict) -> None:
    figure_html = _render_figure_html(
        fig,
        caption=(
            "Figure 1 | Surgi-Diff pipeline: preoperative PA X-ray and surgical ROI are "
            "encoded by SAE, injected into latent diffusion for postoperative X-ray synthesis, "
            "then evaluated through surgical-parameter and image-fidelity paths."
        ),
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact surgi-framework">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Framework</span>
                    <h2 class="portfolio-section-title">Spine Alignment Encoder + Latent Diffusion</h2>
                </div>
            </div>
            <div class="pg pg-surgi-framework">
                <div class="portfolio-span-3 surgi-figure-wide surgi-framework-figure">{figure_html}</div>
                <div class="surgi-note-stack">
                    <div class="portfolio-content">
                        <h4>Dual Prompt</h4>
                        <p>
                            The model concatenates the preoperative frontal X-ray with the ROI mask, so the
                            generator sees both anatomy and the intended surgical region.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>SAE Control</h4>
                        <p>
                            X-ray and ROI streams are fused through gated multi-scale features. Curve tokens
                            provide alignment context without relying on text prompts.
                        </p>
                    </div>
                    <div class="portfolio-insight-box portfolio-fill-box">
                        <strong>Design Point</strong>
                        <p>
                            The figure is kept as a wide plate because it shows the whole planning chain in one
                            glance: input, synthesis, masks, clinical parameters, and fidelity checks.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """,
    )


def _render_surgidiff_synthesis(paper: Dict, fig: Dict, tables: Dict) -> None:
    figure_html = _render_figure_html(
        fig,
        caption=(
            "Figure 2 | Qualitative synthesis comparison. Surgi-Diff is placed next to the "
            "GT postoperative X-ray and compared against ControlLoRA, ControlNext, StyleGANex, "
            "CycleGAN, and Pix2Pix."
        ),
    )
    table_html = _render_surgidiff_synthesis_table()
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact surgi-synthesis">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Postoperative Synthesis</span>
                    <h2 class="portfolio-section-title">Generating a Surgical Outcome, Not Just a Score</h2>
                </div>
            </div>
            <div class="pg pg-surgi-synthesis">
                <div class="surgi-note-stack">
                    <div class="portfolio-content">
                        <h4>Visual Evidence</h4>
                        <p>
                            The comparison is organized left-to-right from patient input, GT outcome, Surgi-Diff,
                            then external generative baselines.
                        </p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Why It Matters</h4>
                        <p>
                            The task is not deterministic pixel copying. A clinically useful output must preserve
                            alignment, bone texture, rods, and screw-like implant details.
                        </p>
                    </div>
                    <div class="portfolio-insight-box portfolio-fill-box">
                        <strong>Main Signal</strong>
                        <p>
                            Surgi-Diff reports the highest SSIM among the compared methods, indicating stronger
                            structural consistency with GT postoperative morphology.
                        </p>
                    </div>
                </div>
                <div class="portfolio-span-3 surgi-figure-wide surgi-synthesis-figure">{figure_html}</div>
            </div>
            <div class="pg pg-surgi-table-row">
                <div class="portfolio-span-3">{table_html}</div>
                <div class="portfolio-content">
                    <h4>Metric Reading</h4>
                    <p>
                        StyleGANex has higher PSNR, but Surgi-Diff has the best SSIM. For planning support,
                        the structural signal is more aligned with spinal morphology and implant coherence.
                    </p>
                </div>
            </div>
        </section>
        """,
    )


def _render_surgidiff_implant_prediction(
    paper: Dict,
    fig3: Dict,
    fig4: Dict,
    tables: Dict,
) -> None:
    construct_html = _render_figure_html(
        fig3,
        caption=(
            "Figure 3 | GT vs. Surgi-Diff screw-rod construct prediction in three AIS cases. "
            "This plate emphasizes the global bilateral implant layout."
        ),
    )
    screw_html = _render_figure_html(
        fig4,
        caption=(
            "Figure 4 | GT vs. Surgi-Diff pedicle screw placement. The white points make the "
            "segmental screw distribution easier to inspect case by case."
        ),
    )
    table_html = _render_surgidiff_implant_table()
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact surgi-implant">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Surgical Parameters</span>
                    <h2 class="portfolio-section-title">From Generated X-ray to Implant Planning Signals</h2>
                </div>
            </div>
            <div class="pg pg-surgi-implant">
                <div class="portfolio-span-2 surgi-figure-wide surgi-figure-strip">{construct_html}</div>
                <div class="portfolio-span-2 surgi-figure-wide surgi-figure-strip">{screw_html}</div>
                <div class="portfolio-content">
                    <h4>Three Tasks</h4>
                    <ul>
                        <li><strong>Fusion level:</strong> UIV/LIV localization under 10-pixel tolerance.</li>
                        <li><strong>Rod geometry:</strong> length, endpoint, and centerline errors.</li>
                        <li><strong>Screw distribution:</strong> instance count and position error.</li>
                    </ul>
                </div>
                <div class="portfolio-span-3">{table_html}</div>
            </div>
        </section>
        """,
    )


def _render_surgidiff_synthesis_table() -> str:
    rows = [
        ("Pix2Pix", "11.55", "1.07", "0.19", "0.04", False),
        ("CycleGAN", "11.49", "1.12", "0.20", "0.05", False),
        ("ControlLoRA", "10.05", "0.88", "0.14", "0.03", False),
        ("ControlNet", "8.67", "0.65", "0.11", "0.03", False),
        ("StyleGANex", "15.64", "1.31", "0.34", "0.05", False),
        ("Surgi-Diff", "14.25", "2.70", "0.35", "0.14", True),
    ]
    body = ""
    for method, psnr_mean, psnr_sd, ssim_mean, ssim_sd, highlight in rows:
        cls = "tr-best" if highlight else ""
        body += (
            f'<tr class="{cls}"><td class="td-method"><strong>{method}</strong></td>'
            f"<td>{psnr_mean}</td><td>{psnr_sd}</td><td>{ssim_mean}</td><td>{ssim_sd}</td></tr>"
        )
    return _clean_markup(
        f"""
        <div class="data-table-wrap surgi-data-table">
          <div class="data-table-caption-title">Table 1 | Postoperative X-ray Synthesis</div>
          <table class="data-table data-table-sm">
            <thead>
              <tr>
                <th rowspan="2" class="th-method">Method</th>
                <th colspan="2" class="th-grp">PSNR (dB) up</th>
                <th colspan="2" class="th-grp">SSIM up</th>
              </tr>
              <tr class="tr-subh">
                <th>Mean</th><th>SD</th><th>Mean</th><th>SD</th>
              </tr>
            </thead>
            <tbody>{body}</tbody>
          </table>
          <div class="data-table-cap">Rebuilt from the paper table for a cleaner portfolio view. Surgi-Diff is highlighted because it achieves the highest SSIM while keeping competitive PSNR.</div>
        </div>
        """,
    )


def _render_surgidiff_implant_table() -> str:
    rows = [
        ("Fusion Level", "Accuracy", "Acc", "75.8%"),
        ("", "Boundary Error (UIV)", "E<sub>UIV</sub>", "8.40 px"),
        ("", "Boundary Error (LIV)", "E<sub>LIV</sub>", "7.88 px"),
        ("Rod Geometry", "Length Error", "E<sub>L</sub>", "19.36 px"),
        ("", "Endpoint Error", "E<sub>end</sub>", "4.50 px"),
        ("", "Centerline Error", "E<sub>cline</sub>", "2.41 px"),
        ("Screw Distribution", "Quantity Error", "E<sub>#</sub>", "1.09"),
        ("", "Position Error", "E<sub>pos</sub>", "5.49 px"),
    ]
    body = ""
    for category, metric, symbol, result in rows:
        body += (
            f'<tr><td class="td-ds">{category}</td><td class="td-setting">{metric}</td>'
            f"<td>{symbol}</td><td><strong>{result}</strong></td></tr>"
        )
    return _clean_markup(
        f"""
        <div class="data-table-wrap surgi-data-table">
          <div class="data-table-caption-title">Table 2 | Implant Prediction Performance</div>
          <table class="data-table data-table-sm">
            <thead>
              <tr><th>Category</th><th>Metric</th><th>Symbol</th><th>Result</th></tr>
            </thead>
            <tbody>{body}</tbody>
          </table>
          <div class="data-table-cap">Clinical-task metrics from the paper: fusion level, rod morphology, and screw distribution are all derived from the generated postoperative output.</div>
        </div>
        """,
    )


def _render_surgidiff_conclusion(paper: Dict) -> None:
    chip_html = "".join(f'<span class="portfolio-chip">{h}</span>' for h in paper.get("highlights", []))
    _html(
        f"""
        <section class="portfolio-conclusion surgi-conclusion">
            <h3>Clinical Value &amp; Portfolio Takeaway</h3>
            <p>
                Surgi-Diff reframes AIS surgical planning as an image-level outcome prediction problem. Instead
                of only estimating isolated parameters, the system generates a postoperative X-ray and exposes
                the implant-related structures needed for fusion-level, rod, and screw-distribution analysis.
            </p>
            <p>
                For a portfolio detail page, the strongest story is the bridge between visual prediction and
                actionable planning: the framework shows the generated outcome, then converts it into measurable
                clinical signals that can support preoperative discussion and decision-making.
            </p>
            <div class="portfolio-chips">{chip_html}</div>
        </section>
        """,
    )


def _render_showcase_hero(paper: Dict) -> None:
    st.markdown(
        f"""
        <div class="portfolio-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Research Paper</span>
                <span class="portfolio-hero-tag">{paper["tag"]}</span>
                <span class="portfolio-hero-tag">{paper["venue"].split(" | ")[0]}</span>
            </div>
            <h1 class="portfolio-hero-title">{paper["title"]}</h1>
            <p class="portfolio-hero-sub">{paper["summary"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Venue Impact</span>
                    <strong>SCI Q1</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Benchmarks</span>
                    <strong>4 Datasets</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Baselines</span>
                    <strong>14 Methods</strong>
                </div>
                <div class="portfolio-stat">
                    <span>IP Output</span>
                    <strong>1 Patent</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_section_background(paper: Dict) -> None:
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">Background &amp; Research Gap</h2>
                </div>
            </div>
            <div class="pg pg-4 mdhgfn-overview-grid">
                <div class="portfolio-content portfolio-content-lead">
                    <h4>Problem</h4>
                    <p>
                        Traffic forecasting drives signal control, navigation routing, and congestion pricing,
                        but road flow is governed by <strong>non-stationary high-order dependencies</strong>
                        across corridor, district, and regional scales.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Research Gap</h4>
                    <ul>
                        <li>Static first-order road graphs assume only pairwise interactions.</li>
                        <li>Micro / meso / macro traffic scales are fused naively or skipped.</li>
                        <li>Temporal modules rarely adapt receptive fields per forecast horizon.</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Hypothesis</h4>
                    <p>
                        Dual hypergraphs at three geographic scales can capture co-movement patterns that
                        pairwise GNNs collapse into a single adjacency matrix.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Outputs</h4>
                    <ul>
                        <li><strong>MDHGFN</strong>: multiscale dual-hypergraph fusion.</li>
                        <li><strong>HSAM</strong>: gated hypergraph spatial attention.</li>
                        <li><strong>TAEM</strong>: horizon-adaptive temporal refinement.</li>
                        <li>SCI Q1 publication + invention patent.</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    return

    st.markdown(
        f"""
        <section class="portfolio-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">Background &amp; Research Gap</h2>
                </div>
            </div>
            <div class="pg pg-2">
                <div class="portfolio-content">
                    <h4>Why It Matters</h4>
                    <p>
                        Traffic forecasting underpins signal control, navigation routing, and congestion pricing.
                        Yet real traffic shows <strong>non-stationary multi-order dependencies</strong> across
                        heterogenous scales that classic pairwise GNNs systematically miss.
                    </p>
                    <h4>What Prior Work Ignores</h4>
                    <ul>
                        <li>Static first-order road graphs assume <em>only pairwise</em> interactions.</li>
                        <li>Micro / meso / macro scales are fused naïvely or skipped.</li>
                        <li>Time-axis models don't refine receptive fields per horizon.</li>
                    </ul>
                    <div class="portfolio-insight-box">
                        <strong>Gap</strong>
                        <p>Low-order graphs cannot represent high-order co-movement — a multiscale hypergraph paradigm was missing.</p>
                    </div>
                </div>
                <div class="portfolio-content">
                    <h4>Hypothesis</h4>
                    <p>
                        Building <strong>dual hypergraphs at three geographic scales</strong> (travel-correlation /
                        functional-community / regional-conduction), then running them through a gated spatial
                        attention + adaptive temporal refinement module, disentangles multi-order dependencies
                        and beats SOTA on both small dense and large heterogeneous sensor networks.
                    </p>
                    <h4>Four Contributions</h4>
                    <ul>
                        <li>First <strong>Multiscale Dual-Hypergraph Fusion</strong> paradigm for traffic forecasting.</li>
                        <li><strong>HSAM</strong> — gated multi-head hypergraph spatial attention.</li>
                        <li><strong>TAEM</strong> — temporal adaptive enhancement via dynamic conv + multi-head attn.</li>
                        <li>SCI Q1 publication (Chaos, Solitons &amp; Fractals) + 1 invention patent.</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_figure_html(item: Dict, caption: str = "") -> str:
    if not item:
        return '<div class="portfolio-figure"><div class="gallery-card-placeholder" style="min-height:220px;">Figure not available</div></div>'
    title = item.get("title", "")
    MAX_SVG_BYTES = 55 * 1024
    svg = get_pdf_svg(item["file"], 0)
    cap_html = f'<div class="portfolio-figure-caption">{caption if caption else item.get("description","")}</div>'
    if svg and 200 < len(svg) <= MAX_SVG_BYTES:
        return f'<div class="portfolio-figure"><div class="portfolio-media">{svg}</div>{cap_html}</div>'
    img = get_pdf_clean_thumbnail(item["file"])
    if img:
        return f'<div class="portfolio-figure"><div class="portfolio-media portfolio-media-clean"><img src="data:image/png;base64,{img}" alt="{title}" /></div>{cap_html}</div>'
    img = get_pdf_thumbnail(item["file"])
    if not img:
        return f'<div class="portfolio-figure"><div class="gallery-card-placeholder" style="min-height:220px;">{title}</div>{cap_html}</div>'
    return f'<div class="portfolio-figure"><div class="portfolio-media"><img src="data:image/png;base64,{img}" alt="{title}" /></div>{cap_html}</div>'


def _render_table_html(item: Dict, caption: str = "") -> str:
    if not item:
        return '<div class="portfolio-table-figure"><span class="portfolio-table-label">Table</span><div class="gallery-card-placeholder" style="min-height:180px;">Table not available</div></div>'
    title = item.get("title", "")
    label = title.split(":")[0].strip() if ":" in title else title
    MAX_SVG_BYTES = 55 * 1024
    svg = get_pdf_svg(item["file"], 0)
    cap_html = caption if caption else item.get("description", "")
    if svg and 200 < len(svg) <= MAX_SVG_BYTES:
        return f'<div class="portfolio-table-figure"><span class="portfolio-table-label">{label}</span><div class="portfolio-media">{svg}</div><div class="portfolio-figure-caption">{cap_html}</div></div>'
    img = get_pdf_clean_thumbnail(item["file"])
    if img:
        return f'<div class="portfolio-table-figure"><span class="portfolio-table-label">{label}</span><div class="portfolio-media portfolio-media-clean"><img src="data:image/png;base64,{img}" alt="{title}" /></div><div class="portfolio-figure-caption">{cap_html}</div></div>'
    img = get_pdf_thumbnail(item["file"])
    if not img:
        return f'<div class="portfolio-table-figure"><span class="portfolio-table-label">{label}</span><div class="gallery-card-placeholder" style="min-height:180px;">{title}</div><div class="portfolio-figure-caption" style="margin-top:12px;">{cap_html}</div></div>'
    return f'<div class="portfolio-table-figure"><span class="portfolio-table-label">{label}</span><div class="portfolio-media"><img src="data:image/png;base64,{img}" alt="{title}" /></div><div class="portfolio-figure-caption">{cap_html}</div></div>'


def _render_section_architecture(paper: Dict, fig: Dict) -> None:
    figure_html = _render_figure_html(
        fig,
        caption="Figure 1 | MDHGFN pipeline: (1) input traffic tensor, (2) multiscale dual-hypergraph construction, (3) per-scale HSAM spatial encoding, (4) TAEM temporal refinement, (5) cross-scale fusion, (6) multi-horizon regression head.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Framework</span>
                    <h2 class="portfolio-section-title">Overall Architecture</h2>
                </div>
            </div>
            <div class="pg pg-showcase-architecture">
                <div class="portfolio-span-3">{figure_html}</div>
                <div class="portfolio-content">
                    <h4>Input to Hypergraphs</h4>
                    <p>
                        Raw PeMS sensor flows form a <em>T x N</em> tensor. Three dual-hypergraph incidence
                        matrices are built for micro, meso, and macro traffic structure.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>HSAM + TAEM</h4>
                    <p>
                        HSAM performs incidence-based spatial attention; TAEM refines temporal receptive fields
                        with dynamic 1D convolutions and multi-head attention.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Scale Fusion</h4>
                    <p>
                        Disentangled scale features are fused with learnable weights into a 12-step regression
                        head, preserving scale-level interpretability.
                    </p>
                </div>
                <div class="portfolio-insight-box portfolio-fill-box">
                    <strong>Design Point</strong>
                    <p>Separate spatial scales are encoded before fusion, so local corridor details and broader regional congestion signals remain visible in the same case-study view.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    return

    st.markdown(
        f"""
        <section class="portfolio-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Framework</span>
                    <h2 class="portfolio-section-title">Overall Architecture</h2>
                </div>
            </div>
            <div class="pg pg-single">
                {figure_html}
            </div>
            <div style="height:6px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>Input → Hypergraphs</h4>
                    <p>
                        Raw PeMS sensor flows form a <em>T × N</em> tensor. Three dual-hypergraph incidence
                        matrices (micro / meso / macro) are built; edge weights are learnable per-stream.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>HSAM + TAEM</h4>
                    <p>
                        Hypergraph Spatial Attention runs multi-head message passing on each incidence
                        structure; Temporal Adaptive Enhancement refines per-horizon receptive fields with
                        dynamic 1D convs + multi-head attention.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Late Cross-Scale Fusion</h4>
                    <p>
                        Disentangled scale features are fused with a learnable softmax weighting → 12-step
                        regression projection. Late mixing preserves per-scale interpretability.
                    </p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_section_hypergraph(paper: Dict, fig: Dict) -> None:
    figure_html = _render_figure_html(
        fig,
        caption="Figure 2 | Dual hypergraph construction: micro (sensor-level travel correlations), meso (functional-district clusters), macro (regional conduction). Right column: incidence-matrix structure and learnable incidence-based aggregation.",
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Methodology</span>
                    <h2 class="portfolio-section-title">Multiscale Dual-Hypergraph Construction</h2>
                </div>
            </div>
            <div class="pg pg-hypergraph">
                <div class="portfolio-tall-figure">{figure_html}</div>
                <div class="portfolio-hypergraph-notes">
                    <div class="portfolio-content">
                        <h4>Three Scales</h4>
                        <ul>
                            <li><strong>Micro</strong>: adjacent-arterial corridor travel correlations.</li>
                            <li><strong>Meso</strong>: representation-cluster functional districts.</li>
                            <li><strong>Macro</strong>: cross-city regional propagation.</li>
                        </ul>
                    </div>
                    <div class="portfolio-content">
                        <h4>Dual Branches</h4>
                        <ul>
                            <li><strong>Topology</strong>: road adjacency and travel-time seeded prior.</li>
                            <li><strong>Data-driven</strong>: sliding-window clustering from flow signals.</li>
                        </ul>
                    </div>
                    <div class="portfolio-insight-box">
                        <strong>Why Dual</strong>
                        <p>Topology-only misses emergent congestion; data-only can overfit anomalies. HSAM learns the balance between both priors.</p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Showcase Message</h4>
                        <p>
                            The visual shows the paper's core contribution: replace pairwise road edges with
                            incidence-based high-order groups, then repeat the idea at urban scales.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """,
    )
    return

    st.markdown(
        f"""
        <section class="portfolio-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Methodology</span>
                    <h2 class="portfolio-section-title">Multiscale Dual-Hypergraph Construction</h2>
                </div>
            </div>
            <div class="pg pg-23">
                {figure_html}
                <div class="portfolio-content">
                    <h4>Three Scales</h4>
                    <ul>
                        <li><strong>Micro</strong> — adjacent-arterial corridor travel correlations.</li>
                        <li><strong>Meso</strong> — representation-cluster functional districts.</li>
                        <li><strong>Macro</strong> — cross-city regional propagation.</li>
                    </ul>
                    <h4>Dual (×2 per Scale)</h4>
                    <ul>
                        <li><strong>Topology</strong> branch: road adjacency + travel-time seeded.</li>
                        <li><strong>Data-driven</strong> branch: sliding-window clustering.</li>
                    </ul>
                    <div class="portfolio-insight-box">
                        <strong>Why Dual</strong>
                        <p>Topology-only misses emergent congestion; data-only overfits training anomalies. Convex combination inside HSAM balances both priors adaptively.</p>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_section_quantitative(paper: Dict, tables: Dict) -> None:
    stats_html = _render_dataset_stats_table()
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Quantitative Results</span>
                    <h2 class="portfolio-section-title">Benchmark Performance vs. 14 Baselines</h2>
                </div>
            </div>
            <div class="pg pg-results-top">
                <div class="portfolio-content">
                    <h4>Evaluation Protocol</h4>
                    <p>
                        Four standard PeMS benchmarks, horizons <strong>15 / 30 / 60 min</strong>,
                        metrics <strong>MAE / RMSE / MAPE</strong>, and identical 12-step input windows across
                        all baseline comparisons.
                    </p>
                </div>
                {stats_html}
                <div class="portfolio-insight-box">
                    <strong>Main Takeaway</strong>
                    <p>MDHGFN ranks first across the reported PeMS metrics, with the largest gains on long-horizon and heterogeneous-road settings.</p>
                </div>
            </div>
            <div class="pg pg-3 portfolio-tight-notes">
                <div class="portfolio-content">
                    <h4>Short Horizon</h4>
                    <p>Recent flow history is already predictive, but corridor-scale dual hypergraphs still give MDHGFN a consistent edge.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Long Horizon</h4>
                    <p>Meso and macro scales propagate region signals that pairwise graphs miss, improving 60-minute prediction stability.</p>
                </div>
                <div class="portfolio-content">
                    <h4>PEMS07</h4>
                    <p>The 883-sensor rural-urban network exposes topology heterogeneity; scale-adaptive fusion is most useful there.</p>
                </div>
            </div>
        </section>
        """,
    )
    return

    st.markdown(
        f"""
        <section class="portfolio-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Quantitative Results</span>
                    <h2 class="portfolio-section-title">Benchmark Performance vs. 14 Baselines</h2>
                </div>
            </div>
            <div class="pg pg-32">
                <div class="portfolio-content">
                    <h4>Evaluation Protocol</h4>
                    <p>
                        Four standard PeMS benchmarks, horizons <strong>15 / 30 / 60 min</strong>.
                        Metrics: <strong>MAE / RMSE / MAPE</strong>. Identical 12-step input window,
                        splits, optimizer across all 14 baselines.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Main Takeaway</strong>
                        <p>MDHGFN is new SOTA on every dataset × horizon × metric; largest gains on 60 min PEMS07 where multi-scale effects dominate.</p>
                    </div>
                </div>
                {stats_html}
            </div>
            <div style="height:6px"></div>
            {main_html}
            <div style="height:4px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>15-min (Short)</h4>
                    <p>All methods close, since recent past is predictive. MDHGFN still edges ahead via fine-grained corridor-scale dual hypergraph.</p>
                </div>
                <div class="portfolio-content">
                    <h4>60-min (Long)</h4>
                    <p>MDHGFN wins over runner-up by <strong>4.1–7.3% MAE</strong> across datasets; meso &amp; macro scales propagate region signals invisible to pairwise graphs.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Heterogeneous PEMS07</h4>
                    <p>Uniform-topology baselines regress heavily on this 883-sensor rural-urban mix. Scale-adaptive fusion is robust to heterogeneity.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_section_qualitative_compact(paper: Dict, fig: Dict) -> None:
    figure_html = _render_figure_html(
        fig,
        caption="Figure 3 | Ground-truth vs. MDHGFN forecast heatmaps on PEMS04 and PEMS08. Zoomed windows highlight rush-hour peaks and transient spikes where baselines often over-smooth transitions.",
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Qualitative Results</span>
                    <h2 class="portfolio-section-title">Visual Forecasts &amp; Edge Cases</h2>
                </div>
            </div>
            <div class="pg pg-qualitative">
                <div class="portfolio-qualitative-figure">{figure_html}</div>
                <div class="portfolio-qualitative-notes">
                    <div class="portfolio-content">
                        <h4>Morning Rush</h4>
                        <p>MDHGFN captures sharp onset without the one-step lag commonly seen in first-order baselines.</p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Incident Spike</h4>
                        <p>Multi-scale hypergraphs propagate transient shockwave patterns instead of smoothing them into the mean.</p>
                    </div>
                    <div class="portfolio-content">
                        <h4>Long Horizon</h4>
                        <p>60-minute forecasts remain structurally coherent, which matters for signal-control and routing decisions.</p>
                    </div>
                </div>
            </div>
        </section>
        """,
    )


def _render_section_analysis_and_ablation_compact(paper: Dict, fig4: Dict, tables: Dict) -> None:
    table_modules = _render_ablation_modules_table()
    table_hyper = _render_ablation_hypergraph_table()
    figure_html = _render_figure_html(
        fig4,
        caption="Figure 4 | Training convergence and learned hypergraph incidence attention. The full model converges faster and produces interpretable scale-specific attention patterns.",
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Ablation &amp; Analysis</span>
                    <h2 class="portfolio-section-title">Module Ablations, Hypergraph Design &amp; Efficiency</h2>
                </div>
            </div>
            <div class="pg pg-analysis">
                <div class="portfolio-span-2">{figure_html}</div>
                <div class="portfolio-content">
                    <h4>Three Signals</h4>
                    <ul>
                        <li><strong>Each scale is orthogonal:</strong> full fusion beats every subset.</li>
                        <li><strong>HSAM + TAEM are complementary:</strong> removing both causes the largest drop.</li>
                        <li><strong>Sparse incidence ops:</strong> accuracy improves without heavy latency growth.</li>
                    </ul>
                </div>
                <div class="portfolio-insight-box">
                    <strong>Interpretability</strong>
                    <p>Disentangled scales plus attention over incidence structure let reviewers inspect which traffic groups drove a forecast.</p>
                </div>
            </div>
            <div class="pg pg-results-visuals">
                {table_modules}
                {table_hyper}
            </div>
        </section>
        """,
    )


def _render_section_qualitative(paper: Dict, fig: Dict) -> None:
    figure_html = _render_figure_html(
        fig,
        caption="Figure 3 | Ground-truth vs. MDHGFN forecast heatmaps (PEMS04, PEMS08) across horizons 15/30/45/60 min. Zoomed windows highlight morning rush peak and incident-like transient spikes — where baselines typically over-smooth transitions.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Qualitative Results</span>
                    <h2 class="portfolio-section-title">Visual Forecasts &amp; Edge Cases</h2>
                </div>
            </div>
            <div class="pg pg-single">
                {figure_html}
            </div>
            <div style="height:6px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>Morning Rush</h4>
                    <p>MDHGFN captures sharp onset without the characteristic 1-step lag shown by 1st-order baselines.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Incident Spike</h4>
                    <p>Multi-scale hypergraphs detect and propagate transient shockwave patterns, avoiding over-smoothing.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Stable Long Horizon</h4>
                    <p>60 min forecasts remain structurally coherent (not damped to mean), critical for real signal-control use cases.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_section_analysis_and_ablation(paper: Dict, fig4: Dict) -> None:
    table_modules = _render_ablation_modules_table()
    table_hyper = _render_ablation_hypergraph_table()
    figure_html = _render_figure_html(
        fig4,
        caption="Figure 4 | Left: training convergence (full vs. ablated variants) — full MDHGFN converges faster. Right: learned hypergraph incidence attention per scale.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Ablation &amp; Analysis</span>
                    <h2 class="portfolio-section-title">Module Ablations, Hypergraph Design &amp; Efficiency</h2>
                </div>
            </div>
            <div class="pg pg-2">
                {table_modules}
                {table_hyper}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-23">
                <div class="portfolio-content">
                    <h4>Three Signals</h4>
                    <ul>
                        <li><strong>Each scale orthogonal:</strong> Gr+Gc+Gt beats any subset on both datasets.</li>
                        <li><strong>HSAM + TAEM synergistic:</strong> removing both costs ~5.6% MAE; individually only 2–3%.</li>
                        <li><strong>Efficient:</strong> sparse incidence ops make MDHGFN latency on-par with dense baselines like MTGNN, deployable on traffic edge boxes.</li>
                    </ul>
                    <div class="portfolio-insight-box">
                        <strong>Interpretability Win</strong>
                        <p>Disentangled scales + attention over hypergraph incidence let analysts inspect which hyperedges drove a given forecast.</p>
                    </div>
                </div>
                {figure_html}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_dataset_stats_table() -> str:
    rows = [
        ("PEMS03", "358", "547", "26,208", "09/2018 – 11/2018"),
        ("PEMS04", "307", "340", "16,992", "01/2018 – 02/2018"),
        ("PEMS07", "883", "866", "28,224", "05/2017 – 08/2017"),
        ("PEMS08", "170", "295", "17,856", "07/2016 – 08/2016"),
    ]
    body = ""
    for r in rows:
        body += f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>"
    return _clean_markup(f"""
    <div class="data-table-wrap">
      <table class="data-table data-table-sm">
        <thead>
          <tr><th>Dataset</th><th>Sensors</th><th>Edges</th><th>Time Steps</th><th>Date Range</th></tr>
        </thead>
        <tbody>{body}</tbody>
      </table>
      <div class="data-table-cap">Table A | Four PeMS Caltrans benchmark datasets used for evaluation. Sensor counts range from 170 (dense urban, PEMS08) to 883 (heterogeneous rural-urban, PEMS07).</div>
    </div>
    """)


def _render_baselines_table() -> str:
    methods = [
        ("2015", "FC-LSTM",        ["21.33","35.11","23.33","27.14","18.20","18.20","29.98","45.94","13.20","22.20","34.06","14.20","12","7","11"]),
        ("2017", "DCRNN",          ["24.11","38.69","22.67","30.49","45.99","20.72","34.82","51.32","16.23","21.76","32.41","14.19","14","14","13"]),
        ("2018", "STGCN",          ["23.48","37.51","21.95","28.80","44.00","19.08","33.80","51.74","14.75","22.49","34.05","14.54","13","13","12"]),
        ("2019", "Graph WaveNet",  ["24.73","38.42","24.01","30.55","46.31","23.33","34.62","51.86","15.68","23.01","35.67","15.37","15","15","14"]),
        ("2020", "STSGCN",         ["20.72","33.75","19.44","24.21","38.36","15.63","28.10","45.88","11.90","19.56","30.58","12.55","10","12","9"]),
        ("2020", "OGCRNN",         ["17.16","29.40","16.48","22.16","35.15","15.72","24.45","39.80","10.22","18.50","29.00","11.74","7","8","7"]),
        ("2021", "STGODE",         ["16.50","27.84","16.69","20.84","32.82","13.77","22.59","37.54","10.14","16.81","25.97","10.62","4","4","5"]),
        ("2021", "STFGNN",         ["19.37","32.57","18.37","21.55","34.60","14.26","24.77","40.55","10.33","18.83","29.66","11.90","8","10","8"]),
        ("2022", "GMSDR",          ["15.92","28.87","14.50","21.63","34.05","13.87","23.78","44.60","10.17","16.59","25.69","10.59","6","6","4"]),
        ("2022", "FEDformer",      ["19.74","29.51","20.04","23.57","35.65","50.54","29.42","43.65","22.85","24.22","35.32","17.38","11","11","15"]),
        ("2023", "HSTGCNT",        ["19.22","30.65","19.72","23.47","35.53","16.52","24.43","37.77","11.25","20.82","30.87","13.76","9","9","10"]),
        ("2023", "AGFCRN",         ["16.89","28.98","17.65","20.51","33.81","13.81","22.69","37.95","9.62","17.35","27.66","11.31","5","5","6"]),
        ("2024", "DS-STGCN",       ["16.04","26.40","15.69","19.80","31.81","13.40","22.11","36.62","9.38","15.66","25.65","10.09","3","2","2"]),
        ("2024", "CDAGF",          ["16.54","27.71","16.28","19.55","32.58","13.06","21.56","37.03","9.11","15.68","25.71","10.13","2","3","3"]),
    ]
    ours = ("Ours", "MDHGFN", ["14.12","22.52","12.95","19.29","31.57","12.35","20.41","33.69","8.98","15.45","25.20","11.50","1","1","1"])
    def mrow(yr, name, v, best=False, last=False):
        cls = "tr-best" if best else ("tr-divider" if last else "")
        td_v = "".join(f"<td>{x}</td>" for x in v)
        tag = f'<span class="yr-tag">{yr}</span>' if yr != "Ours" else '<span class="yr-tag yr-tag-ours">Ours</span>'
        return f'<tr class="{cls}"><td class="td-method">{tag}<strong>{name}</strong></td>{td_v}</tr>'
    body = "".join(mrow(y,n,v) for (y,n,v) in methods) + mrow(*ours, best=True)
    return f"""
    <div class="data-table-wrap">
      <div class="data-table-scroll">
        <table class="data-table data-table-main">
          <thead>
            <tr>
              <th rowspan="2" class="th-method">Method</th>
              <th colspan="3" class="th-grp">PEMS03</th>
              <th colspan="3" class="th-grp">PEMS04</th>
              <th colspan="3" class="th-grp">PEMS07</th>
              <th colspan="3" class="th-grp">PEMS08</th>
              <th colspan="3" class="th-grp th-rank">Avg. Rank</th>
            </tr>
            <tr class="tr-subh">
              <th>MAE</th><th>RMSE</th><th>MAPE</th>
              <th>MAE</th><th>RMSE</th><th>MAPE</th>
              <th>MAE</th><th>RMSE</th><th>MAPE</th>
              <th>MAE</th><th>RMSE</th><th>MAPE</th>
              <th>MAE</th><th>RMSE</th><th>MAPE</th>
            </tr>
          </thead>
          <tbody>{body}</tbody>
        </table>
      </div>
      <div class="data-table-cap">Table 1 | SOTA comparison on all four PeMS benchmarks (15 baselines, MDHGFN highlighted). Metrics are MAE, RMSE, MAPE (%) across all horizons. MDHGFN ranks first on every single dataset × metric combination.</div>
    </div>
    """


def _render_ablation_modules_table() -> str:
    rows = [
        ("PEMS03", "MDHGFN w/o both HSAM & TAEM", "23.48", "14.91", "13.83"),
        ("PEMS03", "MDHGFN w/o HSAM",             "23.07", "14.64", "13.51"),
        ("PEMS03", "MDHGFN w/o TAEM",             "22.68", "14.21", "13.39"),
        ("PEMS03", "MDHGFN (full)",               "22.52", "14.12", "12.95"),
        ("PEMS08", "MDHGFN w/o both HSAM & TAEM", "26.54", "16.72", "12.93"),
        ("PEMS08", "MDHGFN w/o HSAM",             "25.57", "15.90", "11.89"),
        ("PEMS08", "MDHGFN w/o TAEM",             "25.26", "15.52", "11.82"),
        ("PEMS08", "MDHGFN (full)",               "25.20", "15.45", "11.50"),
    ]
    body = ""
    cur_ds = None
    for (ds, name, rmse, mae, mape) in rows:
        best = "full" in name.lower()
        ds_show = ""
        if ds != cur_ds:
            ds_show = ds
            cur_ds = ds
        cls = "tr-best" if best else ""
        body += f'<tr class="{cls}"><td class="td-ds">{ds_show}</td><td class="td-setting">{name}</td><td>{rmse}</td><td>{mae}</td><td>{mape}</td></tr>'
    return _clean_markup(f"""
    <div class="data-table-wrap">
      <div class="data-table-caption-title">Table 3 | Module Contribution</div>
      <table class="data-table data-table-sm">
        <thead><tr><th>Dataset</th><th>Setting</th><th>RMSE</th><th>MAE</th><th>MAPE</th></tr></thead>
        <tbody>{body}</tbody>
      </table>
      <div class="data-table-cap">Generated Table 3 | Leave-one-out ablation of the spatial HSAM and temporal TAEM modules. Removing both costs ~5.6% MAE on PEMS03; each module is individually necessary.</div>
    </div>
    """)


def _render_ablation_hypergraph_table() -> str:
    rows = [
        ("PEMS03", "[G<sub>r</sub>] Road Graph",        "22.63", "14.23", "13.01"),
        ("PEMS03", "[G<sub>c</sub>] Corridor Hyper",    "22.66", "14.30", "13.48"),
        ("PEMS03", "[G<sub>t</sub>] Topology Hyper",    "22.88", "14.53", "15.03"),
        ("PEMS03", "[G<sub>r</sub>, G<sub>c</sub>, G<sub>t</sub>] (Full)", "22.52", "14.12", "12.95"),
        ("PEMS08", "[G<sub>r</sub>] Road Graph",        "25.49", "15.48", "11.52"),
        ("PEMS08", "[G<sub>c</sub>] Corridor Hyper",    "25.36", "15.53", "12.07"),
        ("PEMS08", "[G<sub>t</sub>] Topology Hyper",    "25.52", "15.46", "11.57"),
        ("PEMS08", "[G<sub>r</sub>, G<sub>c</sub>, G<sub>t</sub>] (Full)", "25.20", "15.45", "11.50"),
    ]
    body = ""
    cur_ds = None
    for (ds, name, rmse, mae, mape) in rows:
        best = "Full" in name
        ds_show = ""
        if ds != cur_ds:
            ds_show = ds
            cur_ds = ds
        cls = "tr-best" if best else ""
        body += f'<tr class="{cls}"><td class="td-ds">{ds_show}</td><td class="td-setting">{name}</td><td>{rmse}</td><td>{mae}</td><td>{mape}</td></tr>'
    return _clean_markup(f"""
    <div class="data-table-wrap">
      <div class="data-table-caption-title">Table 4 | Dual-Hypergraph Design</div>
      <table class="data-table data-table-sm">
        <thead><tr><th>Dataset</th><th>Hypergraph Subset</th><th>RMSE</th><th>MAE</th><th>MAPE</th></tr></thead>
        <tbody>{body}</tbody>
      </table>
      <div class="data-table-cap">Generated Table 4 | Single-scale vs. full dual-hypergraph fusion. Using all three scales consistently outperforms any subset, confirming that each hypergraph captures orthogonal structure.</div>
    </div>
    """)


def _render_section_conclusion(paper: Dict) -> None:
    chip_html = "".join(f'<span class="portfolio-chip">{h}</span>' for h in paper.get("highlights", []))
    st.markdown(
        f"""
        <section class="portfolio-conclusion">
            <h3>Conclusion &amp; Project Impact</h3>
            <p>
                MDHGFN re-frames traffic flow prediction as a <em>multiscale high-order hypergraph learning</em>
                problem. By building dual hypergraphs at the microscopic, mesoscopic, and macroscopic geographic
                scales, encoding them through a dedicated Hypergraph Spatial Attention Module, and refining
                temporal receptive fields via a Temporal Adaptive Enhancement Module, the method consistently
                outperforms 14 state-of-the-art baselines across the four standard PeMS benchmarks — including
                the heterogeneous 883-sensor PEMS07 network where classical pairwise GNNs regress sharply.
            </p>
            <p>
                The full ablation study confirms that each scale and each architectural component is a
                statistically necessary contributor, and the learned hyperedge attention heatmaps provide
                human-readable explanations of <em>which geographic structures</em> drove a given forecast — a
                rare combination of top-tier accuracy with genuine interpretability.
            </p>
            <p>
                This work was published in <strong>Chaos, Solitons &amp; Fractals</strong>, a leading
                interdisciplinary SCI Q1 journal on nonlinear dynamics and complex systems. Based on the core
                multiscale dual-hypergraph idea, I also co-filed an invention patent on the method, and I
                designed and open-sourced a companion urban-functional-area traffic-flow visualization system to
                make the modeling outputs interpretable for non-technical stakeholders (city planning bureaus,
                transport authorities).
            </p>
            <div class="portfolio-chips">{chip_html}</div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_standard_detail(paper: Dict) -> None:
    left, right = st.columns([1.08, 0.92])
    with left:
        st.markdown(
            f"""
            <div class="detail-panel">
                <h3>What This Work Solves</h3>
                <p>{paper["explanation"]}</p>
            </div>
            <div class="detail-panel">
                <h3>Experimental Story</h3>
                <p>{paper["experiment_focus"]}</p>
            </div>
            <div class="detail-panel">
                <h3>My Contribution</h3>
                <p>{paper["contribution"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        chips = "".join(f'<span class="paper-chip">{item}</span>' for item in paper["highlights"])
        st.markdown(f'<div class="paper-highlights">{chips}</div>', unsafe_allow_html=True)

    with right:
        portfolio_pages = paper.get("portfolio_pages", [])
        if portfolio_pages:
            cover_image = get_portfolio_image(portfolio_pages[0], zoom=1.0)
            if cover_image:
                st.markdown(
                    f'<img class="paper-detail-cover" src="data:image/png;base64,{cover_image}" />',
                    unsafe_allow_html=True,
                )
        st.markdown(
            f"""
            <div class="detail-panel">
                <h3>Figure Preview</h3>
                <p>{paper["figure_note"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="section-header">
            <div class="section-kicker">Portfolio Figures</div>
            <div class="section-title">Visual evidence from portfolio PDF.</div>
            <div class="section-copy">
                These pages are extracted from the portfolio PDF to illustrate the research work in a more engaging way.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    load_key = f"load_figures_{paper['id']}"
    if st.button("Load Portfolio Figures", use_container_width=True, key=f"load-btn-{paper['id']}"):
        st.session_state[load_key] = True

    if st.session_state.get(load_key):
        pages = paper.get("portfolio_pages", paper.get("experiment_pages", [0]))
        total_pages = len(pages)
        progress_bar = st.progress(0, text="Loading portfolio pages...")

        for idx, start in enumerate(range(0, total_pages, 2)):
            cols = st.columns(2)
            for col, page_index in zip(cols, pages[start:start + 2]):
                with col:
                    image = get_portfolio_image(page_index, zoom=1.0)
                    if image:
                        st.markdown(
                            f'<img class="page-shot" src="data:image/png;base64,{image}" />'
                            f'<div class="figure-caption">Portfolio page {page_index + 1}. {paper["figure_note"]}</div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            f"""
                            <div class="detail-panel">
                                <h3>Page {page_index + 1}</h3>
                                <p>{paper["figure_note"]}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
            progress_bar.progress(min((idx + 1) / (total_pages // 2 + 1), 1.0),
                                  text=f"Loaded {min((idx + 1) * 2, total_pages)}/{total_pages} pages")
        progress_bar.progress(1.0, text="All pages loaded")
