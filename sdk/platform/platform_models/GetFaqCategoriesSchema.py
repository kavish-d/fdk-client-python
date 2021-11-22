"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CategorySchema import CategorySchema


class GetFaqCategoriesSchema(Schema):

    
    categories = fields.List(fields.Nested(CategorySchema, required=False), required=False)
    

