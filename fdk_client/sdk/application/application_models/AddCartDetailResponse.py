"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .CartDetailResponse import CartDetailResponse




class AddCartDetailResponse(BaseSchema):

    
    success = fields.Boolean(required=False)
    
    partial = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    

