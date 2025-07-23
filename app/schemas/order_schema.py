from marshmallow import validates, ValidationError, Schema, fields
from datetime import date

class OrderSchema(Schema):
    """Order schema - validates order information"""
    
    id = fields.Integer(dump_only=True)  # for output only
    user_id = fields.Integer(required=True)  # which user placed this order
    order_date = fields.Date(required=True)  # when the order was placed
    
    @validates('user_id')
    def validate_user_id(self, value):
        """user_id must be positive"""
        if value <= 0:
            raise ValidationError('User ID must be positive.')
        return value
    
    @validates('order_date')
    def validate_order_date(self, value):
        """order date cannot be in future"""
        if value > date.today():
            raise ValidationError('Order date cannot be in the future.')
        return value

# CREATE INSTANCE
order_schema = OrderSchema()  # one order
orders_schema = OrderSchema(many=True)  # multiple orders