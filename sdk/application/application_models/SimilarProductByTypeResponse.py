"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ProductSimilarItem import ProductSimilarItem


class SimilarProductByTypeResponse(Schema):

    
    similars = fields.Nested(ProductSimilarItem, required=False)
    

