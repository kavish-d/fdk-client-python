"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class ChargeCustomerRequest(Schema):

    
    aggregator = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    

