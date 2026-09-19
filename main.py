"""SN Cloud acceptance fixture — FastAPI (DEC-001 AC-01).

No Dockerfile and no provider configuration. The platform detects fastapi AND publishes an
advisory start command (uvicorn main:app ...) which it deliberately does NOT hand to the
builder (ADR-0100) — so this fixture also proves the builder reaches the same conclusion on
its own from the repository.
"""
import os

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"fixture": "sncloud-fixture-fastapi", "framework": "fastapi", "path": "/"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
