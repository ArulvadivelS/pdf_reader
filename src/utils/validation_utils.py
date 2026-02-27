"""Validation utilities."""

def validate_file_size(file_handle, max_bytes: int):
    if file_handle.size > max_bytes:
        raise ValueError(f"File exceeds maximum size of {max_bytes} bytes")