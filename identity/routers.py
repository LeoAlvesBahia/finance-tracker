from argon2 import PasswordHasher
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from models import User
from schemas import SignUpRequest, SignUpResponse

router = APIRouter()
ph = PasswordHasher()


@router.post("/signup", response_model=SignUpResponse, status_code=201)
async def signup(request: SignUpRequest, db: AsyncSession = Depends(get_db)):
    request.email = request.email.lower()

    is_user_registered = await db.scalar(
        select(User).where(User.email == request.email)
    )
    if is_user_registered:
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(email=request.email, hashed_password=ph.hash(password=request.password))
    db.add(user)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Email already registered")

    return user
