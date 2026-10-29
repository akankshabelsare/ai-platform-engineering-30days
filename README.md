# 🤖🔐 30 Days of AI for Platform Engineering

Building **OpsPilot** in public: a secure AI agent that troubleshoots Kubernetes, reviews Terraform plans and explains Jenkins failures, using **MCP**, **Claude** and **local models (Ollama)**, with security built in from Day 1.

> Learn → Build → Document → Share. One hour a day, 30 days, everything runs locally.

## Why
Platform engineers are being asked to "add AI". Few people show how to do it **safely**: least privilege, no secret leakage, prompt-injection defense, human approval for writes. This repo is my hands-on log.

## Stack
`Python` · `MCP (FastMCP)` · `Claude API` · `Ollama` · `Kubernetes (kind)` · `Terraform` · `Jenkins` · `GitHub Actions` · `gitleaks` · `trivy`

## Progress

| Day | Topic | Code | Post |
|---|---|---|---|
| 1 | What is an LLM? + setup + secrets hygiene | [day-01-setup](day-01-setup) | |
| 2 | Python basics for DevOps | | |
| 3 | First LLM call: Claude vs Ollama | | |
| 4 | Prompting + spotting hallucinations: Jenkins log explainer | | |
| 5 | Kubernetes 101 on kind | | |
| 6 | Tool use: read-only `get_pods` | | |
| 7 | Week 1 recap: LLM diagnoses ImagePullBackOff | | |
| 8 | MCP concepts | | |
| 9 | First MCP server (Docker, read-only) | | |
| 10 | Connect MCP to Claude Desktop | | |
| 11 | Kubernetes MCP server | | |
| 12 | Terraform plan reviewer MCP | | |
| 13 | Jenkins MCP | | |
| 14 | Build vs reuse | | |
| 15 | Agent loop from scratch | | |
| 16 | CrashLoopBackOff agent | | |
| 17 | Human-in-the-loop approvals | | |
| 18 | RAG over runbooks | | |
| 19 | Incident triage agent | | |
| 20 | k8sgpt and kagent comparison | | |
| 21 | Eval set + accuracy | | |
| 22 | Threat model (OWASP LLM Top 10) | | |
| 23 | Least-privilege RBAC | | |
| 24 | Prompt injection: attack + defense | | |
| 25 | Secret redaction | | |
| 26 | Guardrails + audit logs | | |
| 27 | Model comparison | | |
| 28 | Secure CI/CD | | |
| 29 | OpsPilot Helm + demo | | |
| 30 | Capstone retro | | |

## Quick start
```bash
cp .env.example .env            # add your ANTHROPIC_API_KEY (never commit .env)
pip install pre-commit && pre-commit install   # gitleaks blocks secret commits
uv sync                          # install Python deps
python day-01-setup/verify_setup.py
```

## Security principles (non-negotiable)
1. Agents get **read-only** access by default; writes need human approval.
2. Secrets never reach the LLM or git.
3. Tool output is **data, not instructions**.
4. Every tool call is audit-logged.

## Connect
Follow along on LinkedIn: `<your LinkedIn URL>`
