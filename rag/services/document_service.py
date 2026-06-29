from rag.loaders.document_loader import DocumentLoader
from rag.preprocessing.metadata_processor import MetadataProcessor


class DocumentService:
    """Load and prepare documents."""

    @staticmethod
    def process(file_path):
        documents = DocumentLoader.load(file_path)

        documents = MetadataProcessor.process(
            documents
        )

        return documents