"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class DiscountValueObject(BaseSchema):
    # Discount swagger.json

    
    min_items = fields.Int(required=False)
    
    value = fields.Int(required=False)
    

