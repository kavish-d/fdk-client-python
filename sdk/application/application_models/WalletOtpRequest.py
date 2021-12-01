"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class WalletOtpRequest(BaseSchema):

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    

