"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class CompanyBrandDetail(BaseSchema):

    
    company_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    total_article = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    

