"""
pipeline.py

Document processing pipeline.

This module orchestrates the complete document ingestion workflow.
"""

from unittest import result

from document_processor.pdf_loader import save_pdf, load_pdf
from document_processor.metadata_extractor import extract_metadata
from document_processor.chunker import create_chunks
from ui import chunks, metadata, summary
from vector_db.pinecone_manager import PineconeManager
from services.document_registry import save_document_info


class DocumentPipeline:
    """Handles the complete document processing workflow."""

    def __init__(self):
        self.pinecone = PineconeManager()

    def process(self, uploaded_file):
        """
        Process an uploaded PDF.

        Args:
            uploaded_file: Streamlit UploadedFile

        Returns:
            dict
        """

        # Save PDF
        file_path = save_pdf(uploaded_file)

        # Load PDF
        documents = load_pdf(file_path)

        # Extract metadata
        metadata = extract_metadata(documents)

        # Split into chunks
        chunks = create_chunks(documents)

        # Ensure Pinecone index exists
        index_status = self.pinecone.create_index()

        # Document summary
        summary = {
            "pages": len(documents),
            "chunks": len(chunks),
            "file_size": uploaded_file.size
        
        }

        result = {
            "file_path": file_path,
            "documents": documents,
            "metadata": metadata,
            "chunks": chunks,
            "summary": summary,
            "pinecone": self.pinecone,
            "index_status": index_status
        }

        save_document_info(
            result,
            uploaded_file.name
        )

        return result