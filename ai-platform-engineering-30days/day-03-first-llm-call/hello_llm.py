"""Day 3 — same ops question to Claude (cloud) and Ollama (local). Compare speed + answer.

Setup:
  uv sync                       # or: pip install anthropic python-dotenv requests
  ollama pull llama3.2          # free local model
  cp .env.example .env          # add ANTHROPIC_API_KEY

Run:
  python day-03-first-llm-call/hello_llm.py
"""

import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

PROMPT = """You are a senior platform engineer.
A Kubernetes pod shows status CrashLoopBackOff and the last log line is:
  KeyError: 'DATABASE_URL'
In 3 bullet points: root cause, how to confirm it with kubectl, and the fix."""


def ask_claude(prompt: str) -> str:
    import anthropic

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env — never hardcode it
    msg = client.messages.create(
        model=os.getenv("CLAUDE_MODEL", "claude-haiku-4-5"),
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    usage = msg.usage
    print(f"   tokens in/out: {usage.input_tokens}/{usage.output_tokens}")
    return msg.content[0].text


def ask_ollama(prompt: str) -> str:
    resp = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": os.getenv("OLLAMA_MODEL", "llama3.2"), "prompt": prompt, "stream": False},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["response"]


def run(name: str, fn) -> None:
    print(f"\n===== {name} =====")
    start = time.perf_counter()
    try:
        answer = fn(PROMPT)
        print(answer)
    except Exception as exc:
        print(f"   skipped: {exc}")
    print(f"   ⏱  {time.perf_counter() - start:.1f}s")


if __name__ == "__main__":
    if os.getenv("ANTHROPIC_API_KEY"):
        run("Claude (cloud)", ask_claude)
    else:
        print("ANTHROPIC_API_KEY not set — skipping Claude")
    run("Ollama (local, free, data stays on your laptop)", ask_ollama)
