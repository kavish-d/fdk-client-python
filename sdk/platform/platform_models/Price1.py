"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class Price1(Schema):

    
    currency_symbol = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    max = fields.Float(required=False)
    

