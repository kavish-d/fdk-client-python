"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class ProductFiltersKey(BaseSchema):

    
    name = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
