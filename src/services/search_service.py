"""Service for searching within extracted PDF content."""

from src.services.llm_service import build_chat_client
from src.core.config import load_app_settings

def search_content(query: str, sections: dict[str, str]) -> str:
    """
    Search for a query within the extracted sections using an LLM.
    Returns a formatted string with relevant findings.
    """
    if not query or not sections:
        return "Please provide a search query and ensure the report is processed."

    settings = load_app_settings()
    provider = settings.get("llm", {}).get("provider", "openai")
    
    
    if provider == "groq":
        model_id = settings["llm"]["groq"].get("model", "llama-3.1-8b-instant")
    elif provider == "openai":
        model_id = settings["openai"].get("model", "gpt-4o-mini")
    elif provider == "gemini":
        model_id = settings["llm"]["gemini"].get("model", "gemini-1.5-flash")
    else:
        return f"Unsupported provider: {provider}"

    context_parts = []
    for name, text in sections.items():
        context_parts.append(f"### Section: {name}\n{text[:2000]}") # Take first 2k chars per section
    
    context = "\n\n".join(context_parts)
    max_chars = settings.get("openai", {}).get("max_commentary_chars", 12000)
    if len(context) > max_chars:
        context = context[:max_chars] + "... [truncated]"

    instruction = (
        "You are an expert Document Retriever for USDA WASDE reports. "
        "Your task is to find and extract the specific information requested by the user from the provided report context. "
        "Guidelines:\n"
        "1. Be thorough—if the answer is in the text, extract it.\n"
        "2. Provide a concise answer based ONLY on the provided context.\n"
        "3. Always cite the section name where you found the information.\n"
        "4. If no information is found that even remotely matches the query, say 'No relevant information found in this report.'\n"
        "5. Be flexible with terminology (e.g., 'soybeans' and 'soybean' are the same)."
    )

    user_prompt = f"User Query: {query}\n\n=== REPORT CONTEXT ===\n{context}\n\n=== END OF CONTEXT ==="

    client = build_chat_client()
    if client is None:
        return "Error: LLM client not configured."

    try:
        resp = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2, 
        )
        return resp.choices[0].message.content.strip()
    except Exception as exc:
        return f"Search Error: {exc}"
