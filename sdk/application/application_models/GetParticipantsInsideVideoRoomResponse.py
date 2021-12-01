"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Participant import Participant


class GetParticipantsInsideVideoRoomResponse(BaseSchema):

    
    participants = fields.List(fields.Nested(Participant, required=False), required=False)
    

