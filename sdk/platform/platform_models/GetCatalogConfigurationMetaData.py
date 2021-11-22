"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .MetaDataListingResponse import MetaDataListingResponse

from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct


class GetCatalogConfigurationMetaData(Schema):

    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    

