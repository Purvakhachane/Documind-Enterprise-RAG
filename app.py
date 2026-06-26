import streamlit as st

st.set_page_config(
    page_title="Documind Enterprise RAG",
    layout="wide"
)

st.title("📄 Documind Enterprise RAG")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )