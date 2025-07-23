from marshmallow import validates, ValidationError, Schema, fields
from datetime import date

# =============================================================================
# 🎯 PRESENTATION NOTE - SERIALIZATION & VALIDATION REQUIREMENT 
# This file demonstrates:
# - FOREIGN KEY FIELD inclusion 
# - DATE VALIDATION 
# - BUSINESS RULE VALIDATION
# =============================================================================

class OrderSchema(Schema):
    """Order schema - validates order information"""
    
    id = fields.Integer(dump_only=True)  # for output only
    # 🎤 PRESENTATION POINT 24: FOREIGN KEY FIELD REQUIREMENT
    user_id = fields.Integer(required=True)  # REQ3: Foreign key field (user who placed order)
    order_date = fields.Date(required=True)  # when the order was placed
    
    @validates('user_id')
    def validate_user_id(self, value):
        """user_id must be positive"""
        if value <= 0:
            raise ValidationError('User ID must be positive.')
        return value
    
    # 🎤 PRESENTATION POINT 25: DATE VALIDATION REQUIREMENT
    @validates('order_date')
    def validate_order_date(self, value):
        """order date cannot be in future"""
        if value > date.today():  # REQ3: Business rule validation
            raise ValidationError('Order date cannot be in the future.')
        return value

# CREATE INSTANCE
order_schema = OrderSchema()  # one order
orders_schema = OrderSchema(many=True)  # multiple orders