"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class CartItem(Schema):

    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    product_id = fields.Str(required=False)
    

