import json
import os
from datetime import datetime

REGISTRY_FILE = "database/document_registry.json"


def register_document(uploaded_file, documents, chunks):
    """Store processed document information."""

    os.makedirs("database", exist_ok=True)

    registry = []

    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "r", encoding="utf-8") as file:
            registry = json.load(file)

    registry.append({
        "filename": uploaded_file.name,
        "pages": len(documents),
        "chunks": len(chunks),
        "size_kb": round(uploaded_file.size / 1024, 2),
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Success"
    })

    with open(REGISTRY_FILE, "w", encoding="utf-8") as file:
        json.dump(registry, file, indent=4)