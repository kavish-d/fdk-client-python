"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ArticleAssignment1(BaseSchema):

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    

