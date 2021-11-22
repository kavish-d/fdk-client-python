"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *







from .CartDetailResponse import CartDetailResponse


class AddCartDetailResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    partial = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    

