"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ProductPrice import ProductPrice

from .ProductPrice import ProductPrice


class ProductPriceInfo(Schema):

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    

