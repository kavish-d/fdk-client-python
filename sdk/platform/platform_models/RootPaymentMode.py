"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema













from .PaymentModeList import PaymentModeList


class RootPaymentMode(BaseSchema):

    
    add_card_enabled = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    display_priority = fields.Int(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    

