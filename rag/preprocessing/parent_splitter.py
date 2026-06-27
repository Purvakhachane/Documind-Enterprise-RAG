from rag.preprocessing.text_splitter import TextSplitter


class ParentSplitter:
    """Generate document chunks."""

    @staticmethod
    def split_documents(documents):
        splitter = TextSplitter.get_splitter()
        return splitter.split_documents(documents)