from fastapi import APIRouter

from .endpoints import auth, servers, sessions

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(servers.router, prefix="/servers", tags=["servers"])
api_router.include_router(sessions.router, prefix="/servers/{server_id}/sessions", tags=["sessions"])
