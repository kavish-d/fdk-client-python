"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CategoryRequestSchema import CategoryRequestSchema


class CreateFaqCategoryRequestSchema(BaseSchema):

    
    category = fields.Nested(CategoryRequestSchema, required=False)
    

