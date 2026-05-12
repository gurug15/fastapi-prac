from fastapi import FastAPI
from app.configs.app_config import getAppConfig
from app.routes import todo

app = FastAPI()

app.include_router(router=todo.router, prefix="/api")


@app.get("/")
def getConfig():
    config = getAppConfig()

    return {
        "app_name": config.app_name
    }