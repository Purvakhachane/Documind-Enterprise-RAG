from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from backend.routes.chat import router as chat_router
from backend.routes.documents import router as documents_router
from backend.routes.conversations import router as conversations_router
from backend.middleware.error_handler import global_exception_handler, validation_exception_handler
from backend.services.document_service import DocumentService
from backend.services.conversation_service import ConversationService

app = FastAPI(
    title="DocuMind Enterprise RAG",
    description="Enterprise Retrieval-Augmented Generation System",
    version="1.0.0"
)

document_service = DocumentService()
conversation_service = ConversationService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(conversations_router)

# Add exception handlers
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"utf-8\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
        <title>DocuMind Enterprise RAG</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; background: #0f172a; color: #f8fafc; }
            .container { max-width: 860px; margin: 0 auto; padding: 3rem 1.5rem; }
            .card { background: #111827; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.25); }
            h1 { margin-top: 0; }
            code { background: #1f2937; padding: 0.15rem 0.4rem; border-radius: 6px; }
            a { color: #93c5fd; }
        </style>
    </head>
    <body>
        <div class=\"container\">
            <div class=\"card\">
                <h1>DocuMind Enterprise RAG</h1>
                <p>Your enterprise-ready document chat assistant is live and ready for exploration.</p>
                <ul>
                    <li><strong>Chat:</strong> <code>/api/chat</code></li>
                    <li><strong>Documents:</strong> <code>/api/documents/upload</code> and <code>/api/documents/list</code></li>
                    <li><strong>Conversations:</strong> <code>/api/conversations/create</code></li>
                </ul>
                <p>Open <a href=\"/docs\">/docs</a> for the interactive API documentation.</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "DocuMind Enterprise RAG",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/api/status")
def status_summary():
    documents = document_service.list_documents()
    conversations = conversation_service.list_conversations()
    return {
        "service": "DocuMind Enterprise RAG",
        "version": "1.0.0",
        "document_count": len(documents),
        "conversation_count": len(conversations),
        "status": "ready"
    }