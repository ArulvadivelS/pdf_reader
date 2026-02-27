"""PDF parsing and commodity section segmentation."""

from pathlib import Path
import fitz
from src.core.config import load_app_settings


def parse_pdf_into_sections(pdf_path: str | Path) -> dict[str, str]:
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("File must be a PDF")

    settings = load_app_settings()
    markers = settings.get("pdf", {}).get("commodity_headers", [])

    pdf_doc = fitz.open(path)
    try:
        document_text = "\n".join(page.get_text() for page in pdf_doc)
    finally:
        pdf_doc.close()

    return _segment_text(document_text, markers)


def _segment_text(text: str, markers: list[str]) -> dict[str, str]:
    if not text.strip():
        return {}

    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]

    marker_positions = []
    for idx, line in enumerate(lines):
        for marker in markers:
            if line.lower().startswith(marker.lower()):
                marker_positions.append((idx, marker))
                break

    if not marker_positions:
        return {markers[0] if markers else "Commentary": text.strip()}

    result = {}
    for i, (start_idx, name) in enumerate(marker_positions):
        end_idx = (
            marker_positions[i + 1][0]
            if i + 1 < len(marker_positions)
            else len(lines)
        )
        segment = "\n".join(lines[start_idx + 1 : end_idx]).strip()
        if segment:
            result[name] = segment

    return result