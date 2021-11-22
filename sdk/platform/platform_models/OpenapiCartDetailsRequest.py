"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CartItem import CartItem


class OpenapiCartDetailsRequest(Schema):

    
    cart_items = fields.Nested(CartItem, required=False)
    

