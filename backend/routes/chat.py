from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from backend.models.request import ChatRequest
from backend.services.rag_service import ask_question
from backend.services.conversation_service import ConversationService
from backend.models.response import ChatResponse
from datetime import datetime, timedelta
from collections import defaultdict


def _build_response_metadata(answer: str, confidence: float) -> dict:
    return {
        "confidence": round(confidence, 2),
        "word_count": len(answer.split()),
        "response_hint": "Answer generated from available document context." if answer else "No answer generated.",
    }


def _check_rate_limit(request: Request) -> None:
    client_ip = request.client.host if request.client else "unknown"
    now = datetime.now()
    request_log[client_ip] = [
        ts for ts in request_log[client_ip] if now - ts < timedelta(seconds=RATE_LIMIT_WINDOW_SECONDS)
    ]
    if len(request_log[client_ip]) >= RATE_LIMIT_MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Too many requests. Please try again shortly.")
    request_log[client_ip].append(now)

router = APIRouter(prefix="/api", tags=["chat"])
conversation_service = ConversationService()
request_log = defaultdict(list)
RATE_LIMIT_WINDOW_SECONDS = 60
RATE_LIMIT_MAX_REQUESTS = 5

@router.post(
    "/chat",
    summary="Ask a question to the RAG assistant",
    description="Send a chat question to the document-aware RAG system and receive an answer along with metadata.",
    response_description="Structured chat response with answer metadata",
    responses={
        200: {
            "description": "Successful chat response",
            "content": {
                "application/json": {
                    "example": {
                        "answer": "The system uses document retrieval to answer questions.",
                        "source": "Sample.pdf",
                        "page": 1,
                        "confidence": 0.85,
                        "conversation_id": "conv_123",
                        "timestamp": "2026-07-06T20:00:00"
                    }
                }
            }
        }
    },
)
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


@router.post(
    "/chat/stream",
    summary="Stream a chat answer",
    description="Return the chat answer as a simple text stream for clients that want incremental output.",
    response_description="Streaming text response",
    responses={
        200: {
            "description": "Streaming response payload",
            "content": {
                "text/plain": {
                    "example": "The system uses document retrieval to answer questions."
                }
            }
        }
    },
)
def stream_chat(request: ChatRequest, http_request: Request):
    """Return a simple streaming-style response for the chat endpoint."""
    try:
        _check_rate_limit(http_request)
        rag_response = ask_question(request.question)
        answer = rag_response["answer"]

        def event_stream():
            for chunk in answer.split():
                yield chunk + " "

        return StreamingResponse(event_stream(), media_type="text/plain")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))