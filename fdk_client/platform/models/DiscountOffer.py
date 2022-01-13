"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class DiscountOffer(BaseSchema):
    # Cart swagger.json

    
    discount_price = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    max_discount_amount = fields.Float(required=False)
    
    discount_amount = fields.Float(required=False)
    
    offer_quantity = fields.Int(required=False)
    
