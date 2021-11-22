"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class StrategyWiseListing(Schema):

    
    quantity = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    
    distance = fields.Int(required=False)
    
    tat = fields.Int(required=False)
    

