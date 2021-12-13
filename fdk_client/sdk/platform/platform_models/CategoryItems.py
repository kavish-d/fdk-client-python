"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls

from .Child import Child

from .ActionPage import ActionPage








class CategoryItems(BaseSchema):

    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

