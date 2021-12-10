"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class Price1(BaseSchema):

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    

