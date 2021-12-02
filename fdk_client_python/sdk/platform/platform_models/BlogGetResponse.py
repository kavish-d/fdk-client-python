"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .BlogSchema import BlogSchema

from .Page import Page


class BlogGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(BlogSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

