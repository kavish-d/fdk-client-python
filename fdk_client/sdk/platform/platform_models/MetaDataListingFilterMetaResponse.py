"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class MetaDataListingFilterMetaResponse(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    units = fields.List(fields.Dict(required=False), required=False)
    
    key = fields.Str(required=False)
    
    filter_types = fields.List(fields.Str(required=False), required=False)
    

