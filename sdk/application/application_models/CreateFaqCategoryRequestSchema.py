"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .CategoryRequestSchema import CategoryRequestSchema


class CreateFaqCategoryRequestSchema(Schema):

    
    category = fields.Nested(CategoryRequestSchema, required=False)
    

