"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UserSchema import UserSchema


class UserSearchResponseSchema(Schema):

    
    users = fields.List(fields.Nested(UserSchema, required=False), required=False)
    

