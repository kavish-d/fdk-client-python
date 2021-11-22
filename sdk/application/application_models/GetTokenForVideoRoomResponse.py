"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class GetTokenForVideoRoomResponse(Schema):

    
    access_token = fields.Str(required=False)
    

