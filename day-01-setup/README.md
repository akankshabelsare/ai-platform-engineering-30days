# Day 01: What is an LLM? + setup + secrets hygiene

## 🎯 Goal
Understand what an LLM really is, set up a local AI + platform lab, and make sure no secret can ever be committed.

📒 Deep notes: [NOTES.md](NOTES.md)

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
- An LLM doesn't search the internet. It predicts the next token from patterns stored in its weights (like a compiled binary, not a database).
- Context reshapes the prediction: `yum install -y nginx` in the prompt turns `systemctl restart ___` into `nginx`.
- Tokens (~4 chars) are what I pay for and what fills the context window (the model's RAM).
- `grep` logs before pasting them: less noise, lower cost, better answer.
- Hallucinations come from missing context or the knowledge cutoff. Treat AI output like a PR from a new teammate: review it and test it before prod.


## 🔐 Security note
API keys live only in `.env` (gitignored) and gitleaks runs before every commit. Spend limit set.
