"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Media1(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    

