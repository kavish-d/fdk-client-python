"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .MultiTenderPaymentMeta import MultiTenderPaymentMeta




class MultiTenderPaymentMethod(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    mode = fields.Str(required=False)
    

