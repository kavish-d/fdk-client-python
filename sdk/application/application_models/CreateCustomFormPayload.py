"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

















from .PollForAssignment import PollForAssignment


class CreateCustomFormPayload(Schema):

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    description = fields.Str(required=False)
    
    header_image = fields.Str(required=False)
    
    priority = fields.Str(required=False, validate=OneOf(PriorityEnum.__members__.keys()))
    
    should_notify = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    

