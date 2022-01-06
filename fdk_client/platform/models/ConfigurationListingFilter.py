"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationListingFilterConfig import ConfigurationListingFilterConfig




class ConfigurationListingFilter(BaseSchema):
    # Catalog swagger.json

    
    attribute_config = fields.List(fields.Nested(ConfigurationListingFilterConfig, required=False), required=False)
    
    allow_single = fields.Boolean(required=False)
    

