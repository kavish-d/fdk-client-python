"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class ValidateCustomerRequest(BaseSchema):

    
    payload = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    merchant_params = fields.Dict(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    

