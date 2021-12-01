"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .PaymentGatewayConfig import PaymentGatewayConfig


class PaymentGatewayConfigRequest(BaseSchema):

    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    

