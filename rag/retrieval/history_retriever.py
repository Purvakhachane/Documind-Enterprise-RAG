from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from rag.llm.gemini import get_llm


class HistoryRetriever:
    """Create a history-aware retriever."""

    @staticmethod
    def build(retriever):
        llm = get_llm()

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Generate a search query using the chat history and latest user question."
                ),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        return create_history_aware_retriever(
            llm,
            retriever,
            prompt,
        )