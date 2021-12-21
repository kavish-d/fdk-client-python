"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class ProductImage(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    

