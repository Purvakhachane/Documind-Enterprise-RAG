import json
import os

import pandas as pd
import streamlit as st


REGISTRY_FILE = "document_registry.json"


def show_registry():
    """
    Display processed documents.
    """

    if not os.path.exists(REGISTRY_FILE):
        return

    with open(REGISTRY_FILE, "r") as file:
        registry = json.load(file)

    st.subheader("📚 Processed Documents")

    st.dataframe(
        pd.DataFrame(registry),
        use_container_width=True
    )