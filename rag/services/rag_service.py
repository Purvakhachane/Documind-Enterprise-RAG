from rag.chains.conversation_chain import ConversationChain
from rag.services.query_service import QueryService


class RAGService:
    """Main service for document question answering."""

    def __init__(self, retriever):
        conversation_chain = ConversationChain.build(
            retriever
        )

        self.query_service = QueryService(
            conversation_chain
        )

    def ask(self, question, chat_history):
        return self.query_service.execute(
            question,
            chat_history,
        )