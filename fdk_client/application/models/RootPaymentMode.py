"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PaymentModeList import PaymentModeList








class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    add_card_enabled = fields.Boolean(required=False)
    
    display_priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    

