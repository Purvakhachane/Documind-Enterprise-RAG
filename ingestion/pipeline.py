"""
pipeline.py

Document Processing Pipeline

Handles:
- Save uploaded PDF
- Load PDF
- Extract metadata
- Create chunks
- Save citation database
- Register processed document
- Connect to Pinecone
- Generate processing report
"""

from document_processor.pdf_loader import save_pdf, load_pdf
from document_processor.metadata_extractor import extract_metadata
from document_processor.chunker import create_chunks

from vector_db.pinecone_manager import PineconeManager

from services.document_registry import register_document
from services.citation_database import save_citations
from services.logger import log_process
from services.report_generator import save_report


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
            dict: Processed document information.
        """

        # -------------------------------
        # Upload & Save PDF
        # -------------------------------

        log_process(f"{uploaded_file.name} uploaded")

        file_path = save_pdf(uploaded_file)

        # -------------------------------
        # Load PDF
        # -------------------------------

        documents = load_pdf(file_path)

        log_process("PDF Loaded")

        # -------------------------------
        # Extract Metadata
        # -------------------------------

        metadata = extract_metadata(documents)

        log_process("Metadata Extracted")

        # -------------------------------
        # Create Chunks
        # -------------------------------

        chunks = create_chunks(documents)

        log_process("Chunks Created")

        # -------------------------------
        # Save Citation Database
        # -------------------------------

        save_citations(chunks)

        log_process("Citation Database Updated")

        # -------------------------------
        # Register Document
        # -------------------------------

        register_document(
            uploaded_file,
            documents,
            chunks
        )

        # -------------------------------
        # Pinecone
        # -------------------------------

        index_status = self.pinecone.create_index()

        log_process("Pinecone Connected")

        # -------------------------------
        # Summary
        # -------------------------------

        summary = {
            "pages": len(documents),
            "chunks": len(chunks),
            "file_size": uploaded_file.size
        }

        # -------------------------------
        # Final Result
        # -------------------------------

        result = {
            "file_path": file_path,
            "documents": documents,
            "metadata": metadata,
            "chunks": chunks,
            "summary": summary,
            "pinecone": self.pinecone,
            "index_status": index_status
        }

        # -------------------------------
        # Generate Report
        # -------------------------------

        save_report(result)

        log_process(f"{uploaded_file.name} processed successfully")

        return result