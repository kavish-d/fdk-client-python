"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .PayoutBankDetails import PayoutBankDetails










class PayoutRequest(Schema):

    
    is_active = fields.Boolean(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    users = fields.Dict(required=False)
    
    transfer_type = fields.Str(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    

