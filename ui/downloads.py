"""
downloads.py

Provides download buttons.
"""

import json
import pandas as pd
import streamlit as st


def download_metadata(metadata):
    """
    Download metadata as JSON.
    """

    metadata_json = json.dumps(
        metadata,
        indent=4
    )

    st.download_button(
        "⬇ Download Metadata JSON",
        metadata_json,
        "metadata.json",
        "application/json"
    )


def download_chunk_metadata(chunks):
    """
    Download chunk metadata as CSV.
    """

    chunk_df = pd.DataFrame(
        [chunk.metadata for chunk in chunks]
    )

    st.download_button(
        "⬇ Download Chunk Metadata CSV",
        chunk_df.to_csv(index=False),
        "chunk_metadata.csv",
        "text/csv"
    )