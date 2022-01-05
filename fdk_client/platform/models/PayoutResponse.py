"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class PayoutResponse(BaseSchema):
    # Payment swagger.json

    
    payment_status = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    payouts = fields.Dict(required=False)
    
    bank_details = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    

