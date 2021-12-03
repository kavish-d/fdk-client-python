"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .ActionPage import ActionPage

from .SecondLevelChild import SecondLevelChild



from .ImageUrls import ImageUrls




class Child(BaseSchema):

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
