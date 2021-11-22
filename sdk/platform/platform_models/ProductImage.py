"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ProductImage(Schema):

    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    

