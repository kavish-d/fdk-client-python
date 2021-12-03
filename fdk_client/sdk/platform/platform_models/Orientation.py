"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Orientation(BaseSchema):

    
    portrait = fields.List(fields.Str(required=False), required=False)
    
    landscape = fields.List(fields.Str(required=False), required=False)
    
