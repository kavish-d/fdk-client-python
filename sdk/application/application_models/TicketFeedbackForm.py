"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class TicketFeedbackForm(BaseSchema):

    
    title = fields.Str(required=False)
    
    display = fields.List(fields.Dict(required=False), required=False)
    

