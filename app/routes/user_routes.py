from flask import Blueprint, request, jsonify
from sqlalchemy import select
from marshmallow import ValidationError
from app.models import db, User
from app.schemas.user_schema import user_schema, users_schema

# =============================================================================
# 🎯 PRESENTATION NOTE - API FUNCTIONALITY REQUIREMENT 
# This file demonstrates ALL 5 required User CRUD endpoints:
# - POST /users          - Create new user
# - GET /users           - Retrieve all users
# - GET /users/<id>     - Retrieve user by ID
# - PUT /users/<id>     - Update user by ID
# - DELETE /users/<id>  - Delete user by ID
# =============================================================================

# Create a blueprint for user routes
user_bp = Blueprint('users', __name__, url_prefix='/users')  # REQ4: Blueprint pattern

# POST /users - CREATE USER REQUIREMENT
@user_bp.route('', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        # Validate the incoming data using our schema
        user_data = user_schema.load(request.json)  # REQ3: Marshmallow validation
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400
    
    # UNIQUE EMAIL CONSTRAINT CHECKING
    # Check if email already exists
    existing_user = db.session.execute(
        select(User).where(User.email == user_data['email'])
    ).scalar_one_or_none()
    
    if existing_user:
        return jsonify({'error': 'Email already exists'}), 409  # REQ2: Proper HTTP status codes
    
    # Create new user
    new_user = User(
        name=user_data['name'],
        email=user_data['email'],
        address=user_data['address']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        'message': 'User created successfully',
        'user': user_schema.dump(new_user)
    }), 201

# GET /users - RETRIEVE ALL USERS REQUIREMENT
@user_bp.route('', methods=['GET'])
def get_users():
    """Get all users"""
    query = select(User)
    users = db.session.execute(query).scalars().all()
    return users_schema.jsonify(users)  # REQ3: Marshmallow serialization

# GET /users/<id> - RETRIEVE USER BY ID REQUIREMENT
@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    """Get user by ID"""
    user = db.session.get(User, id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404  # REQ2: Error handling
    
    return user_schema.jsonify(user)

# PUT /users/<id> - UPDATE USER REQUIREMENT
@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    """Update user by ID"""
    user = db.session.get(User, id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    try:
        user_data = user_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400
    
    # Update user fields
    for field, value in user_data.items():
        setattr(user, field, value)
    
    db.session.commit()
    
    return jsonify({
        'message': 'User updated successfully',
        'user': user_schema.dump(user)
    })

# DELETE /users/<id> - DELETE USER REQUIREMENT
@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Delete user by ID"""
    user = db.session.get(User, id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'}), 204