"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CategoryCreateResponse(BaseSchema):

    
    uid = fields.Int(required=False)
    
    message = fields.Str(required=False)
    

