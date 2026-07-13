class CitationFormatter:
    """Extract citation details from retrieved documents."""

    @staticmethod
    def format(documents):
        citations = []

        for document in documents:
            metadata = document.metadata

            citations.append(
                {
                    "source": metadata.get("source", "Unknown"),
                    "page": metadata.get("page", "Unknown"),
                }
            )

        return citations