"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .OfferPrice import OfferPrice










class OfferItem(BaseSchema):

    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    total = fields.Float(required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    margin = fields.Int(required=False)
    
    best = fields.Boolean(required=False)
    

