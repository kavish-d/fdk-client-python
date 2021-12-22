"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SetSize(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    

