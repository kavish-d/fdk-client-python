"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class DisplayMetaDict(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    

