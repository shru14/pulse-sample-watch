"""Finds earlier calls with the same client, for the adviser's prep."""
from google import genai

EMBED = "gemini-embedding-001"


def embed(text: str) -> list[float]:
    client = genai.Client()
    return client.models.embed_content(model=EMBED, contents=text).embeddings[0].values
