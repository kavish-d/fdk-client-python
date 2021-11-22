"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CategoryRequestSchema(Schema):

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

