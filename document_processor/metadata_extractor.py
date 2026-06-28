def extract_metadata(documents):

    metadata_list = []

    for doc in documents:

        metadata = {
            "source": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", 0) + 1,
            "characters": len(doc.page_content),
            "words": len(doc.page_content.split())
        }

        metadata_list.append(metadata)

    return metadata_list