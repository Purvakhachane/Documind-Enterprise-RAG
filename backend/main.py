from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from backend.routes.chat import router as chat_router
from backend.routes.documents import router as documents_router
from backend.routes.conversations import router as conversations_router
from backend.middleware.error_handler import global_exception_handler, validation_exception_handler

app = FastAPI(
    title="DocuMind Enterprise RAG",
    description="Enterprise Retrieval-Augmented Generation System",
    version="1.0.0"
)

# Include routers
app.include_router(chat_router, prefix="/api")
app.include_router(documents_router)
app.include_router(conversations_router)

# Add exception handlers
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/")
def home():
    return {
        "message": "DocuMind Enterprise RAG Running",
        "version": "1.0.0",
        "endpoints": {
            "chat": "/api/chat",
            "documents": "/api/documents",
            "conversations": "/api/conversations"
        }
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "DocuMind Enterprise RAG"}