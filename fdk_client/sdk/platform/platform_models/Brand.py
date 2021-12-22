"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Logo import Logo






class Brand(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Logo, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

