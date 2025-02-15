"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PaginationSchema(BaseSchema):
    # Theme swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    

