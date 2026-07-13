from langchain.text_splitter import RecursiveCharacterTextSplitter

from rag.config.settings import settings


class TextSplitter:
    """Split documents into chunks."""

    @staticmethod
    def get_splitter():
        return RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )