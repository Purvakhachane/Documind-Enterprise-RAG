"""Custom exceptions used throughout the RAG pipeline."""


class RAGError(Exception):
    """Base exception for all RAG-related errors."""


class DocumentLoadError(RAGError):
    """Raised when a document cannot be loaded."""


class EmptyDocumentError(RAGError):
    """Raised when the loaded document has no content."""


class EmbeddingGenerationError(RAGError):
    """Raised when embedding generation fails."""


class VectorStoreError(RAGError):
    """Raised when vector store operations fail."""


class RetrievalError(RAGError):
    """Raised when document retrieval fails."""


class ResponseGenerationError(RAGError):
    """Raised when the language model cannot generate a response."""