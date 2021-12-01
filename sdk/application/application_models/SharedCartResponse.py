"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .SharedCart import SharedCart


class SharedCartResponse(BaseSchema):

    
    error = fields.Str(required=False)
    
    cart = fields.Nested(SharedCart, required=False)
    

