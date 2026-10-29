"""FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(title="EDU-09 Research Assistant Platform", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Return a lightweight liveness response."""

    return {"status": "ok"}
