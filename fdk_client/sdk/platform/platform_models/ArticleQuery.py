"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ArticleQuery(BaseSchema):

    
    size = fields.Str(required=False)
    
    ignored_stores = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.Int(required=False)
    

