"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ProductStockPrice(Schema):

    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    

