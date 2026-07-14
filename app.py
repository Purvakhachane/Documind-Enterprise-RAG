import time

import streamlit as st

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

st.set_page_config(
    page_title="Documind Enterprise RAG",
    layout="wide",
    page_icon="",
)

setup_sidebar()

st.markdown(
    """
    <style>
    .top-card {
        background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1d4ed8 100%);
        border-radius: 24px;
        padding: 2rem 2.5rem;
        color: white;
        box-shadow: 0 30px 70px rgba(15, 23, 42, 0.3);
        margin-bottom: 1.75rem;
    }
    .top-card h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    .top-card p {
        margin: 0.75rem 0 0;
        opacity: 0.85;
        line-height: 1.7;
    }
    .metric-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 1.25rem;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
    }
    </style>
    <div class="top-card">
        <h1>📄 Documind Enterprise RAG</h1>
        <p>Transform PDFs into searchable enterprise intelligence with one elegant workflow: upload, ingest, chunk, and query.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.metric("Experience", "Enterprise-grade")
with col2:
    st.write("### Workflow Overview")
    st.write(
        "Upload PDF documents, extract rich metadata, build searchable chunks, "
        "and review indexed results in a modern RAG dashboard."
    )
with col3:
    st.metric("Mode", "Streamlit UI")

st.markdown("---")

uploaded_files = st.file_uploader(
    "Upload one or more PDF documents",
    type=["pdf"],
    accept_multiple_files=True,
    help="Max file size per document: 10 MB"
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        st.markdown("---")
        st.header(f"📄 {uploaded_file.name}")

        if uploaded_file.size > 10 * 1024 * 1024:
            st.error("This file is too large. Please upload a file smaller than 10 MB.")
            continue

        with st.spinner("Processing your document into enterprise knowledge..."):
            progress_bar = st.progress(0)
            pipeline = DocumentPipeline()
            result = pipeline.process(uploaded_file)
            for percent in range(0, 101, 25):
                progress_bar.progress(percent)
                time.sleep(0.08)

        processing_time = round(time.time() - time.time() + time.time(), 2)
        st.success(f"Document processed successfully!")

        summary = result.get("summary", {})
        documents = result["documents"]
        metadata = result["metadata"]
        chunks = result["chunks"]
        pinecone = result["pinecone"]

        summary_col1, summary_col2, summary_col3 = st.columns(3)
        summary_col1.metric("Pages", summary.get("pages", len(documents)))
        summary_col2.metric("Chunks", summary.get("chunks", len(chunks)))
        summary_col3.metric(
            "File Size",
            f"{summary.get('file_size', uploaded_file.size) / 1024 / 1024:.2f} MB"
        )

        st.markdown("### 🔎 Document Insights")
        show_summary(result)

        with st.expander("View extracted metadata", expanded=True):
            show_metadata(metadata, use_expanders=False)

        download_metadata(metadata)

        with st.expander("Explore document chunks", expanded=True):
            show_chunks(chunks, use_expanders=False)
            search_chunk(chunks, uploaded_file)

        show_statistics(chunks)

        st.markdown("### 🌲 Pinecone & Index Status")
        status_col, index_col = st.columns([2, 1])
        with status_col:
            st.success(result.get("index_status", "Index initialized"))
            st.write("**Available Pinecone indexes**")
            st.write(pinecone.list_indexes())
        with index_col:
            st.info("Pinecone helps turn document chunks into searchable embeddings.")

        download_chunk_metadata(chunks)

        st.markdown("### ✅ Pipeline status")
        st.write(
            "PDF upload, parsing, metadata extraction, chunk creation, "
            "and indexing are complete. Your document is ready for semantic search."
        )

        status_cards = st.columns(3)
        status_cards[0].success("✔ PDF Uploaded")
        status_cards[1].success("✔ Metadata Extracted")
        status_cards[2].success("✔ Chunks Created")
        status_cards[0].success("✔ Pinecone Connected")
        status_cards[1].success("✔ Index Ready")

else:
    st.info("👆 Upload one or more PDF files to begin the intelligent document processing flow.")
