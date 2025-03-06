from fastapi import FastAPI
from app.api.routers import router as api_router

app = FastAPI(
    title="News Portal API",
    description="A FastAPI backend for a news portal with GraphQL, PostgreSQL, Redis, and Kafka.",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to the News Portal API GET"}
