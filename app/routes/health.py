# This file is covered by tests in test_routes.py for demonstration purposes
from fastapi import APIRouter, Depends
from app.routes.utils import get_settings
from app.config import Settings
from app.logger import logger


router = APIRouter()


@router.get("/health", description="health check endpoint")
async def get_secret(settings: Settings = Depends(get_settings)):
    logger.info("Endpoint /health pinged.")
    return {
        "status": "healthy",
        "container": settings.DOCKERHUB_URL,
        "project": settings.GITHUB_URL,
    }
