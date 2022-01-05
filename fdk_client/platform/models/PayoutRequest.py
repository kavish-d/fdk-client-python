"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PayoutBankDetails import PayoutBankDetails






class PayoutRequest(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    users = fields.Dict(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    transfer_type = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    

