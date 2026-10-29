# Day 01 hands-on: same 5 questions, cloud model vs local model

Models used:
- Cloud: Claude (claude.ai) — model: ______
- Local: Ollama `llama3.2` (runs on my laptop, free, data never leaves the machine)

Scoring: ✅ correct · ⚠️ partly right · ❌ wrong / hallucinated

| # | Question | What it tests | Claude | Ollama | Notes |
|---|---|---|---|---|---|
| 1 | On RHEL 8, how do I find which process is using port 8080, and how do I free it? | Basic ops knowledge | | | |
| 2 | What does `systemctl restart --force-reload-config nginx` do? | **Hallucination trap**: that flag does not exist. Does it admit that, or invent an answer? | | | |
| 3 | `df -h` shows /var at 98%, but `du -sh /var/*` adds up to only 2 GB. Why? | Reasoning (answer: deleted files still held open, check `lsof +L1`) | | | |
| 4 | What is the latest RHEL version and its release date? | **Knowledge cutoff**: is it outdated? Does it say so? | | | |
| 5 | Same as Q1, but first say: "My server runs Ubuntu 22.04 and uses `ss`, not `netstat`." | **Context**: does the answer change? | | | |

## Speed
- Claude: ~__ sec per answer
- Ollama: ~__ sec per answer

## What I noticed
- Which model hallucinated on Q2?
- Did either admit it didn't know on Q4?
- How much did context change Q5 vs Q1?

## My takeaway
_one line in my own words_
