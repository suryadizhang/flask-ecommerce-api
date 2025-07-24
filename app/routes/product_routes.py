from flask import Blueprint, request, jsonify
from sqlalchemy import select
from marshmallow import ValidationError
from app.models import db, Product
from app.schemas.product_schema import product_schema, products_schema

# Create a blueprint for product routes
product_bp = Blueprint('products', __name__, url_prefix='/products')


@product_bp.route('', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        # Validate the incoming data using our schema
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400
    
    # Create new product
    new_product = Product(
        product_name=product_data['product_name'],
        price=product_data['price']
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({
        'message': 'Product created successfully',
        'product': product_schema.dump(new_product)
    }), 201

@product_bp.route('', methods=['GET'])
def get_products():
    """Get all products"""
    query = select(Product)
    products = db.session.execute(query).scalars().all()
    return jsonify(products_schema.dump(products))

@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    """Get product by ID"""
    product = db.session.get(Product, id)
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify(product_schema.dump(product))

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    """Update product by ID"""
    product = db.session.get(Product, id)
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    try:
        product_data = product_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400
    
    # Update product fields
    for field, value in product_data.items():
        setattr(product, field, value)
    
    db.session.commit()
    
    return jsonify({
        'message': 'Product updated successfully',
        'product': product_schema.dump(product)
    })

@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    """Delete product by ID"""
    product = db.session.get(Product, id)
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'}), 204