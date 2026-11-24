# AI use — frontierforge

AI-assisted development is permitted under the workspace policy (`../_governance/POLICY.md`). Every change must record the tools used, the human verification performed, and the data used. A human is the author of record and reviews all AI output before merge and release.

Risk tier and release gate: `../_governance/RISK-REGISTER.md`. Legal screening: `../_governance/AI-REGULATIONS.md`. This is engineering screening, not legal advice.

## Disclosure

Complete before shipping a chatbot, generative feature, or synthetic content: users must be told they are interacting with AI and generated output must be labelled. EU AI Act Article 50 duties apply since 2 August 2026.

## Human oversight

A named human reviews AI output before merge. Tier A deployments additionally require an AI impact assessment, model card, threat model or safety case, and written release sign-off.

## Data

Follow `../_governance/DATA-MAP.md`. Never send secrets, personal data, health recordings, or restricted datasets to models, hosted APIs, web tools, issues, or shared sessions.

## Change record — V2 (2.0.0)

| Field | Record |
| --- | --- |
| Tools/models used | `opencode` with the workspace build agent; local Python 3.12.3 and Docker 29.1.3 only |
| What was delegated | Added four V2 engine tests, per-use-case Dockerfiles and runner, V2 docs/examples, and the testcase log collector; retained the existing V2 engine implementations |
| Human verification | Automated: 20 unittest testcases passed locally and in `frontierforge:tests`; 21/21 local, CLI and Docker commands passed. Named human review required before release/deployment; no release gate claimed here |
| Data used | Synthetic fixtures and seeded in-repo generators only; no personal, health, secret or restricted data |
| Tier/gate | Tier B, no release gate; advisory research experiments, no advantage or safety claim |
