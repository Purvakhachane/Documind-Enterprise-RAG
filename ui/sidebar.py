"""
sidebar.py

Handles the Streamlit sidebar.
"""

import streamlit as st


def setup_sidebar():
    """Display the application sidebar."""

    st.sidebar.title("📄 Documind Enterprise RAG")

    st.sidebar.info(
        "Week 1 - Document Processing Pipeline"
    )

    st.sidebar.markdown("---")

    st.sidebar.write(
        "Upload one or more PDF documents to begin processing."
    )


def show_processing_status():
    """Display completed processing steps."""

    st.sidebar.success("PDF Parsed")
    st.sidebar.success("Metadata Extracted")
    st.sidebar.success("Chunks Created")
    st.sidebar.success("Pinecone Connected")