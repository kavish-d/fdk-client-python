"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class TicketFeedbackForm(Schema):

    
    title = fields.Str(required=False)
    
    display = fields.List(fields.Dict(required=False), required=False)
    

