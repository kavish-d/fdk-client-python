"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .SecondLevelChild import SecondLevelChild





from .ProductListingAction import ProductListingAction

from .ImageUrls import ImageUrls


class Child(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    

