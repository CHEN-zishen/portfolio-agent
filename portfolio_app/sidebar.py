import os

import streamlit as st

from .assets import get_avatar_base64, get_avatar_full_base64
from .config import CATEGORIES, CHROMA_DIR, DATA_DIR, DOCS_DIR, get_setting
from .state import reset_chat_messages


NAVIGATION_LABELS = [
    "🏠 Home / AI Assistant",
    "📝 Research Papers",
    "🏆 Competitions & Awards",
    "💻 Engineering Projects",
    "🎯 Internships & Practices",
]

LEGACY_NAVIGATION_LABELS = {
    "\u9983\u5f54 Home / AI Assistant": "🏠 Home / AI Assistant",
    "\u9983\u6451 Research Papers": "📝 Research Papers",
    "\u9983\u5f33 Competitions": "🏆 Competitions & Awards",
    "\u9983\u6347 Engineering Projects": "💻 Engineering Projects",
    "\u9983\u5e46 Internships & Practices": "🎯 Internships & Practices",
}

def render_sidebar():
    try:
        avatar_base64 = get_avatar_base64()
        avatar_full_base64 = get_avatar_full_base64()
        if avatar_base64:
            st.sidebar.markdown(
                f"""
                <div class="sidebar-avatar-shell">
                    <input id="sidebar-avatar-toggle" class="sidebar-avatar-toggle" type="checkbox" />
                    <label for="sidebar-avatar-toggle" class="sidebar-avatar-trigger" aria-label="Open enlarged profile photo">
                        <img src="data:image/jpeg;base64,{avatar_base64}" class="sidebar-avatar" />
                    </label>
                    <label for="sidebar-avatar-toggle" class="sidebar-avatar-lightbox" aria-label="Close enlarged profile photo"></label>
                    <span class="sidebar-avatar-lightbox-inner">
                        <img src="data:image/jpeg;base64,{avatar_full_base64 or avatar_base64}" class="sidebar-avatar-full" />
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )
    except Exception:
        pass

    st.sidebar.markdown(
        """
        <div class="sidebar-profile">
            <div class="sidebar-name">Zishen Chen</div>
            <div class="sidebar-title">Data Science & AI Research</div>
            <div class="sidebar-contact">
                <a href="mailto:23zschen@stu.edu.cn" class="contact-link">Email: 23zschen@stu.edu.cn</a><br>
                <a href="https://github.com/CHEN-zishen" target="_blank" class="contact-link">GitHub: github.com/CHEN-zishen</a><br>
                <span class="contact-text">Phone: +86 136-0010-8119</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.divider()

    st.sidebar.markdown(
        '<div class="sidebar-section-title">Portfolio Navigation</div>',
        unsafe_allow_html=True,
    )

    active_category = st.session_state.get("active_category")
    if active_category in LEGACY_NAVIGATION_LABELS:
        st.session_state.active_category = LEGACY_NAVIGATION_LABELS[active_category]
    elif active_category not in (None, *NAVIGATION_LABELS):
        st.session_state.active_category = "🏠 Home / AI Assistant"

    selected_option = st.sidebar.radio(
        "Portfolio Navigation",
        NAVIGATION_LABELS,
        index=NAVIGATION_LABELS.index("🏠 Home / AI Assistant"),
        key="active_category",
        help="Open the homepage assistant or browse portfolio showcase pages.",
        label_visibility="collapsed",
    )

    category_label = selected_option
    for icon in ("🏠 ", "📝 ", "🏆 ", "💻 ", "🎯 "):
        category_label = category_label.replace(icon, "")

    api_key = get_setting("DEEPSEEK_API_KEY", "")

    top_k = 6

    if category_label == "Home / AI Assistant":
        from .rag import get_vectorstore_status

        vector_status = get_vectorstore_status()
        status_class = "status-ready" if vector_status["ready"] else "status-missing"
        status_text = "Ready" if vector_status["ready"] else "Needs rebuild"

        st.sidebar.markdown(
            f"""
            <div class="vector-status-card">
                <div class="vector-status-row">
                    <span>Vector Store</span>
                    <strong class="{status_class}">{status_text}</strong>
                </div>
                <div class="vector-status-meta">
                    Chunks: {vector_status["chunks"]}<br>
                    Updated: {vector_status["updated"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.sidebar.button("Clear Chat History", use_container_width=True):
            reset_chat_messages()
            st.rerun()

        st.sidebar.divider()

        st.sidebar.markdown(
            f"""
            <div class="small-note">
            Documents: <code>{DOCS_DIR.name}</code> + <code>{DATA_DIR.name}</code><br>
            Vector DB: <code>{CHROMA_DIR.name}</code><br>
            Formats: PDF text / Markdown / TXT
            </div>
            """,
            unsafe_allow_html=True,
        )

    return category_label, CATEGORIES.get(category_label, ""), api_key, top_k
