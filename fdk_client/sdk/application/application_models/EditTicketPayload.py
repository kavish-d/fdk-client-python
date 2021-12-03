"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .TicketContent import TicketContent











from .AgentChangePayload import AgentChangePayload




class EditTicketPayload(BaseSchema):

    
    content = fields.Nested(TicketContent, required=False)
    
    category = fields.Str(required=False)
    
    sub_category = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    priority = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
    
    assigned_to = fields.Nested(AgentChangePayload, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
