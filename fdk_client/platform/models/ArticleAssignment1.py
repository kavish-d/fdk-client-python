"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ArticleAssignment1(BaseSchema):
    # Catalog swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

