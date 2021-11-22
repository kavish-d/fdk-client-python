"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .ProductListingPrice import ProductListingPrice

from .ProductSize import ProductSize



from .ProductSizeStores import ProductSizeStores

from .SizeChart import SizeChart


class ProductSizes(Schema):

    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    sellable = fields.Boolean(required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    

