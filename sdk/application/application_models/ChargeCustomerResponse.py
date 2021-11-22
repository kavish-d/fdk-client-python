"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
















class ChargeCustomerResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

