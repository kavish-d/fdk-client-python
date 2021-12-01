"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Ticket import Ticket


class SubmitCustomFormResponse(BaseSchema):

    
    ticket = fields.Nested(Ticket, required=False)
    

