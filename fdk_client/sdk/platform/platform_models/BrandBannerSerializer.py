"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class BrandBannerSerializer(BaseSchema):

    
    landscape = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    

