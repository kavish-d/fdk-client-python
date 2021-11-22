"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ThemesSchema import ThemesSchema

from .PaginationSchema import PaginationSchema


class ThemesListingResponseSchema(Schema):

    
    items = fields.List(fields.Nested(ThemesSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

