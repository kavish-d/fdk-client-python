"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class AuthenticationConfig(BaseSchema):

    
    required = fields.Boolean(required=False)
    
    provider = fields.Str(required=False)
    

