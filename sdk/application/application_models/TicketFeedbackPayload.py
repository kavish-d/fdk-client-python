"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class TicketFeedbackPayload(Schema):

    
    form_response = fields.Dict(required=False)
    

