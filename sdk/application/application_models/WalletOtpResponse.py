"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class WalletOtpResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    is_verified_flag = fields.Str(required=False)
    

