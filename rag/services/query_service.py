from rag.guardrails.hallucination_guard import HallucinationGuard
from rag.utils.citation_formatter import CitationFormatter


class QueryService:
    """Handle document queries."""

    def __init__(self, conversation_chain):
        self.conversation_chain = conversation_chain

    def execute(self, question, chat_history):
        response = self.conversation_chain.invoke(
            {
                "input": question,
                "chat_history": chat_history,
            }
        )

        answer = HallucinationGuard.validate(
            response["answer"]
        )

        citations = CitationFormatter.format(
            response["context"]
        )

        return {
            "answer": answer,
            "citations": citations,
        }