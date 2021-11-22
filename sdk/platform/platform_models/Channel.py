"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Channel(Schema):

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

