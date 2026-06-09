from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def add_server():
    # TODO: accept base_url + token, store encrypted
    return {"msg": "add server (stub)"}

@router.get("/")
async def list_servers():
    return {"servers": []}
