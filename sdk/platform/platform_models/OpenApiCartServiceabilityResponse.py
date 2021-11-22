"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CartBreakup import CartBreakup

from .CartProductInfo import CartProductInfo

from .ShipmentPromise import ShipmentPromise






class OpenApiCartServiceabilityResponse(Schema):

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    

