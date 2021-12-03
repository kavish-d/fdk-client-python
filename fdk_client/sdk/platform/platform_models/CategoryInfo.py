"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CategoryInfo(BaseSchema):

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

