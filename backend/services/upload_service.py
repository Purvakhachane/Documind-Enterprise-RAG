from typing import Optional


class UploadService:
    """Placeholder upload service for future document ingestion workflows."""

    def __init__(self):
        self.name = "placeholder-upload-service"

    def upload(self, filename: str, file_content: bytes, doc_type: Optional[str] = None) -> dict:
        return {
            "filename": filename,
            "content_type": doc_type,
            "size_bytes": len(file_content),
            "status": "queued",
        }
