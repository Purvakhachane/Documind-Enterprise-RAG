class RAGService:
    """Placeholder RAG service for the enterprise chat API."""

    def __init__(self):
        self.name = "placeholder-rag"

    def ask_question(self, question: str):
        return {
            "answer": "This is a dummy response.",
            "source": "Sample.pdf",
            "page": 1,
        }


def ask_question(question: str):
    return RAGService().ask_question(question)