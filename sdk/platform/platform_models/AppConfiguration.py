"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .ConfigurationListing import ConfigurationListing

from .ConfigurationProduct import ConfigurationProduct


class AppConfiguration(BaseSchema):

    
    config_id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    

