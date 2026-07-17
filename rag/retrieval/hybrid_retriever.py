from langchain.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

from rag.config.settings import settings


class HybridRetriever:
    """Combine keyword and semantic search."""

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def build(self, documents):
        keyword_retriever = BM25Retriever.from_documents(
            documents
        )
        keyword_retriever.k = settings.SEARCH_K

        semantic_retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": settings.SEARCH_K,
                "fetch_k": settings.FETCH_K,
            }
        )

        return EnsembleRetriever(
            retrievers=[
                keyword_retriever,
                semantic_retriever,
            ],
            weights=[
                settings.KEYWORD_WEIGHT,
                settings.SEMANTIC_WEIGHT,
            ],
        )