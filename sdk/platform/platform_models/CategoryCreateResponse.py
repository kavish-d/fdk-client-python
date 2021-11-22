"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CategoryCreateResponse(Schema):

    
    uid = fields.Int(required=False)
    
    message = fields.Str(required=False)
    

