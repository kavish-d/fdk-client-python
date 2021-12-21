"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




























class SizeGuideResponse(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    guide = fields.Dict(required=False)
    
    active = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    created_by = fields.Dict(required=False)
    

