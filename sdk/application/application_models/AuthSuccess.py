"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .UserSchema import UserSchema


class AuthSuccess(Schema):

    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    
    user = fields.Nested(UserSchema, required=False)
    

