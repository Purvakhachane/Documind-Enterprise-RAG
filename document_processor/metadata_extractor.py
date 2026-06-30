"""
metadata_extractor.py

Extracts useful metadata from LangChain Document objects.
"""

import os


def extract_metadata(documents: list) -> list:
    """
    Extract metadata from each page of the document.

    Args:
        documents (list): List of LangChain Document objects.

    Returns:
        list: Metadata for every page.
    """

    metadata_list = []

    total_pages = len(documents)

    for document in documents:

        source = document.metadata.get("source", "Unknown")

        metadata = {
            "source": os.path.basename(source),
            "page": document.metadata.get("page", 0) + 1,
            "characters": len(document.page_content),
            "words": len(document.page_content.split()),
            "total_pages": total_pages
        }

        metadata_list.append(metadata)

    return metadata_list