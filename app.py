"""Main Streamlit entrypoint."""

import streamlit as st
from pathlib import Path
from src.core.config import load_app_settings
from src.services.pdf_service import parse_pdf_into_sections
from src.services.summary_service import run_batch_summaries
from src.utils.file_utils import save_uploaded_file
from src.ui.theme import inject_custom_theme


def run_app():
    settings = load_app_settings()
    ui_opts = settings.get("ui", {})

    st.set_page_config(
        page_title=ui_opts.get("page_title", "WASDE Summarizer"),
        layout="centered"
    )

    inject_custom_theme()

    # Header
    st.title("WASDE Report Summarizer")
    st.divider()

    # File upload section
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Upload the latest WASDE report (max 200MB)"
    )

    if uploaded_file:
        # Show file details
        col1, col2 = st.columns([3, 1])
        with col1:
            st.success(f"Uploaded: {uploaded_file.name}")
        with col2:
            st.info(f"{uploaded_file.size / (1024 * 1024):.1f} MB")

        # Process button
        if st.button("Run Summarization", type="primary", use_container_width=True):
            with st.spinner("Processing PDF and generating summaries..."):
                try:
                    # Save uploaded file
                    temp_path = save_uploaded_file(uploaded_file)
                    
                    # Parse PDF sections - this returns all sections found
                    sections = parse_pdf_into_sections(temp_path)
                    
                    # Generate summaries for all sections
                    summaries = run_batch_summaries(sections)
                    
                    # Clean up temp file
                    Path(temp_path).unlink()
                    
                    # Store in session state
                    st.session_state['summaries'] = summaries
                    st.session_state['sections_found'] = list(sections.keys())
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Display summaries
    if 'summaries' in st.session_state and st.session_state['summaries']:
        st.divider()
        st.subheader("Summaries")
        
        summaries = st.session_state['summaries']
        
        # Show all sections that were found in the PDF
        for section_name, summary_text in summaries.items():
            with st.expander(f"{section_name}", expanded=True):
                if summary_text:
                    st.markdown(summary_text)
                else:
                    st.caption("No summary available for this section")
        
        # Show count of sections found
        if 'sections_found' in st.session_state:
            st.caption(f"Found {len(st.session_state['sections_found'])} sections in the PDF")

if __name__ == "__main__":
    run_app()