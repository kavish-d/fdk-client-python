"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .SharedCart import SharedCart


class SharedCartResponse(Schema):

    
    error = fields.Str(required=False)
    
    cart = fields.Nested(SharedCart, required=False)
    

