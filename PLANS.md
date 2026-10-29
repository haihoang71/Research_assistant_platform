# research_assistant_platform implementation plan

## Phase 00 — Foundation

- Create repository conventions and Codex context.
- Add FastAPI health endpoint.
- Add Docker Compose for backend, PostgreSQL/pgvector and Redis.
- Add baseline tests, linting and CI.

## Phase 01 — Research project and source discovery

- Research project CRUD.
- Provider adapters for OpenAlex, Semantic Scholar and arXiv.
- Source normalization and deduplication.

## Phase 02 — Document ingestion and evidence

- Open-access document ingestion.
- Object-storage abstraction.
- PDF parsing, chunking and evidence spans.

## Phase 03 — Screening and extraction

- Inclusion/exclusion criteria.
- Human review workflow.
- Structured extraction with confidence and evidence references.

## Phase 04 — Synthesis and citation verification

- Theme synthesis.
- Comparison tables.
- Claim-to-evidence citation verification.

## Phase 05 — Evaluation and research-gap analysis

- Gold evaluation dataset.
- Retrieval, extraction and citation metrics.
- Contradiction and research-gap analysis.

Each phase must have an acceptance checklist in `harness/build/` before implementation begins.
