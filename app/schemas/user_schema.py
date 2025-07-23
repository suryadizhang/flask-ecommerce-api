from marshmallow import validates, ValidationError, Schema, fields
from app.models import User

class UserSchema(Schema):
    #form that check if user information correct
    
    #define the fields we expect
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=lambda x: len(x) > 0)
    email = fields.Email(required=True)
    address = fields.String(required=True, validate=lambda x: len(x) > 0)
    
    @validates('name')
    def validate_name(self, value):
        """name cant be empty"""
        if not value or len(value.strip()) == 0:
            raise ValidationError("Name cannot be empty.")
        return value

#CREATE INSTANCE
user_schema = UserSchema() # one user
users_schema = UserSchema(many=True) #multiple users
