"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .BeneficiaryModeDetails import BeneficiaryModeDetails










class AddBeneficiaryDetailsRequest(Schema):

    
    shipment_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    delights = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    

