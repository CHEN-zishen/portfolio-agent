from html import escape
from typing import Dict
from urllib.parse import quote

import streamlit as st

from .assets import (
    get_image_base64,
    get_image_thumbnail_base64,
    get_pdf_card_thumbnail,
    get_pdf_thumbnail,
)
from .data import INTERNSHIPS, PRACTICES


TAG_COLORS = {
    "Academic": "#217c6f",
    "AI Research": "#1a5c52",
    "Hong Kong": "#3d9e91",
    "Industry": "#78a99a",
    "Web Development": "#4a6b65",
    "Guangzhou": "#5b8c85",
    "Medical Imaging": "#2d8a7e",
    "Graph Neural Networks": "#6ab4a8",
    "Traffic Prediction": "#4a6b65",
    "Foshan": "#5b8c85",
    "Data Processing": "#78a99a",
    "Volunteer": "#217c6f",
    "Community": "#1a5c52",
    "Campus": "#78a99a",
    "Sports": "#3d9e91",
    "Leadership": "#4a6b65",
    "Rural Revitalization": "#2d8a7e",
    "Technology": "#6ab4a8",
    "Social Practice": "#5b8c85",
    "Music": "#6f7d7b",
    "Performance": "#78a99a",
}


def _get_selected_internship_from_query() -> str:
    try:
        value = st.query_params.get("internship")
    except Exception:
        return ""
    if isinstance(value, list):
        return value[0] if value else ""
    return value or ""


def _get_selected_experience_filter() -> str:
    try:
        value = st.query_params.get("experience_type")
    except Exception:
        return "All"
    if isinstance(value, list):
        value = value[0] if value else "All"
    return value if value in {"All", "Internships", "Practices"} else "All"


def _filter_href(label: str) -> str:
    if label == "All":
        return "?"
    return f"?experience_type={quote(label)}"


def _image_mime(path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return "image/jpeg"
    if suffix == ".webp":
        return "image/webp"
    return "image/png"


def _build_tag_chips(tags) -> str:
    return "".join(
        f'<span class="internship-tag" style="background: {TAG_COLORS.get(tag, "#6f7d7b")}15; color: {TAG_COLORS.get(tag, "#6f7d7b")}; border-color: {TAG_COLORS.get(tag, "#6f7d7b")}30;">{escape(tag)}</span>'
        for tag in tags
    )


def _build_card_image(item: Dict) -> str:
    image_path = item.get("image_path")
    if not image_path or not image_path.exists():
        return ""

    if item.get("image_type") == "pdf":
        thumbnail = get_pdf_card_thumbnail(image_path, max_width=700, max_height=520, quality=82)
        if thumbnail:
            return (
                f'<img src="data:image/jpeg;base64,{thumbnail}" '
                'class="experience-card-image experience-card-document" loading="lazy" />'
            )
        return ""

    image_base64 = get_image_thumbnail_base64(image_path, max_width=700, max_height=520, quality=82)
    if not image_base64:
        return ""

    return (
        f'<img src="data:image/jpeg;base64,{image_base64}" '
        'class="experience-card-image" loading="lazy" />'
    )


def _experience_card_html(item: Dict, item_type: str) -> str:
    is_practice = item_type == "practice"
    title = item.get("organization") if is_practice else item.get("company")
    role = item.get("role") if is_practice else item.get("position")
    track_label = "Practice" if is_practice else "Internship"
    image_html = _build_card_image(item)
    is_pending = item["period"] == "Pending"
    button_html = ""
    if not is_pending:
        button_html = f'<a class="experience-card-btn" href="?internship={quote(item["id"])}" target="_self">View Details</a>'

    media_html = image_html or '<div class="experience-card-placeholder"><span class="placeholder-icon">DOC</span></div>'
    return (
        f'<article class="experience-card {item_type}-experience-card {"pending" if is_pending else ""}">'
        '<div class="experience-card-media">'
        f'<div class="experience-card-image-frame">{media_html}</div>'
        f'<div class="experience-card-badge">{escape(item["period"])}</div>'
        '</div>'
        '<div class="experience-card-body">'
        f'<div class="experience-card-track">{track_label}</div>'
        f'<h3 class="experience-card-title">{escape(title or "")}</h3>'
        f'<div class="experience-card-role">{escape(role or "")}</div>'
        f'<div class="experience-card-location">Location: {escape(item["location"])}</div>'
        f'<p class="experience-card-description">{escape(item["description"])}</p>'
        f'<div class="experience-card-tags">{_build_tag_chips(item["tags"])}</div>'
        f'{button_html}'
        '</div>'
        '</article>'
    )


def render_internships_section() -> None:
    selected_id = st.session_state.get("selected_internship")
    query_id = _get_selected_internship_from_query()
    if query_id and query_id != selected_id:
        st.session_state.selected_internship = query_id
        selected_id = query_id

    selected_internship = next((item for item in INTERNSHIPS if item["id"] == selected_id), None)
    selected_practice = next((item for item in PRACTICES if item["id"] == selected_id), None)

    if selected_internship:
        render_internship_detail(selected_internship)
        return
    elif selected_practice:
        render_practice_detail(selected_practice)
        return

    st.markdown(
        (
            '<div class="section-header">'
            '<div class="section-kicker">Internships & Practices</div>'
            '<div class="section-title">Professional Internships & Campus Practices</div>'
            '<div class="section-copy">'
            'Research and industry internships are presented alongside campus, volunteer, and social practice experiences.'
            '</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )

    filter_option = _get_selected_experience_filter()

    all_experiences = []
    if filter_option == "All":
        all_experiences = [{"item": item, "type": "internship"} for item in INTERNSHIPS] + [{"item": item, "type": "practice"} for item in PRACTICES]
    elif filter_option == "Internships":
        all_experiences = [{"item": item, "type": "internship"} for item in INTERNSHIPS]
    else:
        all_experiences = [{"item": item, "type": "practice"} for item in PRACTICES]

    experience_tabs = [
        ("All", len(INTERNSHIPS) + len(PRACTICES)),
        ("Internships", len(INTERNSHIPS)),
        ("Practices", len(PRACTICES)),
    ]
    tabs_html = "".join(
        (
            f'<a class="experience-filter-tab {"active" if filter_option == label else ""}" '
            f'href="{_filter_href(label)}" target="_self">'
            f'<span>{escape(label)}</span><strong>{count}</strong>'
            '</a>'
        )
        for label, count in experience_tabs
    )

    cards_html = "".join(_experience_card_html(exp["item"], exp["type"]) for exp in all_experiences)

    st.markdown(
        (
            '<div class="internships-container">'
            f'<div class="experience-filter-tabs">{tabs_html}</div>'
            f'<div class="experience-card-list">{cards_html}</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )
    return



def render_internship_detail(item: Dict) -> None:
    if st.button("Back to Internships", key="back-to-resume", use_container_width=False):
        st.session_state.selected_internship = None
        try:
            if "internship" in st.query_params:
                del st.query_params["internship"]
        except Exception:
            pass
        st.rerun()

    is_practice = "organization" in item
    company = item.get("organization", item.get("company", ""))
    position = item.get("role", item.get("position", ""))

    has_image = item.get("image_path") is not None and item["image_path"].exists()
    image_html = ""
    if has_image:
        if item["image_type"] == "pdf":
            thumbnail = get_pdf_thumbnail(item["image_path"])
            if thumbnail:
                image_html = '<img src="data:image/png;base64,' + thumbnail + '" class="detail-doc-preview" />'
        else:
            image_base64 = get_image_base64(item["image_path"])
            if image_base64:
                image_html = '<img src="data:image/png;base64,' + image_base64 + '" class="detail-doc-preview" />'

    doc_html = image_html if has_image else '<div class="doc-placeholder"><span class="doc-icon">DOC</span></div>'

    eyebrow_text = "Practice Dossier" if is_practice else "Internship Dossier"

    html_parts = [
        '<div class="detail-page-container">',
        '<div class="detail-topbar">',
        '<div class="detail-eyebrow">' + eyebrow_text + '</div>',
        '<div class="detail-index">Professional Practice Record</div>',
        '</div>',
        '<div class="detail-hero">',
        '<div class="detail-hero-info">',
        '<div class="detail-company">' + escape(company) + '</div>',
        '<div class="detail-position">' + escape(position) + '</div>',
        '<p class="detail-lede">' + escape(item["description"]) + '</p>',
        '<div class="detail-meta-grid">',
        '<div class="detail-meta-card"><span>Period</span><strong>' + escape(item["period"]) + '</strong></div>',
        '<div class="detail-meta-card"><span>Location</span><strong>' + escape(item["location"]) + '</strong></div>',
        '<div class="detail-meta-card"><span>Focus</span><strong>' + escape(item["tags"][0] if item["tags"] else ("Practice" if is_practice else "Internship")) + '</strong></div>',
        '</div>',
        '<div class="detail-tags">',
    ]

    for tag in item["tags"]:
        color = TAG_COLORS.get(tag, "#6f7d7b")
        html_parts.append('<span class="internship-tag" style="background: ' + color + '15; color: ' + color + '; border-color: ' + color + '30;">' + escape(tag) + '</span>')

    html_parts.extend([
        '</div>',
        '</div>',
        '<div class="detail-hero-doc">',
        '<div class="detail-doc-label">Supporting Document</div>',
        '<div class="detail-doc-frame">',
        doc_html,
        '</div>',
        '<div class="detail-doc-caption">Certificate / verification preview</div>',
        '</div>',
        '</div>',
        '<div class="detail-body-grid">',
        '<div class="detail-main-column">',
        '<div class="detail-section detail-overview-section">',
        '<div class="detail-section-header">',
        '<span class="section-icon">01</span>',
        '<div><div class="detail-section-kicker">Context</div><h3 class="detail-section-title">Role Overview</h3></div>',
        '</div>',
        '<p class="detail-section-text">' + escape(item["long_description"]) + '</p>',
        '</div>',
        '<div class="detail-section">',
        '<div class="detail-section-header">',
        '<span class="section-icon">02</span>',
        '<div><div class="detail-section-kicker">Evidence</div><h3 class="detail-section-title">Key Achievements</h3></div>',
        '</div>',
        '<div class="achievements-grid">',
    ])

    for index, achievement in enumerate(item["achievements"], start=1):
        html_parts.append('<div class="achievement-item"><span class="achievement-check">' + f'{index:02d}' + '</span><span class="achievement-text">' + escape(achievement) + '</span></div>')

    html_parts.extend([
        '</div>',
        '</div>',
    ])

    if "gallery_images" in item and item["gallery_images"]:
        gallery_html = []
        for img_path in item["gallery_images"]:
            if img_path.exists():
                img_base64 = get_image_base64(img_path)
                if img_base64:
                    gallery_html.append(f'<div class="gallery-item"><img src="data:image/png;base64,{img_base64}" class="gallery-image" /></div>')
        
        if gallery_html:
            html_parts.extend([
                '<div class="detail-section">',
                '<div class="detail-section-header">',
                '<span class="section-icon">03</span>',
                '<div><div class="detail-section-kicker">Gallery</div><h3 class="detail-section-title">Activity Photos</h3></div>',
                '</div>',
                '<div class="gallery-grid">',
                "".join(gallery_html),
                '</div>',
                '</div>',
            ])

    html_parts.extend([
        '</div>',
        '<div class="detail-side-column">',
        '<div class="detail-section detail-snapshot-section">',
        '<div class="detail-section-header compact">',
        '<span class="section-icon">03</span>',
        '<div><div class="detail-section-kicker">Snapshot</div><h3 class="detail-section-title">Experience Summary</h3></div>',
        '</div>',
        '<div class="detail-stats">',
        '<div class="detail-stat"><strong>' + str(len(item["achievements"])) + '</strong><span>documented outcomes</span></div>',
        '<div class="detail-stat"><strong>' + str(len(item["skills_gained"])) + '</strong><span>skills gained</span></div>',
        '<div class="detail-stat"><strong>' + str(len(item["tags"])) + '</strong><span>focus tags</span></div>',
        '</div>',
        '</div>',
        '<div class="detail-section detail-skills-section">',
        '<div class="detail-section-header">',
        '<span class="section-icon">04</span>',
        '<div><div class="detail-section-kicker">Toolbox</div><h3 class="detail-section-title">Skills Gained</h3></div>',
        '</div>',
        '<div class="skills-grid">',
    ])

    for skill in item["skills_gained"]:
        html_parts.append('<span class="skill-chip">' + escape(skill) + '</span>')

    html_parts.extend([
        '</div>',
        '</div>',
        '</div>',
        '</div>',
        '</div>',
    ])

    full_html = "".join(html_parts)
    st.markdown(full_html, unsafe_allow_html=True)


def render_practice_detail(practice: Dict) -> None:
    if st.button("Back to Practices", key="back-to-practice", use_container_width=False):
        st.session_state.selected_internship = None
        try:
            if "internship" in st.query_params:
                del st.query_params["internship"]
        except Exception:
            pass
        st.rerun()

    has_image = practice.get("image_path") is not None and practice["image_path"].exists()
    image_html = ""
    if has_image:
        if practice["image_type"] == "pdf":
            thumbnail = get_pdf_thumbnail(practice["image_path"])
            if thumbnail:
                image_html = '<img src="data:image/png;base64,' + thumbnail + '" class="practice-detail-doc-preview" />'
        else:
            image_base64 = get_image_base64(practice["image_path"])
            if image_base64:
                image_html = '<img src="data:image/png;base64,' + image_base64 + '" class="practice-detail-doc-preview" />'

    doc_html = image_html if has_image else '<div class="practice-doc-placeholder"><span class="practice-doc-icon">DOC</span></div>'

    html_parts = [
        '<div class="practice-detail-container">',
        '<div class="practice-detail-topbar">',
        '<div class="practice-detail-eyebrow">Practice Experience</div>',
        '<div class="practice-detail-index">Campus & Community Engagement</div>',
        '</div>',
        '<div class="practice-detail-hero">',
        '<div class="practice-detail-hero-left">',
        '<div class="practice-detail-organization">' + escape(practice["organization"]) + '</div>',
        '<div class="practice-detail-role">' + escape(practice["role"]) + '</div>',
        '<p class="practice-detail-lede">' + escape(practice["description"]) + '</p>',
        '<div class="practice-detail-meta">',
        '<div class="practice-meta-item">',
        '<span class="practice-meta-label">Period</span>',
        '<span class="practice-meta-value">' + escape(practice["period"]) + '</span>',
        '</div>',
        '<div class="practice-meta-item">',
        '<span class="practice-meta-label">Location</span>',
        '<span class="practice-meta-value">' + escape(practice["location"]) + '</span>',
        '</div>',
        '</div>',
        '<div class="practice-detail-tags">',
    ]

    for tag in practice["tags"]:
        color = TAG_COLORS.get(tag, "#6f7d7b")
        html_parts.append('<span class="practice-tag" style="background: ' + color + '15; color: ' + color + '; border-color: ' + color + '30;">' + escape(tag) + '</span>')

    html_parts.extend([
        '</div>',
        '</div>',
        '<div class="practice-detail-hero-right">',
        '<div class="practice-detail-doc-card">',
        '<div class="practice-doc-label">Certificate</div>',
        '<div class="practice-doc-frame">',
        doc_html,
        '</div>',
        '<div class="practice-doc-caption">Verification Document</div>',
        '</div>',
        '</div>',
        '</div>',
        '<div class="practice-detail-content">',
        '<div class="practice-detail-section">',
        '<div class="practice-section-header">',
        '<span class="practice-section-icon">01</span>',
        '<div>',
        '<div class="practice-section-kicker">About</div>',
        '<h3 class="practice-section-title">Role Overview</h3>',
        '</div>',
        '</div>',
        '<p class="practice-section-text">' + escape(practice["long_description"]) + '</p>',
        '</div>',
        '<div class="practice-detail-section">',
        '<div class="practice-section-header">',
        '<span class="practice-section-icon">02</span>',
        '<div>',
        '<div class="practice-section-kicker">Highlights</div>',
        '<h3 class="practice-section-title">Key Achievements</h3>',
        '</div>',
        '</div>',
        '<div class="practice-achievements-grid">',
    ])

    for index, achievement in enumerate(practice["achievements"], start=1):
        html_parts.append('<div class="practice-achievement-item"><span class="practice-achievement-icon">' + f'{index:02d}' + '</span><span class="practice-achievement-text">' + escape(achievement) + '</span></div>')

    html_parts.extend([
        '</div>',
        '</div>',
    ])

    if "gallery_images" in practice and practice["gallery_images"]:
        gallery_html = []
        for img_path in practice["gallery_images"]:
            if img_path.exists():
                img_base64 = get_image_base64(img_path)
                if img_base64:
                    gallery_html.append(f'<div class="practice-gallery-item"><img src="data:image/png;base64,{img_base64}" class="practice-gallery-image" /></div>')
        
        if gallery_html:
            html_parts.extend([
                '<div class="practice-detail-section">',
                '<div class="practice-section-header">',
                '<span class="practice-section-icon">03</span>',
                '<div>',
                '<div class="practice-section-kicker">Gallery</div>',
                '<h3 class="practice-section-title">Activity Photos</h3>',
                '</div>',
                '</div>',
                '<div class="practice-gallery-grid">',
                "".join(gallery_html),
                '</div>',
                '</div>',
            ])

    html_parts.extend([
        '<div class="practice-detail-section">',
        '<div class="practice-section-header">',
        '<span class="practice-section-icon">04</span>',
        '<div>',
        '<div class="practice-section-kicker">Skills</div>',
        '<h3 class="practice-section-title">Skills & Competencies</h3>',
        '</div>',
        '</div>',
        '<div class="practice-skills-grid">',
    ])

    for skill in practice["skills_gained"]:
        html_parts.append('<span class="practice-skill-chip">' + escape(skill) + '</span>')

    html_parts.extend([
        '</div>',
        '</div>',
        '</div>',
        '</div>',
    ])

    full_html = "".join(html_parts)
    st.markdown(full_html, unsafe_allow_html=True)
