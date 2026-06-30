"""
summary.py

Displays document summary.
"""

import streamlit as st


def show_summary(documents, chunks, uploaded_file):
    """Display document summary."""

    st.subheader("📊 Document Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Pages",
        len(documents)
    )

    col2.metric(
        "Chunks",
        len(chunks)
    )

    col3.metric(
        "File Size",
        f"{uploaded_file.size / 1024:.2f} KB"
    )

    st.subheader("📄 Document Preview")

    st.write(
        documents[0].page_content[:1000]
    )