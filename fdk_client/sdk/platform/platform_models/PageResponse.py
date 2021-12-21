"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class PageResponse(BaseSchema):
    # Catalog swagger.json

    
    current = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    

