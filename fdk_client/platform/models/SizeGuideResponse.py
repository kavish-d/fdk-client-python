"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class SizeGuideResponse(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    tag = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    guide = fields.Dict(required=False)
    
    subtitle = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    id = fields.Str(required=False)
    

