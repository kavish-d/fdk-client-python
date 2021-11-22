"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .UserSchema import UserSchema

from .PaginationSchema import PaginationSchema


class CustomerListResponseSchema(Schema):

    
    items = fields.List(fields.Nested(UserSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

