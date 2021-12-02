"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .UserSchema import UserSchema




class VerifyMobileOTPSuccess(BaseSchema):

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_mobile_link = fields.Boolean(required=False)
    

