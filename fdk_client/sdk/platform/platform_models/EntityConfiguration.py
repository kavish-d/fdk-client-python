"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct







from .GetCatalogConfigurationDetailsSchemaListing import GetCatalogConfigurationDetailsSchemaListing




class EntityConfiguration(BaseSchema):

    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    listing = fields.Nested(GetCatalogConfigurationDetailsSchemaListing, required=False)
    
    config_id = fields.Str(required=False)
    

