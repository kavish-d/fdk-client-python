"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class WalletOtpRequest(Schema):

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    

