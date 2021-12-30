"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductDetail import ProductDetail






class ProductSimilarItem(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
