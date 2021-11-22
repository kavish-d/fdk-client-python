"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class BrandCompanyInfo(Schema):

    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

