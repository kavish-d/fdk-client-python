"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .UserSchema import UserSchema


class AuthSuccess(BaseSchema):

    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    
    user = fields.Nested(UserSchema, required=False)
    

