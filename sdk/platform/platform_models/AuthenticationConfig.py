"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class AuthenticationConfig(Schema):

    
    required = fields.Boolean(required=False)
    
    provider = fields.Str(required=False)
    

