"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class BlocksProps(BaseSchema):

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
