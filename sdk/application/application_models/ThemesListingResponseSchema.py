"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ThemesSchema import ThemesSchema

from .PaginationSchema import PaginationSchema


class ThemesListingResponseSchema(BaseSchema):

    
    items = fields.List(fields.Nested(ThemesSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

