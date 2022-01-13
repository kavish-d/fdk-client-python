"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class MultiTenderPaymentMeta(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    

