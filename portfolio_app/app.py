from pathlib import Path
import sys

# Keep this module runnable both as package code and as a direct Streamlit script.
if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    __package__ = "portfolio_app"

import streamlit as st

from .sidebar import render_sidebar
from .state import clear_research_detail_state, init_session_state
from .styles import render_css


@st.cache_resource(show_spinner=False)
def init_home_agent_once():
    from .rag import ensure_docs_structure, ensure_vectorstore_ready

    ensure_docs_structure()
    ensure_vectorstore_ready()


def _get_query_value(key: str) -> str:
    try:
        value = st.query_params.get(key)
    except Exception:
        return ""
    if isinstance(value, list):
        return value[0] if value else ""
    return value or ""


def _clear_query_value(key: str) -> None:
    try:
        if key in st.query_params:
            del st.query_params[key]
    except Exception:
        pass


def _get_deep_link_target():
    deep_links = [
        ("paper", "📝 Research Papers"),
        ("project", "💻 Engineering Projects"),
        ("competition", "🏆 Competitions & Awards"),
        ("internship", "🎯 Internships & Practices"),
        ("competition_category", "🏆 Competitions & Awards"),
        ("experience_type", "🎯 Internships & Practices"),
    ]
    for key, category in deep_links:
        value = _get_query_value(key)
        if value:
            return key, value, category
    return None


def _apply_deep_link_category() -> None:
    target = _get_deep_link_target()
    if not target:
        st.session_state.pop("_handled_deep_link", None)
        return

    key, value, category = target
    signature = f"{key}:{value}"
    if st.session_state.get("_handled_deep_link") == signature:
        return

    st.session_state.active_category = category
    st.session_state["_handled_deep_link"] = signature


def main() -> None:
    st.set_page_config(
        page_title="Portfolio RAG Agent",
        page_icon="PR",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    init_session_state()
    render_css()

    _apply_deep_link_category()

    category_label, category_dir, api_key, top_k = render_sidebar()
    if category_label != "Internships & Practices":
        st.session_state.selected_internship = None
        _clear_query_value("internship")
        _clear_query_value("experience_type")

    if category_label != "Competitions & Awards":
        st.session_state.selected_competition = None
        _clear_query_value("competition")
        _clear_query_value("competition_category")

    if category_label != "Research Papers":
        if st.session_state.get("selected_research_paper"):
            clear_research_detail_state()
        _clear_query_value("paper")

    if category_label != "Engineering Projects":
        st.session_state.selected_project = None
        _clear_query_value("project")

    if category_label == "Research Papers":
        from .data import RESEARCH_PAPERS
        from .research import render_research_papers_section

        for paper in RESEARCH_PAPERS:
            if st.session_state.get(f"view-{paper['id']}"):
                st.session_state.selected_research_paper = paper["id"]
                break
        render_research_papers_section()
    elif category_label == "Competitions & Awards":
        from .competitions import render_competitions_section
        from .data import COMPETITION_AWARDS

        for award in COMPETITION_AWARDS:
            if st.session_state.get(f"view-comp-{award['id']}"):
                st.session_state.selected_competition = award["id"]
                break
        render_competitions_section()
    elif category_label == "Engineering Projects":
        from .data import PROJECTS
        from .projects import render_projects_section

        for project in PROJECTS:
            if st.session_state.get(f"view-project-{project['id']}"):
                st.session_state.selected_project = project["id"]
                break
        render_projects_section()
    elif category_label == "Internships & Practices":
        from .internships import render_internships_section

        render_internships_section()
    elif category_label == "Home / AI Assistant":
        with st.spinner("Preparing portfolio knowledge base..."):
            init_home_agent_once()
        from .chat import render_home_chat
        from .profile import render_profile_card

        render_profile_card()
        render_home_chat(api_key=api_key, top_k=top_k)
    else:
        st.markdown(
            f"""
            <div class="section-header">
                <div class="section-kicker">{category_label}</div>
                <div class="section-title">This portfolio section is ready for the next round of refinement.</div>
                <div class="section-copy">
                    The RAG assistant can already search this category after the vector store is reloaded.
                    We can add a tailored visual showcase for this section next.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
