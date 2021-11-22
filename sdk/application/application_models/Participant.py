"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UserSchema import UserSchema






class Participant(Schema):

    
    user = fields.Nested(UserSchema, required=False)
    
    identity = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

