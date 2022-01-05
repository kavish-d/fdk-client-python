"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Image(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio_f = fields.Float(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    

