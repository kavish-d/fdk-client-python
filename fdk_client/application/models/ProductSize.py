"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    display = fields.Str(required=False)
    

