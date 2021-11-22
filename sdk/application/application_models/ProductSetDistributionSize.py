"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ProductSetDistributionSize(Schema):

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    

