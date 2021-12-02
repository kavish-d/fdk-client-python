"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






















class PayoutResponse(BaseSchema):

    
    users = fields.Dict(required=False)
    
    transfer_type = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    payouts = fields.Dict(required=False)
    
    payment_status = fields.Str(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    bank_details = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    

