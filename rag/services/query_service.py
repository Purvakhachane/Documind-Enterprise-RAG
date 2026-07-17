from rag.exceptions import (
    ResponseGenerationError,
    RetrievalError,
)
from rag.guardrails.hallucination_guard import HallucinationGuard
from rag.utils.citation_formatter import CitationFormatter
from rag.utils.response_formatter import ResponseFormatter


class QueryService:
    """Handle document queries."""

    def __init__(self, conversation_chain):
        self.conversation_chain = conversation_chain

    def execute(self, question, chat_history):
        """Execute a RAG query."""

        if not question or not question.strip():
            raise RetrievalError(
                "Question cannot be empty."
            )

        if self.conversation_chain is None:
            raise RetrievalError(
                "Conversation chain is not initialized."
            )

        try:
            response = self.conversation_chain.invoke(
                {
                    "input": question.strip(),
                    "chat_history": chat_history,
                }
            )

            answer = HallucinationGuard.validate(
                response["answer"]
            )

            citations = CitationFormatter.format(
                response["context"]
            )

            return ResponseFormatter.format(
                answer,
                citations,
            )

        except RetrievalError:
            raise

        except Exception as error:
            raise ResponseGenerationError(
                f"Failed to generate response: {error}"
            ) from error