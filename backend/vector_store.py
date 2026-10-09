import hashlib
import chromadb
import streamlit as st

from config import (
    VECTOR_DB_DIR,
    COLLECTION_NAME,
    TOP_K
)

from backend.embeddings import create_embeddings


@st.cache_resource
def get_collection():
    client = chromadb.PersistentClient(
        path=VECTOR_DB_DIR
    )

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )


def store_documents(chunks):
    collection = get_collection()

    if not chunks:
        return

    texts = [chunk["text"] for chunk in chunks]

    embeddings = create_embeddings(texts)

    ids = [
        hashlib.sha256(
            (
                chunk["source"] + ":" +
                str(index) + ":" +
                chunk["text"]
            ).encode("utf-8")
        ).hexdigest()
        for index, chunk in enumerate(chunks)
    ]

    metadatas = [
        {"source": chunk["source"]}
        for chunk in chunks
    ]

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search_documents(query):
    collection = get_collection()

    if collection.count() == 0:
        return []

    query_embedding = create_embeddings([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(TOP_K, collection.count())
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return [
        {
            "text": text,
            "source": metadata["source"]
        }
        for text, metadata in zip(documents, metadatas)
    ]