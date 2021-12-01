"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class TicketFeedbackPayload(BaseSchema):

    
    form_response = fields.Dict(required=False)
    

