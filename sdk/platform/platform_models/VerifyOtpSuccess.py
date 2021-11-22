"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .UserSchema import UserSchema






class VerifyOtpSuccess(Schema):

    
    user = fields.Nested(UserSchema, required=False)
    
    user_exists = fields.Boolean(required=False)
    
    register_token = fields.Str(required=False)
    

