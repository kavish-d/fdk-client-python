"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Trader(Schema):

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    

