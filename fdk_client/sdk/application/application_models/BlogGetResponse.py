"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .BlogSchema import BlogSchema

from .Page import Page


class BlogGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(BlogSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
