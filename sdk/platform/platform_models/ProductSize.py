"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ProductSize(Schema):

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    

