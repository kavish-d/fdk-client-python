"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .PaymentGatewayConfig import PaymentGatewayConfig


class PaymentGatewayConfigRequest(Schema):

    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    

