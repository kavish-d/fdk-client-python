"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    is_applied = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    total = fields.Float(required=False)
    
    applicable = fields.Float(required=False)
    

