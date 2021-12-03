"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductVariantItemResponse import ProductVariantItemResponse








class ProductVariantResponse(BaseSchema):

    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    
    header = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
