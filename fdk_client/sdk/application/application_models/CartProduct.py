"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ProductImage import ProductImage



from .CategoryInfo import CategoryInfo





from .BaseInfo import BaseInfo

from .ProductAction import ProductAction


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    name = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    

