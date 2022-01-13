"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductAction import ProductAction

from .ProductImage import ProductImage

from .CategoryInfo import CategoryInfo

from .BaseInfo import BaseInfo










class CartProduct(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(ProductAction, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

