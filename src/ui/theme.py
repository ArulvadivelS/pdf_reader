import streamlit as st

def inject_custom_theme():
    st.markdown("""
    <style>
        /* Dark theme styling */
        .stApp {
            background-color: #0E1117;
        }
        
        /* Remove header */
        header[data-testid="stHeader"] {
            display: none;
        }
        
        /* Main container */
        .block-container {
            max-width: 800px;
            padding: 2rem 1rem;
        }
        
        /* Title */
        h1 {
            font-size: 2rem;
            font-weight: 500;
            color: #FFFFFF;
            margin-bottom: 0.25rem;
        }
        
        /* Caption */
        .stCaption {
            color: #9CA3AF;
            font-size: 0.9rem;
        }
        
        /* Divider */
        hr {
            margin: 1.5rem 0;
            border: none;
            border-top: 1px solid #2D3748;
        }
        
        /* File uploader */
        .stFileUploader {
            padding: 0.5rem 0;
        }
        
        /* File uploader text */
        .stFileUploader > div > div {
            color: #FFFFFF !important;
        }
        
        /* Uploaded file info */
        .stAlert {
            background-color: #1A1E26 !important;
            color: #FFFFFF !important;
            border: 1px solid #2D3748 !important;
        }
        
        /* Success message */
        div[data-testid="stSuccess"] {
            background-color: #1A1E26 !important;
            border-left: 3px solid #10B981 !important;
            color: #FFFFFF !important;
        }
        
        div[data-testid="stSuccess"] p {
            color: #FFFFFF !important;
        }
        
        /* Info message */
        div[data-testid="stInfo"] {
            background-color: #1A1E26 !important;
            border-left: 3px solid #6B7280 !important;
            color: #FFFFFF !important;
        }
        
        div[data-testid="stInfo"] p {
            color: #FFFFFF !important;
        }
        
        /* Error message */
        div[data-testid="stError"] {
            background-color: #2D1A1A !important;
            border-left: 3px solid #EF4444 !important;
            color: #FFFFFF !important;
        }
        
        div[data-testid="stError"] p {
            color: #FFFFFF !important;
        }
        
        /* Button */
        .stButton > button {
            background-color: #2D3748;
            color: #FFFFFF;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-weight: 400;
            border: none;
            width: 100%;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }
        
        .stButton > button:hover {
            background-color: #4A5568;
            border: none;
            color: #FFFFFF;
            cursor: pointer;
        }
        
        /* Expander */
        div[data-testid="stExpander"] {
            border: 1px solid #2D3748;
            border-radius: 4px;
            margin-bottom: 0.75rem;
            background-color: #0E1117;
        }
        
        div[data-testid="stExpander"] summary {
            font-weight: 500;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            color: #FFFFFF;
            background-color: #1A1E26;
            border-radius: 4px 4px 0 0;
        }
        
        div[data-testid="stExpander"] summary:hover {
            background-color: #2D3748;
            cursor: pointer;
        }
        
        div[data-testid="stExpander"] .streamlit-expanderContent {
            padding: 1rem;
            border-top: 1px solid #2D3748;
            background-color: #0E1117;
            border-radius: 0 0 4px 4px;
            color: #E5E7EB;
        }
        
        /* Subheader */
        h3 {
            font-size: 1.2rem;
            font-weight: 500;
            color: #FFFFFF;
            margin: 1rem 0;
        }
        
        /* Caption text for section count */
        .stCaption {
            color: #9CA3AF;
            font-size: 0.85rem;
            margin-top: 1rem;
        }
        
        /* Hide streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Markdown text */
        .stMarkdown {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #E5E7EB;
        }
        
        /* File uploader drag & drop area */
        .stFileUploader > div {
            background-color: #1A1E26 !important;
            border-color: #2D3748 !important;
            color: #FFFFFF !important;
        }
        
        .stFileUploader > div:hover {
            border-color: #4A5568 !important;
            background-color: #2D3748 !important;
        }
        
        /* File uploader text */
        .stFileUploader label {
            color: #FFFFFF !important;
        }
        
        /* Column text */
        .stColumn {
            color: #FFFFFF;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-top-color: #FFFFFF !important;
        }
        
        /* Select box if any */
        .stSelectbox label {
            color: #FFFFFF !important;
        }
        
        /* Radio buttons if any */
        .stRadio label {
            color: #FFFFFF !important;
        }
        
        /* Text input if any */
        .stTextInput label {
            color: #FFFFFF !important;
        }
        
        .stTextInput input {
            background-color: #1A1E26 !important;
            color: #FFFFFF !important;
            border-color: #2D3748 !important;
        }
        
        .stTextInput input:focus {
            border-color: #4A5568 !important;
        }
    </style>
    """, unsafe_allow_html=True)