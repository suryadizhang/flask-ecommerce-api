from sqlalchemy.orm import DeclarativeBase  # ← Change this line
from flask_sqlalchemy import SQLAlchemy

#this is the foundation of everything
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Association table for many-to-many relationships
order_products = db.Table(
    "Order_Products",
    Base.metadata,
    db.Column("order_id", db.ForeignKey("orders.id")),
    db.Column("product_id", db.ForeignKey("products.id"))
)

#import all models here then it will be available when we import this package
from .user import User
from .product import Product
from .order import Order

__all__ = ["Base","db","order_products","User", "Product", "Order"]