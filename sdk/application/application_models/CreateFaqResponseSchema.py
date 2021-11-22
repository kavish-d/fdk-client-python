"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FaqSchema import FaqSchema


class CreateFaqResponseSchema(Schema):

    
    faq = fields.Nested(FaqSchema, required=False)
    

