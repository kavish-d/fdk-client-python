"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AttributeMetadata import AttributeMetadata

from .ProductDetail import ProductDetail


class ProductsComparisonResponse(BaseSchema):
    # Catalog swagger.json

    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    

