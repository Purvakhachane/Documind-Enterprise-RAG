from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    question: str
    conversation_id: Optional[str] = None

class DocumentUploadRequest(BaseModel):
    document_name: str
    document_type: str

class ConversationRequest(BaseModel):
    conversation_id: str