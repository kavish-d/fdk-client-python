"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ConfigurationProduct import ConfigurationProduct





from .ConfigurationListing import ConfigurationListing




class AppConfiguration(BaseSchema):

    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    config_type = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    app_id = fields.Str(required=False)
    

