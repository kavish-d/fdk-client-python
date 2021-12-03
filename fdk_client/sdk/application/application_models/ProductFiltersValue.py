"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema


























class ProductFiltersValue(BaseSchema):

    
    query_format = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    selected_min = fields.Int(required=False)
    
    selected_max = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    display_format = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
