"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .UserSchema import UserSchema

from .PaginationSchema import PaginationSchema


class CustomerListResponseSchema(BaseSchema):

    
    items = fields.List(fields.Nested(UserSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

