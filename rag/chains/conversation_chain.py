from rag.chains.rag_chain import RAGChain
from rag.retrieval.history_retriever import HistoryRetriever


class ConversationChain:
    """Build a conversation-aware RAG pipeline."""

    @staticmethod
    def build(retriever):
        history_retriever = HistoryRetriever.build(
            retriever
        )

        return RAGChain.build(
            history_retriever
        )