"""
statistics.py

Displays chunk statistics.
"""

import streamlit as st


def show_statistics(chunks):
    """
    Display statistics about generated chunks.
    """

    if not chunks:
        return

    total_chunks = len(chunks)

    average_words = round(
        sum(chunk.metadata["words"] for chunk in chunks) / total_chunks
    )

    average_characters = round(
        sum(chunk.metadata["characters"] for chunk in chunks) / total_chunks
    )

    st.subheader("📊 Chunk Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Chunks",
        total_chunks
    )

    col2.metric(
        "Average Words",
        average_words
    )

    col3.metric(
        "Average Characters",
        average_characters
    )