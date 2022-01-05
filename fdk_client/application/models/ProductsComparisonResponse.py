"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductDetail import ProductDetail

from .AttributeMetadata import AttributeMetadata


class ProductsComparisonResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    

