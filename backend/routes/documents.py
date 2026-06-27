from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.document_service import DocumentService
from backend.models.response import DocumentResponse, DocumentListResponse

router = APIRouter(prefix="/api/documents", tags=["documents"])
document_service = DocumentService()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload a new document"""
    try:
        content = await file.read()
        doc_metadata = document_service.upload_document(
            filename=file.filename,
            file_content=content,
            doc_type=file.content_type
        )
        return doc_metadata
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list")
def list_documents():
    """List all uploaded documents"""
    try:
        documents = document_service.list_documents()
        return DocumentListResponse(
            documents=documents,
            total_count=len(documents)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{doc_id}")
def get_document(doc_id: str):
    """Get document metadata by ID"""
    try:
        doc = document_service.get_document(doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{doc_id}")
def delete_document(doc_id: str):
    """Delete a document by ID"""
    try:
        if not document_service.delete_document(doc_id):
            raise HTTPException(status_code=404, detail="Document not found")
        return {"message": "Document deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
