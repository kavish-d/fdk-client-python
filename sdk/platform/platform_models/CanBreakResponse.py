"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CanBreakResponse(Schema):

    
    status = fields.Boolean(required=False)
    
    valid_actions = fields.Dict(required=False)
    

