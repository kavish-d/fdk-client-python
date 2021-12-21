"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class CompanyBrandPostRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    company = fields.Int(required=False)
    

