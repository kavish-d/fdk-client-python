"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Manufacturer(BaseSchema):
    # Order swagger.json

    
    is_default = fields.Boolean(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

