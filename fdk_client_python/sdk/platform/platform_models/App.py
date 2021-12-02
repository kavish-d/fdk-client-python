"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .ApplicationAuth import ApplicationAuth






class App(BaseSchema):

    
    company_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    auth = fields.Nested(ApplicationAuth, required=False)
    
    name = fields.Str(required=False)
    
    desc = fields.Str(required=False)
    

