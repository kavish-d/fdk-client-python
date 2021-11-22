"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class CreateVideoRoomResponse(Schema):

    
    unique_name = fields.Str(required=False)
    

