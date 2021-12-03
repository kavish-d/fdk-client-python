"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








































class OrderBeneficiaryDetails(BaseSchema):

    
    branch_name = fields.Boolean(required=False)
    
    account_holder = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    delights_user_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    mobile = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    comment = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    subtitle = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
