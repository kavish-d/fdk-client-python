"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class BrandBannerSerializer(Schema):

    
    landscape = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    

