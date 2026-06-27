from fastapi import APIRouter, HTTPException
from backend.models.request import ChatRequest
from backend.services.rag_service import ask_question
from backend.services.conversation_service import ConversationService
from backend.models.response import ChatResponse
from datetime import datetime

router = APIRouter(prefix="/api", tags=["chat"])
conversation_service = ConversationService()

@router.post("/chat")
def chat(request: ChatRequest):
    """Process a chat request with RAG"""
    try:
        # Get RAG response
        rag_response = ask_question(request.question)
        
        # Create conversation if not provided
        conversation_id = request.conversation_id
        if not conversation_id:
            conversation_id = conversation_service.create_conversation()
        
        # Add to conversation history
        conversation_service.add_message(
            conversation_id,
            request.question,
            rag_response["answer"]
        )
        
        # Return structured response
        return ChatResponse(
            answer=rag_response["answer"],
            source=rag_response["source"],
            page=rag_response["page"],
            confidence=0.85,
            conversation_id=conversation_id,
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))