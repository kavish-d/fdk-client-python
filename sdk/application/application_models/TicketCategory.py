"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .CustomForm import CustomForm

from .TicketSubCategory import TicketSubCategory

from .TicketFeedbackForm import TicketFeedbackForm


class TicketCategory(Schema):

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    form = fields.Nested(CustomForm, required=False)
    
    sub_categories = fields.List(fields.Nested(TicketSubCategory, required=False), required=False)
    
    feedback_form = fields.Nested(TicketFeedbackForm, required=False)
    

