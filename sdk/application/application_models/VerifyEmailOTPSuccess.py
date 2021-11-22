"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UserSchema import UserSchema




class VerifyEmailOTPSuccess(Schema):

    
    user = fields.Nested(UserSchema, required=False)
    
    verify_email_link = fields.Boolean(required=False)
    

