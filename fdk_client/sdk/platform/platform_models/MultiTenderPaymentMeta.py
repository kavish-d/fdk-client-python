"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class MultiTenderPaymentMeta(BaseSchema):
    # Payment swagger.json

    
    payment_id = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    

