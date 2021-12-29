"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class ConfigurationListingSortConfig(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

