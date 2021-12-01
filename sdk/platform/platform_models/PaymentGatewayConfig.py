"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class PaymentGatewayConfig(BaseSchema):

    
    key = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    config_type = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    

