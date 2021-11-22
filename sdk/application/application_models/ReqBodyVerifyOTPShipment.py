"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ReqBodyVerifyOTPShipment(Schema):

    
    request_id = fields.Str(required=False)
    
    otp_code = fields.Str(required=False)
    

