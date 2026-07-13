"""
chunker.py

Splits documents into smaller chunks and enriches each chunk
with metadata for vector storage and citation.
"""

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Chunking configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def create_chunks(documents: list) -> list:
    """
    Split documents into smaller chunks and attach metadata.

    Args:
        documents (list): List of LangChain Document objects.

    Returns:
        list: List of chunked LangChain Document objects.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    for index, chunk in enumerate(chunks, start=1):

        source = os.path.basename(
            chunk.metadata.get("source", "Unknown")
        )

        page = chunk.metadata.get("page", 0) + 1

        chunk.metadata.update({

            "source": source,

            "page": page,

            "chunk_number": index,

            "chunk_id": f"{source}_page_{page}_chunk_{index}",

            "characters": len(chunk.page_content),

            "words": len(chunk.page_content.split())

        })

    return chunks