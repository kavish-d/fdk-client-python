"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CartProductInfo import CartProductInfo

from .CartBreakup import CartBreakup


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    

