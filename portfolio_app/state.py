import streamlit as st

from .data import RESEARCH_PAPERS

def init_session_state() -> None:
    if "messages" not in st.session_state:
        reset_chat_messages()


def reset_chat_messages() -> None:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, I am your portfolio research assistant. Choose a portfolio section on the left, then ask an interview-style question.",
        }
    ]


def clear_research_detail_state() -> None:
    st.session_state.selected_research_paper = None
    for paper in RESEARCH_PAPERS:
        st.session_state[f"load_figures_{paper['id']}"] = False
        st.session_state[f"download_ready_{paper['id']}"] = False
