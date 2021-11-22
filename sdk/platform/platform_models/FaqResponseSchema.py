"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .FaqSchema import FaqSchema


class FaqResponseSchema(Schema):

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    

