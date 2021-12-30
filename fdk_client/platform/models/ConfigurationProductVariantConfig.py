"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .ProductSize import ProductSize


class ConfigurationProductVariantConfig(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    display_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
