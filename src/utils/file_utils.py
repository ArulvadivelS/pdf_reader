"""Temporary file handling utilities."""

import tempfile
from pathlib import Path


def save_uploaded_file(file_handle) -> Path:
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(file_handle.read())
        return Path(tmp.name)