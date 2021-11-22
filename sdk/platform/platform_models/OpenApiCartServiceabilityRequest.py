"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ShippingAddress import ShippingAddress

from .CartItem import CartItem


class OpenApiCartServiceabilityRequest(Schema):

    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    cart_items = fields.Nested(CartItem, required=False)
    

