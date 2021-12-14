"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .TicketFeedback import TicketFeedback


class TicketFeedbackList(BaseSchema):
    # Lead swagger.json

    
    items = fields.List(fields.Nested(TicketFeedback, required=False), required=False)
    

