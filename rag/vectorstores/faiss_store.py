import os

from langchain_community.vectorstores import FAISS

from rag.embeddings.embedding_model import get_embedding_model


class FAISSStore:
    """Manage FAISS vector store."""

    def __init__(self):
        self.embedding_model = get_embedding_model()

    def create(self):
        return FAISS.from_texts(
            texts=["Initialization"],
            embedding=self.embedding_model,
        )

    def save(self, vector_store, save_path):
        os.makedirs(save_path, exist_ok=True)
        vector_store.save_local(save_path)

    def load(self, save_path):
        return FAISS.load_local(
            folder_path=save_path,
            embeddings=self.embedding_model,
            allow_dangerous_deserialization=True,
        )