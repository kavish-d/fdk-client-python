"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ArticleAssignment1(Schema):

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    

