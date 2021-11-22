"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class CreateUserSessionRequestSchema(Schema):

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    user_id = fields.Str(required=False)
    

