class MetadataProcessor:
    """Process document metadata."""

    @staticmethod
    def process(documents):
        processed_documents = []

        for document in documents:
            metadata = document.metadata

            document.metadata = {
                "source": metadata.get("source"),
                "page": metadata.get("page", 0)
            }

            processed_documents.append(document)

        return processed_documents