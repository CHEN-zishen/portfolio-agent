from html import escape
from typing import Dict, List
from urllib.parse import quote

import streamlit as st

from .assets import get_image_base64
from .data import COMPETITION_AWARDS


LEVEL_COLORS = {
    "International": "#1a5c52",
    "National": "#217c6f",
    "Provincial": "#78a99a",
    "Regional": "#9cc8b8",
    "University": "#c5dfd7",
}

CATEGORY_MARKS = {
    "Competition": "CMP",
    "Scholarship": "SCH",
    "Sports": "SPT",
}

LEVEL_ORDER = {
    "International": 0,
    "National": 1,
    "Provincial": 2,
    "Regional": 3,
    "University": 4,
}


def _get_query_value(key: str) -> str:
    try:
        value = st.query_params.get(key)
    except Exception:
        return ""
    if isinstance(value, list):
        return value[0] if value else ""
    return value or ""


def _get_selected_competition_from_query() -> str:
    return _get_query_value("competition")


def _get_selected_category(categories: List[str]) -> str:
    requested = _get_query_value("competition_category")
    return requested if requested in categories else "All"


def _image_mime(path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return "image/jpeg"
    if suffix == ".webp":
        return "image/webp"
    return "image/png"


def _category_counts() -> Dict[str, int]:
    categories = sorted(set(award["category"] for award in COMPETITION_AWARDS))
    return {
        category: sum(1 for award in COMPETITION_AWARDS if award["category"] == category)
        for category in categories
    }


def _filter_href(category: str) -> str:
    if category == "All":
        return "?"
    return f"?competition_category={quote(category)}"


def _sorted_awards(awards: List[Dict]) -> List[Dict]:
    return sorted(
        awards,
        key=lambda award: (-int(award["year"]), LEVEL_ORDER.get(award["level"], 9), award["title"]),
    )


def _award_card_html(award: Dict) -> str:
    image_base64 = get_image_base64(award["image"])
    level_color = LEVEL_COLORS.get(award["level"], "#6f7d7b")
    category_mark = CATEGORY_MARKS.get(award["category"], "AWD")
    chips = "".join(f'<span class="competition-chip">{escape(tag)}</span>' for tag in award["tags"])
    image_html = (
        f'<img class="competition-image" src="data:{_image_mime(award["image"])};base64,{image_base64}" loading="lazy" />'
        if image_base64
        else f'<div class="competition-image-placeholder">{escape(category_mark)}</div>'
    )

    return f"""
        <article class="competition-card">
            <div class="competition-image-wrapper">
                {image_html}
                <div class="competition-year-badge">{escape(award["year"])}</div>
                <div class="competition-level-badge" style="background: {level_color}1A; color: {level_color}; border-color: {level_color}36;">{escape(award["level"])}</div>
            </div>
            <div class="competition-body">
                <div class="competition-category">
                    <span class="competition-category-mark">{escape(category_mark)}</span>
                    <span class="competition-category-text">{escape(award["category"])}</span>
                </div>
                <h3 class="competition-title">{escape(award["title"])}</h3>
                <p class="competition-description">{escape(award["description"])}</p>
                <div class="competition-tags">{chips}</div>
            </div>
            <a class="competition-card-btn" href="?competition={quote(award["id"])}" target="_self">View Detail</a>
        </article>
    """


def render_competitions_section() -> None:
    selected_id = st.session_state.get("selected_competition")
    query_id = _get_selected_competition_from_query()
    if query_id and query_id != selected_id:
        st.session_state.selected_competition = query_id
        selected_id = query_id

    selected_award = next((award for award in COMPETITION_AWARDS if award["id"] == selected_id), None)

    if selected_award:
        render_competition_detail(selected_award)
        return

    st.markdown(
        """
        <div class="section-header">
            <div class="section-kicker">Competitions & Awards</div>
            <div class="section-title">Competitive Achievements & Recognitions</div>
            <div class="section-copy">
                A consolidated record of competition awards, scholarships, and sports recognitions with certificate evidence.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    categories = sorted(set(award["category"] for award in COMPETITION_AWARDS))
    selected_category = _get_selected_category(categories)
    counts = _category_counts()
    filter_options = [("All", len(COMPETITION_AWARDS))] + [
        (category, counts[category]) for category in categories
    ]
    category_tabs = "".join(
        f"""
        <a class="competition-filter-tab {'active' if selected_category == category else ''}"
           href="{_filter_href(category)}"
           target="_self">
            <span>{escape(category)}</span>
            <strong>{count}</strong>
        </a>
        """
        for category, count in filter_options
    )

    st.markdown(
        f"""
        <div class="competition-filter-tabs">
            {category_tabs}
        </div>
        """,
        unsafe_allow_html=True,
    )

    filtered_awards = COMPETITION_AWARDS
    if selected_category != "All":
        filtered_awards = [award for award in COMPETITION_AWARDS if award["category"] == selected_category]
    filtered_awards = _sorted_awards(filtered_awards)
    cards_html = "".join(_award_card_html(award) for award in filtered_awards)

    st.markdown(
        f"""
        <div class="competition-grid">
            {cards_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_competition_detail(award: Dict) -> None:
    if st.button("Back to Competitions", key="back-to-competitions"):
        st.session_state.selected_competition = None
        try:
            if "competition" in st.query_params:
                del st.query_params["competition"]
        except Exception:
            pass
        st.rerun()

    image_base64 = get_image_base64(award["image"])
    level_color = LEVEL_COLORS.get(award["level"], "#6f7d7b")
    category_mark = CATEGORY_MARKS.get(award["category"], "AWD")

    st.markdown(
        f"""
        <div class="competition-detail-header">
            <div class="competition-detail-category">
                <span class="competition-detail-category-mark">{escape(category_mark)}</span>
                <span class="competition-detail-category-text">{escape(award["category"])}</span>
                <span class="competition-detail-level" style="background: {level_color}20; color: {level_color}; border-color: {level_color}30;">{escape(award["level"])}</span>
                <span class="competition-detail-year">{escape(award["year"])}</span>
            </div>
            <div class="competition-detail-title">{escape(award["title"])}</div>
            <div class="competition-detail-description">{escape(award["description"])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([2, 1])
    with left:
        if image_base64:
            st.markdown(
                f'<div class="competition-detail-image-container"><img class="competition-detail-image" src="data:{_image_mime(award["image"])};base64,{image_base64}" /></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="competition-detail-image-container"><div class="competition-detail-image-placeholder">{escape(category_mark)}</div></div>',
                unsafe_allow_html=True,
            )

    with right:
        info_items = [
            ("Category", award["category"]),
            ("Level", award["level"]),
            ("Year", award["year"]),
        ]
        info_html = "".join(
            f'<div class="competition-info-row"><span class="competition-info-label">{escape(label)}</span><span class="competition-info-value">{escape(value)}</span></div>'
            for label, value in info_items
        )
        tag_html = "".join(f'<span class="competition-chip">{escape(tag)}</span>' for tag in award["tags"])

        st.markdown(
            f"""
            <div class="competition-detail-panel">
                <h3>Award Information</h3>
                {info_html}
                <div class="competition-detail-tags">{tag_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="competition-detail-body">', unsafe_allow_html=True)

    if award.get("long_description"):
        st.markdown(
            f"""
            <div class="competition-detail-section">
                <div class="competition-detail-section-header">
                    <span class="competition-detail-section-icon">01</span>
                    <div>
                        <div class="competition-detail-section-kicker">Project Overview</div>
                        <h3 class="competition-detail-section-title">About the Project</h3>
                    </div>
                </div>
                <p class="competition-detail-section-text">{escape(award["long_description"])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if award.get("methodology"):
        st.markdown(
            f"""
            <div class="competition-detail-section">
                <div class="competition-detail-section-header">
                    <span class="competition-detail-section-icon">02</span>
                    <div>
                        <div class="competition-detail-section-kicker">Technical Approach</div>
                        <h3 class="competition-detail-section-title">Methodology</h3>
                    </div>
                </div>
                <p class="competition-detail-section-text">{escape(award["methodology"])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if award.get("achievements"):
        achievements_html = "".join(
            f'<div class="competition-achievement-item"><span class="competition-achievement-check">{index:02d}</span><span class="competition-achievement-text">{escape(achievement)}</span></div>'
            for index, achievement in enumerate(award["achievements"], start=1)
        )
        st.markdown(
            f"""
            <div class="competition-detail-section">
                <div class="competition-detail-section-header">
                    <span class="competition-detail-section-icon">03</span>
                    <div>
                        <div class="competition-detail-section-kicker">Key Outcomes</div>
                        <h3 class="competition-detail-section-title">Achievements</h3>
                    </div>
                </div>
                <div class="competition-achievements-grid">{achievements_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
