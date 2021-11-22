"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .HSNData import HSNData




class HSNCodesResponse(Schema):

    
    data = fields.Nested(HSNData, required=False)
    
    message = fields.Str(required=False)
    

