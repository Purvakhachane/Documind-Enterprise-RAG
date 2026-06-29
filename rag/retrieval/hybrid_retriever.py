from langchain.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever


class HybridRetriever:
    """Combine keyword and semantic search."""

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def build(self, documents):
        keyword_retriever = BM25Retriever.from_documents(
            documents
        )
        keyword_retriever.k = 4

        semantic_retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 4}
        )

        hybrid_retriever = EnsembleRetriever(
            retrievers=[
                keyword_retriever,
                semantic_retriever,
            ],
            weights=[
                0.4,
                0.6,
            ],
        )

        return hybrid_retriever