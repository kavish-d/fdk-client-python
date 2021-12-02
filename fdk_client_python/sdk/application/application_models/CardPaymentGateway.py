"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class CardPaymentGateway(BaseSchema):

    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    api = fields.Str(required=False)
    

