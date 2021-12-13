"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls



from .SecondLevelChild import SecondLevelChild

from .ActionPage import ActionPage








class Child(BaseSchema):

    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

