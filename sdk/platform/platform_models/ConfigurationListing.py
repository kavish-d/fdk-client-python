"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ConfigurationListingFilter import ConfigurationListingFilter

from .ConfigurationListingSort import ConfigurationListingSort


class ConfigurationListing(Schema):

    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    

