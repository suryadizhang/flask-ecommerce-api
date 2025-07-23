from flask import Blueprint, request, jsonify
from sqlalchemy import select
from marshmallow import ValidationError
from app.models import db, Order, User, Product
from app.schemas.order_schema import order_schema, orders_schema

# =============================================================================
# 🎯 PRESENTATION NOTE - API FUNCTIONALITY REQUIREMENT 
# This file demonstrates SPECIFIC ORDER REQUIREMENTS:
# - POST /orders              - Create order (requires user ID and order date)
# - PUT add_product           - Add product to order (prevent duplicates)  
# - DELETE remove_product    - Remove product from order
# - GET orders by user       - Get orders for a user
# - GET order products       - Get products in an order
# =============================================================================

# Create a blueprint for order routes
order_bp = Blueprint('orders', __name__, url_prefix='/orders')

# CREATE ORDER REQUIREMENT (requires user ID and order date)
@order_bp.route('', methods=['POST'])
def create_order():
    """Create a new order"""
    try:
        # Validate the incoming data using our schema
        order_data = order_schema.load(request.json)  # REQ3: Schema validation
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400
    
    # USER ID VALIDATION REQUIREMENT
    # Check if user exists
    user = db.session.get(User, order_data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Create new order
    new_order = Order(
        user_id=order_data['user_id'],      # REQ2: Requires user ID
        order_date=order_data['order_date']  # REQ2: Requires order date
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({
        'message': 'Order created successfully',
        'order': order_schema.dump(new_order)
    }), 201

@order_bp.route('', methods=['GET'])
def get_orders():
    """Get all orders"""
    query = select(Order)
    orders = db.session.execute(query).scalars().all()
    return orders_schema.jsonify(orders)

@order_bp.route('/<int:id>', methods=['GET'])
def get_order(id):
    """Get order by ID"""
    order = db.session.get(Order, id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    return order_schema.jsonify(order)

# ADD PRODUCT TO ORDER REQUIREMENT (with duplicate prevention)
@order_bp.route('/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    """Add a product to an order"""
    order = db.session.get(Order, order_id)
    product = db.session.get(Product, product_id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    # PREVENT DUPLICATES REQUIREMENT
    # Check if product is already in the order
    if product in order.products:  # REQ2: Prevents duplicates as required
        return jsonify({'error': 'Product already in order'}), 400
    
    # MANY-TO-MANY OPERATION
    # Add product to order
    order.products.append(product)  # REQ1: Many-to-many relationship operation
    db.session.commit()
    
    return jsonify({
        'message': 'Product added to order successfully',
        'order': order_schema.dump(order)
    }), 200

# REMOVE PRODUCT FROM ORDER REQUIREMENT
@order_bp.route('/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    """Remove a product from an order"""
    order = db.session.get(Order, order_id)
    product = db.session.get(Product, product_id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    # Check if product is in the order
    if product not in order.products:
        return jsonify({'error': 'Product not in order'}), 400
    
    # Remove product from order
    order.products.remove(product)
    db.session.commit()
    
    return jsonify({
        'message': 'Product removed from order successfully',
        'order': order_schema.dump(order)
    }), 200

# GET ORDERS BY USER REQUIREMENT
@order_bp.route('/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    """Get all orders for a specific user"""
    user = db.session.get(User, user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    query = select(Order).where(Order.user_id == user_id)  # REQ2: Filter by user
    orders = db.session.execute(query).scalars().all()
    
    return orders_schema.jsonify(orders)

# GET PRODUCTS IN ORDER REQUIREMENT
@order_bp.route('/<int:order_id>/products', methods=['GET'])
def get_order_products(order_id):
    """Get all products in an order"""
    order = db.session.get(Order, order_id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    from app.schemas.product_schema import products_schema
    return products_schema.jsonify(order.products)  # REQ1: Access relationship

@order_bp.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    """Delete order by ID"""
    order = db.session.get(Order, id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    db.session.delete(order)
    db.session.commit()
    
    return jsonify({'message': 'Order deleted successfully'}), 204