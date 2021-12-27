"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class StrategyWiseListing(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    tat = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    
    distance = fields.Int(required=False)
    

