from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class RegisterIn(BaseModel):
    email: str
    password: str

@router.post("/register")
async def register(payload: RegisterIn):
    # TODO: implement registration (email verification)
    return {"msg": "registration endpoint (stub)"}

@router.post("/login")
async def login():
    # TODO: implement login -> return JWT tokens
    raise HTTPException(status_code=501, detail="Not implemented")
