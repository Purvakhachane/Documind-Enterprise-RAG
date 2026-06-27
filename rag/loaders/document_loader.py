import os

from rag.loaders.pdf_loader import PDFLoader


class DocumentLoader:
    """Load supported documents."""

    @staticmethod
    def load(file_path):
        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return PDFLoader.load(file_path)

        raise ValueError(f"Unsupported file type: {extension}")