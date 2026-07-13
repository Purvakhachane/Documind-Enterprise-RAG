"""
summary.py

Displays document summary.
"""

import streamlit as st


def show_summary(result):
    """
    Display document summary and preview.
    """

    summary = result["summary"]
    documents = result["documents"]

    st.subheader("📊 Document Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Pages",
        summary["pages"]
    )

    col2.metric(
        "Chunks",
        summary["chunks"]
    )

    col3.metric(
        "File Size",
        f"{summary['file_size'] / 1024:.2f} KB"
    )

    st.subheader("📄 Document Preview")

    st.write(
        documents[0].page_content[:1000]
    )