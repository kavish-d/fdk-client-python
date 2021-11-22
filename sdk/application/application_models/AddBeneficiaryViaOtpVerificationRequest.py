"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class AddBeneficiaryViaOtpVerificationRequest(Schema):

    
    otp = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    

