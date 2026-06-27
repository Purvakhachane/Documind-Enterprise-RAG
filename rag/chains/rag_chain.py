from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from rag.llm.gemini import get_llm
from rag.prompts.prompt_template import get_prompt


class RAGChain:
    """Create the complete retrieval chain."""

    @staticmethod
    def build(retriever):
        llm = get_llm()
        prompt = get_prompt()

        document_chain = create_stuff_documents_chain(
            llm,
            prompt,
        )

        return create_retrieval_chain(
            retriever,
            document_chain,
        )