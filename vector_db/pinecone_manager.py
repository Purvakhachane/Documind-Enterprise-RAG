"""
pinecone_manager.py

Handles all Pinecone operations:
- Connect to Pinecone
- Create index
- Get index
- Upload vectors
- View index statistics
"""

import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

INDEX_DIMENSION = 768
METRIC = "cosine"
CLOUD = "aws"
REGION = "us-east-1"


class PineconeManager:
    """Manage Pinecone index operations."""

    def __init__(self):
        self.api_key = os.getenv("PINECONE_API_KEY")
        self.index_name = os.getenv("PINECONE_INDEX")

        if not self.api_key:
            raise ValueError("PINECONE_API_KEY not found in .env")

        if not self.index_name:
            raise ValueError("PINECONE_INDEX not found in .env")

        self.client = Pinecone(api_key=self.api_key)

    def create_index(self) -> str:
        """
        Create the Pinecone index if it doesn't already exist.

        Returns:
            str: Status message.
        """

        existing_indexes = self.client.list_indexes().names()

        if self.index_name in existing_indexes:
            return "Index already exists"

        self.client.create_index(
            name=self.index_name,
            dimension=INDEX_DIMENSION,
            metric=METRIC,
            spec=ServerlessSpec(
                cloud=CLOUD,
                region=REGION
            )
        )

        return "Index created successfully"

    def get_index(self):
        """
        Return the Pinecone index object.
        """
        return self.client.Index(self.index_name)

    def list_indexes(self) -> list:
        """
        Return all available Pinecone indexes.
        """
        return self.client.list_indexes().names()

    def upsert_vectors(self, vectors: list) -> int:
        """
        Upload vectors to Pinecone.

        Args:
            vectors (list): List of vectors.

        Returns:
            int: Number of uploaded vectors.
        """

        if not vectors:
            return 0

        index = self.get_index()
        index.upsert(vectors=vectors)

        return len(vectors)

    def get_index_stats(self):
        """
        Return Pinecone index statistics.
        """
        index = self.get_index()
        return index.describe_index_stats()

    def delete_all_vectors(self):
        """
        Delete all vectors from the index.
        Useful during development/testing.
        """
        index = self.get_index()
        index.delete(delete_all=True)