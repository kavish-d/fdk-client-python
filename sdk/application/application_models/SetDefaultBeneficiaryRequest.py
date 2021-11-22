"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class SetDefaultBeneficiaryRequest(Schema):

    
    beneficiary_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    

