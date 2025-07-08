from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    DYNAMODB_TABLE_NAME: str
    CODE_NAME: str
    DOCKERHUB_URL: str
    GITHUB_URL: str
