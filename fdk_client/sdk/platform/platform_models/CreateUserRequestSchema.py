"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class CreateUserRequestSchema(BaseSchema):
    # User swagger.json

    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

