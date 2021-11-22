"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ArticleAssignment(Schema):

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

