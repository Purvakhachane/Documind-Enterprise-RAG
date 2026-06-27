from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:
    """Load PDF documents."""

    @staticmethod
    def load(file_path):
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        return documents