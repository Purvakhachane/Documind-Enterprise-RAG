import time

import streamlit as st

from ui.registry import show_registry

from ui.citations import show_citations

from ingestion.pipeline import DocumentPipeline

from ui.sidebar import (
    setup_sidebar,
    show_processing_status
    
)

from ui.summary import show_summary
from ui.metadata import show_metadata
from ui.chunks import (
    show_chunks,
    search_chunk
)
from ui.statistics import show_statistics
from ui.downloads import (
    download_metadata,
    download_chunk_metadata
)

# ---------------- PAGE CONFIG ---------------- #
show_registry()
show_citations()
st.set_page_config(
    page_title="Documind Enterprise RAG",
    layout="wide"
)

setup_sidebar()

st.title("📄 Documind Enterprise RAG")

st.subheader(
    "Enterprise Document Processing Pipeline"
)

uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        st.markdown("---")

        st.header(f"📄 {uploaded_file.name}")

        try:

            if uploaded_file.size > 10 * 1024 * 1024:

                st.error(
                    "Maximum file size is 10 MB."
                )

                continue

            start_time = time.time()

            pipeline = DocumentPipeline()

            result = pipeline.process(uploaded_file)

            processing_time = round(
                time.time() - start_time,
                2
            )

            show_processing_status()

            st.success(
                f"Processed Successfully in {processing_time} seconds"
            )

            documents = result["documents"]
            metadata = result["metadata"]
            chunks = result["chunks"]
            pinecone = result["pinecone"]

            show_summary(result)

            show_metadata(metadata)

            download_metadata(metadata)

            show_chunks(chunks)

            search_chunk(
                chunks,
                uploaded_file
            )

            show_statistics(chunks)

            st.subheader("🌲 Pinecone Status")

            st.success(
                result["index_status"]
            )

            st.write(
                "Available Indexes:"
            )

            st.write(
                pinecone.list_indexes()
            )

            download_chunk_metadata(
                chunks
            )

            st.subheader(
                "✅ Pipeline Status"
            )

            st.success("✔ PDF Uploaded")
            st.success("✔ PDF Parsed")
            st.success("✔ Metadata Extracted")
            st.success("✔ Chunking Completed")
            st.success("✔ Pinecone Connected")
            st.success("✔ Index Ready")

        except Exception as error:

            st.error(
                f"Error processing {uploaded_file.name}"
            )

            st.exception(error)

else:

    st.info(
        "👆 Upload one or more PDF files to begin processing."
    )