# Initial architecture

## Foundation

The initial system is a modular monolith:

- FastAPI backend.
- PostgreSQL with pgvector for application data and initial retrieval.
- Redis reserved for cache and future job queues.
- Separate frontend application.
- Provider, storage and vector-store interfaces to keep future migrations possible.

## Planned runtime flow

```text
Frontend -> API -> application modules -> providers/storage/database
                         |
                         +-> worker/job queue for long-running workflows
```

## Module boundaries

- `projects` — research project lifecycle.
- `sources` — paper metadata and provider adapters.
- `ingestion` — document acquisition and normalization.
- `retrieval` — chunking, embeddings and search.
- `screening` — inclusion/exclusion decisions.
- `extraction` — structured facts and evidence spans.
- `synthesis` — report sections and claims.
- `citations` — source and evidence verification.

Material architecture changes require an ADR under `docs/adr/`.
