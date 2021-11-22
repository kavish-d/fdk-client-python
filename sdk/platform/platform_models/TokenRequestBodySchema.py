"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class TokenRequestBodySchema(Schema):

    
    token = fields.Str(required=False)
    

