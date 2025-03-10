import os

from fastapi import FastAPI

from app.api.routers import router as api_router

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI(
    title="News Portal API",
    description="A FastAPI backend for a news portal with GraphQL, PostgreSQL, and Redis",
    version="1.0.0",
    docs_url="/docs" if ENVIRONMENT == "development" else None,
    redoc_url="/redoc" if ENVIRONMENT == "development" else None,
    openapi_url="/openapi.json" if ENVIRONMENT == "development" else None,
)

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to the News Portal API GET"}
