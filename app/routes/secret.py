# This file is covered by tests in test_routes.py for demonstration purposes
from fastapi import APIRouter, Depends
from app.routes.utils import get_settings
from app.services.secret import Secret
from app.config import Settings
from app.logger import logger


router = APIRouter()


@router.get("/secret", description="Retrieve secret code from DynamoDB")
async def get_secret(settings: Settings = Depends(get_settings)):
    logger.info("Endpoint /secret pinged.")

    secret_service = Secret(
        table_name=settings.DYNAMODB_TABLE_NAME,
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

    try:
        secret_code = secret_service.retrieve_secret(settings.CODE_NAME)
        return {"secret_code": secret_code}
    except Exception as e:
        logger.warning(f"Secret not found: {e}")
        raise HTTPException(status_code=404, detail="Secret not found")

