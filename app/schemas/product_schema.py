from marshmallow import validates, ValidationError, Schema, fields

# =============================================================================
# 🎯 PRESENTATION NOTE - SERIALIZATION & VALIDATION REQUIREMENT 
# This file demonstrates:
# - POSITIVE PRICE VALIDATION
# - BUSINESS RULE VALIDATION
# - CUSTOM VALIDATION FUNCTIONS
# =============================================================================

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True) #for output only
    product_name = fields.String(required=True, validate=lambda x: len(x) > 0)
    # 🎤 PRESENTATION POINT 26: POSITIVE PRICE VALIDATION REQUIREMENT
    price = fields.Float(required=True, validate=lambda x: x > 0)  # REQ3: Price always positive

    @validates('product_name')
    def validate_product_name(self, value):
        """product_name cant be empty"""
        if not value or len(value.strip()) == 0:
            raise ValidationError("Product name cannot be empty.")
        return value
    
    # 🎤 PRESENTATION POINT 27: BUSINESS RULE VALIDATION REQUIREMENT
    @validates('price')
    def validate_price(self, value):
        """price must be positive"""
        if value <= 0:  # REQ3: Business rule - prices must be positive
            raise ValidationError("Price must be positive.")
        return value

#CREATE INSTANCE
product_schema = ProductSchema()  # one product
products_schema = ProductSchema(many=True)  # multiple products (note the 's')
