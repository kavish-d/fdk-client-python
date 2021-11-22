"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class CartCurrency(Schema):

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

