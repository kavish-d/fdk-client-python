"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *







from .PaymentModeList import PaymentModeList








class RootPaymentMode(Schema):

    
    aggregator_name = fields.Str(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    

