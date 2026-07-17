import os

from langchain_community.vectorstores import FAISS

from rag.embeddings.embedding_model import get_embedding_model
from rag.exceptions import VectorStoreError


class FAISSStore:
    """Manage FAISS vector store."""

    def __init__(self):
        self.embedding_model = get_embedding_model()

    def create(self):
        """Create an empty FAISS vector store."""

        if self.embedding_model is None:
            raise VectorStoreError(
                "Embedding model is not initialized."
            )

        try:
            return FAISS.from_texts(
                texts=["Initialization"],
                embedding=self.embedding_model,
            )

        except Exception as error:
            raise VectorStoreError(
                f"Failed to create vector store: {error}"
            ) from error

    def save(self, vector_store, save_path):
        """Save the vector store to disk."""

        if vector_store is None:
            raise VectorStoreError(
                "Vector store is not initialized."
            )

        try:
            os.makedirs(save_path, exist_ok=True)
            vector_store.save_local(save_path)

        except Exception as error:
            raise VectorStoreError(
                f"Failed to save vector store: {error}"
            ) from error

    def load(self, save_path):
        """Load an existing FAISS vector store."""

        if not os.path.exists(save_path):
            raise VectorStoreError(
                f"Vector store not found: {save_path}"
            )

        try:
            return FAISS.load_local(
                folder_path=save_path,
                embeddings=self.embedding_model,
                allow_dangerous_deserialization=True,
            )

        except Exception as error:
            raise VectorStoreError(
                f"Failed to load vector store: {error}"
            ) from error