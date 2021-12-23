"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class GetPingResponse(BaseSchema):
    # Order swagger.json

    
    ping = fields.Str(required=False)
    

