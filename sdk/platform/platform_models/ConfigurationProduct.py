"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ConfigurationProductSimilar import ConfigurationProductSimilar

from .ConfigurationProductVariant import ConfigurationProductVariant


class ConfigurationProduct(Schema):

    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    

