"""
sidebar.py

Handles the Streamlit sidebar.
"""

import streamlit as st


def setup_sidebar():
    """Display the application sidebar."""

    st.sidebar.title(" DocuMind Flow")
    st.sidebar.markdown(
        "Streamline PDF ingestion, metadata extraction, and semantic search in one vibrant workspace."
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("**How to use this app**")
    st.sidebar.markdown(
        "1. Upload PDF documents\n"
        "2. Process and inspect extracted metadata\n"
        "3. Explore chunks and download results"
    )

    st.sidebar.markdown("---")

    st.sidebar.write("**Quick tips:**")
    st.sidebar.write("• Keep files under 10 MB")
    st.sidebar.write("• Use clean, text-based PDFs for best extraction")
    st.sidebar.write("• Check the Pinecone status for index health")


def show_processing_status():
    """Display completed processing steps."""

    st.sidebar.success("✔ PDF Parsed")
    st.sidebar.success("✔ Metadata Extracted")
    st.sidebar.success("✔ Chunks Created")
    st.sidebar.success("✔ Pinecone Connected")
    st.sidebar.success("✔ Index Ready")
