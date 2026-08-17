import uuid
from enum import StrEnum
from datetime import datetime

from sqlalchemy import DateTime, String, text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class CategoryType(StrEnum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSACTION = "transaction"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuidv7()")
    )
    name: Mapped[str] = mapped_column(
        String(25), unique=True
    )
    category_type: Mapped[CategoryType] = mapped_column(
        Enum(CategoryType, 
             values_callable=lambda x: [e.value for e in x])
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
