"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Trader(BaseSchema):

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    

