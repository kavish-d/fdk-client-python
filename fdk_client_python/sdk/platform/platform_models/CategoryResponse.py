"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Category import Category

from .Page import Page


class CategoryResponse(BaseSchema):

    
    items = fields.List(fields.Nested(Category, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

