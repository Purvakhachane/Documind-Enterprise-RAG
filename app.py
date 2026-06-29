import streamlit as st
import pandas as pd
import json
import time

from document_processor.pdf_loader import save_pdf, load_pdf
from document_processor.metadata_extractor import extract_metadata
from document_processor.chunker import create_chunks

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Documind Enterprise RAG",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📄 Documind Enterprise RAG")

st.sidebar.info(
    "Week 1 - Document Processing Pipeline"
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Upload one or more PDF documents to begin processing."
)

# ---------------- TITLE ---------------- #

st.title("📄 Documind Enterprise RAG")

st.subheader(
    "Enterprise Document Processing Pipeline"
)

# ---------------- FILE UPLOADER ---------------- #

uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------- MAIN APP ---------------- #

if uploaded_files:

    st.sidebar.success("PDF Uploaded")

    for uploaded_file in uploaded_files:

        st.markdown("---")

        st.header(f"📄 {uploaded_file.name}")

        try:

            # File Size Validation

            if uploaded_file.size > 10 * 1024 * 1024:

                st.error("Maximum file size is 10 MB.")

                continue

            start_time = time.time()

            # Save PDF

            file_path = save_pdf(uploaded_file)

            # Load PDF

            documents = load_pdf(file_path)

            st.sidebar.success("PDF Parsed")

            # Metadata

            metadata = extract_metadata(documents)

            st.sidebar.success("Metadata Extracted")

            # Chunking

            chunks = create_chunks(documents)

            st.sidebar.success("Chunks Created")

            processing_time = round(
                time.time() - start_time,
                2
            )

            st.success(
                f"Processed Successfully in {processing_time} seconds"
            )

            # ---------------- DOCUMENT SUMMARY ---------------- #

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
                f"{uploaded_file.size/1024:.2f} KB"
            )

            # ---------------- PREVIEW ---------------- #

            st.subheader("📄 Document Preview")

            st.write(
                documents[0].page_content[:1000]
            )

            # ---------------- METADATA ---------------- #

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

            # ---------------- CHUNKS ---------------- #

            st.subheader("🧩 Document Chunks")

            st.success(
                f"Total Chunks : {len(chunks)}"
            )

            for chunk in chunks[:5]:

                with st.expander(
                    chunk.metadata["chunk_id"]
                ):

                    st.write(
                        f"Source : {chunk.metadata['source']}"
                    )

                    st.write(
                        f"Page : {chunk.metadata['page'] + 1}"
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

            # ---------------- SEARCH CHUNK ---------------- #

            st.subheader("🔍 Search Chunk")

            search_chunk = st.text_input(
                "Enter Chunk ID",
                key=f"search_{uploaded_file.name}"
            )

            if search_chunk:

                found = False

                for chunk in chunks:

                    if chunk.metadata["chunk_id"] == search_chunk:

                        st.success("Chunk Found")

                        st.json(chunk.metadata)

                        st.write(chunk.page_content)

                        found = True

                        break

                if not found:

                    st.warning("Chunk ID not found.")

            # ---------------- CHUNK STATISTICS ---------------- #

            st.subheader("📊 Chunk Statistics")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Total Chunks",
                len(chunks)
            )

            col2.metric(
                "Average Words",
                round(
                    sum(
                        c.metadata["words"]
                        for c in chunks
                    ) / len(chunks)
                )
            )

            col3.metric(
                "Average Characters",
                round(
                    sum(
                        c.metadata["characters"]
                        for c in chunks
                    ) / len(chunks)
                )
            )

            # ---------------- DOWNLOAD CHUNK CSV ---------------- #

            chunk_df = pd.DataFrame(
                [chunk.metadata for chunk in chunks]
            )

            st.download_button(
                "⬇ Download Chunk Metadata CSV",
                chunk_df.to_csv(index=False),
                "chunk_metadata.csv",
                "text/csv"
            )

            # ---------------- PIPELINE SUMMARY ---------------- #

            st.subheader("✅ Pipeline Status")

            st.success("✔ PDF Uploaded")

            st.success("✔ PDF Parsed")

            st.success("✔ Metadata Extracted")

            st.success("✔ Chunking Completed")

            st.success("✔ Ready for Embedding Generation")

        except Exception as e:

            st.error(
                f"Error processing {uploaded_file.name}"
            )

            st.exception(e)

else:

    st.info(
        "👆 Upload one or more PDF files to begin processing."
    )