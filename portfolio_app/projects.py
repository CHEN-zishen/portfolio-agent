from pathlib import Path
from textwrap import dedent
from html import escape
from typing import Dict, Iterable, List, Tuple

import streamlit as st

from .assets import get_image_base64
from .data import PROJECTS


TAG_COLORS = {
    "Deep Learning": "#217c6f",
    "Web Development": "#78a99a",
    "Data Engineering": "#4a6b65",
    "AI Agent": "#1a5c52",
    "WeChat Mini Program": "#07c160",
    "Business Intelligence": "#5b8c85",
    "Multi-Agent": "#2d8a7e",
    "LLM": "#3d9e91",
    "Simulation": "#6ab4a8",
    "Social Network": "#8ec8bf",
    "Algorithm": "#16756f",
    "Web Application": "#1e8f85",
    "Education": "#3da699",
    "Visualization": "#5db5a8",
    "Computer Vision": "#16756f",
    "Image Processing": "#1e8f85",
    "MATLAB": "#3da699",
    "Information Retrieval": "#5db5a8",
}

ENGINEERING_DISPLAY = {
    "traffic_prediction": {
        "subtitle": "城市交通流预测系统",
        "summary": "A deployable traffic-flow prediction system that connects data upload, LSTM/GRU training, live evaluation, user management, and FastAPI documentation in one operational workflow.",
    },
    "venture_agent": {
        "subtitle": "AI 商业评估小程序",
        "summary": "A WeChat Mini Program that turns a business plan into AI evaluation, trend analysis, case exploration, knowledge graph browsing, and report export.",
    },
    "social_diffusion": {
        "subtitle": "社交扩散多智能体系统",
        "summary": "A multi-agent simulation environment for information diffusion, trust memory, hybrid decision making, intervention experiments, and result analysis.",
    },
    "puzzle_solver": {
        "subtitle": "搜索算法解谜系统",
        "summary": "An interactive learning system that makes DFS, BFS, A*, and backtracking concrete through puzzle generation, animation, and AI explanations.",
    },
    "image_search": {
        "subtitle": "多源特征融合图像检索系统",
        "summary": "A MATLAB image-retrieval application that combines color, texture, and shape features with fusion scoring and performance evaluation.",
    },
}


def _clean_markup(markup: str) -> str:
    clean = "\n".join(line.lstrip() for line in dedent(markup).strip().splitlines())
    return clean


def _html(markup: str) -> None:
    st.markdown(_clean_markup(markup), unsafe_allow_html=True)


def _render_image_html(item: Dict, caption: str = "", class_name: str = "") -> str:
    figure_class = f"portfolio-figure {class_name}".strip()
    if not item:
        return f'<div class="{figure_class}"><div class="gallery-card-placeholder" style="min-height:220px;">Image not available</div></div>'
    title = escape(item.get("title", ""), quote=True)
    file_path = item.get("file")
    caption_text = caption if caption else item.get("description", "")
    cap_html = f'<div class="portfolio-figure-caption">{escape(caption_text)}</div>'
    if file_path:
        b64 = get_image_base64(file_path)
        if b64:
            suffix = Path(file_path).suffix.lower()
            mime = "image/jpeg" if suffix in {".jpg", ".jpeg"} else "image/png"
            return f'<div class="{figure_class}"><div class="portfolio-media"><img src="data:{mime};base64,{b64}" alt="{title}" /></div>{cap_html}</div>'
    return f'<div class="{figure_class}"><div class="gallery-card-placeholder" style="min-height:220px;">{title}</div>{cap_html}</div>'


def render_projects_section() -> None:
    selected_id = st.session_state.get("selected_project")
    query_id = st.query_params.get("project", "")
    if isinstance(query_id, list):
        query_id = query_id[0] if query_id else ""
    if query_id and query_id != selected_id:
        st.session_state.selected_project = query_id
        selected_id = query_id
    selected_project = next((project for project in PROJECTS if project["id"] == selected_id), None)
    
    if selected_project:
        render_project_detail(selected_project)
        return

    st.markdown(
        """
        <div class="section-header">
            <div class="section-kicker">Engineering Projects</div>
            <div class="section-title">Showcase of software engineering and AI development projects.</div>
            <div class="section-copy">
                Click on any project to view detailed information including tech stack, architecture, and features.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    all_tags = sorted(set(tag for project in PROJECTS for tag in project["tags"]))
    selected_tags = st.multiselect(
        "Filter by Tags",
        all_tags,
        key="project_tags_filter",
    )

    filtered_projects = PROJECTS
    if selected_tags:
        filtered_projects = [
            p for p in PROJECTS if any(tag in p["tags"] for tag in selected_tags)
        ]

    cols = st.columns(2)
    for idx, project in enumerate(filtered_projects):
        with cols[idx % 2]:
            tag_chips = "".join(
                f'<span class="project-chip" style="background: {TAG_COLORS.get(tag, "#6f7d7b")}15; color: {TAG_COLORS.get(tag, "#6f7d7b")}; border-color: {TAG_COLORS.get(tag, "#6f7d7b")}30;">{tag}</span>'
                for tag in project["tags"]
            )

            tech_stack_preview = []
            for category in ["frontend", "backend", "ai", "algorithm", "language"]:
                if category in project["tech_stack"]:
                    tech_stack_preview.extend(project["tech_stack"][category][:2])
            
            tech_chips = "".join(
                f'<span class="tech-chip">{tech}</span>' for tech in tech_stack_preview[:4]
            )

            st.markdown(
                f"""
                <div class="project-card">
                    <div class="project-header">
                        <div class="project-title">{project["title"]}</div>
                        <a href="{project['github_url']}" target="_blank" class="project-github-link">
                            <svg viewBox="0 0 24 24" fill="currentColor" height="20" width="20">
                                <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.114 2.504.336 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .268.18.578.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
                            </svg>
                        </a>
                    </div>
                    <div class="project-chinese-title">{project["chinese_title"]}</div>
                    <div class="project-description">{project["description"]}</div>
                    <div class="project-tags">{tag_chips}</div>
                    <div class="project-tech-preview">
                        <span class="project-tech-label">Tech Stack:</span>
                        {tech_chips}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("View Detail", use_container_width=True, key=f"view-project-{project['id']}"):
                st.session_state.selected_project = project["id"]
                st.query_params["project"] = project["id"]
                st.rerun()


def render_project_detail(project: Dict) -> None:
    if st.button("Back to Projects", key="back-to-projects"):
        st.session_state.selected_project = None
        try:
            if "project" in st.query_params:
                del st.query_params["project"]
        except Exception:
            pass
        st.rerun()

    if project.get("gallery"):
        render_project_showcase(project)
        return

    tag_chips = "".join(
        f'<span class="project-chip" style="background: {TAG_COLORS.get(tag, "#6f7d7b")}15; color: {TAG_COLORS.get(tag, "#6f7d7b")}; border-color: {TAG_COLORS.get(tag, "#6f7d7b")}30;">{tag}</span>'
        for tag in project["tags"]
    )

    st.markdown(
        f"""
        <div class="project-detail-header">
            <div class="project-detail-title-row">
                <div>
                    <div class="project-detail-title">{project["title"]}</div>
                    <div class="project-detail-chinese-title">{project["chinese_title"]}</div>
                </div>
                <a href="{project['github_url']}" target="_blank" class="project-detail-github">
                    <svg viewBox="0 0 24 24" fill="currentColor" height="28" width="28">
                        <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.114 2.504.336 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .268.18.578.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
                    </svg>
                    <span>View on GitHub</span>
                </a>
            </div>
            <div class="project-detail-tags">{tag_chips}</div>
            <div class="project-detail-description">{project["long_description"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.2, 0.8])
    
    with left:
        st.markdown(
            """
            <div class="project-detail-section">
                <h3>🏗️ Architecture</h3>
                """,
            unsafe_allow_html=True,
        )
        
        st.markdown(
            f'<div class="project-architecture">{project["architecture"]["overview"]}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <h4>Layered Architecture:</h4>
            <ul class="project-features">
            """,
            unsafe_allow_html=True,
        )
        for layer in project["architecture"]["layers"]:
            st.markdown(
                f'<li><strong>{layer["name"]}</strong>: {layer["description"]}</li>',
                unsafe_allow_html=True,
            )
        st.markdown('</ul>', unsafe_allow_html=True)

        st.markdown(
            """
            <h4>Data Flow:</h4>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="project-architecture">{project["architecture"]["flow"]}</div>',
            unsafe_allow_html=True,
        )

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="project-detail-section">
                <h3>✨ Features</h3>
                <div class="project-features-grid">
            """,
            unsafe_allow_html=True,
        )
        for feature in project["features"]:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-name">{feature["name"]}</div>
                    <div class="feature-description">{feature["description"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown('</div></div>', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="project-detail-section">
                <h3>🏆 Highlights</h3>
                <div class="project-highlights">
            """,
            unsafe_allow_html=True,
        )
        for highlight in project["highlights"]:
            st.markdown(f'<span class="project-highlight-tag">{highlight}</span>', unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

    with right:
        st.markdown(
            """
            <div class="project-detail-panel">
                <h3>🛠️ Technology Stack</h3>
                """,
            unsafe_allow_html=True,
        )

        tech_stack = project["tech_stack"]
        for category, technologies in tech_stack.items():
            category_label = category.replace("_", " ").title()
            tech_chips = "".join(
                f'<span class="tech-stack-chip">{tech}</span>' for tech in technologies
            )
            st.markdown(
                f"""
                <div class="tech-category">
                    <div class="tech-category-label">{category_label}</div>
                    <div class="tech-category-items">{tech_chips}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown('</div>', unsafe_allow_html=True)


def render_project_showcase(project: Dict) -> None:
    gallery = project.get("gallery", {})
    figures = {f["title"].split(":")[0].strip(): f for f in gallery.get("figures", [])}

    if project["id"] in {"traffic_prediction", "traffic_flow", "social_diffusion", "puzzle_solver", "venture_agent", "image_search"}:
        _render_compact_engineering_showcase(project, figures)
    elif project["id"] == "social_diffusion":
        _render_project_showcase_hero(project)
        _render_project_section_overview(project, figures)
        _render_project_section_agent_types(project, figures)
        _render_project_section_visualization(project, figures)
        _render_project_section_decision_engine(project, figures)
        _render_project_section_experiment(project, figures)
        _render_project_section_results(project, figures)
    elif project["id"] == "traffic_flow":
        _render_tfp_showcase_hero(project)
        _render_tfp_section_overview(project, figures)
        _render_tfp_section_visualization(project, figures)
        _render_tfp_section_models(project, figures)
        _render_tfp_section_features(project, figures)
        _render_tfp_section_api(project, figures)
    elif project["id"] == "puzzle_solver":
        _render_puzzle_showcase_hero(project)
        _render_puzzle_section_overview(project, figures)
        _render_puzzle_section_puzzles(project, figures)
        _render_puzzle_section_algorithm(project, figures)
        _render_puzzle_section_visualization(project, figures)
        _render_puzzle_section_ai_features(project, figures)
    elif project["id"] == "venture_agent":
        _render_va_showcase_hero(project)
        _render_va_section_overview(project, figures)
        _render_va_section_evaluation(project, figures)
        _render_va_section_features(project, figures)
        _render_va_section_visualization(project, figures)
    elif project["id"] == "image_search":
        _render_ims_showcase_hero(project)
        _render_ims_section_overview(project, figures)
        _render_ims_section_features(project, figures)
        _render_ims_section_results(project, figures)
    else:
        _render_project_showcase_hero(project)
        _render_project_section_overview(project, figures)
        _render_project_section_agent_types(project, figures)
        _render_project_section_visualization(project, figures)
        _render_project_section_decision_engine(project, figures)
        _render_project_section_experiment(project, figures)
        _render_project_section_results(project, figures)


def _content_card(title: str, body_html: str, class_name: str = "") -> str:
    return f"""
    <div class="portfolio-content eng-note {class_name}">
        <h4>{escape(title)}</h4>
        {body_html}
    </div>
    """


def _list_card(title: str, items: Iterable[str], class_name: str = "") -> str:
    item_html = "".join(f"<li>{item}</li>" for item in items)
    return _content_card(title, f"<ul>{item_html}</ul>", class_name)


def _figure(figures: Dict, key: str, caption: str, class_name: str) -> str:
    return _render_image_html(figures.get(key), caption=caption, class_name=class_name)


def _stack(items: Iterable[str], class_name: str = "") -> str:
    return f'<div class="eng-stack {class_name}">{"".join(items)}</div>'


def _render_engineering_hero(project: Dict, stats: List[Tuple[str, str]]) -> None:
    display = ENGINEERING_DISPLAY.get(project["id"], {})
    tag_chips = "".join(
        f'<span class="portfolio-hero-tag">{escape(tag)}</span>' for tag in project["tags"]
    )
    stats_html = "".join(
        f"""
        <div class="portfolio-stat">
            <span>{escape(label)}</span>
            <strong>{escape(value)}</strong>
        </div>
        """
        for label, value in stats
    )
    description = display.get("summary") or project.get("summary") or project.get("long_description") or project.get("description", "")
    subtitle = display.get("subtitle") or project["chinese_title"]
    _html(
        f"""
        <div class="portfolio-hero eng-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Engineering Project</span>
                {tag_chips}
            </div>
            <h1 class="portfolio-hero-title">{escape(project["title"])}</h1>
            <div class="portfolio-hero-sub">{escape(subtitle)}</div>
            <p class="portfolio-hero-sub">{escape(description)}</p>
            <div class="portfolio-hero-stats">{stats_html}</div>
        </div>
        """
    )


def _repo_summary_cards(project: Dict, stack_items: Iterable[str], feature_items: Iterable[str]) -> str:
    repo = escape(project["github_url"], quote=True)
    return f"""
    <div class="eng-grid eng-grid-summary eng-span-12">
        {_content_card(
            "Repository",
            f'<p><a href="{repo}" target="_blank">{repo}</a></p>',
            "eng-span-4 eng-note-compact",
        )}
        {_list_card("Tech Stack", stack_items, "eng-span-4 eng-note-compact")}
        {_list_card("Portfolio Value", feature_items, "eng-span-4 eng-note-compact")}
    </div>
    """


def _render_compact_engineering_showcase(project: Dict, figures: Dict) -> None:
    project_id = project["id"]
    if project_id in {"traffic_prediction", "traffic_flow"}:
        _render_tfp_compact(project, figures)
    elif project_id == "venture_agent":
        _render_va_compact(project, figures)
    elif project_id == "social_diffusion":
        _render_social_compact(project, figures)
    elif project_id == "puzzle_solver":
        _render_puzzle_compact(project, figures)
    elif project_id == "image_search":
        _render_ims_compact(project, figures)


def _render_tfp_compact(project: Dict, figures: Dict) -> None:
    _render_engineering_hero(
        project,
        [
            ("Models", "LSTM + GRU"),
            ("Dataset", "PEMS04"),
            ("Backend", "FastAPI"),
            ("Database", "MySQL"),
        ],
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Control Room</span>
                    <h2 class="portfolio-section-title">Prediction workflow, live training, and result validation</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 1", "Figure 1 | Main dashboard: data overview, prediction status, and navigation are treated as the entry point of the system.", "eng-span-7 project-shot project-shot-main")}
                {_stack([
                    _figure(figures, "Figure 8", "Figure 8 | Training progress: loss curve and epoch status provide immediate feedback during model fitting.", "project-shot project-shot-compact"),
                    _content_card(
                        "Design Logic",
                        "<p>The detail page now follows the actual user path: upload or inspect data, train LSTM/GRU models, then validate predictions with charts instead of isolating every screenshot into a separate row.</p>",
                        "eng-note-compact",
                    ),
                ], "eng-span-5")}
                {_figure(figures, "Figure 2", "Figure 2 | Traffic heatmap: spatial and temporal flow distribution explains where congestion patterns emerge.", "eng-span-6 project-shot")}
                {_figure(figures, "Figure 4", "Figure 4 | Prediction results: predicted and observed values are placed next to the heatmap for direct comparison.", "eng-span-6 project-shot")}
            </div>
        </section>

        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Engineering Surface</span>
                    <h2 class="portfolio-section-title">Model controls, data operations, and API access</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 3", "Figure 3 | Model comparison: LSTM and GRU outputs are shown side by side to support model selection.", "eng-span-5 project-shot")}
                {_figure(figures, "Figure 5", "Figure 5 | Model configuration: hyperparameters stay close to the performance chart because they directly change the result.", "eng-span-4 project-shot")}
                {_list_card(
                    "System Modules",
                    [
                        "<strong>Training:</strong> configurable epochs, hidden dimensions, and sequence length.",
                        "<strong>Prediction:</strong> chart-based comparison with traffic-flow history.",
                        "<strong>Management:</strong> users, roles, and historical data are maintained as operational features.",
                    ],
                    "eng-span-3 eng-note-compact",
                )}
                {_figure(figures, "Figure 6", "Figure 6 | User management: registration, login, and role permissions are grouped with the data-management surface.", "eng-span-5 project-shot project-shot-wide")}
                {_figure(figures, "Figure 7", "Figure 7 | Data management: upload, query, and export flows for historical traffic records.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 9", "Figure 9 | API documentation: the very wide Swagger screen becomes a compact strip rather than an oversized block.", "eng-span-3 project-shot project-shot-strip")}
            </div>
            {_repo_summary_cards(
                project,
                ["FastAPI + Flask", "PyTorch LSTM/GRU", "MySQL + SQLAlchemy", "Bootstrap charts"],
                ["End-to-end forecasting workflow", "Model comparison and tuning", "Operational API and data-management layer"],
            )}
        </section>
        """
    )


def _render_social_compact(project: Dict, figures: Dict) -> None:
    _render_engineering_hero(
        project,
        [
            ("Agent Types", "6 Personalities"),
            ("Decision Mode", "Rule + LLM"),
            ("Memory", "SQLite"),
            ("Visualization", "NetworkX"),
        ],
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Simulation Setup</span>
                    <h2 class="portfolio-section-title">Dashboard, live status, and agent configuration</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 1", "Figure 1 | System dashboard: the main control surface combines parameter setup, progress state, and network preview.", "eng-span-8 project-shot project-shot-main")}
                {_stack([
                    _figure(figures, "Figure 12", "Figure 12 | System stats: the ultra-wide metric strip is kept slim so it does not waste vertical space.", "project-shot project-shot-strip"),
                    _content_card(
                        "Setup Narrative",
                        "<p>The page starts with the control dashboard and the live statistics strip, then immediately shows how agent personalities and simulation parameters shape the experiment.</p>",
                        "eng-note-compact",
                    ),
                    _figure(figures, "Figure 10", "Figure 10 | Parameter settings: network scale, propagation probability, and iteration count.", "project-shot project-shot-compact"),
                ], "eng-span-4")}
                {_figure(figures, "Figure 2", "Figure 2 | Agent types: six personality presets define different forwarding and belief-update behavior.", "eng-span-6 project-shot")}
                {_list_card(
                    "Agent Spectrum",
                    [
                        "<strong>Gullible / Emotional:</strong> accelerate spread and create volatile cascades.",
                        "<strong>Rational / Debunker:</strong> slow propagation through verification and correction.",
                        "<strong>Influencer / Silent:</strong> change topology pressure through connectivity or low activity.",
                    ],
                    "eng-span-6 eng-note",
                )}
            </div>
        </section>

        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Network Dynamics</span>
                    <h2 class="portfolio-section-title">Topology, diffusion, trust, and memory in one visual run</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 3", "Figure 3 | Social network visualization: colored nodes reveal the agent-type distribution and network structure.", "eng-span-7 project-shot")}
                {_figure(figures, "Figure 4", "Figure 4 | Information diffusion: propagation state is placed beside topology so the cause-effect relation is readable.", "eng-span-5 project-shot")}
                {_figure(figures, "Figure 5", "Figure 5 | Trust matrix: pairwise trust changes are shown as a compact heatmap.", "eng-span-6 project-shot")}
                {_figure(figures, "Figure 9", "Figure 9 | Agent memory viewer: interaction records and trust history explain why agents make later decisions.", "eng-span-6 project-shot project-shot-strip")}
            </div>
        </section>

        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Experiment & Results</span>
                    <h2 class="portfolio-section-title">Decision engine, intervention design, and outcome comparison</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 6", "Figure 6 | Decision engine: switch between rule-based decisions and LLM-driven context reasoning.", "eng-span-5 project-shot")}
                {_figure(figures, "Figure 7", "Figure 7 | Intervention panel: education, censorship, counter-message, and quarantine strategies.", "eng-span-4 project-shot")}
                {_list_card(
                    "Experiment Controls",
                    [
                        "<strong>Rule mode:</strong> fast and reproducible for large simulations.",
                        "<strong>LLM mode:</strong> richer social context for selected agents.",
                        "<strong>A/B setup:</strong> compare intervention policies under matched initial conditions.",
                    ],
                    "eng-span-3 eng-note-compact",
                )}
                {_figure(figures, "Figure 11", "Figure 11 | A/B experiment setup: two intervention strategies can be compared side by side.", "eng-span-5 project-shot project-shot-strip")}
                {_figure(figures, "Figure 8", "Figure 8 | Simulation results: diffusion curves and intervention effect metrics close the experiment loop.", "eng-span-7 project-shot project-shot-strip")}
            </div>
            {_repo_summary_cards(
                project,
                ["Python + Streamlit", "DeepSeek API", "SQLite + SQLAlchemy", "NetworkX + Matplotlib"],
                ["Multi-agent simulation", "Rule/LLM decision modes", "Intervention strategy evaluation"],
            )}
        </section>
        """
    )


def _render_puzzle_compact(project: Dict, figures: Dict) -> None:
    _render_engineering_hero(
        project,
        [
            ("Puzzles", "5 Types"),
            ("Algorithms", "DFS/BFS/A*"),
            ("Backend", "Flask"),
            ("Visualization", "Canvas"),
        ],
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Learning Workflow</span>
                    <h2 class="portfolio-section-title">Choose a puzzle, configure it, then inspect the solved path</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 1", "Figure 1 | Homepage: puzzle selection is the first portfolio signal, so it receives the lead position.", "eng-span-7 project-shot")}
                {_stack([
                    _figure(figures, "Figure 12", "Figure 12 | Puzzle configuration: difficulty and board-size settings stay next to the homepage.", "project-shot project-shot-compact"),
                    _content_card(
                        "Interaction Flow",
                        "<p>The screenshots are ordered around how a learner actually uses the system: select a problem, tune it, run a solver, watch the path, and review performance or history.</p>",
                        "eng-note-compact",
                    ),
                ], "eng-span-5")}
                {_figure(figures, "Figure 2", "Figure 2 | Maze puzzle: pathfinding mode with DFS/BFS/A* visualization.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 13", "Figure 13 | Solution path: the solved route is paired with the maze because it is the immediate outcome.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 8", "Figure 8 | Search animation: the taller animation view is constrained and placed as a visual anchor.", "eng-span-4 project-shot project-shot-tall")}
            </div>
        </section>

        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Puzzle Gallery</span>
                    <h2 class="portfolio-section-title">Five puzzle types arranged by visual density</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 3", "Figure 3 | 8-Puzzle: sliding-tile search state and controls.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 4", "Figure 4 | N-Queens: the only portrait-like board view is placed among wider puzzle screens to balance the row.", "eng-span-4 project-shot project-shot-tall")}
                {_figure(figures, "Figure 5", "Figure 5 | Sudoku: constraint-solving interface with manual and automatic modes.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 6", "Figure 6 | Sokoban: box-pushing puzzle state and solver controls.", "eng-span-4 project-shot")}
                {_list_card(
                    "Puzzle Coverage",
                    [
                        "<strong>Path search:</strong> Maze and Sokoban emphasize route planning.",
                        "<strong>State search:</strong> 8-Puzzle highlights permutation search.",
                        "<strong>Constraint solving:</strong> N-Queens and Sudoku show backtracking behavior.",
                    ],
                    "eng-span-4 eng-note",
                )}
                {_figure(figures, "Figure 16", "Figure 16 | Settings: animation speed and theme controls are kept as a small utility screenshot.", "eng-span-4 project-shot project-shot-compact")}
            </div>
        </section>

        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Algorithms & Learning</span>
                    <h2 class="portfolio-section-title">Performance comparison, solver selection, and AI guidance</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 7", "Figure 7 | Algorithm comparison: expanded nodes and timing metrics compare DFS, BFS, and A*.", "eng-span-5 project-shot")}
                {_figure(figures, "Figure 14", "Figure 14 | Performance stats: complexity and runtime feedback sit beside the comparison chart.", "eng-span-4 project-shot")}
                {_list_card(
                    "Algorithm Layer",
                    [
                        "<strong>DFS:</strong> memory-light exploration.",
                        "<strong>BFS:</strong> complete and optimal for uniform costs.",
                        "<strong>A*:</strong> heuristic-guided search for faster convergence.",
                        "<strong>Backtracking:</strong> constraint pruning for board puzzles.",
                    ],
                    "eng-span-3 eng-note-compact",
                )}
                {_figure(figures, "Figure 11", "Figure 11 | Algorithm selection: users can switch solving methods before running a puzzle.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 9", "Figure 9 | AI learning assistant: DeepSeek explanations convert solver behavior into teaching content.", "eng-span-4 project-shot")}
                {_figure(figures, "Figure 10", "Figure 10 | User profile: learning progress and solved history.", "eng-span-2 project-shot project-shot-compact")}
                {_figure(figures, "Figure 15", "Figure 15 | History records: replay and review previous solutions.", "eng-span-2 project-shot project-shot-compact")}
            </div>
            {_repo_summary_cards(
                project,
                ["Flask + Python", "HTML5 Canvas", "SQLite + SQLAlchemy", "DeepSeek API"],
                ["Interactive algorithm education", "Real-time solver animation", "Search performance comparison"],
            )}
        </section>
        """
    )


def _render_va_compact(project: Dict, figures: Dict) -> None:
    _render_engineering_hero(
        project,
        [
            ("Platform", "WeChat Mini Program"),
            ("AI Engine", "DeepSeek"),
            ("Backend", "Node.js"),
            ("Database", "MongoDB"),
        ],
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Core Journey</span>
                    <h2 class="portfolio-section-title">From business input to AI report export</h2>
                </div>
            </div>
            <div class="eng-phone-grid">
                {_figure(figures, "Figure 1", "Figure 1 | Entry screen: core feature entry points for the mini program.", "project-shot project-shot-phone")}
                {_figure(figures, "Figure 2", "Figure 2 | Business plan evaluation: users provide a plan for AI analysis.", "project-shot project-shot-phone")}
                {_figure(figures, "Figure 3", "Figure 3 | Evaluation report: multi-dimensional scores and generated recommendations.", "project-shot project-shot-phone")}
                {_figure(figures, "Figure 9", "Figure 9 | Report export: the final evaluation can be exported as a professional document.", "project-shot project-shot-phone")}
            </div>
            <div class="eng-grid eng-grid-after-phone">
                {_list_card(
                    "Evaluation Pipeline",
                    [
                        "<strong>Input:</strong> collect business-plan content inside the mini program.",
                        "<strong>Analysis:</strong> DeepSeek evaluates market, team, product, finance, and risk dimensions.",
                        "<strong>Output:</strong> structured report with grade, confidence, suggestions, and export flow.",
                    ],
                    "eng-span-8 eng-note",
                )}
                {_content_card(
                    "Layout Choice",
                    "<p>All VentureAgent screenshots are tall phone captures, so the page uses a screen wall instead of oversized single screenshots. This keeps the portfolio compact while still preserving the full mobile UI.</p>",
                    "eng-span-4 eng-note-compact",
                )}
            </div>
        </section>

        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Business Intelligence</span>
                    <h2 class="portfolio-section-title">Market analysis, cases, knowledge graph, and user center</h2>
                </div>
            </div>
            <div class="eng-phone-grid eng-phone-grid-mixed">
                {_figure(figures, "Figure 4", "Figure 4 | Market trend analysis: industry movement and trend summaries.", "project-shot project-shot-phone")}
                {_figure(figures, "Figure 5", "Figure 5 | Business case library: categorized cases and keyword search.", "project-shot project-shot-phone")}
                {_figure(figures, "Figure 6", "Figure 6 | Knowledge graph: relationships between business concepts visualized as a network.", "project-shot project-shot-phone")}
                {_figure(figures, "Figure 7", "Figure 7 | Knowledge base: articles covering financing, legal, operations, and startup execution.", "project-shot project-shot-phone")}
            </div>
            <div class="eng-grid eng-grid-after-phone">
                {_figure(figures, "Figure 8", "Figure 8 | User profile: evaluation history and personal collections.", "eng-span-3 project-shot project-shot-phone project-shot-phone-small")}
                {_list_card(
                    "Feature Map",
                    [
                        "<strong>Analysis:</strong> market trend summaries and business-plan scoring.",
                        "<strong>Knowledge:</strong> case library, startup articles, and concept graph.",
                        "<strong>User system:</strong> profile, history, favorites, and report export.",
                    ],
                    "eng-span-5 eng-note",
                )}
                {_repo_summary_cards(
                    project,
                    ["WeChat Mini Program", "Node.js + Express", "DeepSeek API", "MongoDB + Mongoose"],
                    ["Complete mobile product flow", "AI business-evaluation workflow", "Knowledge and case-based learning system"],
                )}
            </div>
        </section>
        """
    )


def _render_ims_compact(project: Dict, figures: Dict) -> None:
    _render_engineering_hero(
        project,
        [
            ("Language", "MATLAB"),
            ("Features", "Color/Texture/Shape"),
            ("Fusion", "Weighted + Decision"),
            ("Evaluation", "Precision/Recall"),
        ],
    )
    _html(
        f"""
        <section class="portfolio-section portfolio-section-compact eng-section">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Retrieval Workflow</span>
                    <h2 class="portfolio-section-title">Query, feature fusion, results, and evaluation in one compact spread</h2>
                </div>
            </div>
            <div class="eng-grid">
                {_figure(figures, "Figure 1", "Figure 1 | System interface: query image, dataset controls, and retrieval workflow are introduced first.", "eng-span-7 project-shot project-shot-main")}
                {_stack([
                    _content_card(
                        "Fusion Logic",
                        "<p>The application extracts complementary visual descriptors, then combines similarity scores so color, texture, and shape do not compete as isolated signals.</p>",
                        "eng-note-compact",
                    ),
                    _list_card(
                        "Feature Sources",
                        ["Color histogram", "GLCM texture statistics", "Hu moments shape descriptor", "Weighted and decision-level fusion"],
                        "eng-note-compact",
                    ),
                ], "eng-span-5")}
                {_figure(figures, "Figure 2", "Figure 2 | Retrieval results: ranked matches are placed before feature details because this is the user-visible outcome.", "eng-span-6 project-shot")}
                {_figure(figures, "Figure 3", "Figure 3 | Feature visualization: color, texture, and shape descriptors explain why the ranking changes.", "eng-span-6 project-shot")}
            </div>
            {_repo_summary_cards(
                project,
                ["MATLAB", "Image Processing Toolbox", "Computer Vision Toolbox", "Feature vector database"],
                ["Multi-source image retrieval", "Similarity and fusion strategy comparison", "Precision, recall, MAP, and F1 evaluation"],
            )}
        </section>
        """
    )


def _render_project_showcase_hero(project: Dict) -> None:
    tag_chips = "".join(
        f'<span class="portfolio-hero-tag">{tag}</span>' for tag in project["tags"]
    )
    st.markdown(
        f"""
        <div class="portfolio-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Engineering Project</span>
                {tag_chips}
            </div>
            <h1 class="portfolio-hero-title">{project["title"]}</h1>
            <div class="portfolio-hero-sub">{project["chinese_title"]}</div>
            <p class="portfolio-hero-sub">{project["summary"] if "summary" in project else project["long_description"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Agent Types</span>
                    <strong>6 Personalities</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Decision Mode</span>
                    <strong>Rule + LLM</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Database</span>
                    <strong>SQLite</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Visualization</span>
                    <strong>NetworkX + Charts</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_project_section_overview(project: Dict, figures: Dict) -> None:
    figure_html = _render_image_html(
        figures.get("Figure 1"),
        caption="Figure 1 | System Dashboard — main control panel with parameter configuration, simulation progress, and network topology preview.",
    )
    figure_html12 = _render_image_html(
        figures.get("Figure 12"),
        caption="Figure 12 | System Stats — real-time metrics showing agent count, message propagation volume, and simulation status.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">System Architecture & Workflow</h2>
                </div>
            </div>
            <div class="pg pg-32">
                {figure_html}
                <div>
                    {figure_html12}
                    <div class="pg pg-single">
                        <div class="portfolio-content">
                            <h4>Problem</h4>
                            <p>
                                Social networks exhibit complex information diffusion patterns that are hard to predict and control. Existing models lack personalized agent behaviors and real-time visualization.
                            </p>
                        </div>
                        <div class="portfolio-content">
                            <h4>Solution</h4>
                            <p>
                                Build a multi-agent simulation platform with 6 personality types, hybrid decision engine, persistent memory, and interactive visualization.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="pg pg-2">
                <div class="portfolio-content">
                    <h4>Tech Stack</h4>
                    <p>
                        Streamlit frontend, Python backend, DeepSeek LLM, SQLite/SQLAlchemy, NetworkX visualization.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Key Features</h4>
                    <ul>
                        <li>Real-time network visualization</li>
                        <li>A/B experiment framework</li>
                        <li>Intervention strategy testing</li>
                        <li>Trust relationship modeling</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_project_section_agent_types(project: Dict, figures: Dict) -> None:
    figure_html = _render_image_html(
        figures.get("Figure 2"),
        caption="Figure 2 | Agent Types Configuration — six personality types: Gullible, Rational, Influencer, Debunker, Emotional, Silent.",
    )
    figure_html10 = _render_image_html(
        figures.get("Figure 10"),
        caption="Figure 10 | Parameter Settings — detailed configuration for network scale, propagation probability, iteration count, and agent distribution.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Agent System</span>
                    <h2 class="portfolio-section-title">Six Personality Agent Types</h2>
                </div>
            </div>
            <div class="pg pg-23">
                {figure_html}
                <div class="portfolio-content">
                    <h4>Agent Personality Spectrum</h4>
                    <ul>
                        <li><strong>Gullible (轻信型)</strong>: High trust, easily influenced, fast information spreader.</li>
                        <li><strong>Rational (理性型)</strong>: Low trust, fact-checks before forwarding, slow but accurate.</li>
                        <li><strong>Influencer (影响者型)</strong>: High connectivity, amplifies messages it believes.</li>
                        <li><strong>Debunker (辟谣型)</strong>: Actively identifies and counters misinformation.</li>
                        <li><strong>Emotional (情感型)</strong>: Decisions based on sentiment, volatile behavior.</li>
                        <li><strong>Silent (沉默型)</strong>: Rarely initiates, only responds when directly engaged.</li>
                    </ul>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                {figure_html10}
                <div class="portfolio-content">
                    <h4>Parameter Configuration</h4>
                    <p>
                        The system supports fine-grained parameter tuning including network size, edge density, information propagation probability, intervention intensity, and iteration steps. Each parameter can be adjusted independently or preset to common simulation scenarios.
                    </p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_project_section_visualization(project: Dict, figures: Dict) -> None:
    figure_html3 = _render_image_html(
        figures.get("Figure 3"),
        caption="Figure 3 | Social Network Visualization — dynamic topology showing agent nodes with different colors representing personality types.",
    )
    figure_html4 = _render_image_html(
        figures.get("Figure 4"),
        caption="Figure 4 | Information Diffusion Simulation — color-coded propagation showing how information spreads across the network over time.",
    )
    figure_html5 = _render_image_html(
        figures.get("Figure 5"),
        caption="Figure 5 | Trust Relationship Matrix — heatmap showing trust levels between agent pairs, updated dynamically during simulation.",
    )
    figure_html9 = _render_image_html(
        figures.get("Figure 9"),
        caption="Figure 9 | Agent Memory Viewer — detailed view of trust history and interaction records for individual agents.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Visualization</span>
                    <h2 class="portfolio-section-title">Network Topology & Diffusion Visualization</h2>
                </div>
            </div>
            <div class="pg pg-single">
                {figure_html3}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                {figure_html4}
                {figure_html5}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                {figure_html9}
                <div class="portfolio-content">
                    <h4>Persistent Memory System</h4>
                    <p>
                        Each agent maintains a memory database recording:
                    </p>
                    <ul>
                        <li>Trust scores for every other agent</li>
                        <li>History of interactions and messages received</li>
                        <li>Decisions made and outcomes observed</li>
                        <li>Social network structure changes over time</li>
                    </ul>
                    <div class="portfolio-insight-box">
                        <strong>Memory-Driven Behavior</strong>
                        <p>Agents update trust based on past interactions, creating emergent social dynamics that mimic real-world social networks.</p>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_project_section_decision_engine(project: Dict, figures: Dict) -> None:
    figure_html = _render_image_html(
        figures.get("Figure 6"),
        caption="Figure 6 | Decision Engine — supports both rule-based and LLM-driven decision modes with seamless switching.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Core Engine</span>
                    <h2 class="portfolio-section-title">Hybrid Decision Engine</h2>
                </div>
            </div>
            <div class="pg pg-23">
                <div class="portfolio-content">
                    <h4>Rule-Based Decision</h4>
                    <p>
                        Agents use predefined rules based on personality traits, trust scores, and message characteristics to make decisions. This mode is fast and deterministic, suitable for large-scale simulations.
                    </p>
                    <h4>LLM-Driven Decision</h4>
                    <p>
                        For more realistic behavior, agents can query DeepSeek API to make context-aware decisions. The LLM considers agent personality, message content, trust relationships, and social context.
                    </p>
                    <h4>Hybrid Mode</h4>
                    <p>
                        The system supports mixing both modes — some agents use rules for efficiency while key influencers use LLM for nuanced behavior.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Architecture Design</strong>
                        <p>The decision engine is pluggable, making it easy to extend with new decision algorithms or swap LLM providers.</p>
                    </div>
                </div>
                {figure_html}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_project_section_experiment(project: Dict, figures: Dict) -> None:
    figure_html7 = _render_image_html(
        figures.get("Figure 7"),
        caption="Figure 7 | Intervention Strategy Panel — configure different rumor control strategies: education, censorship, counter-messaging, quarantine.",
    )
    figure_html11 = _render_image_html(
        figures.get("Figure 11"),
        caption="Figure 11 | A/B Experiment Setup — compare two different intervention strategies side by side under identical initial conditions.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Experiment</span>
                    <h2 class="portfolio-section-title">Intervention Strategies & A/B Testing</h2>
                </div>
            </div>
            <div class="pg pg-2">
                {figure_html7}
                {figure_html11}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-4">
                <div class="portfolio-content">
                    <h4>Education</h4>
                    <p>Improve agent critical thinking over time, reducing gullibility gradually.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Censorship</h4>
                    <p>Block specific messages at source or during propagation.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Counter-Messaging</h4>
                    <p>Introduce debunking messages from trusted sources.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Quarantine</h4>
                    <p>Isolate highly connected nodes temporarily.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_project_section_results(project: Dict, figures: Dict) -> None:
    figure_html = _render_image_html(
        figures.get("Figure 8"),
        caption="Figure 8 | Simulation Results Chart — information diffusion curves comparing different intervention strategies and their effectiveness.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Results</span>
                    <h2 class="portfolio-section-title">Simulation Results & Analysis</h2>
                </div>
            </div>
            <div class="pg pg-23">
                {figure_html}
                <div class="portfolio-content">
                    <h4>Key Metrics</h4>
                    <ul>
                        <li><strong>Spread Rate</strong>: How quickly information reaches the network.</li>
                        <li><strong>Penetration Rate</strong>: Percentage of agents exposed to the message.</li>
                        <li><strong>Belief Persistence</strong>: How long agents maintain their opinion.</li>
                        <li><strong>Intervention Effectiveness</strong>: Reduction in misinformation spread.</li>
                    </ul>
                    <div class="portfolio-insight-box">
                        <strong>Research Value</strong>
                        <p>This platform enables researchers to study information diffusion dynamics, test intervention strategies, and understand how different personality distributions affect rumor spread.</p>
                    </div>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>GitHub Repository</h4>
                    <p>
                        <a href="{project['github_url']}" target="_blank" style="color:#1a5c52;font-weight:bold;">{project['github_url']}</a>
                    </p>
                    <p>Complete with unit tests, documentation, and Docker support.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Tech Stack Summary</h4>
                    <ul>
                        <li>Python + Streamlit</li>
                        <li>DeepSeek API</li>
                        <li>SQLite + SQLAlchemy</li>
                        <li>NetworkX + Matplotlib</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Features</h4>
                    <ul>
                        <li>6 personality types</li>
                        <li>Rule + LLM decisions</li>
                        <li>A/B experiment</li>
                        <li>Real-time visualization</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_tfp_showcase_hero(project: Dict) -> None:
    tag_chips = "".join(
        f'<span class="portfolio-hero-tag">{tag}</span>' for tag in project["tags"]
    )
    st.markdown(
        f"""
        <div class="portfolio-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Engineering Project</span>
                {tag_chips}
            </div>
            <h1 class="portfolio-hero-title">{project["title"]}</h1>
            <div class="portfolio-hero-sub">{project["chinese_title"]}</div>
            <p class="portfolio-hero-sub">{project["long_description"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Models</span>
                    <strong>LSTM + GRU</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Dataset</span>
                    <strong>PEMS04</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Backend</span>
                    <strong>FastAPI</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Database</span>
                    <strong>MySQL</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_tfp_section_overview(project: Dict, figures: Dict) -> None:
    figure_html1 = _render_image_html(
        figures.get("Figure 1"),
        caption="Figure 1 | System Dashboard — main control panel with data overview, prediction status, and navigation.",
    )
    figure_html8 = _render_image_html(
        figures.get("Figure 8"),
        caption="Figure 8 | Training Progress — model training loss curve and progress visualization.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">System Architecture & Workflow</h2>
                </div>
            </div>
            <div class="pg pg-32">
                {figure_html1}
                <div>
                    {figure_html8}
                    <div class="pg pg-single">
                        <div class="portfolio-content">
                            <h4>Problem</h4>
                            <p>
                                Urban traffic flow prediction is crucial for intelligent transportation systems. Traditional methods fail to capture complex spatiotemporal dependencies between urban functional areas.
                            </p>
                        </div>
                        <div class="portfolio-content">
                            <h4>Solution</h4>
                            <p>
                                Build an end-to-end deep learning prediction system using LSTM/GRU models, incorporating urban functional area spatial relationships as key features.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="pg pg-2">
                <div class="portfolio-content">
                    <h4>Tech Stack</h4>
                    <p>
                        FastAPI backend, PyTorch for LSTM/GRU models, MySQL database, Bootstrap frontend with chart visualization.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Key Features</h4>
                    <ul>
                        <li>End-to-end deep learning prediction</li>
                        <li>RESTful API service</li>
                        <li>Real-time visualization</li>
                        <li>User authentication & permissions</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_tfp_section_visualization(project: Dict, figures: Dict) -> None:
    figure_html2 = _render_image_html(
        figures.get("Figure 2"),
        caption="Figure 2 | Traffic Flow Visualization — heatmap and spatiotemporal distribution of traffic flow.",
    )
    figure_html4 = _render_image_html(
        figures.get("Figure 4"),
        caption="Figure 4 | Prediction Results — comparison between predicted and actual values with error analysis.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Visualization</span>
                    <h2 class="portfolio-section-title">Traffic Flow Visualization & Results</h2>
                </div>
            </div>
            <div class="pg pg-2">
                {figure_html2}
                {figure_html4}
            </div>
            <div class="pg pg-2">
                <div class="portfolio-content">
                    <h4>Heatmap Visualization</h4>
                    <p>
                        Real-time traffic flow heatmap showing congestion patterns across different urban functional areas. Color intensity represents flow volume.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Prediction Comparison</h4>
                    <p>
                        Line charts comparing predicted vs. actual traffic flow at multiple sensor locations. Error metrics and confidence intervals are displayed.
                    </p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_tfp_section_models(project: Dict, figures: Dict) -> None:
    figure_html3 = _render_image_html(
        figures.get("Figure 3"),
        caption="Figure 3 | Model Comparison — LSTM vs GRU prediction performance comparison chart.",
    )
    figure_html5 = _render_image_html(
        figures.get("Figure 5"),
        caption="Figure 5 | Model Configuration — hyperparameter tuning interface for learning rate, epochs, hidden layers.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Models</span>
                    <h2 class="portfolio-section-title">LSTM &amp; GRU Prediction Models</h2>
                </div>
            </div>
            <div class="pg pg-23">
                <div class="portfolio-content">
                    <h4>LSTM Model</h4>
                    <p>
                        Long Short-Term Memory network captures long-term temporal dependencies in traffic flow sequences. Bidirectional LSTM processes both past and future context.
                    </p>
                    <h4>GRU Model</h4>
                    <p>
                        Gated Recurrent Unit simplifies LSTM by combining forget and input gates, reducing computation while maintaining performance.
                    </p>
                    <h4>Model Comparison</h4>
                    <p>
                        The system supports side-by-side comparison of LSTM and GRU models, showing which performs better on different traffic patterns.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Design Choice</strong>
                        <p>Providing both models allows users to experiment and choose based on their specific traffic characteristics and computational constraints.</p>
                    </div>
                </div>
                {figure_html3}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                {figure_html5}
                <div class="portfolio-content">
                    <h4>Hyperparameter Tuning</h4>
                    <p>
                        The configuration panel allows adjusting learning rate, batch size, number of epochs, hidden layer dimensions, and sequence length. Real-time validation metrics help find optimal settings.
                    </p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_tfp_section_features(project: Dict, figures: Dict) -> None:
    figure_html6 = _render_image_html(
        figures.get("Figure 6"),
        caption="Figure 6 | User Management — user registration, login, and role-based permission control.",
    )
    figure_html7 = _render_image_html(
        figures.get("Figure 7"),
        caption="Figure 7 | Data Management — historical traffic data upload, query, and export interface.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Features</span>
                    <h2 class="portfolio-section-title">User System & Data Management</h2>
                </div>
            </div>
            <div class="pg pg-2">
                {figure_html6}
                {figure_html7}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-4">
                <div class="portfolio-content">
                    <h4>User Authentication</h4>
                    <p>Complete registration, login, and session management with JWT tokens.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Role Management</h4>
                    <p>Admin, researcher, and viewer roles with granular permission control.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Data Upload</h4>
                    <p>Support for CSV/XLS upload of historical traffic flow data.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Data Export</h4>
                    <p>Export prediction results and analysis reports in multiple formats.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_tfp_section_api(project: Dict, figures: Dict) -> None:
    figure_html9 = _render_image_html(
        figures.get("Figure 9"),
        caption="Figure 9 | API Documentation — FastAPI automatically generated Swagger UI with interactive endpoints.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">API & Deployment</span>
                    <h2 class="portfolio-section-title">RESTful API & System Deployment</h2>
                </div>
            </div>
            <div class="pg pg-23">
                {figure_html9}
                <div class="portfolio-content">
                    <h4>FastAPI Endpoints</h4>
                    <ul>
                        <li><strong>Model Training</strong>: POST /api/model/train</li>
                        <li><strong>Prediction</strong>: POST /api/predict</li>
                        <li><strong>Data Query</strong>: GET /api/data</li>
                        <li><strong>User Management</strong>: CRUD /api/users</li>
                    </ul>
                    <div class="portfolio-insight-box">
                        <strong>API First Design</strong>
                        <p>Built with FastAPI for automatic OpenAPI documentation and async support, making integration with other systems seamless.</p>
                    </div>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>GitHub Repository</h4>
                    <p>
                        <a href="{project['github_url']}" target="_blank" style="color:#1a5c52;font-weight:bold;">{project['github_url']}</a>
                    </p>
                    <p>Complete with Docker support for easy deployment.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Tech Stack Summary</h4>
                    <ul>
                        <li>FastAPI + Flask</li>
                        <li>PyTorch LSTM/GRU</li>
                        <li>MySQL + SQLAlchemy</li>
                        <li>Bootstrap + Charts</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Features</h4>
                    <ul>
                        <li>End-to-end prediction</li>
                        <li>LSTM + GRU models</li>
                        <li>RESTful API</li>
                        <li>User management</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_puzzle_showcase_hero(project: Dict) -> None:
    tag_chips = "".join(
        f'<span class="portfolio-hero-tag">{tag}</span>' for tag in project["tags"]
    )
    st.markdown(
        f"""
        <div class="portfolio-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Engineering Project</span>
                {tag_chips}
            </div>
            <h1 class="portfolio-hero-title">{project["title"]}</h1>
            <div class="portfolio-hero-sub">{project["chinese_title"]}</div>
            <p class="portfolio-hero-sub">{project["long_description"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Puzzles</span>
                    <strong>5 Types</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Algorithms</span>
                    <strong>4 Methods</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Backend</span>
                    <strong>Flask</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Visualization</span>
                    <strong>Canvas</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_puzzle_section_overview(project: Dict, figures: Dict) -> None:
    figure_html1 = _render_image_html(
        figures.get("Figure 1"),
        caption="Figure 1 | System Homepage — five puzzle type selection cards.",
    )
    figure_html12 = _render_image_html(
        figures.get("Figure 12"),
        caption="Figure 12 | Puzzle Configuration — difficulty and size settings.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">Interactive Algorithm Learning Platform</h2>
                </div>
            </div>
            <div class="pg pg-32">
                {figure_html1}
                <div>
                    {figure_html12}
                    <div class="pg pg-single">
                        <div class="portfolio-content">
                            <h4>Problem</h4>
                            <p>
                                Learning search algorithms can be abstract and difficult. Traditional textbook explanations lack interactive visualization, making it hard to understand algorithm execution.
                            </p>
                        </div>
                        <div class="portfolio-content">
                            <h4>Solution</h4>
                            <p>
                                Build an interactive platform that visualizes search algorithms solving classic puzzles in real-time, making abstract concepts concrete and engaging.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="pg pg-2">
                <div class="portfolio-content">
                    <h4>Tech Stack</h4>
                    <p>
                        Flask backend, Python algorithms, Canvas visualization, SQLite database, DeepSeek AI integration.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Key Features</h4>
                    <ul>
                        <li>5 classic puzzles</li>
                        <li>4 search algorithms</li>
                        <li>Real-time Canvas animation</li>
                        <li>AI learning assistant</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_puzzle_section_puzzles(project: Dict, figures: Dict) -> None:
    figure_html2 = _render_image_html(figures.get("Figure 2"), caption="Figure 2 | Maze Puzzle")
    figure_html3 = _render_image_html(figures.get("Figure 3"), caption="Figure 3 | 8-Puzzle")
    figure_html4 = _render_image_html(figures.get("Figure 4"), caption="Figure 4 | N-Queens")
    figure_html5 = _render_image_html(figures.get("Figure 5"), caption="Figure 5 | Sudoku")
    figure_html6 = _render_image_html(figures.get("Figure 6"), caption="Figure 6 | Sokoban")
    figure_html13 = _render_image_html(figures.get("Figure 13"), caption="Figure 13 | Solution Path")
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Puzzles</span>
                    <h2 class="portfolio-section-title">Five Classic Puzzles</h2>
                </div>
            </div>
            <div class="pg pg-3">
                {figure_html2}
                {figure_html3}
                {figure_html4}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-3">
                {figure_html5}
                {figure_html6}
                {figure_html13}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-5">
                <div class="portfolio-content">
                    <h4>Maze</h4>
                    <p>Grid-based maze generation and pathfinding.</p>
                </div>
                <div class="portfolio-content">
                    <h4>8-Puzzle</h4>
                    <p>Sliding tile puzzle with 8 numbered tiles.</p>
                </div>
                <div class="portfolio-content">
                    <h4>N-Queens</h4>
                    <p>Place N queens on N×N board without attacking.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Sudoku</h4>
                    <p>9×9 grid number placement puzzle.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Sokoban</h4>
                    <p>Push boxes to target positions.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_puzzle_section_algorithm(project: Dict, figures: Dict) -> None:
    figure_html7 = _render_image_html(
        figures.get("Figure 7"),
        caption="Figure 7 | Algorithm Comparison — DFS, BFS, A* performance metrics.",
    )
    figure_html11 = _render_image_html(
        figures.get("Figure 11"),
        caption="Figure 11 | Algorithm Selection — choose between DFS, BFS, A*, Backtracking.",
    )
    figure_html14 = _render_image_html(
        figures.get("Figure 14"),
        caption="Figure 14 | Performance Stats — time/space complexity and expanded nodes.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Algorithms</span>
                    <h2 class="portfolio-section-title">Four Search Algorithms</h2>
                </div>
            </div>
            <div class="pg pg-2">
                {figure_html7}
                {figure_html14}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-23">
                <div class="portfolio-content">
                    <h4>DFS (Depth-First Search)</h4>
                    <p>Explores as far as possible along each branch before backtracking. Memory efficient but not optimal.</p>
                    <h4>BFS (Breadth-First Search)</h4>
                    <p>Explores all nodes at the present depth level before moving to nodes at the next depth level. Optimal but memory intensive.</p>
                    <h4>A* (A-Star)</h4>
                    <p>Best-first search using heuristic function to guide search. Optimal and efficient with good heuristics.</p>
                    <h4>Backtracking</h4>
                    <p>Incrementally builds candidates, abandoning paths that fail constraint checks. Ideal for constraint satisfaction problems.</p>
                </div>
                {figure_html11}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_puzzle_section_visualization(project: Dict, figures: Dict) -> None:
    figure_html8 = _render_image_html(
        figures.get("Figure 8"),
        caption="Figure 8 | Search Animation — real-time node expansion visualization.",
    )
    figure_html16 = _render_image_html(
        figures.get("Figure 16"),
        caption="Figure 16 | Settings — animation speed and theme configuration.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Visualization</span>
                    <h2 class="portfolio-section-title">Dynamic Canvas Animation</h2>
                </div>
            </div>
            <div class="pg pg-23">
                {figure_html8}
                <div>
                    {figure_html16}
                    <div class="portfolio-content">
                        <h4>Real-time Visualization</h4>
                        <ul>
                            <li><strong>Node Expansion</strong>: Watch each node being explored in real-time.</li>
                            <li><strong>Path Highlighting</strong>: Visualize the discovered path as it unfolds.</li>
                            <li><strong>State Transitions</strong>: See how the puzzle state changes step by step.</li>
                            <li><strong>Speed Control</strong>: Adjust animation speed from slow to fast.</li>
                        </ul>
                        <div class="portfolio-insight-box">
                            <strong>Educational Value</strong>
                            <p>The visualization transforms abstract algorithm concepts into concrete visual experiences, making it much easier for learners to understand how search algorithms work.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_puzzle_section_ai_features(project: Dict, figures: Dict) -> None:
    figure_html9 = _render_image_html(
        figures.get("Figure 9"),
        caption="Figure 9 | AI Learning Assistant — DeepSeek-powered algorithm explanations.",
    )
    figure_html10 = _render_image_html(
        figures.get("Figure 10"),
        caption="Figure 10 | User Profile — learning progress and puzzle solving history.",
    )
    figure_html15 = _render_image_html(
        figures.get("Figure 15"),
        caption="Figure 15 | History Records — view and replay past solutions.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">AI & Features</span>
                    <h2 class="portfolio-section-title">AI Learning Assistant & User System</h2>
                </div>
            </div>
            <div class="pg pg-3">
                {figure_html9}
                {figure_html10}
                {figure_html15}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>AI Learning Assistant</h4>
                    <p>
                        <a href="{project['github_url']}" target="_blank" style="color:#1a5c52;font-weight:bold;">{project['github_url']}</a>
                    </p>
                    <p>Integrates DeepSeek API to explain algorithm principles, provide problem-solving hints, and answer questions about search strategies.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Tech Stack Summary</h4>
                    <ul>
                        <li>Flask + Python</li>
                        <li>HTML5 Canvas</li>
                        <li>SQLite + SQLAlchemy</li>
                        <li>DeepSeek API</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Features</h4>
                    <ul>
                        <li>5 puzzle types</li>
                        <li>4 search algorithms</li>
                        <li>Canvas animation</li>
                        <li>AI explanations</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_va_showcase_hero(project: Dict) -> None:
    tag_chips = "".join(
        f'<span class="portfolio-hero-tag">{tag}</span>' for tag in project["tags"]
    )
    st.markdown(
        f"""
        <div class="portfolio-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Engineering Project</span>
                {tag_chips}
            </div>
            <h1 class="portfolio-hero-title">{project["title"]}</h1>
            <div class="portfolio-hero-sub">{project["chinese_title"]}</div>
            <p class="portfolio-hero-sub">{project["long_description"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Platform</span>
                    <strong>WeChat Mini Program</strong>
                </div>
                <div class="portfolio-stat">
                    <span>AI Engine</span>
                    <strong>DeepSeek</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Backend</span>
                    <strong>Node.js</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Database</span>
                    <strong>MongoDB</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_va_section_overview(project: Dict, figures: Dict) -> None:
    figure_html1 = _render_image_html(
        figures.get("Figure 1"),
        caption="Figure 1 | Welcome Page — mini-program home with core function entries.",
    )
    figure_html6 = _render_image_html(
        figures.get("Figure 6"),
        caption="Figure 6 | Knowledge Graph — visual representation of business concept relationships.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">AI-Powered Business Assistant</h2>
                </div>
            </div>
            <div class="pg pg-single">
                {figure_html1}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>Problem</h4>
                    <p>
                        Entrepreneurs and business enthusiasts lack accessible tools for professional business plan evaluation, market analysis, and learning resources.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Solution</h4>
                    <p>
                        Build a WeChat Mini Program that integrates AI to provide intelligent business evaluation, market trend analysis, case studies, and knowledge sharing.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Tech Stack</h4>
                    <p>
                        WeChat Mini Program frontend, Node.js + Express backend, DeepSeek AI API, MongoDB database.
                    </p>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                {figure_html6}
                <div class="portfolio-content">
                    <h4>Knowledge Graph</h4>
                    <p>
                        Interactive knowledge graph visualizes relationships between business concepts, helping users understand complex business logic and identify connections between different domains.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Visual Learning</strong>
                        <p>The knowledge graph transforms abstract business concepts into intuitive visual networks, making complex relationships easy to understand at a glance.</p>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_va_section_evaluation(project: Dict, figures: Dict) -> None:
    figure_html2 = _render_image_html(
        figures.get("Figure 2"),
        caption="Figure 2 | Business Plan Evaluation — input or upload business plan for AI analysis.",
    )
    figure_html3 = _render_image_html(
        figures.get("Figure 3"),
        caption="Figure 3 | Evaluation Report — multi-dimensional scoring with AI-generated recommendations.",
    )
    figure_html9 = _render_image_html(
        figures.get("Figure 9"),
        caption="Figure 9 | Report Export — export professional evaluation reports in PDF format.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Core Feature</span>
                    <h2 class="portfolio-section-title">AI Business Plan Evaluation</h2>
                </div>
            </div>
            <div class="pg pg-32">
                <div>
                    {figure_html2}
                    {figure_html3}
                </div>
                <div>
                    {figure_html9}
                    <div class="portfolio-content">
                        <h4>Evaluation Process</h4>
                        <ul>
                            <li><strong>Input</strong>: Users enter or upload business plan content.</li>
                            <li><strong>AI Analysis</strong>: DeepSeek API performs multi-dimensional analysis.</li>
                            <li><strong>Report Generation</strong>: Structured evaluation report with scores and suggestions.</li>
                            <li><strong>Export</strong>: Download PDF report for sharing and reference.</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-5">
                <div class="portfolio-content">
                    <h4>Market Potential</h4>
                    <p>Assess market size and growth opportunities.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Business Model</h4>
                    <p>Evaluate revenue model viability.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Competitive Edge</h4>
                    <p>Analyze competitive positioning.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Financial Feasibility</h4>
                    <p>Review financial projections.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Risk Assessment</h4>
                    <p>Identify potential risks and mitigation.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_va_section_features(project: Dict, figures: Dict) -> None:
    figure_html4 = _render_image_html(
        figures.get("Figure 4"),
        caption="Figure 4 | Market Trend Analysis — industry dynamics and trend predictions.",
    )
    figure_html5 = _render_image_html(
        figures.get("Figure 5"),
        caption="Figure 5 | Business Case Library — categorized browsing and keyword search.",
    )
    figure_html7 = _render_image_html(
        figures.get("Figure 7"),
        caption="Figure 7 | Entrepreneurship Knowledge Base — articles on financing, legal, operations.",
    )
    figure_html8 = _render_image_html(
        figures.get("Figure 8"),
        caption="Figure 8 | User Profile — personal center with evaluation history and favorites.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Features</span>
                    <h2 class="portfolio-section-title">Business Intelligence & Knowledge</h2>
                </div>
            </div>
            <div class="pg pg-2">
                <div class="pg pg-single">
                    {figure_html4}
                </div>
                <div class="pg pg-single">
                    {figure_html5}
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                {figure_html7}
                {figure_html8}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-4">
                <div class="portfolio-content">
                    <h4>Market Analysis</h4>
                    <p>AI-powered analysis of industry trends and consumer behavior.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Case Library</h4>
                    <p>Real business cases with success factors and failure lessons.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Knowledge Base</h4>
                    <p>Resources covering financing, legal compliance, operations.</p>
                </div>
                <div class="portfolio-content">
                    <h4>User Center</h4>
                    <p>Track evaluation history and manage personal collections.</p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_va_section_visualization(project: Dict, figures: Dict) -> None:
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Summary</span>
                    <h2 class="portfolio-section-title">Tech Stack & Highlights</h2>
                </div>
            </div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>GitHub Repository</h4>
                    <p>
                        <a href="{project['github_url']}" target="_blank" style="color:#1a5c52;font-weight:bold;">{project['github_url']}</a>
                    </p>
                    <p>Complete WeChat Mini Program with Node.js backend.</p>
                </div>
                <div class="portfolio-content">
                    <h4>Tech Stack</h4>
                    <ul>
                        <li>WeChat Mini Program</li>
                        <li>Node.js + Express</li>
                        <li>DeepSeek API</li>
                        <li>MongoDB + Mongoose</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Features</h4>
                    <ul>
                        <li>AI business evaluation</li>
                        <li>Market analysis</li>
                        <li>Case library</li>
                        <li>Knowledge graph</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_ims_showcase_hero(project: Dict) -> None:
    tag_chips = "".join(
        f'<span class="portfolio-hero-tag">{tag}</span>' for tag in project["tags"]
    )
    st.markdown(
        f"""
        <div class="portfolio-hero">
            <div class="portfolio-hero-meta">
                <span class="portfolio-hero-tag">Engineering Project</span>
                {tag_chips}
            </div>
            <h1 class="portfolio-hero-title">{project["title"]}</h1>
            <div class="portfolio-hero-sub">{project["chinese_title"]}</div>
            <p class="portfolio-hero-sub">{project["long_description"]}</p>
            <div class="portfolio-hero-stats">
                <div class="portfolio-stat">
                    <span>Language</span>
                    <strong>MATLAB</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Features</span>
                    <strong>Multi-source</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Algorithms</span>
                    <strong>6+ Methods</strong>
                </div>
                <div class="portfolio-stat">
                    <span>Evaluation</span>
                    <strong>Multiple Metrics</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_ims_section_overview(project: Dict, figures: Dict) -> None:
    figure_html1 = _render_image_html(
        figures.get("Figure 1"),
        caption="Figure 1 | System Interface — main application with retrieval workflow and modules.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Project Overview</span>
                    <h2 class="portfolio-section-title">Multi-source Feature Fusion for Image Retrieval</h2>
                </div>
            </div>
            <div class="pg pg-single">
                {figure_html1}
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-2">
                <div class="portfolio-content">
                    <h4>Problem</h4>
                    <p>
                        Single-feature image retrieval methods often fail to capture the full complexity of visual content. Different features (color, texture, shape) each capture different aspects of an image.
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Solution</h4>
                    <p>
                        Integrate multiple feature extraction methods and apply fusion strategies to combine their strengths, improving retrieval accuracy and robustness.
                    </p>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-4">
                <div class="portfolio-content">
                    <h4>Tech Stack</h4>
                    <p>MATLAB, Image Processing Toolbox, Computer Vision Toolbox</p>
                </div>
                <div class="portfolio-content">
                    <h4>Feature Types</h4>
                    <ul>
                        <li>Color Histogram</li>
                        <li>GLCM Texture</li>
                        <li>Hu Moments</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Similarity Metrics</h4>
                    <ul>
                        <li>Euclidean Distance</li>
                        <li>Cosine Similarity</li>
                        <li>Bhattacharyya</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Fusion Strategies</h4>
                    <ul>
                        <li>Weighted Fusion</li>
                        <li>Decision Fusion</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_ims_section_features(project: Dict, figures: Dict) -> None:
    figure_html3 = _render_image_html(
        figures.get("Figure 3"),
        caption="Figure 3 | Feature Visualization — color histogram, texture features, and shape descriptors.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Feature Extraction</span>
                    <h2 class="portfolio-section-title">Multi-source Feature Extraction Methods</h2>
                </div>
            </div>
            <div class="pg pg-23">
                <div class="portfolio-content">
                    <h4>Color Features</h4>
                    <p>
                        Color histogram extraction captures the distribution of colors in an image. Supports multiple color spaces including RGB, HSV, and Lab. The histogram is normalized and quantized for efficient comparison.
                    </p>
                    <h4>Texture Features</h4>
                    <p>
                        Gray Level Co-occurrence Matrix (GLCM) extracts texture information by analyzing the spatial relationship between pixel intensities. Four Haralick texture features are computed: contrast, correlation, energy, and homogeneity.
                    </p>
                    <h4>Shape Features</h4>
                    <p>
                        Hu moments provide translation, rotation, and scale invariant shape descriptors. These seven invariant moments capture the global shape characteristics of objects in images.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Complementary Information</strong>
                        <p>Each feature type captures different aspects of visual content. Color describes appearance, texture describes surface properties, and shape describes object structure. Together they provide comprehensive representation.</p>
                    </div>
                </div>
                {figure_html3}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_ims_section_results(project: Dict, figures: Dict) -> None:
    figure_html2 = _render_image_html(
        figures.get("Figure 2"),
        caption="Figure 2 | Retrieval Results — ranked matching images displayed by similarity score.",
    )
    st.markdown(
        f"""
        <section class="portfolio-section portfolio-section-compact">
            <div class="portfolio-section-header">
                <div>
                    <span class="portfolio-section-kicker">Results & Evaluation</span>
                    <h2 class="portfolio-section-title">Retrieval Performance & Metrics</h2>
                </div>
            </div>
            <div class="pg pg-23">
                {figure_html2}
                <div class="portfolio-content">
                    <h4>Evaluation Metrics</h4>
                    <ul>
                        <li><strong>Precision</strong>: Percentage of relevant images in top results.</li>
                        <li><strong>Recall</strong>: Percentage of all relevant images retrieved.</li>
                        <li><strong>MAP</strong>: Mean Average Precision across queries.</li>
                        <li><strong>F1-Score</strong>: Harmonic mean of precision and recall.</li>
                    </ul>
                    <h4>Fusion Strategies</h4>
                    <p>
                        <strong>Weighted Fusion</strong>: Combine similarity scores with learned weights based on feature reliability.<br>
                        <strong>Decision Fusion</strong>: Apply majority voting across multiple feature-based rankings.
                    </p>
                    <div class="portfolio-insight-box">
                        <strong>Research Value</strong>
                        <p>This project demonstrates that multi-source feature fusion significantly outperforms single-feature methods, providing a solid foundation for more advanced retrieval systems.</p>
                    </div>
                </div>
            </div>
            <div style="height:4px"></div>
            <div class="pg pg-3">
                <div class="portfolio-content">
                    <h4>GitHub Repository</h4>
                    <p>
                        <a href="{project['github_url']}" target="_blank" style="color:#1a5c52;font-weight:bold;">{project['github_url']}</a>
                    </p>
                </div>
                <div class="portfolio-content">
                    <h4>Tech Stack Summary</h4>
                    <ul>
                        <li>MATLAB</li>
                        <li>Image Processing Toolbox</li>
                        <li>Computer Vision Toolbox</li>
                        <li>Feature Extraction</li>
                    </ul>
                </div>
                <div class="portfolio-content">
                    <h4>Features</h4>
                    <ul>
                        <li>Multi-source features</li>
                        <li>Fusion strategies</li>
                        <li>Performance metrics</li>
                        <li>Visualization</li>
                    </ul>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
