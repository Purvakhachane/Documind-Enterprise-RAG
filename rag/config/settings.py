import os
from dotenv import load_dotenv

load_dotenv()

# API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini Models
LLM_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/text-embedding-004"

# Chunking Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Store
VECTOR_DB_PATH = "data/faiss_index"