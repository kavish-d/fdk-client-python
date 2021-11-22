"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ConfigurationProductConfig import ConfigurationProductConfig


class ConfigurationProductSimilar(Schema):

    
    config = fields.List(fields.Nested(ConfigurationProductConfig, required=False), required=False)
    

