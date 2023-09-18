"""Main module for the FastAPI application."""

from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base, User

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    """Return a root message."""
    return {"message": "Hello"}
