import streamlit as st

from document_processor.pdf_loader import save_pdf, load_pdf
from document_processor.metadata_extractor import extract_metadata
from document_processor.chunker import create_chunks


st.set_page_config(
    page_title="Documind Enterprise RAG",
    layout="wide"
)

st.title("📄 Documind Enterprise RAG")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    # Save uploaded PDF
    file_path = save_pdf(uploaded_file)

    # Load PDF
    documents = load_pdf(file_path)

    # Extract Metadata
    metadata = extract_metadata(documents)
    
    # Create Chunks
    chunks = create_chunks(documents)

    st.success("PDF Loaded Successfully!")

    # Preview
    st.subheader("Document Preview")

    st.write(documents[0].page_content[:1000])

    # Metadata
    st.subheader("Document Metadata")

    for page in metadata:

        st.markdown("---")

        st.write(f"📄 Source: {page['source']}")

        st.write(f"📑 Page Number: {page['page']}")

        st.write(f"🔤 Characters: {page['characters']}")

        st.write(f"📝 Words: {page['words']}")
    

    st.subheader("Document Chunks")
    st.success(f"Total Chunks Created: {len(chunks)}")

    for chunk in chunks[:5]:

        st.markdown("---")

        st.write(f"🆔 Chunk ID: {chunk.metadata['chunk_id']}")

        st.write(f"📄 Source: {chunk.metadata['source']}")

        st.write(f"📑 Page: {chunk.metadata['page'] + 1}")

        st.write(f"🔢 Chunk Number: {chunk.metadata['chunk_number']}")

        st.write(f"🔤 Characters: {chunk.metadata['characters']}")

        st.write(f"📝 Words: {chunk.metadata['words']}")

        st.text(chunk.page_content[:300])
    
    st.subheader("Search Chunk")

    search_chunk = st.text_input("Enter Chunk ID")

    if search_chunk:

        found = False

        for chunk in chunks:

            if chunk.metadata["chunk_id"] == search_chunk:

                st.success("Chunk Found")

                st.write(chunk.metadata)

                st.write(chunk.page_content)

                found = True

                break

        if not found:

            st.warning("Chunk ID not found.")
        
    st.subheader("Chunk Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Chunks",
        len(chunks)
    )

    col2.metric(
        "Average Words",
        round(
            sum(c.metadata["words"] for c in chunks) / len(chunks)
        )
    )

    col3.metric(
        "Average Characters",
        round(
            sum(c.metadata["characters"] for c in chunks) / len(chunks)
        )
    )