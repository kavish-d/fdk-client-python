"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








































class OrderBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    modified_on = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    comment = fields.Boolean(required=False)
    
    account_no = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    branch_name = fields.Boolean(required=False)
    
    address = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    mobile = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False)
    

