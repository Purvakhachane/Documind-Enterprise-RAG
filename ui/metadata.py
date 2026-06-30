"""
metadata.py

Displays page metadata.
"""

import streamlit as st


def show_metadata(metadata):
    """Display metadata."""

    st.subheader("📑 Metadata")

    for page in metadata:

        with st.expander(
            f"Page {page['page']}"
        ):

            st.write(
                f"Source : {page['source']}"
            )

            st.write(
                f"Characters : {page['characters']}"
            )

            st.write(
                f"Words : {page['words']}"
            )