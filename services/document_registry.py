"""
document_registry.py

Stores information about every processed document.
"""

import json
import os
from datetime import datetime


REGISTRY_FILE = "document_registry.json"


def save_document_info(result, filename):
    """
    Save processed document information.

    Args:
        result (dict): Pipeline result.
        filename (str): Uploaded file name.
    """

    summary = result["summary"]

    document_info = {
        "filename": filename,
        "pages": summary["pages"],
        "chunks": summary["chunks"],
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Processed"
    }

    if os.path.exists(REGISTRY_FILE):

        with open(REGISTRY_FILE, "r") as file:
            registry = json.load(file)

    else:

        registry = []

    registry.append(document_info)

    with open(REGISTRY_FILE, "w") as file:
        json.dump(registry, file, indent=4)