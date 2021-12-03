"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






















class PayoutResponse(BaseSchema):

    
    is_active = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    payouts = fields.Dict(required=False)
    
    created = fields.Boolean(required=False)
    
    users = fields.Dict(required=False)
    
    payment_status = fields.Str(required=False)
    
    bank_details = fields.Dict(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
