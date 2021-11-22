"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .MultiTenderPaymentMeta import MultiTenderPaymentMeta




class MultiTenderPaymentMethod(Schema):

    
    amount = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    mode = fields.Str(required=False)
    

