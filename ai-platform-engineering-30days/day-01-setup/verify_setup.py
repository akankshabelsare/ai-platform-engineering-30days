"""Day 1 — verify my AI Platform Engineering toolbox is installed.

Run:  python day-01-setup/verify_setup.py
"""

import os
import shutil
import subprocess
from pathlib import Path

TOOLS = {
    "python3": ["python3", "--version"],
    "uv": ["uv", "--version"],
    "docker": ["docker", "--version"],
    "kind": ["kind", "version"],
    "kubectl": ["kubectl", "version", "--client"],
    "helm": ["helm", "version", "--short"],
    "terraform": ["terraform", "version"],
    "node": ["node", "--version"],
    "ollama": ["ollama", "--version"],
    "gitleaks": ["gitleaks", "version"],
    "gh": ["gh", "--version"],
}


def check_tool(name: str, cmd: list[str]) -> tuple[bool, str]:
    if shutil.which(cmd[0]) is None:
        return False, "not installed"
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        first_line = (out.stdout or out.stderr).strip().splitlines()[0]
        return True, first_line[:60]
    except Exception as exc:  # tool exists but errored (e.g. docker daemon down)
        return False, f"error: {exc}"


def check_secrets_hygiene() -> list[str]:
    """Security checks: the API key must come from .env and .env must be gitignored."""
    issues = []
    root = Path(__file__).resolve().parents[1]
    gitignore = (root / ".gitignore").read_text() if (root / ".gitignore").exists() else ""
    if ".env" not in gitignore.split():
        issues.append(".env is NOT in .gitignore")
    if not (root / ".env").exists():
        issues.append(".env missing — copy .env.example to .env and add your key")
    if not (root / ".pre-commit-config.yaml").exists():
        issues.append("no pre-commit config (gitleaks)")
    return issues


def main() -> None:
    print("🔧 Toolbox check\n")
    missing = 0
    for name, cmd in TOOLS.items():
        ok, info = check_tool(name, cmd)
        missing += not ok
        print(f"  {'✅' if ok else '❌'} {name:<10} {info}")

    print("\n🔐 Secrets hygiene\n")
    issues = check_secrets_hygiene()
    for issue in issues:
        print(f"  ⚠️  {issue}")
    if not issues:
        print("  ✅ .env gitignored, present, gitleaks hook configured")

    key_set = bool(os.getenv("ANTHROPIC_API_KEY"))
    print(f"\n  {'✅' if key_set else 'ℹ️ '} ANTHROPIC_API_KEY loaded in this shell: {key_set}")
    print(f"\n{len(TOOLS) - missing}/{len(TOOLS)} tools ready.")


if __name__ == "__main__":
    main()
