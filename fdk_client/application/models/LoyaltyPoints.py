"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    

