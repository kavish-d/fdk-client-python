"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Price(BaseSchema):
    # Catalog swagger.json

    
    min_effective = fields.Float(required=False)
    
    min_marked = fields.Float(required=False)
    
    max_marked = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    max_effective = fields.Float(required=False)
    

