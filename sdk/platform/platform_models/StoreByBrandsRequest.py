"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class StoreByBrandsRequest(BaseSchema):

    
    company_id = fields.Int(required=False)
    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    

