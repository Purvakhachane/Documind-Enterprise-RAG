import streamlit as st

from document_processor.pdf_loader import save_pdf, load_pdf
from document_processor.metadata_extractor import extract_metadata

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