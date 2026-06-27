from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChatResponse(BaseModel):
    answer: str
    source: str
    page: int
    confidence: float
    conversation_id: str
    timestamp: datetime

class DocumentResponse(BaseModel):
    document_id: str
    document_name: str
    document_type: str
    uploaded_at: datetime
    file_size: int

class DocumentListResponse(BaseModel):
    documents: List[DocumentResponse]
    total_count: int

class ConversationHistoryItem(BaseModel):
    question: str
    answer: str
    timestamp: datetime

class ConversationResponse(BaseModel):
    conversation_id: str
    history: List[ConversationHistoryItem]

class ErrorResponse(BaseModel):
    error: str
    detail: str
    status_code: int