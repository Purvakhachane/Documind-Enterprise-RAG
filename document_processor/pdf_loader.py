"""
pdf_loader.py

Handles saving uploaded PDF files and loading them
using LangChain's PyPDFLoader.
"""

import os
from langchain_community.document_loaders import PyPDFLoader

# Folder where uploaded PDFs are stored
UPLOAD_FOLDER = "uploads"


def save_pdf(uploaded_file) -> str:
    """
    Save the uploaded PDF to the uploads folder.

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        str: Path of the saved PDF.
    """

    if uploaded_file is None:
        raise ValueError("No PDF file was uploaded.")

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as pdf:
        pdf.write(uploaded_file.getbuffer())

    return file_path


def load_pdf(file_path: str):
    """
    Load a PDF using LangChain's PyPDFLoader.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        list: List of LangChain Document objects.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF not found: {file_path}")

    loader = PyPDFLoader(file_path)
    return loader.load()