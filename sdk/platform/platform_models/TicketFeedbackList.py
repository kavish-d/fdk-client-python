"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TicketFeedback import TicketFeedback


class TicketFeedbackList(BaseSchema):

    
    items = fields.List(fields.Nested(TicketFeedback, required=False), required=False)
    

