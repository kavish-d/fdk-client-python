"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class CompanyStore(Schema):

    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    

