"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *









from .TicketContent import TicketContent


class AddTicketPayload(Schema):

    
    created_by = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
    
    category = fields.Str(required=False)
    
    content = fields.Nested(TicketContent, required=False)
    

