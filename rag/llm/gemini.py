from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.settings import settings


def get_llm():
    """Return configured Gemini model."""

    return ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=settings.TEMPERATURE,
    )