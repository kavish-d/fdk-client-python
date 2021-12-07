"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class State(BaseSchema):

    
    is_public = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    is_display = fields.Boolean(required=False)
    

