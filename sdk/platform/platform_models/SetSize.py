"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SetSize(Schema):

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    

