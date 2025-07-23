from marshmallow import validates, ValidationError, Schema, fields

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True) #for output only
    product_name = fields.String(required=True, validate=lambda x: len(x) > 0)
    price = fields.Float(required=True, validate=lambda x: x > 0) # price always positif

    @validates('product_name')
    def validate_product_name(self, value):
        """product_name cant be empty"""
        if not value or len(value.strip()) == 0:
            raise ValidationError("Product name cannot be empty.")
        return value
    
    @validates('price')
    def validate_price(self, value):
        """price must be positive"""
        if value <= 0:
            raise ValidationError("Price must be positive.")
        return value

#CREATE INSTANCE
product_schema = ProductSchema()  # one product
products_schema = ProductSchema(many=True)  # multiple products (note the 's')
