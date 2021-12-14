"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Sellable(BaseSchema):
    # Order swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    

