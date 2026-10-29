# Day 01 — Setup + secrets hygiene

## 🎯 Goal
Set up a local AI + platform lab and make sure no secret can ever be committed.

## 🛠 Steps
1. Install: Python 3.11+, `uv`, Docker Desktop, `kind`, `kubectl`, `helm`, Terraform, Node 20, Ollama, `gh`, `gitleaks`.
   - Windows: use WSL2 (Ubuntu) for everything.
2. Get a Claude API key at console.anthropic.com, then **set a $10 monthly spend limit**.
3. `cp .env.example .env` and paste the key into `.env` (it is already gitignored).
4. `pip install pre-commit && pre-commit install`
5. Test the guardrail: put a fake key such as `sk-ant-api03-AAAA...` in a file and try to commit it. Gitleaks should block it.
6. `ollama pull llama3.2`
7. `python day-01-setup/verify_setup.py`

## 💡 Takeaways
- _fill in_

## ❌ What broke & how I fixed it
- _fill in_

## 🔐 Security note
API keys live only in `.env` (gitignored) and gitleaks runs before every commit. Spend limit set.
