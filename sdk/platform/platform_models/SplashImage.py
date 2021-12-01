"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SplashImage(BaseSchema):

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    

