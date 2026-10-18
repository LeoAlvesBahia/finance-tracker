from argon2 import PasswordHasher
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from models import User
from schemas import SignUpRequest, SignUpResponse

router = APIRouter()
ph = PasswordHasher()


@router.post("/signup", response_model=SignUpResponse, status_code=201)
async def signup(request: SignUpRequest, db: AsyncSession = Depends(get_db)):
    user = await db.scalar(select(User).where(User.email == request.email))
    if user:
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(email=request.email, hashed_password=ph.hash(password=request.password))
    db.add(user)
    await db.commit()
    return user
