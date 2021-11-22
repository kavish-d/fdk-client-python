"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .BankDetailsForOTP import BankDetailsForOTP


class AddBeneficiaryDetailsOTPRequest(Schema):

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    

