"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .LandingImage import LandingImage

from .SplashImage import SplashImage














class MobileAppConfiguration(BaseSchema):

    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    app_name = fields.Str(required=False)
    
    landing_image = fields.Nested(LandingImage, required=False)
    
    splash_image = fields.Nested(SplashImage, required=False)
    
    application = fields.Str(required=False)
    
    platform_type = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    package_name = fields.Str(required=False)
    

