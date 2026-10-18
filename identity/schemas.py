import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SignUpRequest(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Email address to be registered",
        examples=["user@example.com"],
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password to be registered to the user",
        examples=["StrongPassword1029384756!@"],
    )


class SignUpResponse(BaseModel):
    id: uuid.UUID = Field(
        ...,
        description="Registered user uuid",
        examples=["123e4567-e89b-12d3-a456-426614174000"],
    )
    email: EmailStr = Field(
        ..., description="Registered user email address", examples=["user@example.com"]
    )

    model_config = ConfigDict(from_attributes=True)
