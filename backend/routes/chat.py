from fastapi import APIRouter
from backend.models.request import ChatRequest
from backend.services.rag_service import ask_question

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    return ask_question(request.question)