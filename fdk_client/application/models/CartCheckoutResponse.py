"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CheckCart import CheckCart






class CartCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.Dict(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

