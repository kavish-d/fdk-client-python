"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class OptInPostRequest(BaseSchema):
    # Catalog swagger.json

    
    opt_level = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    enabled = fields.Boolean(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    

