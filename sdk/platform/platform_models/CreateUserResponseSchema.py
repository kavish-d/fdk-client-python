"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .UserSchema import UserSchema


class CreateUserResponseSchema(Schema):

    
    user = fields.Nested(UserSchema, required=False)
    

