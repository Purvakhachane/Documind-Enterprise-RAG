from langchain.retrievers import ParentDocumentRetriever

from rag.preprocessing.parent_splitter import ParentSplitter
from rag.preprocessing.text_splitter import TextSplitter
from rag.vectorstores.docstore import DocumentStore


class ParentRetriever:
    """Build a parent document retriever."""

    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.doc_store = DocumentStore().get_store()

    def build(self):
        retriever = ParentDocumentRetriever(
            vectorstore=self.vector_store,
            docstore=self.doc_store,
            child_splitter=TextSplitter.get_splitter(),
            parent_splitter=ParentSplitter.get_splitter(),
        )

        return retriever