# Day 01: What is an LLM? (deep notes)

## Concept in my own words
An LLM predicts the next token, one at a time, based on patterns it learned in training.
It does NOT search the internet or look anything up. Web search is a tool some apps add on top.

- **Training** = reading huge amounts of text once and storing the patterns as numbers (weights).
  Like compiling: the source isn't in the binary, only the behaviour.
- **Inference** = every time I chat: predict next token → add it → repeat.

## Key terms
| Term | Meaning | Ops analogy |
|---|---|---|
| Weights | Learned patterns, frozen after training (has a cutoff date) | Compiled binary |
| Token | ~4-character chunk of text; what the model reads and what I pay for | Billing per API call |
| Context window | Everything in the current chat (my messages, replies, pasted logs); limited size | RAM |
| Hallucination | Confident but wrong answer | Untested runbook step |

## How it works
`systemctl restart ___` → the model ranks every possible next word (httpd 22%, nginx 18%...).
Add `yum install -y nginx` above it → the ranking **reshapes**: nginx 91%.
Same weights, different input → different answer. **Context is everything.**

## Why it gets things wrong
1. It must always pick a next word. Its default isn't "I don't know".
2. Missing context → falls back to the most common pattern (suggests `apt` on RHEL).
3. Knowledge cutoff → doesn't know recent releases or CVEs.

## Context window lessons
- Pasting a 5,000-line log (~125k tokens): costs more on every message, and the noise dilutes the answer.
  → `grep -iE "error|fail|exception" -B5 -A10` first. (Week 2: MCP tools will do this filtering for me.)
- Long chats: old parts get dropped or compressed (e.g. "RHEL 8" disappears).
  → Start a new chat with a 3-line handover summary.
- No memory between chats. "Memory" features = the app pasting saved notes back in.

## How I'll use AI safely as an engineer
- Give real context (OS, versions, exact error)
- Ask for verification commands, not just answers
- Never paste AI commands straight into prod: test in staging, review like a PR

## Questions I still have
- How does the model decide when to stop generating?
- Why do bigger models hallucinate less?

## Self-test (answer without looking)
1. Does an LLM search the internet? Who adds web search?
2. Why did the same prompt suggest nginx instead of httpd?
3. Two problems with pasting a 5,000-line log?
4. Why might AI suggest `apt` on a RHEL server after a long chat?

## Resources
- Andrej Karpathy, "Intro to Large Language Models" (YouTube, 1 hr), watch tonight
- Andrej Karpathy, "Deep Dive into LLMs like ChatGPT" (YouTube, 3.5 hr), over the week

