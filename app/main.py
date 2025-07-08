from fastapi import FastAPI
from app.routes import secret, health
import uvicorn
from app.logger import logger


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(secret.router)
    app.include_router(health.router)

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
