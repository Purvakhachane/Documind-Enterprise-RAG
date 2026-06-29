from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Question to ask the RAG system")
    conversation_id: Optional[str] = None

class DocumentUploadRequest(BaseModel):
    document_name: str
    document_type: str

class ConversationRequest(BaseModel):
    conversation_id: str