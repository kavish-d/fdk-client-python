"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ArticleAssignment(BaseSchema):

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

