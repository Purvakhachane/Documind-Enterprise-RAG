import os
from typing import List, Optional
from datetime import datetime
import json

from backend.config import UPLOAD_STORAGE_PATH


class DocumentService:
    def __init__(self, storage_path: str = UPLOAD_STORAGE_PATH):
        self.storage_path = storage_path
        self.metadata_file = os.path.join(storage_path, "metadata.json")
        
        # Create storage directory if it doesn't exist
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
        
        # Initialize metadata file if it doesn't exist
        if not os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'w') as f:
                json.dump([], f)
    
    def upload_document(self, filename: str, file_content: bytes, doc_type: str) -> dict:
        """Upload a document and store metadata"""
        self._validate_pdf(filename, file_content, doc_type)

        doc_id = f"doc_{datetime.now().timestamp()}"
        file_path = os.path.join(self.storage_path, f"{doc_id}_{filename}")
        
        # Save file
        with open(file_path, 'wb') as f:
            f.write(file_content)
        
        # Update metadata
        metadata = self._read_metadata()
        doc_metadata = {
            "document_id": doc_id,
            "document_name": filename,
            "document_type": doc_type,
            "uploaded_at": datetime.now().isoformat(),
            "file_size": len(file_content),
            "file_path": file_path
        }
        metadata.append(doc_metadata)
        self._write_metadata(metadata)
        
        return doc_metadata
    
    def list_documents(self) -> List[dict]:
        """List all uploaded documents"""
        metadata = self._read_metadata()
        return metadata
    
    def delete_document(self, doc_id: str) -> bool:
        """Delete a document by ID"""
        metadata = self._read_metadata()
        doc_to_delete = next((d for d in metadata if d["document_id"] == doc_id), None)
        
        if not doc_to_delete:
            return False
        
        # Delete file
        if os.path.exists(doc_to_delete["file_path"]):
            os.remove(doc_to_delete["file_path"])
        
        # Update metadata
        metadata = [d for d in metadata if d["document_id"] != doc_id]
        self._write_metadata(metadata)
        
        return True
    
    def get_document(self, doc_id: str) -> Optional[dict]:
        """Get document metadata by ID"""
        metadata = self._read_metadata()
        return next((d for d in metadata if d["document_id"] == doc_id), None)
    
    def _validate_pdf(self, filename: str, file_content: bytes, doc_type: Optional[str]) -> None:
        """Ensure requested uploads are valid PDF files."""
        if not filename:
            raise ValueError("Filename is required")

        lower_name = filename.lower()
        if not lower_name.endswith(".pdf"):
            raise ValueError("Only PDF files are supported")

        if doc_type and doc_type.lower() != "application/pdf":
            raise ValueError("Content type must be application/pdf")

        if not file_content.startswith(b"%PDF"):
            raise ValueError("Uploaded file is not a valid PDF")

    def _read_metadata(self) -> List[dict]:
        """Read metadata file"""
        try:
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def _write_metadata(self, metadata: List[dict]) -> None:
        """Write metadata file"""
        with open(self.metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
