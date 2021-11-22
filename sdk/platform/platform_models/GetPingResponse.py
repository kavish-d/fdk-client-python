"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class GetPingResponse(Schema):

    
    ping = fields.Str(required=False)
    

