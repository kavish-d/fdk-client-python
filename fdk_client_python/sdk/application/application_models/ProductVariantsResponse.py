"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductVariantResponse import ProductVariantResponse


class ProductVariantsResponse(BaseSchema):

    
    variants = fields.List(fields.Nested(ProductVariantResponse, required=False), required=False)
    

