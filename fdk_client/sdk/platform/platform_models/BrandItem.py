"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls

from .Media import Media



from .ActionPage import ActionPage










class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    discount = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    

