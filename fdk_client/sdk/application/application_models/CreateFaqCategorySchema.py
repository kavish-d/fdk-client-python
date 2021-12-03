"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CategorySchema import CategorySchema


class CreateFaqCategorySchema(BaseSchema):

    
    category = fields.Nested(CategorySchema, required=False)
    
