"""Business logic for generating summaries."""

from src.services.llm_service import build_chat_client
from src.core.config import load_app_settings


def generate_section_summary(section_name: str, section_text: str) -> str:
    settings = load_app_settings()
    provider = settings.get("llm", {}).get("provider", "openai")
    openai_opts = settings.get("openai", {})

    content = (section_text or "").strip()
    if len(content) < 50:
        return "(No commentary extracted for this section.)"

    instruction = (
        "You are an analyst summarizing USDA WASDE report commentary. "
        "Provide a concise 2–5 sentence summary."
    )

    user_prompt = f"Summarize commentary for {section_name}:\n\n{content}"

    client = build_chat_client()
    if client is None:
        return "Error: LLM client not configured."

    if provider == "groq":
        model_id = settings["llm"]["groq"].get("model", "llama-3.1-8b-instant")
    elif provider == "openai":
        model_id = settings["openai"].get("model", "gpt-4.1")
    elif provider == "gemini":
        model_id = settings["llm"]["gemini"].get("model", "gemini-1.5-flash")
    else:
        return f"Unsupported provider: {provider}"
    
    try:
        resp = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=openai_opts.get("max_tokens", 2048),
            temperature=openai_opts.get("temperature", 0.3),
        )
        return resp.choices[0].message.content.strip()
    except Exception as exc:
        return f"LLM Error: {exc}"


def run_batch_summaries(sections: dict[str, str]) -> dict[str, str]:
    return {
        name: generate_section_summary(name, text)
        for name, text in sections.items()
    }