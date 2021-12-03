"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .FaqSchema import FaqSchema


class FaqResponseSchema(BaseSchema):

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    

