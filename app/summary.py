"""Writes the call summary the adviser checks before it goes on the client's file."""
import anthropic

MODEL = "claude-sonnet-4-5-20250929"
GERMAN = "mistral-large-2512"  # calls held in German


def summarise(transcript: str) -> str:
    client = anthropic.Anthropic()
    reply = client.messages.create(model=MODEL, max_tokens=800,
                                   messages=[{"role": "user", "content": "Summarise this client call:\n" + transcript}])
    return reply.content[0].text
