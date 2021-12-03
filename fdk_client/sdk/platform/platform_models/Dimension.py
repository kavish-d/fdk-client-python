"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class Dimension(BaseSchema):

    
    height = fields.Int(required=False)
    
    width = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    length = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    
