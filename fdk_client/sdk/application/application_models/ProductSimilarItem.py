"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ProductDetail import ProductDetail




class ProductSimilarItem(BaseSchema):

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    subtitle = fields.Str(required=False)
    

