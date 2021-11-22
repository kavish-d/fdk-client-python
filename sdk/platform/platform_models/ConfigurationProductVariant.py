"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ConfigurationProductVariantConfig import ConfigurationProductVariantConfig


class ConfigurationProductVariant(Schema):

    
    config = fields.List(fields.Nested(ConfigurationProductVariantConfig, required=False), required=False)
    

