"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class Images(BaseSchema):

    
    desktop = fields.List(fields.Str(required=False), required=False)
    
    android = fields.List(fields.Str(required=False), required=False)
    
    ios = fields.List(fields.Str(required=False), required=False)
    
    thumbnail = fields.List(fields.Str(required=False), required=False)
    

