from fastapi import APIRouter, HTTPException
from backend.models.request import ChatRequest
from backend.services.rag_service import ask_question
from backend.services.conversation_service import ConversationService
from backend.models.response import ChatResponse
from datetime import datetime


def _build_response_metadata(answer: str, confidence: float) -> dict:
    return {
        "confidence": round(confidence, 2),
        "word_count": len(answer.split()),
        "response_hint": "Answer generated from available document context." if answer else "No answer generated.",
    }

router = APIRouter(prefix="/api", tags=["chat"])
conversation_service = ConversationService()

@router.post("/chat")
def chat(request: ChatRequest):
    """Process a chat request with RAG and persist it in a conversation."""
    try:
        rag_response = ask_question(request.question)
        metadata = _build_response_metadata(rag_response["answer"], 0.85)

        conversation_id = request.conversation_id or conversation_service.create_conversation()

        conversation_service.add_message(
            conversation_id,
            request.question,
            rag_response["answer"],
        )

        return ChatResponse(
            answer=rag_response["answer"],
            source=rag_response["source"],
            page=rag_response["page"],
            confidence=metadata["confidence"],
            conversation_id=conversation_id,
            timestamp=datetime.now(),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))