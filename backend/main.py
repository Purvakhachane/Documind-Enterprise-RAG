from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import HTTPException
from backend.routes.chat import router as chat_router
from backend.routes.documents import router as documents_router
from backend.routes.conversations import router as conversations_router
from backend.middleware.error_handler import global_exception_handler, validation_exception_handler, http_exception_handler
from backend.middleware.request_logging import RequestLoggingMiddleware
from backend.services.document_service import DocumentService
from backend.services.conversation_service import ConversationService
from backend.config import APP_TITLE, APP_DESCRIPTION, APP_VERSION, ENVIRONMENT

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

document_service = DocumentService()
conversation_service = ConversationService()

app.add_middleware(RequestLoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include routers
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(conversations_router)

# Add exception handlers
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

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
            :root { color-scheme: dark; }
            body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: linear-gradient(135deg, #020617, #0f172a); color: #f8fafc; }
            .container { max-width: 960px; margin: 0 auto; padding: 3rem 1.5rem; }
            .card { background: rgba(15, 23, 42, 0.95); padding: 2rem; border-radius: 18px; box-shadow: 0 18px 45px rgba(0,0,0,0.35); border: 1px solid rgba(148, 163, 184, 0.18); }
            h1 { margin-top: 0; font-size: 2rem; }
            .badge { display: inline-block; padding: 0.3rem 0.7rem; border-radius: 999px; background: #1d4ed8; font-size: 0.85rem; margin-bottom: 1rem; }
            code { background: #1f2937; padding: 0.15rem 0.45rem; border-radius: 6px; }
            a { color: #93c5fd; }
            ul { line-height: 1.7; }
        </style>
    </head>
    <body>
        <div class=\"container\">
            <div class=\"card\">
                <div class=\"badge\">Professional • Enterprise Ready</div>
                <h1>DocuMind Enterprise RAG</h1>
                <p>Your enterprise-grade document intelligence assistant is live and ready for secure, intelligent exploration.</p>
                <ul>
                    <li><strong>Chat:</strong> <code>/api/chat</code></li>
                    <li><strong>Documents:</strong> <code>/api/documents/upload</code> and <code>/api/documents/list</code></li>
                    <li><strong>Conversations:</strong> <code>/api/conversations/create</code></li>
                    <li><strong>Status:</strong> <code>/api/status</code></li>
                </ul>
                <p>Open <a href=\"/docs\">/docs</a> for the interactive API documentation or <a href=\"/redoc\">/redoc</a> for a structured reference.</p>
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
        "version": APP_VERSION,
        "environment": ENVIRONMENT
    }

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": f"The route {request.url.path} was not found.",
            "status_code": 404,
        },
    )

@app.get("/api/status")
def status_summary():
    documents = document_service.list_documents()
    conversations = conversation_service.list_conversations()
    return {
        "service": APP_TITLE,
        "version": APP_VERSION,
        "document_count": len(documents),
        "conversation_count": len(conversations),
        "status": "ready"
    }