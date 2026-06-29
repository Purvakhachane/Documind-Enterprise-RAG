from rag.retrieval.parent_retriever import ParentRetriever
from rag.vectorstores.faiss_store import FAISSStore


class IndexingService:
    """Create searchable document index."""

    def __init__(self):
        self.vector_store = FAISSStore().create()

    def build_index(self, documents):
        retriever = ParentRetriever(
            self.vector_store
        ).build()

        retriever.add_documents(documents)

        return retriever