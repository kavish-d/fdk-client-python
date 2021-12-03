"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .FaqSchema import FaqSchema


class CreateFaqResponseSchema(BaseSchema):

    
    faq = fields.Nested(FaqSchema, required=False)
    

