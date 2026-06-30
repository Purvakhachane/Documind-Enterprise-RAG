from pydantic import BaseModel, Field, validator
from typing import Optional


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Question to ask the RAG system")
    conversation_id: Optional[str] = None

    @validator("question")
    def validate_question(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Question cannot be empty")
        if len(cleaned) < 3:
            raise ValueError("Question must be at least 3 characters long")
        if len(cleaned) > 1000:
            raise ValueError("Question is too long")
        return cleaned


class DocumentUploadRequest(BaseModel):
    document_name: str = Field(..., min_length=1)
    document_type: str = Field(..., min_length=1)


class ConversationRequest(BaseModel):
    conversation_id: str = Field(..., min_length=1)