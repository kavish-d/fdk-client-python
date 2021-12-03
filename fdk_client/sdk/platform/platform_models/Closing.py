"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Closing(BaseSchema):

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    

