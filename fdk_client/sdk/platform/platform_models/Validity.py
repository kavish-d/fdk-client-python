"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class Validity(BaseSchema):
    # Cart swagger.json

    
    priority = fields.Int(required=False)
    

