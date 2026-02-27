"""Load application settings and resolve environment keys."""

import os
from pathlib import Path
import yaml
from dotenv import load_dotenv

load_dotenv()

_SETTINGS_FILE = Path(__file__).resolve().parent.parent / "config.yaml"
_settings_cache = None


def load_app_settings() -> dict:
    global _settings_cache

    if _settings_cache is not None:
        return _settings_cache

    if not _SETTINGS_FILE.exists():
        _settings_cache = _builtin_settings()
        return _settings_cache

    with open(_SETTINGS_FILE, "r", encoding="utf-8") as fh:
        _settings_cache = yaml.safe_load(fh) or _builtin_settings()

    return _settings_cache


def _builtin_settings() -> dict:
    return {
        "llm": {
            "provider": "groq",
            "groq": {
                "base_url": "https://api.groq.com/openai/v1",
                "model": "llama-3.1-8b-instant",
            },
            "gemini": {"model": "gemini-1.5-flash"},
        },
        "openai": {
            "model": "gpt-4o-mini",
            "max_tokens": 2048,
            "temperature": 0.3,
            "max_commentary_chars": 12000,
        },
        "pdf": {
            "commodity_headers": [
                "Wheat", "Coarse Grains", "Rice",
                "Oilseeds", "Cotton", "Sugar",
                "Livestock", "Poultry", "Dairy",
            ]
        },
        "ui": {
            "page_title": "WASDE Report Summarizer",
            "max_file_size_mb": 50,
        },
    }


def resolve_openai_key() -> str:
    return os.getenv("OPENAI_API_KEY", "").strip()


def resolve_groq_key() -> str:
    return os.getenv("GROQ_API_KEY", "").strip()


def resolve_gemini_key() -> str:
    return (
        os.getenv("GEMINI_API_KEY", "").strip()
        or os.getenv("GOOGLE_API_KEY", "").strip()
    )