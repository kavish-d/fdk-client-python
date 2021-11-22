"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ArticleBrand(Schema):

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

