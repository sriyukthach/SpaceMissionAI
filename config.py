import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

GROQ_MODEL = "openai/gpt-oss-20b"

DATA_DIR = "data"
VECTOR_DB_DIR = "vector_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

COLLECTION_NAME = "space_mission_knowledge"

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100
TOP_K = 3