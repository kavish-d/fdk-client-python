"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Debug(Schema):

    
    source = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    

