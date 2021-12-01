"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CanBreakResponse(BaseSchema):

    
    status = fields.Boolean(required=False)
    
    valid_actions = fields.Dict(required=False)
    

