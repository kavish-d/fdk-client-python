"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ProductVariantResponse import ProductVariantResponse


class ProductVariantsResponse(Schema):

    
    variants = fields.List(fields.Nested(ProductVariantResponse, required=False), required=False)
    

