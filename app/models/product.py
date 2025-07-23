from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from . import Base, db, order_products

class Product(Base):
    # product model
    __tablename__ = "products"

    # table columns
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(db.String(225), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    
    #relationship many to many
    orders: Mapped[List["Order"]] = db.relationship(
        secondary=order_products, 
        back_populates="products")

    def __repr__(self):
        return f"<Product {self.id}: {self.product_name} - {self.price}>"
