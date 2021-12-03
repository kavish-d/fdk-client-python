"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CategoryRequestSchema import CategoryRequestSchema


class CreateFaqCategoryRequestSchema(BaseSchema):

    
    category = fields.Nested(CategoryRequestSchema, required=False)
    

