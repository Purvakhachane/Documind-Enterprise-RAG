"""
pipeline.py

This module manages the complete document processing pipeline.

Workflow:
Upload PDF
    ↓
Save PDF
    ↓
Load PDF
    ↓
Extract Metadata
    ↓
Create Chunks
    ↓
Create Pinecone Index
    ↓
Return Processing Result
"""

from document_processor.pdf_loader import save_pdf, load_pdf
from document_processor.metadata_extractor import extract_metadata
from document_processor.chunker import create_chunks
from vector_db.pinecone_manager import PineconeManager


def process_document(uploaded_file):
    """
    Process a PDF from upload to chunk creation.

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        dict: All processed document information.
    """

    # Save uploaded PDF
    file_path = save_pdf(uploaded_file)

    # Load PDF
    documents = load_pdf(file_path)

    # Extract page metadata
    metadata = extract_metadata(documents)

    # Split document into chunks
    chunks = create_chunks(documents)

    # Initialize Pinecone
    pinecone = PineconeManager()

    # Create index if needed
    index_status = pinecone.create_index()

    return {
        "documents": documents,
        "metadata": metadata,
        "chunks": chunks,
        "pinecone": pinecone,
        "index_status": index_status
    }