"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Participant import Participant


class GetParticipantsInsideVideoRoomResponse(Schema):

    
    participants = fields.List(fields.Nested(Participant, required=False), required=False)
    

