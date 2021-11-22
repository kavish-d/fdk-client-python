"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .ConfigurationListingSortConfig import ConfigurationListingSortConfig


class ConfigurationListingSort(Schema):

    
    default_key = fields.Str(required=False)
    
    config = fields.List(fields.Nested(ConfigurationListingSortConfig, required=False), required=False)
    

