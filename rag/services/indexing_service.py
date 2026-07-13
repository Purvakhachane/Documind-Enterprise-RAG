from rag.retrieval.parent_retriever import ParentRetriever
from rag.vectorstores.faiss_store import FAISSStore
from rag.retrieval.hybrid_retriever import HybridRetriever


class IndexingService:
    """Create searchable document index."""

    def __init__(self):
        self.vector_store = FAISSStore().create()

    def build_index(self, documents):
        parent_retriever = ParentRetriever(
            self.vector_store
        ).build()

        parent_retriever.add_documents(documents)

        hybrid_retriever = HybridRetriever(
            self.vector_store
        ).build(documents)

        return hybrid_retriever