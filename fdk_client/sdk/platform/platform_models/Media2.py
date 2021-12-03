"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Media2(BaseSchema):

    
    portrait = fields.Str(required=False)
    
    landscape = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
