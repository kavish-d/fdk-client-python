"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PayoutBankDetails import PayoutBankDetails












class PayoutRequest(BaseSchema):

    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    users = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    

