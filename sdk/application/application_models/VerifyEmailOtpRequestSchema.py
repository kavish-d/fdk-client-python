"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class VerifyEmailOtpRequestSchema(BaseSchema):

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

