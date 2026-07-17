import json
import os

DATABASE_FILE = "database/citation_database.json"


def save_citations(chunks):
    """
    Save chunk metadata for citation retrieval.
    """

    os.makedirs("database", exist_ok=True)

    citations = []

    for chunk in chunks:
        citations.append({
            "chunk_id": chunk.metadata["chunk_id"],
            "source": chunk.metadata["source"],
            "page": chunk.metadata["page"],
            "chunk_number": chunk.metadata["chunk_number"],
            "characters": chunk.metadata["characters"],
            "words": chunk.metadata["words"],
            "text": chunk.page_content
        })

    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(citations, file, indent=4, ensure_ascii=False)

    return DATABASE_FILE
