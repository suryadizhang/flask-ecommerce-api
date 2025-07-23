from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from datetime import date
from . import Base, db, order_products

# =============================================================================
# 🎯 PRESENTATION NOTE - DATABASE MODELS REQUIREMENT 
# This file demonstrates:
# - FOREIGN KEY REFERENCE
# - DATETIME FIELD
# - MANY-TO-MANY RELATIONSHIP
# =============================================================================

class Order(Base):
    #order modal conect user to product
    __tablename__ = "orders"

    # table columns
    id: Mapped[int] = mapped_column(primary_key=True)
    #  FOREIGN KEY REFERENCE REQUIREMENT
    user_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"), nullable=False)  # REQ1: Foreign key to users
    # DATETIME FIELD REQUIREMENT
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)  # REQ1: DateTime field as required

    # RELATIONSHIP DEFINITIONS
    # relationship many to one relationship to User
    user: Mapped["User"] = db.relationship("User", back_populates="orders")
    
    # MANY-TO-MANY RELATIONSHIP REQUIREMENT
    # Many Orders ←→ Many Products (uses association table)
    products: Mapped[List["Product"]] = db.relationship(
        secondary=order_products,  # REQ1: Uses association table
        back_populates="orders"
    )

    def __repr__(self):
        return f"<Order {self.id}: User {self.user_id} - {self.order_date}>"