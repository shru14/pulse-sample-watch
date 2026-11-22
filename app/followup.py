"""Drafts the follow-up email; the adviser edits and sends it."""
from openai import OpenAI

MODEL = "gpt-5-mini"


def draft(summary: str) -> str:
    client = OpenAI()
    reply = client.responses.create(model=MODEL, input="Draft a short follow-up email from this call summary:\n" + summary)
    return reply.output_text
