class ResponseFormatter:
    """Format AI responses."""

    @staticmethod
    def format(answer, citations):
        return {
            "answer": answer,
            "citations": citations,
            "total_sources": len(citations),
        }