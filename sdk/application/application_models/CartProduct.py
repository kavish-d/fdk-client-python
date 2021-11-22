"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .ProductImage import ProductImage

from .ProductAction import ProductAction





from .CategoryInfo import CategoryInfo

from .BaseInfo import BaseInfo


class CartProduct(Schema):

    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    

