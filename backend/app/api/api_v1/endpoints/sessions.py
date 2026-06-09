from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_sessions(server_id: int):
    # TODO: proxy to Emby Sessions API
    return {"sessions": []}

@router.post("/{session_id}/stop")
async def stop_session(server_id: int, session_id: str):
    # TODO: send stop command to Emby
    return {"msg": "stopped"}
