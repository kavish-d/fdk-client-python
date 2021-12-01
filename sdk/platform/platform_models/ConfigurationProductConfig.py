"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ProductSize import ProductSize












class ConfigurationProductConfig(BaseSchema):

    
    subtitle = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    key = fields.Str(required=False)
    

