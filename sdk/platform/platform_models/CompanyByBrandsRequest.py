"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CompanyByBrandsRequest(Schema):

    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    

