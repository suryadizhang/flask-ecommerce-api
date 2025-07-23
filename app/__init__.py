from flask import Flask
from flask_marshmallow import Marshmallow
from config import config

# Import the db instance from models (don't create a new one)
from app.models import db

# Initialize Marshmallow
ma = Marshmallow()

# =============================================================================
# 🎯 PRESENTATION NOTE - CODE QUALITY & CONFIGURATION REQUIREMENT 
# This file demonstrates:
# - MODULAR ARCHITECTURE with blueprints
# - BLUEPRINT REGISTRATION
# - DATABASE TABLE CREATION
# - APPLICATION FACTORY PATTERN
# =============================================================================

def create_app(config_name='development'):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions with app
    db.init_app(app)
    ma.init_app(app)
    
    # MODULAR ARCHITECTURE REQUIREMENT
    # Import and register blueprints
    from app.routes.user_routes import user_bp
    from app.routes.product_routes import product_bp
    from app.routes.order_routes import order_bp
    
    # BLUEPRINT REGISTRATION REQUIREMENT
    app.register_blueprint(user_bp)      # REQ4: /users endpoints
    app.register_blueprint(product_bp)   # REQ4: /products endpoints
    app.register_blueprint(order_bp)     # REQ4: /orders endpoints
    
    # Add a home route
    @app.route('/')
    def home():
        return {
            'message': 'Welcome to E-commerce API',
            'version': '1.0',
            'endpoints': {
                'users': '/users',
                'products': '/products',
                'orders': '/orders'
            }
        }
    
    # 🎤 PRESENTATION POINT 30: DATABASE TABLE CREATION REQUIREMENT
    # Create tables
    with app.app_context():
        db.create_all()  # REQ4: db.create_all() as required by assignment
    
    return app