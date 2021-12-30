"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ArticleQuery(BaseSchema):
    # Catalog swagger.json

    
    ignored_stores = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
