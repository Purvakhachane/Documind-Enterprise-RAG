"""
chunks.py

Displays document chunks.
"""

import streamlit as st


def show_chunks(chunks, use_expanders: bool = True):
    """Display first five chunks.

    When `use_expanders` is False, this renders chunk metadata without
    nested `st.expander` controls.
    """

    st.subheader("🧩 Document Chunks")

    st.success(
        f"Total Chunks : {len(chunks)}"
    )

    for chunk in chunks[:5]:
        if use_expanders:
            with st.expander(
                chunk.metadata["chunk_id"]
            ):
                st.write(
                    f"Source : {chunk.metadata['source']}"
                )

                st.write(
                    f"Page : {chunk.metadata['page']}"
                )

                st.write(
                    f"Chunk Number : {chunk.metadata['chunk_number']}"
                )

                st.write(
                    f"Characters : {chunk.metadata['characters']}"
                )

                st.write(
                    f"Words : {chunk.metadata['words']}"
                )

                st.write(
                    chunk.page_content
                )
        else:
            st.markdown(f"**Chunk {chunk.metadata['chunk_id']}**")
            st.write(
                f"Source : {chunk.metadata['source']}"
            )

            st.write(
                f"Page : {chunk.metadata['page']}"
            )

            st.write(
                f"Chunk Number : {chunk.metadata['chunk_number']}"
            )

            st.write(
                f"Characters : {chunk.metadata['characters']}"
            )

            st.write(
                f"Words : {chunk.metadata['words']}"
            )

            st.write(
                chunk.page_content
            )


def search_chunk(chunks, uploaded_file):
    """Search chunk by chunk id."""

    st.subheader("🔍 Search Chunk")

    search = st.text_input(
        "Enter Chunk ID",
        key=f"search_{uploaded_file.name}"
    )

    if not search:
        return

    for chunk in chunks:

        if chunk.metadata["chunk_id"] == search:

            st.success("Chunk Found")

            st.json(chunk.metadata)

            st.write(chunk.page_content)

            return

    st.warning("Chunk ID not found.")