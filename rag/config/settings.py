import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application configuration."""

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    LLM_MODEL = "gemini-2.5-flash"

    EMBEDDING_MODEL = "models/text-embedding-004"

    CHUNK_SIZE = 1000

    CHUNK_OVERLAP = 200

    VECTOR_STORE_PATH = "data/vectorstore"

    DOCUMENT_PATH = "data/documents"

    SEARCH_K = 4

    FETCH_K = 8

    KEYWORD_WEIGHT = 0.4

    SEMANTIC_WEIGHT = 0.6

    TEMPERATURE = 0.2


settings = Settings()