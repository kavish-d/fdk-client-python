"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class Activity(Schema):

    
    current_state = fields.Dict(required=False)
    
    document_id = fields.Str(required=False)
    
    previous_state = fields.Dict(required=False)
    

