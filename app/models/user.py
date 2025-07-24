from sqlalchemy.orm import Mapped, mapped_column
from typing import List, TYPE_CHECKING
from . import Base, db

if TYPE_CHECKING:
    from .order import Order

# =============================================================================
# 🎯 PRESENTATION NOTE - DATABASE MODELS REQUIREMENT
# This file demonstrates:
# - UNIQUE EMAIL CONSTRAINT
# - ONE-TO-MANY RELATIONSHIP
# =============================================================================


class User(Base):
    __tablename__ = "users"

    # table columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(225), nullable=False)
    # UNIQUE EMAIL CONSTRAINT REQUIREMENT
    # REQ1: Ensure email is unique
    email: Mapped[str] = mapped_column(
        db.String(225), nullable=False, unique=True
    )
    address: Mapped[str] = mapped_column(db.String(225), nullable=False)

    # ONE-TO-MANY RELATIONSHIP REQUIREMENT
    # One User → Many Orders (as required by assignment)
    # REQ1: One-to-Many relationship
    orders: Mapped[List["Order"]] = db.relationship(
        back_populates="user"
    )

    def __repr__(self):
        return f"<User {self.name}>"