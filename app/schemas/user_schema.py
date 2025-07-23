from marshmallow import validates, ValidationError, Schema, fields
from app.models import User

# =============================================================================
# 🎯 PRESENTATION NOTE - SERIALIZATION & VALIDATION REQUIREMENT 
# This file demonstrates:
# - EMAIL VALIDATION
# - CUSTOM VALIDATION FUNCTIONS
# - PROPER FIELD DEFINITIONS with validation rules
# =============================================================================

class UserSchema(Schema):
    #form that check if user information correct
    
    #define the fields we expect
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=lambda x: len(x) > 0)
    #  EMAIL VALIDATION REQUIREMENT
    email = fields.Email(required=True)  # REQ3: Built-in email validation as required
    address = fields.String(required=True, validate=lambda x: len(x) > 0)
    
    #  CUSTOM VALIDATION REQUIREMENT
    @validates('name')
    def validate_name(self, value):
        """name cant be empty"""
        if not value or len(value.strip()) == 0:
            raise ValidationError("Name cannot be empty.")  # REQ3: Custom validation
        return value

#CREATE INSTANCE
user_schema = UserSchema() # one user
users_schema = UserSchema(many=True) #multiple users
