from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat():
    return {
        "answer":"Sample Answer",
        "source":"Policy.pdf",
        "page":12
    }