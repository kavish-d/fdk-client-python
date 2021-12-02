"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class BankDetailsForOTP(BaseSchema):

    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    

