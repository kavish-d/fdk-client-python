"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UserSchema import UserSchema






class LoginSuccess(Schema):

    
    user = fields.Nested(UserSchema, required=False)
    
    request_id = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    

