🚦 Change Risk Agent

An autonomous GitHub Actions–based Change Risk Agent that analyzes pull requests for deployment risk using deterministic heuristics and LLM-based semantic reasoning, posts explainable risk assessments directly on PRs, and blocks high-risk changes from being merged.

📌 Problem Statement

Modern CI/CD pipelines primarily answer:

Does the code build?
Do tests pass?

They do not answer:

Is this change dangerous?
Does it touch too many critical areas?
Are config and logic changing together?
Is this risky even if tests pass (or are missing)?
As a result, many production issues occur despite successful CI runs.

💡 Solution

Change Risk Agent introduces an additional safety layer at the Pull Request (PR) stage:

Automatically analyzes every PR
Determines how risky the change is
Explains why it is risky
Posts feedback directly on the PR
Blocks the merge if the risk is HIGH
This prevents risky changes before they reach production.

🧠 How the Agent Works

The agent follows an autonomous decision loop:

1️⃣ Observe (PR Awareness)

Triggered automatically on every pull request:
Reads PR metadata (author, branches, size)
Fetches changed files via GitHub API

2️⃣ Analyze (Deterministic Risk Scoring)

Applies transparent engineering rules such as:
Multiple code files modified
No test files updated
Configuration files changed
Large number of lines added

Outputs:

Risk Score (0–100)
Risk Level (LOW / MEDIUM / HIGH)
Explainable reasons

3️⃣ Reason (LLM Semantic Analysis)

Uses an LLM only where rules fall short, to detect:

Cross-file coupling
CI/CD workflow risks
Dependency compatibility issues
Potential runtime or integration problems
Architectural smells
The LLM augments, not replaces, deterministic logic.

4️⃣ Act (Enforcement)

Posts a detailed risk report directly on the PR
Fails the CI job when risk is HIGH
Branch protection rules block the merge automatically
This makes risk control enforced, not advisory.

🧩 Architecture Overview

Pull Request
     ↓
GitHub Action Trigger
     ↓
Change Extraction (GitHub API)
     ↓
Deterministic Risk Engine
     ↓
LLM Semantic Reasoning
     ↓
PR Comment + Risk Report
     ↓
CI Pass / Fail (Merge Allowed or Blocked)

🛠️ Tech Stack

Python
GitHub Actions
GitHub REST API
OpenAI API
Requests (HTTP client)

🔐 Security & Best Practices

API keys stored securely using GitHub Secrets
No secrets hardcoded in code or workflows
Uses scoped GitHub Action permissions
CI runner remains stateless and reproducible

🚫 Merge Blocking Logic

If:

Risk Level == HIGH


Then:

GitHub Action exits with non-zero status
Required status check fails
Branch protection prevents merge into main
This enforces automated risk governance.

📈 Why This Matters in Industry

This project mirrors internal tools used by:
Platform Engineering teams
DevOps & SRE teams
Cloud & CI/CD modernization teams
It addresses real-world problems such as:
Preventing production outages
Enforcing quality at scale
Reducing manual review fatigue
Catching semantic risks tests miss

📄 Example PR Comment Output
⚠️ Change Risk Assessment

Risk Score: 100
Risk Level: HIGH

Deterministic Risk Signals:
- Multiple code files modified
- No test files updated
- Configuration files modified
- Large number of lines added

LLM Semantic Risk Insights:
- CI/CD workflow changes may affect deployments
- Cross-file coupling increases integration risk
- Missing tests raise regression probability

🚀 Future Enhancements 

Edit existing PR comment instead of posting new ones
Historical risk tracking
Risk trend dashboards
Learning-based rule tuning
Support for monorepos and microservices

🏁 Conclusion

Change Risk Agent demonstrates how AI can be used responsibly in software engineering — not as a replacement for logic, but as a reasoning layer that strengthens decision-making.

It transforms CI/CD from “does it pass?” to “is it safe?”.