from pathlib import Path
from pypdf import PdfReader

from config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP


def load_documents():
    documents = []

    data_path = Path(DATA_DIR)
    data_path.mkdir(exist_ok=True)

    for file_path in sorted(data_path.iterdir()):

        if file_path.suffix.lower() == ".txt":
            text = file_path.read_text(
                encoding="utf-8"
            )

        elif file_path.suffix.lower() == ".pdf":
            reader = PdfReader(str(file_path))

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        else:
            continue

        if text.strip():
            documents.append({
                "source": file_path.name,
                "text": text
            })

    return documents


def chunk_documents(documents):
    chunks = []

    step = CHUNK_SIZE - CHUNK_OVERLAP

    if step <= 0:
        raise ValueError(
            "CHUNK_SIZE must exceed CHUNK_OVERLAP"
        )

    for document in documents:
        text = document["text"]

        for start in range(0, len(text), step):
            chunk = text[start:start + CHUNK_SIZE]

            if chunk.strip():
                chunks.append({
                    "text": chunk,
                    "source": document["source"]
                })

            if start + CHUNK_SIZE >= len(text):
                break

    return chunks