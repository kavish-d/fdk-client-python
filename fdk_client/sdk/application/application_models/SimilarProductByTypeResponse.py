"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductSimilarItem import ProductSimilarItem


class SimilarProductByTypeResponse(BaseSchema):

    
    similars = fields.Nested(ProductSimilarItem, required=False)
    

