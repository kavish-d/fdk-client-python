"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class GetCatalogConfigurationDetailsProduct(Schema):

    
    similar = fields.Dict(required=False)
    
    compare = fields.Dict(required=False)
    
    detail = fields.Dict(required=False)
    
    variant = fields.Dict(required=False)
    

