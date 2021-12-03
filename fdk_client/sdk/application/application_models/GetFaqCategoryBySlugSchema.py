"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .FAQCategorySchema import FAQCategorySchema


class GetFaqCategoryBySlugSchema(BaseSchema):

    
    category = fields.Nested(FAQCategorySchema, required=False)
    

