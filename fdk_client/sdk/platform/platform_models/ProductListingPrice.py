"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Price1 import Price1

from .Price1 import Price1


class ProductListingPrice(BaseSchema):

    
    marked = fields.Nested(Price1, required=False)
    
    effective = fields.Nested(Price1, required=False)
    

