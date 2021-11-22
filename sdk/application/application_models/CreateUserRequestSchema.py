"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
















class CreateUserRequestSchema(Schema):

    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

