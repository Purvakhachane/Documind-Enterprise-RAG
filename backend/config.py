import os


APP_TITLE = os.getenv("APP_TITLE", "DocuMind Enterprise RAG")
APP_DESCRIPTION = os.getenv(
    "APP_DESCRIPTION",
    "Professional enterprise retrieval-augmented generation platform",
)
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
UPLOAD_STORAGE_PATH = os.getenv("UPLOAD_STORAGE_PATH", "./documents")
