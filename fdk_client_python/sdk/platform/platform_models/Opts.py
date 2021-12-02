"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class Opts(BaseSchema):

    
    attempts = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    

