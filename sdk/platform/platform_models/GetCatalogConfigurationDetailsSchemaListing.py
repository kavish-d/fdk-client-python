"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class GetCatalogConfigurationDetailsSchemaListing(Schema):

    
    filter = fields.Dict(required=False)
    
    sort = fields.Dict(required=False)
    

