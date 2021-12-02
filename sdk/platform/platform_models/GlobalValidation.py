"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .Properties import Properties






class GlobalValidation(BaseSchema):

    
    description = fields.Str(required=False)
    
    definitions = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    properties = fields.Nested(Properties, required=False)
    
    required = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    

