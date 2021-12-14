"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class TicketFeedbackForm(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    display = fields.List(fields.Dict(required=False), required=False)
    

