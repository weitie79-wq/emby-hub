from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
import os

# Initialize FastAPI app
app = FastAPI(title="Emby Hub - Unified App")

# Serve frontend static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

# Middleware (e.g., CORS)
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# API Router
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Emby Hub API is running."}

# SPA Fallback
@app.exception_handler(404)
async def spa_fallback(request, exc):
    if os.path.exists(os.path.join(static_dir, "index.html")):
        from fastapi.responses import FileResponse
        return FileResponse(os.path.join(static_dir, "index.html"))
    return {"message": "Resource not found"}
