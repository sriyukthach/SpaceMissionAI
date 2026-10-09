import streamlit as st

from backend.document_loader import (
    load_documents,
    chunk_documents
)
from backend.vector_store import (
    store_documents,
    get_collection
)
from backend.chatbot import get_chatbot_response


st.set_page_config(
    page_title="SpaceMissionAI",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #080d1c, #142447
    );
    color: white;
}
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}
h1 {
    color: #83caff !important;
}
div.stButton > button {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def initialize_knowledge_base():
    documents = load_documents()
    chunks = chunk_documents(documents)

    if chunks:
        store_documents(chunks)

    return len(documents), len(chunks)


st.title("🚀 SpaceMissionAI")
st.caption(
    "Your AI-powered guide to space mission operations"
)

with st.sidebar:
    st.header("🛰️ Mission Control Center")

    st.write(
        "Learn how space missions are planned, "
        "launched, and monitored."
    )

    st.divider()

    st.subheader("📚 Knowledge Base")

    try:
        document_count, chunk_count = (
            initialize_knowledge_base()
        )

        st.success("Knowledge base ready!")
        st.metric("Documents", document_count)
        st.metric("Text Chunks", chunk_count)
        st.metric(
            "Stored Vectors",
            get_collection().count()
        )

    except Exception as error:
        st.error(
            "Knowledge base initialization failed. "
            "Check the terminal for details."
        )
        st.exception(error)
        st.stop()

    st.divider()
    st.info(
        "Educational explanations only. "
        "No real spacecraft control or simulations."
    )

st.subheader("🌌 Explore Space Operations")

sample_questions = [
    "Explain rocket launch sequence",
    "What happens during mission control?",
    "Explain satellite deployment process",
    "What is pre-launch testing?"
]

col1, col2 = st.columns(2)

for index, question in enumerate(sample_questions):
    column = col1 if index % 2 == 0 else col2

    with column:
        if st.button(
            question,
            key=f"sample_{index}",
            use_container_width=True
        ):
            st.session_state.pending_question = question

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            st.caption(
                "📚 Retrieved sources: " +
                ", ".join(message["sources"])
            )

typed_question = st.chat_input(
    "Ask anything about space missions..."
)

question = st.session_state.pop(
    "pending_question", None
) or typed_question

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching mission knowledge..."):
            answer, sources = get_chatbot_response(
                question
            )

        st.markdown(answer)

        if sources:
            st.caption(
                "📚 Retrieved sources: " +
                ", ".join(sources)
            )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })