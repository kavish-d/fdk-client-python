"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .BeneficiaryModeDetails import BeneficiaryModeDetails


class AddBeneficiaryDetailsRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
    delights = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    

