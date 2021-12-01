"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .HSNData import HSNData




class HSNCodesResponse(BaseSchema):

    
    data = fields.Nested(HSNData, required=False)
    
    message = fields.Str(required=False)
    

