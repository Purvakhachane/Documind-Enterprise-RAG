import os

from rag.exceptions import DocumentLoadError, EmptyDocumentError
from rag.loaders.pdf_loader import PDFLoader


class DocumentLoader:
    """Load supported documents."""

    @staticmethod
    def load(file_path):
        """Load a supported document and validate its content."""

        extension = os.path.splitext(file_path)[1].lower()

        try:
            if extension != ".pdf":
                raise DocumentLoadError(
                    f"Unsupported file type: {extension}"
                )

            documents = PDFLoader.load(file_path)

            if not documents:
                raise EmptyDocumentError(
                    "The document does not contain any readable content."
                )

            return documents

        except (DocumentLoadError, EmptyDocumentError):
            raise

        except Exception as error:
            raise DocumentLoadError(
                f"Failed to load document: {error}"
            ) from error