import asyncio
from fastapi import FastAPI
from .api.api_v1.api import api_router

app = FastAPI(title="Emby Hub - API")
app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup():
    # 初始化数据库、缓存连接等
    print("Starting Emby Hub API")

@app.get("/")
async def root():
    return {"message": "Emby Hub API"}
