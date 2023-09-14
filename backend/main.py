"""Main module for the FastAPI application."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return a root message."""
    return {"Hello": "World"}
