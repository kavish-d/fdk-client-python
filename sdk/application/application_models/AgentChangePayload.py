"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class AgentChangePayload(Schema):

    
    agent_id = fields.Str(required=False)
    

