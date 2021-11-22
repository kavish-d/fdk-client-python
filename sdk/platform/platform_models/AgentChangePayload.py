"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class AgentChangePayload(Schema):

    
    agent_id = fields.Str(required=False)
    

