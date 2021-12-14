"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ForgotPasswordRequestSchema(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    

