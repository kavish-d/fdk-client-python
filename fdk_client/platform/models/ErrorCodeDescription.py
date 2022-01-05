"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    

