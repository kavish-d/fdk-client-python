"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .ConfigurationProduct import ConfigurationProduct





from .ConfigurationListing import ConfigurationListing


class AppConfiguration(Schema):

    
    config_type = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    config_id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    

