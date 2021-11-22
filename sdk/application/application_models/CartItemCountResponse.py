"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class CartItemCountResponse(Schema):

    
    user_cart_items_count = fields.Int(required=False)
    

