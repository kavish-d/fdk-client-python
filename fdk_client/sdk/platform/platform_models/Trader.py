"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Trader(BaseSchema):

    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

