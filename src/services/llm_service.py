"""LLM client builder and invocation."""

from openai import OpenAI
from src.core.config import (
    load_app_settings,
    resolve_gemini_key,
    resolve_groq_key,
    resolve_openai_key,
)


def build_chat_client():
    settings = load_app_settings()
    provider = settings.get("llm", {}).get("provider", "openai")

    if provider == "groq":
        api_key = resolve_groq_key()
        if not api_key:
            return None
        base_url = settings["llm"]["groq"]["base_url"]
        return OpenAI(api_key=api_key, base_url=base_url)

    api_key = resolve_openai_key()
    if not api_key:
        return None

    return OpenAI(api_key=api_key)