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

    st.write(f"Total Chunks Created: {len(chunks)}")

    for i, chunk in enumerate(chunks[:5], start=1):

        st.markdown("---")

        st.write(f"Chunk {i}")

        st.write(chunk.page_content[:300])

        st.write(chunk.metadata)