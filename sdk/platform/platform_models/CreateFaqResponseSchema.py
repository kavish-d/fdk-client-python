"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .FaqSchema import FaqSchema


class CreateFaqResponseSchema(Schema):

    
    faq = fields.Nested(FaqSchema, required=False)
    

