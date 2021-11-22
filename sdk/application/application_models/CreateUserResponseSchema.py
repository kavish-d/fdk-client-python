"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UserSchema import UserSchema


class CreateUserResponseSchema(Schema):

    
    user = fields.Nested(UserSchema, required=False)
    

