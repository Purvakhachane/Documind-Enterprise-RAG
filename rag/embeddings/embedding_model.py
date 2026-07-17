from langchain_google_genai import GoogleGenerativeAIEmbeddings

from rag.config.settings import settings
from rag.exceptions import EmbeddingGenerationError


def get_embedding_model():
    """Return the configured Gemini embedding model."""

    if not settings.GOOGLE_API_KEY:
        raise EmbeddingGenerationError(
            "Google API key is not configured."
        )

    if not settings.EMBEDDING_MODEL:
        raise EmbeddingGenerationError(
            "Embedding model is not configured."
        )

    try:
        return GoogleGenerativeAIEmbeddings(
            model=settings.EMBEDDING_MODEL,
            google_api_key=settings.GOOGLE_API_KEY,
        )

    except Exception as error:
        raise EmbeddingGenerationError(
            f"Failed to initialize embedding model: {error}"
        ) from error