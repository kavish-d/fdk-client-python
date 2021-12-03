"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .UserSchema import UserSchema
















class ProfileEditSuccess(BaseSchema):

    
    user = fields.Nested(UserSchema, required=False)
    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    
    verify_email_link = fields.Boolean(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
