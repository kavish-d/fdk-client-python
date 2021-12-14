"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class OptType(BaseSchema):
    # Configuration swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

