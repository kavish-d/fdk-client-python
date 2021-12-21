"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CartItem import CartItem

from .ShippingAddress import ShippingAddress


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    

