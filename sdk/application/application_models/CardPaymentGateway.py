"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class CardPaymentGateway(Schema):

    
    aggregator = fields.Str(required=False)
    
    api = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    

