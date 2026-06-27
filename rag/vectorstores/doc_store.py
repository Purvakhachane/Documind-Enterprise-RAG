from langchain.storage import InMemoryStore


class DocumentStore:
    """Manage document storage for parent retrieval."""

    def __init__(self):
        self.store = InMemoryStore()

    def get_store(self):
        return self.store