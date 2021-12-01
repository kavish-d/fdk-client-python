"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class SendMobileOtpRequestSchema(BaseSchema):

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    android_hash = fields.Str(required=False)
    
    force = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    

