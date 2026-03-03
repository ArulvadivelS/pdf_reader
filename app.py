"""Main Streamlit entrypoint."""

import streamlit as st
from pathlib import Path
from src.core.config import load_app_settings
from src.services.pdf_service import parse_pdf_into_sections
from src.services.summary_service import run_batch_summaries
from src.utils.file_utils import save_uploaded_file
from src.services.search_service import search_content
from src.ui.theme import inject_custom_theme


def run_app():
    settings = load_app_settings()
    ui_opts = settings.get("ui", {})

    st.set_page_config(
        page_title=ui_opts.get("page_title", "WASDE Summarizer"),
        layout="centered"
    )

    inject_custom_theme()

    st.title("WASDE Report Summarizer")
    st.divider()

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Upload the latest WASDE report (max 200MB)"
    )

    if uploaded_file:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.success(f"Uploaded: {uploaded_file.name}")
        with col2:
            st.info(f"{uploaded_file.size / (1024 * 1024):.1f} MB")

        if st.button("Run Summarization", type="primary", use_container_width=True):
            with st.spinner("Processing PDF and generating summaries..."):
                try:
                    temp_path = save_uploaded_file(uploaded_file)
                    
                    sections = parse_pdf_into_sections(temp_path)
                    
                    summaries = run_batch_summaries(sections)
                    
                    Path(temp_path).unlink()
                    
                    st.session_state['summaries'] = summaries
                    st.session_state['sections'] = sections # Store raw text for search
                    st.session_state['sections_found'] = list(sections.keys())
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    if 'summaries' in st.session_state and st.session_state['summaries']:
        tab1, tab2 = st.tabs(["📋 Summaries", "🔍 Search in Report"])

        with tab1:
            st.subheader("Section Summaries")
            summaries = st.session_state['summaries']
            for section_name, summary_text in summaries.items():
                with st.expander(f"{section_name}", expanded=False):
                    if summary_text:
                        st.markdown(summary_text)
                    else:
                        st.caption("No summary available for this section")
            
            if 'sections_found' in st.session_state:
                st.caption(f"Found {len(st.session_state['sections_found'])} sections in the PDF")

        with tab2:
            st.subheader("Semantic Search")
            st.info("Search for specific information across all sections of the report.")
            
            query = st.text_input("Enter your search query or paragraph:", placeholder="e.g., What is the outlook for Brazil coarse grains?")
            
            if query:
                with st.spinner("Searching through report content..."):
                    results = search_content(query, st.session_state['sections'])
                    st.markdown("### Search Results")
                    st.markdown(f'<div class="search-results">{results}</div>', unsafe_allow_html=True)
                    st.divider()

    st.divider()

if __name__ == "__main__":
    run_app()
