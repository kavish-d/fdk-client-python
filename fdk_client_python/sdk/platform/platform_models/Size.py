"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class Size(BaseSchema):

    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    

