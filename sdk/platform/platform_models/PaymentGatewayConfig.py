"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *












class PaymentGatewayConfig(Schema):

    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    

