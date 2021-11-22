"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class AppOrderConfig(Schema):

    
    enabled = fields.Boolean(required=False)
    
    force_reassignment = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

