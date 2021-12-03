"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ErrorCodeDescription(BaseSchema):

    
    description = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    

