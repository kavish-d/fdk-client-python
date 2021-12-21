"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ProductImage(BaseSchema):
    # Cart swagger.json

    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

