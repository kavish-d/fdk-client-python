"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class AuthMeta(Schema):

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    

