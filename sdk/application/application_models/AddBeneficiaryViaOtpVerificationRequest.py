"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):

    
    request_id = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

