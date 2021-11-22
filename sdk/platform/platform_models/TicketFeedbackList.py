"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TicketFeedback import TicketFeedback


class TicketFeedbackList(Schema):

    
    items = fields.List(fields.Nested(TicketFeedback, required=False), required=False)
    

