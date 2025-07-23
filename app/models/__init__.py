from sqlalchemy.orm import DeclarativeBase  # ← Change this line
from flask_sqlalchemy import SQLAlchemy

# =============================================================================
# 🎯 PRESENTATION NOTE - DATABASE MODELS REQUIREMENT 
# This file demonstrates:
# - ASSOCIATION TABLE for Many-to-Many relationships 
# - FOREIGN KEY CONSTRAINTS
# - PREVENTS DUPLICATES with composite primary key
# =============================================================================

#this is the foundation of everything
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# ASSOCIATION TABLE REQUIREMENT
# Many Orders ←→ Many Products (as required by assignment)
# Association table for many-to-many relationships
order_products = db.Table(
    "Order_Products",
    Base.metadata,
    db.Column("order_id", db.ForeignKey("orders.id")),    # REQ1: FOREIGN KEY to orders
    db.Column("product_id", db.ForeignKey("products.id"))  # REQ1: FOREIGN KEY to products
    # REQ1: Composite primary key prevents duplicate product entries in same order
)

#import all models here then it will be available when we import this package
from .user import User
from .product import Product
from .order import Order

__all__ = ["Base","db","order_products","User", "Product", "Order"]