"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ProductDetailAttribute import ProductDetailAttribute


class ProductDetailGroupedAttribute(BaseSchema):

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    

