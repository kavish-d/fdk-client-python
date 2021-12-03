"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ConfigurationListingFilterValue import ConfigurationListingFilterValue












class ConfigurationListingFilterConfig(BaseSchema):

    
    name = fields.Str(required=False)
    
    value_config = fields.Nested(ConfigurationListingFilterValue, required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
