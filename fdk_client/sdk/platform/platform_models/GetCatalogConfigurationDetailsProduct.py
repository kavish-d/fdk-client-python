"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class GetCatalogConfigurationDetailsProduct(BaseSchema):

    
    detail = fields.Dict(required=False)
    
    compare = fields.Dict(required=False)
    
    similar = fields.Dict(required=False)
    
    variant = fields.Dict(required=False)
    

