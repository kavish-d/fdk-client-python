"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ConfigurationListingFilterConfig import ConfigurationListingFilterConfig




class ConfigurationListingFilter(Schema):

    
    attribute_config = fields.List(fields.Nested(ConfigurationListingFilterConfig, required=False), required=False)
    
    allow_single = fields.Boolean(required=False)
    

