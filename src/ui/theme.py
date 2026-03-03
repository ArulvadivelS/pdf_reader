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
            background-color: #064E3B !important; /* Dark Green */
            border: 1px solid #10B981 !important;
            border-left: 5px solid #10B981 !important;
            color: #FFFFFF !important;
            border-radius: 8px;
        }
        
        div[data-testid="stSuccess"] p {
            color: #FFFFFF !important;
            font-weight: 500;
        }
        
        /* Info message */
        div[data-testid="stInfo"] {
            background-color: #1E3A8A !important; /* Dark Blue */
            border: 1px solid #3B82F6 !important;
            border-left: 5px solid #3B82F6 !important;
            color: #FFFFFF !important;
            border-radius: 8px;
        }
        
        div[data-testid="stInfo"] p {
            color: #FFFFFF !important;
            font-weight: 500;
        }
        
        /* Error message */
        div[data-testid="stError"] {
            background-color: #450A0A !important; /* Dark Red */
            border: 1px solid #EF4444 !important;
            border-left: 5px solid #EF4444 !important;
            color: #FFFFFF !important;
            border-radius: 8px;
        }
        
        div[data-testid="stError"] p {
            color: #FFFFFF !important;
            font-weight: 500;
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
        
        /* Title */
        h1 {
            font-size: 2rem;
            font-weight: 500;
            color: #FFFFFF !important;
            margin-bottom: 0.25rem;
        }

        /* Subheader */
        h3 {
            font-size: 1.2rem;
            font-weight: 500;
            color: #FFFFFF !important;
            margin: 1rem 0;
        }

        /* Markdown text */
        .stMarkdown {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #FFFFFF !important;
        }

        /* Labels and Captions */
        label, .stCaption, p {
            color: #FFFFFF !important;
        }
        
        /* File uploader drag & drop area */
        .stFileUploader [data-testid="stFileUploaderDropzone"] {
            background-color: #111827 !important;
            border: 2px dashed #4B5563 !important;
            color: #FFFFFF !important;
            border-radius: 12px;
        }
        
        .stFileUploader [data-testid="stFileUploaderDropzone"]:hover {
            border-color: #3B82F6 !important;
            background-color: #1F2937 !important;
        }
        
        /* File uploader text/button */
        .stFileUploader label, .stFileUploader p, .stFileUploader span {
            color: #FFFFFF !important;
        }
        
        /* Selected file name visibility */
        [data-testid="stFileUploaderFileName"] {
            color: #FFFFFF !important;
        }

        /* File uploader icon and placeholder */
        .stFileUploader svg {
            fill: #FFFFFF !important;
        }
        
        .stFileUploader button {
            background-color: #3B82F6 !important;
            color: white !important;
            border-radius: 6px !important;
        }

        /* Placeholder text specifically */
        .stFileUploader [data-testid="stFileUploaderDropzone"] div div {
            color: #E5E7EB !important;
        }
        
        /* Column text */
        .stColumn {
            color: #FFFFFF;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-top-color: #FFFFFF !important;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
            background-color: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent !important;
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
            color: #9CA3AF !important;
            font-weight: 400;
        }

        .stTabs [aria-selected="true"] {
            background-color: #1A1E26 !important;
            color: #FFFFFF !important;
            border-bottom: 2px solid #3B82F6 !important;
        }

        /* Text area and input enhancement */
        .stTextInput input, .stTextArea textarea {
            background-color: #1A1E26 !important;
            color: #FFFFFF !important;
            border: 1px solid #3B82F6 !important; /* Blue border for visibility */
            font-size: 1rem !important;
        }
        
        /* Search results styling */
        .search-results {
            background-color: #1A1E26;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #3B82F6;
            margin-top: 1rem;
            color: #FFFFFF;
        }
    </style>
    """, unsafe_allow_html=True)