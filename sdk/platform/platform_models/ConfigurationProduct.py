"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ConfigurationProductVariant import ConfigurationProductVariant

from .ConfigurationProductSimilar import ConfigurationProductSimilar


class ConfigurationProduct(BaseSchema):

    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    

