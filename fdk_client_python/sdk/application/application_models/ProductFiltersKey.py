"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class ProductFiltersKey(BaseSchema):

    
    logo = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

