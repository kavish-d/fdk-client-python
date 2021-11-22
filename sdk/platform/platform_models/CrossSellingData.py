"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CrossSellingData(Schema):

    
    products = fields.Int(required=False)
    
    articles = fields.Int(required=False)
    

