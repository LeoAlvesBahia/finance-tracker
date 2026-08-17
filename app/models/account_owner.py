import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AccountOwner(Base):
    __tablename__ = "account_owners"

    account_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("accounts.id"), primary_key=True
    )
    person_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("people.id"), primary_key=True
    )