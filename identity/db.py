import os
from functools import lru_cache

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


async def get_db():
    async_session = get_session_factory()
    async with async_session() as session:
        yield session


@lru_cache
def get_engine():
    DATABASE_URL = os.environ["DATABASE_URL"]

    engine = create_async_engine(DATABASE_URL)

    return engine


@lru_cache
def get_session_factory():
    async_session = async_sessionmaker(get_engine(), expire_on_commit=False)
    return async_session
