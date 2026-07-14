"""
metadata.py

Displays page metadata.
"""

import streamlit as st


def show_metadata(metadata, use_expanders: bool = True):
    """Display metadata.

    Parameters
    - metadata: iterable of page metadata dicts
    - use_expanders: when True display each page in its own `st.expander`.
      Set to False when calling from inside another expander to avoid nesting.
    """

    st.subheader("📑 Metadata")

    for page in metadata:
        title = f"Page {page['page']}"

        if use_expanders:
            with st.expander(title):
                st.write(f"Source : {page['source']}")
                st.write(f"Characters : {page['characters']}")
                st.write(f"Words : {page['words']}")
        else:
            st.markdown(f"**{title}**")
            st.write(f"Source : {page['source']}")
            st.write(f"Characters : {page['characters']}")
            st.write(f"Words : {page['words']}")