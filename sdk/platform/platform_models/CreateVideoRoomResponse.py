"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CreateVideoRoomResponse(Schema):

    
    unique_name = fields.Str(required=False)
    

