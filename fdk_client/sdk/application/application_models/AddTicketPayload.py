"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema









from .TicketContent import TicketContent


class AddTicketPayload(BaseSchema):

    
    created_by = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
    
    category = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    

