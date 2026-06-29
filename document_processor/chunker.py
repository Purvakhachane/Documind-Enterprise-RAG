from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    enhanced_chunks = []

    for index, chunk in enumerate(chunks):

        source = chunk.metadata.get("source", "Unknown")
        page = chunk.metadata.get("page", 0) + 1

        chunk.metadata.update({

            "chunk_number": index + 1,

            "chunk_id": f"{source}_page_{page}_chunk_{index+1}",

            "characters": len(chunk.page_content),

            "words": len(chunk.page_content.split())

        })

        enhanced_chunks.append(chunk)

    return enhanced_chunks