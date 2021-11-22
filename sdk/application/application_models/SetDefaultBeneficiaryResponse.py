"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class SetDefaultBeneficiaryResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    is_beneficiary_set = fields.Boolean(required=False)
    

