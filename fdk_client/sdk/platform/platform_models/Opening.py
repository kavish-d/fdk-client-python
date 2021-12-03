"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Opening(BaseSchema):

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    
