import json
import streamlit as st

DATABASE_FILE = "database/citation_database.json"


def show_citations():
    """Display saved citations."""

    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            citations = json.load(file)
        
        st.download_button(
            "⬇ Download Citation Database",
            json.dumps(citations),
            file_name="citation_database.json",
            mime="application/json"
        )

        st.subheader("📚 Citation Database")

        st.write(f"Total Citations: {len(citations)}")

        for citation in citations[:5]:
            with st.expander(citation["chunk_id"]):
                st.write(f"Source: {citation['source']}")
                st.write(f"Page: {citation['page']}")
                st.write(f"Chunk: {citation['chunk_number']}")
                st.write(citation["text"])

    except FileNotFoundError:
        st.info("No citation database available.")