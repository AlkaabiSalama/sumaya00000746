"""Compatibility entrypoint for deployments expecting `ChangeAnalysis:app`.

This module re-exports the FastAPI application defined in ``main.py`` so the
existing HTML frontend keeps working with all current backend routes.
"""

from main import app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ChangeAnalysis:app", host="0.0.0.0", port=8000, reload=False)
