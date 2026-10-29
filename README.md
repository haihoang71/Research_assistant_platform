# EDU-09 — Research Assistant Platform

Evidence-grounded AI assistant for literature review, paper screening, structured extraction and research synthesis.

## Current status

This repository contains the initial project foundation only. Product features are intentionally not implemented yet.

## Local development

```powershell
docker compose up --build
```

The backend health endpoint is available at `http://localhost:8000/health`.

## Repository layout

- `backend/` — FastAPI application and backend tests.
- `frontend/` — frontend application placeholder.
- `tests/` — cross-component and end-to-end tests.
- `docs/` — product, architecture and decision documents.
- `eval/` — evaluation datasets and experiment results.
- `harness/` — Codex phase plans and build logs.

## Scope boundary

The system must ground research claims in verifiable sources. A human researcher or reviewer owns the final interpretation and report.
