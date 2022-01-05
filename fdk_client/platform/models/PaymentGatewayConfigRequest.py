"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PaymentGatewayConfig import PaymentGatewayConfig




class PaymentGatewayConfigRequest(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    
    app_id = fields.Str(required=False)
    

