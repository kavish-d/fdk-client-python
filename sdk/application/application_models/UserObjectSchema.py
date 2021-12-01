"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .UserSchema import UserSchema


class UserObjectSchema(BaseSchema):

    
    user = fields.Nested(UserSchema, required=False)
    

