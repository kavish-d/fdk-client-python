"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class ProductSize(BaseSchema):

    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
