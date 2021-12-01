"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Meta(BaseSchema):

    
    headers = fields.Dict(required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    
    unit = fields.Str(required=False)
    

