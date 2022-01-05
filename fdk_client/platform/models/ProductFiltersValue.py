"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class ProductFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    min = fields.Int(required=False)
    
    count = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    selected_min = fields.Int(required=False)
    
    selected_max = fields.Int(required=False)
    
    query_format = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    max = fields.Int(required=False)
    
    display_format = fields.Str(required=False)
    

