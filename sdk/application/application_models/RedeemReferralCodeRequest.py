"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class RedeemReferralCodeRequest(Schema):

    
    device_id = fields.Str(required=False)
    
    referral_code = fields.Str(required=False)
    

