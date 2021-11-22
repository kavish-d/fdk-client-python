"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *















from .ItemTotal import ItemTotal


class PlatformOrderPage(Schema):

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    item_total = fields.Nested(ItemTotal, required=False)
    

