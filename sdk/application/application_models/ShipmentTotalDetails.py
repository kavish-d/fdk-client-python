"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ShipmentTotalDetails(Schema):

    
    total_price = fields.Float(required=False)
    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    

