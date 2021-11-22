"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *













from .CheckCart import CheckCart


class CartCheckoutResponse(Schema):

    
    callback_url = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    

