"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .FAQCategorySchema import FAQCategorySchema


class GetFaqCategoryBySlugSchema(BaseSchema):

    
    category = fields.Nested(FAQCategorySchema, required=False)
    

