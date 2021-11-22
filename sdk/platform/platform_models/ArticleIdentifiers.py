"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ArticleIdentifiers(Schema):

    
    ean = fields.Str(required=False)
    

