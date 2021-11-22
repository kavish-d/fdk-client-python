"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class TicketFeedbackPayload(Schema):

    
    form_response = fields.Dict(required=False)
    

