"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class CodeRequestBodySchema(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    

