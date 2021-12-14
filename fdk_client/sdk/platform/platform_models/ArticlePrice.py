"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class ArticlePrice(BaseSchema):
    # Order swagger.json

    
    marked = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    transfer = fields.Int(required=False)
    

