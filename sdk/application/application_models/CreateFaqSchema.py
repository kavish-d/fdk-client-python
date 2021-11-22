"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FAQ import FAQ


class CreateFaqSchema(Schema):

    
    faq = fields.Nested(FAQ, required=False)
    

