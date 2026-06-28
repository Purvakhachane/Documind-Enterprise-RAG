import streamlit as st

from document_processor.pdf_loader import save_pdf, load_pdf

st.set_page_config(
    page_title="Documind Enterprise RAG",
    layout="wide"
)

st.title("📄 Documind Enterprise RAG")

# Create the uploader FIRST
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# Now uploaded_file exists
if uploaded_file is not None:

    file_path = save_pdf(uploaded_file)

    documents = load_pdf(file_path)

    st.success("PDF Loaded Successfully!")

    st.subheader("Document Preview")

    st.write(documents[0].page_content[:1000])