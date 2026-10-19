import pytest
import pytest_asyncio
from httpx2 import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from testcontainers.community.postgres import PostgresContainer

from db import get_db
from main import app
from models import Base


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:18-trixie") as postgres:
        yield postgres


@pytest_asyncio.fixture(scope="session")
async def test_engine(postgres_container: PostgresContainer):
    sync_url = postgres_container.get_connection_url()
    async_url = sync_url.replace("psycopg2", "asyncpg")
    engine = create_async_engine(async_url)

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield engine


@pytest.fixture()
def session_factory(test_engine: AsyncEngine):
    async_session = async_sessionmaker(test_engine, expire_on_commit=False)
    return async_session


@pytest_asyncio.fixture()
async def client(session_factory: async_sessionmaker[AsyncSession]):
    async def override_get_db():
        async with session_factory() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as test_client:
        yield test_client

    app.dependency_overrides.clear()
