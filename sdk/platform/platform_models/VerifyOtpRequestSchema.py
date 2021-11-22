"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class VerifyOtpRequestSchema(Schema):

    
    request_id = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

