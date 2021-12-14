"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Ticket import Ticket


class SubmitCustomFormResponse(BaseSchema):
    # Lead swagger.json

    
    ticket = fields.Nested(Ticket, required=False)
    

