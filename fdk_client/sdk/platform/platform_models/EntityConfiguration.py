"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .GetCatalogConfigurationDetailsSchemaListing import GetCatalogConfigurationDetailsSchemaListing





from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct


class EntityConfiguration(BaseSchema):

    
    config_type = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    listing = fields.Nested(GetCatalogConfigurationDetailsSchemaListing, required=False)
    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
