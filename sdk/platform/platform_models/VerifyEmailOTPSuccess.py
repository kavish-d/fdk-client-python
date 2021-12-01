"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .UserSchema import UserSchema




class VerifyEmailOTPSuccess(BaseSchema):

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_email_link = fields.Boolean(required=False)
    

