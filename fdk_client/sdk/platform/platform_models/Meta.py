"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Meta(BaseSchema):
    # Catalog swagger.json

    
    values = fields.List(fields.Dict(required=False), required=False)
    
    headers = fields.Dict(required=False)
    
    unit = fields.Str(required=False)
    

