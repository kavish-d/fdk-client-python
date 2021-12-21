"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class PromiseFormatted(BaseSchema):
    # Cart swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    

