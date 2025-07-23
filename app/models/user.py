from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from . import Base, db

class User(Base):
    __tablename__ = "users"

    # table columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(225), nullable=False)
    email: Mapped[str] = mapped_column(db.String(225), nullable=False, unique=True) # Ensure email is unique
    address: Mapped[str] = mapped_column(db.String(225), nullable=False)

    #relationships
    orders: Mapped[List["Order"]] = db.relationship(back_populates="user")

    def __repr__(self):
        return f"<User {self.name}>"