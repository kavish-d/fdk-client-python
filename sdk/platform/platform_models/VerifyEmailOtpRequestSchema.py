"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class VerifyEmailOtpRequestSchema(Schema):

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

