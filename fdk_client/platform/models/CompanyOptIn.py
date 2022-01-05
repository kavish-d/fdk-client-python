"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class CompanyOptIn(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    created_on = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    platform = fields.Str(required=False)
    
    opt_level = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    

