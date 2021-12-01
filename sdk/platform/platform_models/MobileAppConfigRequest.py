"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .LandingImage import LandingImage

from .SplashImage import SplashImage




class MobileAppConfigRequest(BaseSchema):

    
    app_name = fields.Str(required=False)
    
    landing_image = fields.Nested(LandingImage, required=False)
    
    splash_image = fields.Nested(SplashImage, required=False)
    
    is_active = fields.Boolean(required=False)
    

