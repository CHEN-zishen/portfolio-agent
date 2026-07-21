from pathlib import Path

import streamlit as st

from .assets import get_image_base64
from .config import SCHOOL_ICON_PATH
from .data import INTERNSHIP_EXPERIENCES, MAIN_COURSES, PERSONAL_INFO, RESEARCH_DIRECTIONS

def render_profile_card() -> None:
    school_icon_base64 = get_image_base64(SCHOOL_ICON_PATH)
    info_emojis = {
        "Name": "👤",
        "University": "🏫",
        "Major": "🎓",
        "Research Interests": "🔬",
        "Technical Stack": "🛠️",
        "Career Goal": "🚀",
    }

    info_items = []
    for key, value in PERSONAL_INFO.items():
        if key not in ["GPA", "Academic Ranking"]:
            emoji = info_emojis.get(key, "•")
            if key == "University" and school_icon_base64:
                value_html = (
                    f'<div class="info-value school-value">'
                    f'<img src="data:image/png;base64,{school_icon_base64}" class="school-icon" />'
                    f'<span>{value}</span>'
                    f'</div>'
                )
            else:
                value_html = f'<div class="info-value">{value}</div>'
            info_items.append(
                f'<div class="info-item">'
                f'<div class="info-key"><span class="info-emoji">{emoji}</span><span>{key}</span></div>'
                f'{value_html}'
                f'</div>'
            )
    info_html = "".join(info_items)

    courses_html = []
    for course in MAIN_COURSES:
        score_color = "#217c6f" if course["score"] >= 95 else "#2a9d8f" if course["score"] >= 94 else "#e9c46a" if \
        course["score"] >= 90 else "#d94343"
        courses_html.append(
            f'<div class="course-item">'
            f'<div class="course-icon">{course["icon"]}</div>'
            f'<div class="course-content">'
            f'<div class="course-name">{course["name"]}</div>'
            f'</div>'
            f'<div class="course-score-badge" style="background: {score_color}20; color: {score_color};">{course["score"]}</div>'
            f'</div>'
        )
    courses_html = "".join(courses_html)

    research_html = "".join(
        f'<div class="research-card">'
        f'<div class="research-title">{item["title"]}</div>'
        f'<div class="research-desc">{item["description"]}</div>'
        f'<div class="research-projects">{" · ".join(item["projects"])}</div>'
        f'</div>'
        for item in RESEARCH_DIRECTIONS
    )

    internship_html_parts = []
    for item in INTERNSHIP_EXPERIENCES:
        icon_val = item.get("icon", "💼")
        if isinstance(icon_val, Path) and icon_val.exists():
            icon_base64 = get_image_base64(icon_val)
            icon_html = f'<img src="data:image/png;base64,{icon_base64}" class="internship-icon-img" />'
        else:
            icon_html = f'<div class="internship-icon-emoji">{icon_val}</div>'

        internship_html_parts.append(
            f'<div class="internship-card">'
            f'<div class="internship-icon-wrapper">'
            f'{icon_html}'
            f'</div>'
            f'<div class="internship-content">'
            f'<div class="internship-head">'
            f'<div>'
            f'<div class="internship-org-row">'
            f'<div class="internship-org">{item["organization"]}</div>'
            f'</div>'
            f'<div class="internship-role">{item["role"]}</div>'
            f'</div>'
            f'<div class="internship-period">{item["period"]}</div>'
            f'</div>'
            f'<div class="internship-columns">'
            f'<div class="internship-column">'
            f'<div class="internship-subtitle">📋 Main Experience</div>'
            f'<ul class="internship-list">{"".join(f"<li>{point}</li>" for point in item["work"])}</ul>'
            f'</div>'
            f'<div class="internship-column">'
            f'<div class="internship-subtitle">🎯 Key Outcomes</div>'
            f'<ul class="internship-list">{"".join(f"<li>{point}</li>" for point in item["outcomes"])}</ul>'
            f'</div>'
            f'</div></div></div>'
        )
    internship_html = "".join(internship_html_parts)

    st.markdown(
        f'<div class="profile-hero">'
        f'<div class="profile-hero-content">'
        f'<div class="profile-hero-text">'
        f'<div class="profile-text-main">'
        f'<div class="profile-kicker">Data Science & AI Research</div>'
        f'<div class="profile-title">Zishen Chen</div>'
        f'<div class="profile-subtitle">Shantou University | Data Science and Big Data Technology</div>'
        f'</div></div>'
        f'<div class="profile-stats">'
        f'<span class="profile-stat"><span class="stat-icon">🎓</span><span class="stat-content"><strong>4.0/5.0</strong><span class="profile-stat-label">GPA</span></span></span>'
        f'<span class="profile-stat"><span class="stat-icon">🏆</span><span class="stat-content"><strong>Top 10%</strong><span class="profile-stat-label">Academic Ranking</span></span></span>'
        f'<span class="profile-stat"><span class="stat-icon">🔬</span><span class="stat-content"><strong>5</strong><span class="profile-stat-label">Research</span></span></span>'
        f'</div></div></div>'
        f'<div class="profile-grid">'
        f'<div class="profile-card">'
        f'<div class="profile-card-header">'
        f'<div class="profile-card-icon">Profile</div>'
        f'<div class="profile-card-title">Personal Profile</div>'
        f'</div>'
        f'<div class="profile-info-grid">{info_html}</div>'
        f'</div>'
        f'<div class="achievement-section">'
        f'<div class="achievement-title">Selected Achievements</div>'
        f'<div class="achievement-medals">'
        f'<span class="achievement-medal"><span class="medal-wrap"><span class="medal-ribbons"></span><strong class="medal-face">10+</strong></span><span class="achievement-label">Discipline and innovation awards</span></span>'
        f'<span class="achievement-medal"><span class="medal-wrap"><span class="medal-ribbons"></span><strong class="medal-face">5</strong></span><span class="achievement-label">Published or completed research papers</span></span>'
        f'<span class="achievement-medal"><span class="medal-wrap"><span class="medal-ribbons"></span><strong class="medal-face">1</strong></span><span class="achievement-label">Authorized invention patent</span></span>'
        f'<span class="achievement-medal"><span class="medal-wrap"><span class="medal-ribbons"></span><strong class="medal-face">8</strong></span><span class="achievement-label">Sports medals at national, provincial, university and college levels</span></span>'
        f'</div></div>'
        f'<div class="profile-card">'
        f'<div class="profile-card-header">'
        f'<div class="profile-card-icon">Scores</div>'
        f'<div class="profile-card-title">Major courses:</div>'
        f'</div>'
        f'<div class="courses-list">{courses_html}</div>'
        f'</div>'
        f'</div>'
        f'<div class="research-section">'
        f'<div class="section-header">'
        f'<div class="section-kicker">Research Directions</div>'
        f'<div class="section-title">Core research fields and future interests</div>'
        f'</div>'
        f'<div class="research-grid">{research_html}</div>'
        f'</div>'
        f'<div class="internship-section">'
        f'<div class="section-header">'
        f'<div class="section-kicker">Internship Experience</div>'
        f'<div class="section-title">Research and engineering practice</div>'
        f'<div class="section-copy">A concise overview of research internships, technical responsibilities, and representative outcomes.</div>'
        f'</div>'
        f'<div class="internship-timeline">{internship_html}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
