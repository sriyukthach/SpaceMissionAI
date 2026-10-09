import streamlit as st
from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


@st.cache_resource
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)


def create_embeddings(texts):
    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings.tolist()