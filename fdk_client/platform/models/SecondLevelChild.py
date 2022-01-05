"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ImageUrls import ImageUrls



from .ThirdLevelChild import ThirdLevelChild

from .ProductListingAction import ProductListingAction






class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

