"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct

from .MetaDataListingResponse import MetaDataListingResponse


class GetCatalogConfigurationMetaData(BaseSchema):

    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    

