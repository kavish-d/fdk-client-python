"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Media import Media





from .ActionPage import ActionPage







from .ImageUrls import ImageUrls


class BrandItem(BaseSchema):

    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    

