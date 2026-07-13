from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config.settings import settings


def get_embedding_model():
    """Return Gemini embedding model."""

    return GoogleGenerativeAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
    )