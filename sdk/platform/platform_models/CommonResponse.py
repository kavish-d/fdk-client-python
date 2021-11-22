"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CommonResponse(Schema):

    
    success = fields.Str(required=False)
    

