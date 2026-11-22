"""Turns a recorded client call into text."""
from openai import OpenAI

MODEL = "gpt-4o-transcribe"


def transcribe(path: str) -> str:
    client = OpenAI()
    with open(path, "rb") as audio:
        return client.audio.transcriptions.create(model=MODEL, file=audio).text
