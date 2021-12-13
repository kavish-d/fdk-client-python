"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls



from .ActionPage import ActionPage







from .Media import Media




class BrandItem(BaseSchema):

    
    banners = fields.Nested(ImageUrls, required=False)
    
    discount = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    

