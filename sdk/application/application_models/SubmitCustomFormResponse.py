"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Ticket import Ticket


class SubmitCustomFormResponse(Schema):

    
    ticket = fields.Nested(Ticket, required=False)
    

