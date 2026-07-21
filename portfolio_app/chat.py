import streamlit as st

from .rag import (
    detect_response_language,
    get_thinking_message,
    render_thinking_state,
    stream_deepseek_answer,
)

def render_home_chat(api_key: str, top_k: int) -> None:
    category_label = "Full Portfolio"
    category_dir = None

    st.markdown(
        f"""
        <div class="chat-panel">
            <div class="chat-panel-inner">
                <div>
                    <div class="chat-panel-kicker">Portfolio RAG Assistant</div>
                    <div class="chat-panel-title">Ask questions about the full portfolio</div>
                    <div class="chat-panel-copy">
                        Answers are grounded in local portfolio documents, structured profile data, and optional web evidence for school-specific questions.
                        Other navigation pages are visual showcases and do not include chat.
                    </div>
                </div>
                <div class="chat-scope-pill">Assistant scope: {category_label}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(
                message["content"],
                unsafe_allow_html=message["role"] == "assistant",
            )

    user_question = st.chat_input("Ask an interview question, e.g. Summarize my strongest research contribution.")
    if not user_question or not user_question.strip():
        return

    user_question = user_question.strip()
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        placeholder = st.empty()
        if not api_key:
            answer = "API key is not configured. Please set DEEPSEEK_API_KEY in the deployment secrets or local .env file."
            placeholder.warning(answer)
        else:
            try:
                response_language = detect_response_language(user_question)
                render_thinking_state(placeholder, response_language, "retrieving")
                with status_placeholder.status(
                        get_thinking_message(response_language, "retrieving"),
                        expanded=True,
                        state="running",
                ) as status_box:
                    answer = stream_deepseek_answer(
                        api_key=api_key,
                        question=user_question,
                        category_label=category_label,
                        category_dir=category_dir,
                        top_k=top_k,
                        placeholder=placeholder,
                        status_box=status_box,
                    )
                status_placeholder.empty()
            except Exception as exc:
                status_placeholder.empty()
                answer = f"Call failed: {exc}"
                placeholder.error(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
