"""Ollama AI service for email generation."""

import os
from openai import OpenAI

BASE_URL = os.environ.get("OPENAI_API_BASE", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "ollama/glm-5.1:cloud")
# Strip "ollama/" prefix if present for the API call
API_MODEL = MODEL_NAME.replace("ollama/", "") if MODEL_NAME.startswith("ollama/") else MODEL_NAME
API_KEY = os.environ.get("OPENAI_API_KEY", "ollama")

_client = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    return _client


def check_ollama_available() -> bool:
    """Check if Ollama is reachable."""
    try:
        client = _get_client()
        client.models.list()
        return True
    except Exception:
        return False


def generate_email(prompt: str) -> str:
    """Generate an email using the Ollama model."""
    client = _get_client()
    response = client.chat.completions.create(
        model=API_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800,
    )
    return response.choices[0].message.content.strip()


def regenerate_email(prompt: str, tweak: str = "") -> str:
    """Regenerate an email with optional tweak instructions."""
    if tweak:
        prompt = f"{prompt}\n\nADDITIONAL INSTRUCTIONS: {tweak}"
    return generate_email(prompt)