"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema














class ProductPrice(BaseSchema):

    
    effective = fields.Float(required=False)
    
    add_on = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
