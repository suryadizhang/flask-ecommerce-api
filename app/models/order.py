from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from datetime import date
from . import Base, db, order_products

class Order(Base):
    #order modal conect user to product
    __tablename__ = "orders"

    # table columns
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"), nullable=False)
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)

    # relationship many to one relationship to User
    user: Mapped["User"] = db.relationship("User", back_populates="orders")
    
    # relationship many to many relationship to Product
    products: Mapped[List["Product"]] = db.relationship(
        secondary=order_products,
        back_populates="orders"
    )

    def __repr__(self):
        return f"<Order {self.id}: User {self.user_id} - {self.order_date}>"