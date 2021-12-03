"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class AuthMeta(BaseSchema):

    
    type = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    

