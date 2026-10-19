from httpx2 import AsyncClient


async def test_signup(client: AsyncClient):
    response = await client.post(
        "/signup", json={"email": "user@example.com", "password": "test123456"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["email"] == "user@example.com"
    assert "password" not in data
    assert "hashed_password" not in data

    response = await client.post(
        "/signup", json={"email": "user2@example.com", "password": "test123456"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["email"] == "user2@example.com"
    assert "password" not in data
    assert "hashed_password" not in data

    response = await client.post(
        "/signup", json={"email": "user@example.com", "password": "test123456"}
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Email already registered"}
