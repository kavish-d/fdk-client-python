"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FAQCategorySchema import FAQCategorySchema


class GetFaqCategoryBySlugSchema(Schema):

    
    category = fields.Nested(FAQCategorySchema, required=False)
    

