"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class TatacliqLuxury(Schema):

    
    sku = fields.Str(required=False)
    

