"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .ImageUrls import ImageUrls







from .ActionPage import ActionPage

from .Media import Media


class BrandItem(BaseSchema):

    
    discount = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    logo = fields.Nested(Media, required=False)
    

