"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ApiError(BaseSchema):

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
